"""Phantom Doctrine save watcher.

Reads the most-recently-modified save file and reports both file freshness
(which slot changed, when) AND real in-game state: chapter, day, hideout
location, current map, cash, danger, difficulty, ironman flag.

FORMAT (established 2026-08-18 by analysis of all ten save slots on disk):
`.PDSave` is plain UTF-8 XML, obfuscated -- NOT encrypted -- with a repeating
XOR keystream whose key byte is simply an incrementing counter:

    key[i] = (0x45 + i) & 0xFF        # period 256, identical in every save

To read a save: decode the file as UTF-8, take each character's codepoint as
one payload byte, then XOR by the counter above. The result is the game's XML
(`<meta><IWTBSaveMetadata .../></meta>` followed by an `<IWTBSAVE>` document).

Evidence the earlier "encrypted" classification was wrong: XOR-ing two
different saves together yields bytes that are 100% below 0x80 with only ~134
distinct values -- the signature of two 7-bit-ASCII plaintexts sharing one
keystream. Real encryption (per-save IV) cannot produce that, and no save
carries per-file key material: two different saves are byte-identical wherever
their plaintext matches. The original call rested on "no readable strings in
the first 16KB", which distinguishes "not plaintext" but not "encrypted" from
"obfuscated" or "compressed".

This script is READ-ONLY. It never writes to a save file.

Agent-level questions: use `save_extract.py` (semantics-labeled roster JSON)
instead of grepping `--xml` output. Field semantics + the raw-read traps
(base-vs-current stats, gated spoiler fields, staleness): `save_schema.md`.

Usage:
    python save_watcher.py            # latest save: freshness + in-game state
    python save_watcher.py --snapshot # also write save_state/latest.json
    python save_watcher.py --all      # every slot
    python save_watcher.py --xml      # dump the decoded XML of the latest save
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from pathlib import Path

# === CONFIGURE ===

# Phantom Doctrine keys its save folder by Steam64 ID under
# %LOCALAPPDATA%\PhantomDoctrine\Saved\<steamid>\SaveGames -- the ID is
# per-player, so we auto-discover it instead of hardcoding one player's ID
# (keeps this script portable if the guide is ever shared).
SAVED_ROOT = Path(os.environ.get(
    "PHANTOM_DOCTRINE_SAVED_ROOT",
    os.path.expandvars(r"%LOCALAPPDATA%\PhantomDoctrine\Saved"),
))

# Non-save-slot subfolders under Saved\ to ignore when auto-discovering the
# Steam-ID folder.
_NON_SLOT_DIRS = {"Config", "Crashes", "Logs"}

SAVE_GLOB = "*.PDSave"
EXCLUDE: set[str] = set()  # PlayerProfile.dat / steam_autocloud.vdf don't match the glob anyway.

SNAPSHOT_DIR = Path(__file__).parent / "save_state"

# The obfuscation key: an incrementing byte starting at 0x45, wrapping at 256.
XOR_KEY_START = 0x45


@dataclass
class SaveSummary:
    slot_path: str
    slot_name: str
    modified: str
    # In-game state (None when a save can't be decoded -- freshness still works).
    readable: bool = False
    chapter: str | None = None
    day: str | None = None
    in_game_timestamp: str | None = None
    hideout_location: str | None = None
    current_map: str | None = None
    level_name: str | None = None
    mode: str | None = None          # "strategic" (hideout/world map) or "tactical" (mission)
    campaign_stage: str | None = None
    cash: str | None = None
    danger: str | None = None
    difficulty: str | None = None
    ironman: str | None = None
    agents: int | None = None
    notes: list[str] = field(default_factory=list)


def decode_save(path: Path) -> str | None:
    """Return the save's decoded XML, or None if it doesn't match the known format."""
    try:
        raw = path.read_bytes().decode("utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    # Each character's codepoint is one payload byte (a few stray codepoints
    # above 0xFF appear in the wild; they are not part of the header we read).
    payload = bytes((ord(c) if ord(c) < 256 else 0x3F) for c in raw)
    plain = bytes(b ^ ((XOR_KEY_START + i) & 0xFF) for i, b in enumerate(payload))
    text = plain.decode("ascii", "replace")
    return text if "IWTBSAVE" in text[:4096] else None


def _attrs(xml: str, tag: str) -> dict[str, str]:
    """Pull the attributes of the first <tag ... /> occurrence."""
    m = re.search(r"<" + re.escape(tag) + r"\b([^>]*)>", xml)
    if not m:
        return {}
    return dict(re.findall(r'(\w+)\s*=\s*"([^"]*)"', m.group(1)))


def summarize(path: Path) -> SaveSummary:
    mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat()
    summary = SaveSummary(slot_path=str(path), slot_name=path.stem, modified=mtime)

    xml = decode_save(path)
    if xml is None:
        summary.notes.append(
            "could not decode: file does not match the known XOR-obfuscated XML format "
            "(the game may have changed it -- re-derive before trusting this script)"
        )
        return summary

    meta = _attrs(xml, "IWTBSaveMetadata")
    game = _attrs(xml, "game")
    strat = _attrs(xml, "strategic")

    summary.readable = True
    summary.chapter = meta.get("OperationName") or strat.get("ChapterID")
    summary.day = meta.get("Day")
    summary.in_game_timestamp = meta.get("Timestamp")
    summary.hideout_location = strat.get("HideoutLocation") or meta.get("Location")
    summary.current_map = strat.get("CurrentMapName") or meta.get("MapName") or None
    summary.level_name = game.get("levelname") or None
    summary.mode = "strategic" if meta.get("Strategic") == "1" else "tactical"
    summary.campaign_stage = strat.get("CampaignStage")
    summary.cash = strat.get("Cash")
    summary.danger = strat.get("Danger")
    summary.difficulty = strat.get("DifficultyLevel")
    summary.ironman = strat.get("ironman")
    summary.agents = len(re.findall(r"<agent\b", xml)) or None
    summary.notes.append(
        "location/map/chapter values are the game's internal ids (e.g. place_000, "
        "ChapterName_02); they are not player-facing names"
    )
    return summary


def find_save_dir() -> Path | None:
    """Auto-discover <Saved>/<steamid-or-hash>/SaveGames, or use the env override directly."""
    override = os.environ.get("PHANTOM_DOCTRINE_SAVE_DIR")
    if override:
        return Path(override)
    if not SAVED_ROOT.exists():
        return None
    for child in SAVED_ROOT.iterdir():
        if not child.is_dir() or child.name in _NON_SLOT_DIRS:
            continue
        candidate = child / "SaveGames"
        if candidate.is_dir():
            return candidate
    return None


def find_latest_save(save_dir: Path) -> Path | None:
    candidates = [
        p for p in save_dir.glob(SAVE_GLOB)
        if p.name not in EXCLUDE and p.is_file()
    ]
    if not candidates:
        return None
    return max(candidates, key=lambda p: p.stat().st_mtime)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", action="store_true",
                        help="Write JSON snapshot to save_state/latest.json")
    parser.add_argument("--all", action="store_true",
                        help="Print summary for every save slot")
    parser.add_argument("--xml", action="store_true",
                        help="Dump the decoded XML of the latest save to stdout")
    args = parser.parse_args()

    save_dir = find_save_dir()
    if not save_dir or not save_dir.exists():
        print(f"save dir not found (looked under {SAVED_ROOT}); "
              f"set PHANTOM_DOCTRINE_SAVE_DIR to override", file=sys.stderr)
        sys.exit(1)

    if args.all:
        for path in sorted(save_dir.glob(SAVE_GLOB)):
            if path.name in EXCLUDE:
                continue
            print(json.dumps(asdict(summarize(path)), indent=2))
        return

    latest = find_latest_save(save_dir)
    if not latest:
        print(f"no saves found in {save_dir}")
        sys.exit(1)

    if args.xml:
        xml = decode_save(latest)
        if xml is None:
            print(f"could not decode {latest}", file=sys.stderr)
            sys.exit(1)
        print(xml)
        return

    summary = summarize(latest)
    print(json.dumps(asdict(summary), indent=2))

    if args.snapshot:
        SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
        snapshot_path = SNAPSHOT_DIR / "latest.json"
        snapshot_path.write_text(json.dumps(asdict(summary), indent=2), encoding="utf-8")
        print(f"\nsnapshot written: {snapshot_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
