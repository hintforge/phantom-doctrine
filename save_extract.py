"""Phantom Doctrine roster extractor -- structured, semantics-labeled agent data.

Companion to `save_watcher.py` (which owns decode + slot discovery). This script
turns the decoded save XML into per-agent JSON a reader session can trust,
applying the field semantics documented in `save_schema.md` so the known
mis-read traps are impossible to hit silently:

  * `Stat_A-D` are BASE (pre-compound) values for EVERY agent. This script
    labels them `base_stats` and only emits `current_stats` when it can
    actually compute them (base + all applied compounds mapped to names).
    (2026-08-20 incident: base values reported as live stats -> wrong hire rec.)
  * The `<Stats>` block's derived fields (Max_HP, Max_AP, DodgeCost, ...)
    serialize 0 in saves -- never read them. Live HP is on the parent <agent>.
  * Spoiler-gated fields (`sidestoryparticipant`, `undercover`, `revealstatus`,
    `knownbyai`) are EXCLUDED unless `--gated` is passed (prints a warning).
  * Saves lag live play (cash, HP, hires). Output carries the save's own
    in-game timestamp; treat volatile fields as "as of that save", not "now".

ALWAYS run against the live save (default): the newest save in the game's
standard folder (%LOCALAPPDATA%/PhantomDoctrine/Saved/<steamid>/SaveGames), or
the folder named by the PHANTOM_DOCTRINE_SAVE_DIR environment variable.
Never parse an old decoded dump for current state.

Usage:
    python save_extract.py                 # hired roster, semantics-labeled JSON
    python save_extract.py --pool          # hire-pool candidates instead
    python save_extract.py --all-agents    # every agent record in the save
    python save_extract.py --gated         # include spoiler-gated fields (warns)
    python save_extract.py --snapshot      # also write save_state/roster_extract.json

Extending the compound id map: see save_schema.md "Compound id mapping".
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from save_watcher import decode_save, find_save_dir, find_latest_save

HERE = Path(__file__).parent
ID_MAP_PATH = HERE / "save_state" / "compound_id_map.json"
SNAPSHOT_PATH = HERE / "save_state" / "roster_extract.json"

# Primary 4-stat deltas per compound, (circ, resp, sens, moto) -- note the
# order: it matches the save's Stat_A..D letters AND the in-game dossier
# layout, NOT the original wiki column order. The corpus table's Sens/Resp
# columns were verified transposed on 2026-08-21 (3-agent screenshot
# cross-check: Reza, Elke, Adel -- see save_schema.md), so these tuples are
# the wiki values read in corrected order.
# Source: items/abilities.md "Full compound table". Keep in sync -- it is the
# authority, this is a copy.
COMPOUND_PRIMARY = {
    "AMPEA":       (14,  7, 15,  8),
    "THG":         (17, 17, 14,  8),
    "TST":         ( 7, 13, 15,  9),
    "BMA":         ( 9, 15, 10, 16),
    "Bolasterone": (-1, 11,  0, -1),
    "DXAMPEA":     ( 8,  7, 11, 11),
    "Gonadorelin": ( 2,  1, -4, 16),
    "EPO":         (13,  0,  0, -2),
    "Danazol":     (-2,  0, 15,  2),
    "DHEA":        (13, 12,  9, 19),
    "Anadrol":     (17, 14, 11, 14),
    "Bolandiol":   (-2,  8,  1, -3),
    "Calusterone": ( 0, 10,  0, -2),
    "Cyclofenil":  (18, -19, 29, 20),
    "Formebolone": (-1,  2, 10,  3),
    "Mannitol":    (38, 24,  0, -10),
    "ARGOXY":      (10, -1,  0,  0),
    "AMPK":        (22,  0, -10, 32),
    "Raloxifene":  ( 0, 19, -15, -10),
    "XENOXY":      (17,  0,  0, -4),
    "Albumin":     (-10, 24, 30,  6),
    "IGF-1":       (-10, 19, 28, 31),
    "FGF":         (-5,  1,  3,  8),
    "Formoterol":  ( 2,  0,  2, 14),
    "Stanozolol":  ( 0,  0,  9,  5),
}

# Fire/Action Point thresholds on CURRENT stats.
# Source: mechanics.md (Circulatory 150/200 -> FP, Motoric 100/140 -> AP).
FP_TIERS = ((200, 3), (150, 2), (0, 1))   # circulatory >= threshold -> FP
AP_TIERS = ((140, 4), (100, 3), (0, 2))   # motoric >= threshold -> AP

GATED_FIELDS = ("sidestoryparticipant", "undercover", "revealstatus",
                "knownbyai", "iscritical")

# Stat_A..D -> stat, verified 2026-08-21 (Reza/Elke/Adel screenshot solve).
STAT_KEYS = ("circulatory", "respiratory", "sensory", "motoric")


def _attrs(fragment: str) -> dict[str, str]:
    return dict(re.findall(r'(\w+)\s*=\s*"([^"]*)"', fragment))


def load_id_map() -> dict:
    if ID_MAP_PATH.exists():
        return json.loads(ID_MAP_PATH.read_text(encoding="utf-8"))
    return {}


def tier(value: int, tiers) -> int:
    for threshold, points in tiers:
        if value >= threshold:
            return points
    return tiers[-1][1]


def parse_agents(xml: str) -> list[dict]:
    agents = []
    for block in re.split(r"(?=<agent )", xml):
        if not block.startswith("<agent "):
            continue
        head = re.match(r"<agent\b([^>]*)>", block)
        if not head:
            continue
        a = _attrs(head.group(1))
        stats_m = re.search(r"<Stats\b([^>]*)>", block)
        st = _attrs(stats_m.group(1)) if stats_m else {}
        agents.append((a, st))
    return agents


def build_record(a: dict, st: dict, id_map: dict, include_gated: bool) -> dict:
    base = {}
    for key, letter in zip(STAT_KEYS, "ABCD"):
        raw = st.get(f"Stat_{letter}")
        base[key] = int(raw) if raw and raw.lstrip("-").isdigit() else None

    raw_ids = [c for c in a.get("compounds", "").split(",") if c]
    named, unmapped = [], []
    for cid in raw_ids:
        entry = id_map.get(cid)
        if entry and entry.get("name") in COMPOUND_PRIMARY:
            named.append(entry["name"])
        else:
            unmapped.append(cid)

    current, current_note = None, None
    if not raw_ids:
        current = dict(base)
        current_note = "no compounds applied in this save; current = base"
    elif not unmapped and all(v is not None for v in base.values()):
        current = dict(base)
        for name in named:
            for key, delta in zip(STAT_KEYS, COMPOUND_PRIMARY[name]):
                current[key] += delta
        current_note = ("computed: base + " + "+".join(named)
                        + " (mapping confidence: see save_state/compound_id_map.json)")
    else:
        current_note = (f"NOT computable -- unmapped compound id(s) {unmapped}; "
                        "use an in-game dossier screenshot for current stats")

    rec = {
        # uniqueid is the ONLY stable per-agent key. Real names are NOT stable:
        # the in-game new-identity mechanic rewrites firstname/lastname, and it
        # did (Reza Golshani -> Deepak Pappu, Mateo Torres -> Khalid Saad,
        # caught 2026-09-16). Match roster files on this, never on a name.
        "uniqueid": a.get("uniqueid"),
        "first_name": a.get("firstname"),
        "last_name": a.get("lastname"),
        "codename_internal": a.get("codename") or None,  # NOT the display codename
        "hirestate": a.get("hirestate"),
        "strategicstate": a.get("strategicstate"),
        "hp_live": int(a["HP"]) if a.get("HP", "").isdigit() else None,
        "xp": a.get("xp"),
        "rank": a.get("rank"),
        "cost": a.get("cost"),
        "nationality": a.get("nationality"),
        "background": a.get("agencybg"),
        "languages": [x for x in a.get("languages", "").split(",") if x],
        "abilities": [x for x in a.get("abilities", "").split(",") if x],
        "completed_trainings": [x for x in a.get("completedtrainings", "").split(",") if x],
        "current_training": a.get("currenttrainingID") or None,
        "place_id": a.get("c_place") or None,
        "base_stats": base,
        "compounds_raw": raw_ids,
        "compounds_named": named,
        "compounds_unmapped": unmapped,
        "current_stats": current,
        "current_stats_note": current_note,
    }
    if current and all(isinstance(v, int) for v in current.values()):
        rec["fp_from_current"] = tier(current["circulatory"], FP_TIERS)
        rec["ap_from_current"] = tier(current["motoric"], AP_TIERS)
        rec["breakpoint_gaps"] = {
            "circ_to_next_fp": next((t - current["circulatory"]
                                     for t, _ in reversed(FP_TIERS)
                                     if t > current["circulatory"]), 0),
            "moto_to_next_ap": next((t - current["motoric"]
                                     for t, _ in reversed(AP_TIERS)
                                     if t > current["motoric"]), 0),
        }
    if include_gated:
        rec["gated"] = {f: a.get(f) for f in GATED_FIELDS}
    return rec


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool", action="store_true",
                        help="hire-pool candidates (OnPlayerHireList) instead of hired roster")
    parser.add_argument("--all-agents", action="store_true",
                        help="every agent record in the save")
    parser.add_argument("--gated", action="store_true",
                        help="include spoiler-gated save fields (see save_schema.md)")
    parser.add_argument("--snapshot", action="store_true",
                        help="also write save_state/roster_extract.json")
    args = parser.parse_args()

    save_dir = find_save_dir()
    if not save_dir or not save_dir.exists():
        print("save dir not found -- see save_watcher.py for overrides", file=sys.stderr)
        sys.exit(1)
    latest = find_latest_save(save_dir)
    if not latest:
        print(f"no saves in {save_dir}", file=sys.stderr)
        sys.exit(1)
    xml = decode_save(latest)
    if xml is None:
        print(f"could not decode {latest} -- format may have changed", file=sys.stderr)
        sys.exit(1)

    if args.gated:
        print("WARNING: --gated includes fields that can carry hidden-identity /"
              " story-progression state. Reader sessions: check warning_tiers.md"
              " and the standing narrow-answer rule before surfacing ANY of them.",
              file=sys.stderr)

    meta_m = re.search(r"<IWTBSaveMetadata\b([^>]*)>", xml)
    meta = _attrs(meta_m.group(1)) if meta_m else {}
    id_map = load_id_map()

    if args.all_agents:
        keep = lambda a: True
    elif args.pool:
        keep = lambda a: a.get("hirestate") == "OnPlayerHireList"
    else:
        keep = lambda a: a.get("hirestate") == "HiredByPlayer"

    records = [build_record(a, st, id_map, args.gated)
               for a, st in parse_agents(xml) if keep(a)]

    out = {
        "save_slot": latest.name,
        "in_game_timestamp": meta.get("Timestamp"),
        "in_game_day": meta.get("Day"),
        "extracted_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "semantics": ("base_stats are PRE-COMPOUND for every agent; current_stats"
                      " only where computable; derived <Stats> fields are never"
                      " read (they serialize 0); volatile fields (hp_live, cash)"
                      " are as-of the save, which lags live play. Full field"
                      " reference: save_schema.md"),
        "agent_count": len(records),
        "agents": records,
    }
    print(json.dumps(out, indent=2))
    if args.snapshot:
        SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
        SNAPSHOT_PATH.write_text(json.dumps(out, indent=2), encoding="utf-8")
        print(f"\nsnapshot written: {SNAPSHOT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
