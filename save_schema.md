# Phantom Doctrine save-file schema -- field semantics for safe extraction

Authoritative reference for reading `.PDSave` data. Written 2026-08-21 after two
save-read failures reached the player: base stats reported as live stats (wrong
hire recommendation, 2026-08-20) and a hidden-identity flag volunteered at
spoiler tier 0 (2026-08-19). Every rule below exists because a raw field was
read without knowing its semantics. **Read this before parsing any save XML.**

## The tools (use these, don't re-derive)

| Tool | Job |
|---|---|
| `save_watcher.py` | Decode + campaign summary (chapter, day, cash, danger). `--xml` dumps raw XML -- see "Gated fields" before using it. |
| `save_extract.py` | Per-agent roster JSON with semantics already applied: base vs current labeled, compounds mapped, FP/AP breakpoint distances computed. **Default tool for any agent-stat question.** |
| `save_state/compound_id_map.json` | Save compound-id -> compound-name mapping with per-id confidence. |

## Decode (owned by save_watcher.py)

`.PDSave` = UTF-8 XML XOR-obfuscated with `key[i] = (0x45 + i) & 0xFF`. Result:
a `<meta><IWTBSaveMetadata .../></meta>` header then one `<IWTBSAVE>` document.
Slot discovery: `%LOCALAPPDATA%\PhantomDoctrine\Saved\<steamid>\SaveGames`.

## `<agent>` fields -- semantics table

Each agent is one `<agent ...>` element with a nested `<Stats .../>` child.
Semantics classes: **live** (current as of the save), **base** (pre-compound,
never current), **id** (internal token, not player-facing), **volatile** (lags
live play), **gated** (spoiler / unresolved -- see below), **dead** (serializes
0, never read).

| Field | Class | Meaning + trap |
|---|---|---|
| `uniqueid` | id | **The ONLY stable per-agent key** (`default_avatar_us_male`, `generated_agent_51`, `story_agent_lamster`). Survives renames, rehires and codename rerolls. Match your notes on this. |
| `firstname` / `lastname` | **volatile** | Real name -- **NOT stable, do not key on it.** The in-game new-identity mechanic rewrites it: two agents matched on `uniqueid` (`default_avatar_us_male` and `generated_agent_51`) changed names between saves while base stats, background, nationality and portraitid stayed unchanged. An agent who "vanished" from a name search is almost always renamed, not gone. |
| `codename` | id | Internal token (`generated_agent_NNN` or `false`). **The display codename (for example, Lamster) is NOT in the save** -- map via a screenshot or the player's own notes. |
| `hirestate` | live | `HiredByPlayer` / `OnPlayerHireList` / `HiredByEnemy` / `NotInitialized` / `OutOfLoop`. |
| `HP` | volatile | Live current HP (the one live stat on the parent tag). Lags the game -- an agent read 49 in a save while a fresher read showed 18. |
| `Stats` `Stat_A/B/C/D` | **base** | **A=Circulatory, B=Respiratory, C=Sensory, D=Motoric** (verified 2026-08-21, 3-agent screenshot solve). ALWAYS pre-compound base, for every agent, hired or not -- it only *looks* current on an agent with zero compounds. Current = base + applied compounds (see below) or a dossier screenshot. Never report these as an agent's stats directly. |
| `Stats` everything else (`Max_HP`, `Max_AP`, `DodgeCost`, `Max_Awareness`, ...) | dead | Serialize 0 in saves. Derived stats are NOT in the save; get them from a dossier screenshot. |
| `compounds` | live | Comma list of opaque ids (`compound_01,...`). Map via `save_state/compound_id_map.json`; unmapped id -> current stats not computable, say so. |
| `abilities` / `reactiveabs` | live | Internal ability ids; readable names, safe. |
| `levelupperks` | **trap** | **The PENDING LEVEL-UP DRAW (the options being offered), NOT the agent's owned perks.** An example agent with 7 owned perks has an **empty** field; another agent's field reads `intuitionperk_20,22,28,14`, matching the 4-option draw offered at level-up, while owned Survivor and Low Profile are absent. It is populated on agents sitting at a fresh level-up. **Never name an agent's perks from this field.** Owned perks come from the in-game tooltip or a player report. Use this field to identify options offered for the next pick. |
| `completedtrainings` / `currenttrainingID` | live | Internal training ids (`training_01`). id->display-name mapping was resolved for all 16 ids (2026-08-26) from the game's own text; that mapping is not shipped with this guide, so take training names from the in-game tooltip (`items/abilities.md` lists the training names). |
| `agencybg` | live | Background id (`background_kgb`) -> `items/abilities.md` "Agent backgrounds". |
| `languages`, `nationality`, `cost`, `xp`, `rank` | live | Straightforward. |
| `c_place` / `d_place` / `o_place` | id | Internal place ids (`place_054`); id->zone mapping unfinished (`limitations.md`). |
| `sidestoryparticipant`, `undercover`, `revealstatus`, `knownbyai` | **gated** | Can encode hidden-identity / story state. Caused the 2026-08-19 tier-0 mole leak AND was misread again 2026-08-20. Excluded from `save_extract.py` unless `--gated`. Never volunteer; answer only the narrow asked question per `warning_tiers.md` Breach log. |
| `iscritical` | **dead (for our purposes)** | **RESOLVED 2026-09-16: carries no information about the agent's condition -- never report or interpret it.** It is set once when a character is generated and never changes afterwards. Evidence: across all 12 save slots plus the 2026-08-20 dump, no existing agent ever flips it; the roster-wide count only rises when a *new* agent appears already carrying it. It is true only on procedurally generated characters (every `story_*`, `default_*` and `tutorial_*` vispreset reads false, as does every `neverchange="true"` and every `ReservedForGD` character), runs ~47% true among generated ones, and is uncorrelated with HP, wounds, medical hold, stats, cost, hirestate, capture, limbo or story participation. Its position in the tag confirms the reading: it sits inside the appearance block (`visobject, vispreset, iscritical, ismale, portraitid, firstname`), not near the health or story flags. |

Campaign-level volatile fields (`Cash`, `Danger` on `<strategic>`): same
staleness rule -- after a hire the save's cash lagged the transaction entirely.
State "as of save <in-game timestamp>", never "now".

## Computing current stats (the base-stat trap, solved)

```
current[stat] = Stat_<letter> + sum(compound primary deltas, corrected order)
```

Validation record (2026-08-21, extended by the same-day screenshot-archive
sweep to **12 dossier cross-checks, zero contradictions**): agent A 92/67/75/75
computed = dossier exactly; agent B pre-EPO 79/82/82/84 exactly; agent C's full L6
dossier 71/62/74/60 exactly; Lamster 73/76/77/76 = base + AMPEA + BMA
exactly; plus six exact base matches (including agent A before compounds)
and two further agents matching base + AMPEA.
The same solve proved the corpus compound table's original Sens/Resp columns
were transposed (now corrected in `items/abilities.md` -- headers there are
the fixed order).

**Treatment-popup Awareness anomaly (n=4):** the Body Engineering
treatment-complete popup's MAX AWARENESS "before" consistently reads
dossier-value-minus-delta (popup-after == same-era dossier). Cause
unresolved; never chain popup Awareness numbers with dossier numbers. Detail:
`ui_reference.md` "Treatment Complete popup".
FP/AP tiers from current stats: Circ >=150 -> 2 FP, >=200 -> 3 FP; Moto >=100
-> 3 AP, >=140 -> 4 AP (`mechanics.md`).

**Precedence: a fresh dossier screenshot > computed current > nothing. Base
stats alone are never an answer to "what are their stats."** Known open
anomaly: an example agent card carried current stats equal to base + exactly
2x AMPEA -- likely a double-count when the card was built;
re-verify any such card against the agent's dossier.

## Compound id mapping -- how to extend it

Ids are assigned by the game, order unknown; the map is built from evidence:

1. **Application diff (best):** when the player applies a compound in-game,
   run `save_extract.py` after the next save; the new id in that agent's
   `compounds_raw` IS that compound. Add it to `compound_id_map.json` with the
   date + agent as evidence.
2. **Delta solve:** for an agent with N unmapped ids, a dossier screenshot, and
   known base: `screenshot - base` must equal the sum of N compounds' deltas;
   search the table for the unique combination. (This is how AMPEA/BMA were
   pinned.) Only accept exact 4/4 matches.

## Re-deriving all of this from scratch (if the game patches the format)

1. Decode per `save_watcher.py` docstring; confirm `IWTBSAVE` appears.
2. Letter mapping: find an agent with `compounds=""` and a dossier screenshot
   stat line with four distinct values; match letters to stats directly.
3. Base-vs-current: pick an agent with compounds; if `Stat_A-D` != dossier,
   they are still base (expected). If a patch makes them current, the constant
   hire-pool delta trick (step 2 of "Compound id mapping") stops working --
   re-document before trusting anything.
4. Update this file with the evidence, dated.

## Tactical saves expose live loot and document positions

**Discovered live-play 2026-08-22.** Strategic saves (`pdsauto*`, `pdregular*`,
`savetype="1"`, `Strategic="1"`) carry no map contents. **Tactical saves
(`pdtauto*`, `savetype="2"`, `Strategic="0"`, `MapName="L###_..."`) do.** This
answers "where is the remaining loot on this map" directly, with no mod and no
screenshot. Supersedes `mechanics.md`'s "no remaining-loot counter exists" as
the last word: no *in-game* counter exists, but the save has the data.

Placed world objects serialize as `<GridObj>`. The loot-bearing ones carry a
`MaxUses` / `UsedTimes` pair:

| Attribute | Meaning |
| --- | --- |
| `grid_object_class` | `LootContainer_Safe_C`, `LootContainer_Closet_C`, `LootContainer_Briefcase_C`, `SecretContainer_SecretFile_C`, `SecretContainer_Map_C`, `SecretContainer_Blueprints_C`, `CCTVCentral_C` |
| `UsedTimes` vs `MaxUses` | `0/1` = **not yet taken**. `1/1` = already looted -- but see the correction below before treating `0/1` as "still worth going for." |
| `lootcon` | `true` on real loot/document containers. **Correction, 2026-09-16: NOT true on every container class** -- `CCTVCentral` reads `lootcon="false"`. It's an objective interactable (hack the cameras), never a pickup, despite otherwise looking like a container in this element. |
| `secretcon` | `true` = intel/document (yellow glow). `false` = gear loot (blue glow). Matches the two-glow-color rule in `mechanics.md`. |
| `loot` | **Correction, 2026-09-16: this is the authoritative "is this container a real mission objective" signal, not an occasional hint.** A container can have `lootcon="true"` and still be an unpopulated decoy/prop with `loot=""` that was empty from the very first read (never counts toward the mission's own LOOT COLLECTED / CLASSIFIED DOCS COLLECTED HUD tallies -- confirmed against a HUD screenshot). **But the game also clears `loot` to `""` once a real container IS taken**, so a snapshot taken after pickup can't distinguish "always empty" from "real, already collected" by looking at `loot` alone -- only by having seen it non-empty on an earlier read. A reader that needs this should keep a cache of every container ever seen with real contents, keyed on `(map, class, floor, tile)` -- not on `uniqueid`, because a container's real payload can be lost for good once every tactical autosave slot (only `pdtauto0/1/2`, 3 total) has rotated past the snapshot that showed it non-empty. Hit exactly this 2026-09-16: 6 already-taken real objectives had no surviving on-disk snapshot with their `loot` populated by the time the mismatch was noticed. |
| `actor_xloc` / `actor_yloc` / `actor_zloc` | World units. See conversion below. |

**Coordinate conversion (derived 2026-08-22, not vendor-documented).**
`<GridObj>` uses world units; `<tchar>` uses tile indices. **tile = world / 60**
(verified: every container on `L093_ESCI_soviet_blocks` divided to a clean
integer, and the range matched the player agents' own `xloc`/`yloc`).
Floor from `actor_zloc`: `~0` = floor 0, `~305` = floor 1, `~600` = floor 2
(matches `<tchar zloc="0|1|2">`). Confidence medium: one map, one sample.
Re-verify the divisor on a second map before trusting it blindly.

**Read your own agents' positions** from `<tchar Side="HumanPlayer">` to convert
a container tile into a direction to walk.

_source: live-play save parse 2026-08-22 (`pdtauto0.PDSave`, map
`L093_ESCI_soviet_blocks`) · capture: manual_paste · confidence: high (mechanism
and attribute semantics read directly from the save) / medium (tile divisor and
floor thresholds derived from one map) · enemy-tier: 0 · puzzle-tier: 0 ·
category: meta (tooling, not in-game content) · spoiler: none_

## Workshop tech-tree research state is readable from strategic saves

**Discovered live-play 2026-08-22.** Alongside `<facilitylist>`, strategic saves
carry a tech list where each tracked Workshop tech serializes as
`<tech uniqueid="tech_NNN" facility="mechanicalworkshop" status="..." start="..." time="..." duration="..." />`.
Confirmed on `pdregular3.PDSave` (Day 28): 194 tracked entries. `status` is one
of `Researched` (35, done) / `Unlocked` (15, available to research right now)
/ `Unavailable` (144, still gated behind unmet prerequisites). `Unlocked` is
the direct answer to "what can I research right now" -- no screenshot needed.

**Known gap: id -> name/effect mapping does not exist.** Unlike compounds
(`compound_id_map.json`), there is no `tech_id_map.json`. `items/upgrades.md`
already flags this as unresearched: the tree exists (113 elements per
research) but per-upgrade detail -- what each id actually unlocks -- was never
catalogued; LordRedStone's "Tech Upgrades Flowchart" Steam guide is the
cited-but-unfetched source. Raw `tech_NNN` ids are not player-facing and
should never be presented to the player as if they were a recommendation.
**Also unreconciled:** the save's 194 tracked entries vs. the corpus's
researched "113 elements" figure -- open whether the save tracks non-Workshop
techs too, or 113 undercounts.

_source: live-play save parse 2026-08-22 (`pdregular3.PDSave`) · capture:
manual_paste · confidence: high (fields read directly) / none (id->name
mapping, does not exist yet) · enemy-tier: 1 · puzzle-tier: 0 · category: meta
(tooling, not in-game content) · spoiler: progression_

**Checked and ruled out, 2026-08-22: no loose game-data source solves the id mapping.** The game's Steam install folder ships loose XML under `Content\Data\Design\` but it's mission/campaign logic only, no tech-tree file, and the one `tech_`-prefixed XML block found is stale dev placeholder content on a different id scheme (see `mechanics.md` "Third-party modding" correction, 2026-08-22). The real definitions are compiled into two `.pak` archives (~23GB total) -- readable only with an Unreal asset-extraction tool, not attempted. Delta-solving via in-game play (above) remains the working method.

### How this was found (recreate it on any unmapped save field)

The finding above did not come from searching the save for the word "loot". It
came from **enumerating every XML element name in the file and looking at what
was there.** A keyword search would have missed it: the element is called
`GridObj`, which contains no word a person would think to grep for. Repeat these
five steps against any question of the form "does the save know X?"

**Step 1 -- list the real save directory, newest first.** Do not reason from
`save_schema.md` about which saves exist. Look. (Run the one-liners in this
section from the guide folder, where `save_watcher.py` lives.)

```bash
python -c "import glob,os,time;from save_watcher import find_save_dir;d=find_save_dir();print(d);[print(time.strftime('%H:%M:%S',time.localtime(os.path.getmtime(f))),os.path.getsize(f),os.path.basename(f)) for f in sorted(glob.glob(os.path.join(str(d),'*.PDSave')),key=os.path.getmtime,reverse=True)[:12]]"
```

Filename prefix is the save class and it is the whole trick: `pds*` = strategic
autosave, `pdregular*` = manual, **`pdt*` = tactical (in-mission)**. Tactical
saves are also visibly larger (~2.2 MB vs ~1.37 MB). Anyone reading only
`save_schema.md`'s strategic-save documentation concludes the data does not
exist; the directory listing shows it does in one command.

**Step 2 -- decode the newest tactical save and confirm what it is** via the
`<IWTBSaveMetadata>` header: `savetype="2"`, `Strategic="0"`, and a populated
`MapName`. That header is the authoritative tactical/strategic discriminator.

**Step 3 -- enumerate element names, do not grep for content words.** This is
the load-bearing step and the one that generalizes:

```bash
python -c "import re,collections;from save_watcher import decode_save,find_save_dir;x=decode_save(find_save_dir()/'pdtauto0.PDSave');print(collections.Counter(re.findall(r'<([A-Za-z_][\w.:-]*)',x)).most_common(50))"
```

`GridObj` x176 stood out as "placed world objects" purely from the count and the
name. No prior knowledge of the schema was needed.

**Step 4 -- dump that element's full attribute-key census, not a sample.** Print
every distinct attribute name across all instances with its frequency. The
partial-coverage keys are the signal: `MaxUses` / `UsedTimes` / `lootcon` /
`secretcon` appeared on exactly 10 of 176 objects, which is what identified the
container subset. A first-five-rows sample would have shown only doors and
windows and looked like a dead end.

**Step 5 -- resolve coordinates against something already trusted.** `GridObj`
world units meant nothing alone. Dividing by 60 was confirmed correct only
because it produced clean integers in the same numeric range as the
`<tchar Side="HumanPlayer">` agents' own `xloc`/`yloc`. Always calibrate an
unknown coordinate space against a known one inside the same file.

**Transferable rule.** When a doc is silent about a capability, that silence is
evidence about the doc, not about the game. Enumerate the artifact's actual
structure before concluding a field does not exist. The cost here was two
commands.

_source: live-play save parse 2026-08-22 · capture: manual_paste · confidence:
high (procedure re-run and verified end to end) · enemy-tier: 0 ·
puzzle-tier: 0 · category: meta (tooling, not in-game content) · spoiler: none_
