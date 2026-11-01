# Phantom Doctrine -- Upgrades

**status:** research-integrated
**last_reconciled:** 2026-08-22 (live-play pull, superseding the P1 stub below)

**Workshop tech tree:** 113 elements per the (now-removed) LordRedStone community count, across 15 facility categories. *Well-equipped* achievement = research the entire tree in one playthrough (see `../achievements.md` Collection).

**Facility expansions** unlock through Workshop tech + story progression (see `../mechanics.md` "HQ facility screens"). *Fully Operational* achievement = unlock all 8 facilities.

## Source note -- the original flowchart is gone

LordRedStone's "Tech Upgrades Flowchart" Steam guide (the source this file originally cited for the 113-element count) **has been removed from Steam Community for violating guidelines** -- confirmed 2026-08-22, visible only to the original author now. Its content lived entirely in three linked image files (imgur), never transcribed to text, so nothing is recoverable from it directly.

**Substitute source used instead:** the Phantom Doctrine Fandom Wiki's "Technology Tree" page, fetched clean 2026-08-22 (`https://phantom-doctrine.fandom.com/wiki/Technology_Tree`). It organizes the same underlying content differently -- **by story-chapter unlock gate** rather than by facility category -- and gives cost + research time for early chapters, name + effect only (no cost/time) from Chapter 4 onward. Chapter 3 Part 2's Workshop Upgrades section is itself blank in the wiki source (marked `???`) -- a gap in the substitute source, not something this pass introduced.

_source: live-play WebFetch 2026-08-22 (Phantom Doctrine Fandom Wiki, "Technology Tree") · capture: web_fetch · confidence: high (direct wiki fetch, internally consistent chapter-by-chapter table) · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_

## Save-id mapping -- still unsolved, here's the method

The save (`save_schema.md` "Workshop tech-tree research state") tracks 194 `<tech uniqueid="tech_NNN">` entries with `status: Researched/Unlocked/Unavailable` -- but only opaque ids, no names. This file supplies the names; nothing yet links a specific `tech_NNN` id to a specific named upgrade below. **Build that link the same way `compound_id_map.json` was built:** run `save_extract.py`-style raw tech dump before and after researching something in-game -- whichever id flips from `Unlocked` to `Researched` is that named upgrade. First confirmed pair goes in a new `save_state/tech_id_map.json`, evidence-dated, same format as the compound map.

## Workshop Upgrades by unlock gate

Each block header names the story beat that opens it, per the wiki source -- **shown here because the corpus's own `nav/` files already document the full chapter-by-chapter mission list at the same tier** (`mechanics.md`, `nav/architecture.md`); nothing below reveals a beat not already in this corpus. Still tagged `spoiler: progression` throughout -- Cardinal does not volunteer entries past the player's current chapter unprompted; this file is browsed player-side, same as any `nav/` file.

### Chapter 1 Part 1 -- available from campaign start

| Upgrade | Cost | Time | Effect | Requires |
|---|---|---|---|---|
| Forger Facility | $1000 | 10h | Unlocks the Forger facility (cash forging, identity customization). | -- |
| Recon Equipment | $1100 | 8h | Unlocks the Tactical Recon job -- tactical advantage during missions. | -- |
| Crew Quarters Expansion | $1550 | 14h | Increases the Agent limit. | -- |
| Analytics Expansion | $900 | 9h | Additional Investigation Board job slot. | -- |
| Infirmary Expansion | $700 | 8h | One more Infirmary slot. | -- |
| Infirmary Expansion (2nd) | $800 | 9h | One more Infirmary slot. | Infirmary Expansion (1st) |
| Hideout Perimeter Detectors | $1000 | 8h | Max Danger increased -- lowers raid risk. | -- |
| Improved Real Estate Contacts | $600 | 8h | More hideout candidates found on World Map. | -- |
| Optimized Printing Press | $1500 | 15h | Agents forge more cash. | Forger Facility |

### Chapter 1 Part 2 -- unlocks after "Tail the GRU agents converging on our hideout" (KGB path)

| Upgrade | Cost | Time | Effect | Requires |
|---|---|---|---|---|
| Body Engineering Facility | $1500 | 10h | Unlocks Body Engineering (compound stat boosts). | -- |
| Better Cashflow | $2400 | 13h | Increases passive income. | -- |
| Better Informer Search | $2200 | 16h | Informers discovered more frequently. | -- |
| Hideout Concealment | $750 | 5h | Danger threshold increased. | -- |
| Workshop Expansion | $1450 | 5h | One more Workshop crafting slot. | -- |
| Improved Forging Tools | $2100 | 17h | New identities are cheaper. | -- |
| Better Negotiations Methodology | $2600 | 14h | Faster Informer secret-document reveals. | Better Informer Search |
| Watermarking Tools | $800 | 6h | Agents tolerate more Heat before compromised. | Improved Forging Tools |
| High Quality Passports | $750 | 5h | Reduces travel/job penalties for compromised Agents. | Improved Forging Tools |

### Chapter 2 -- unlocks after "Assault the docks in Petropavlovsk to sabotage the K-429" (KGB path)

| Upgrade | Cost | Time | Effect | Requires |
|---|---|---|---|---|
| MKULTRA Facility | $1500 | 10h | Unlocks MKULTRA (brainwashing/interrogation). | -- |
| Forger Expansion | $2400 | 15h | One more counterfeiting job slot. | -- |
| Personnel Location Equipment | $1300 | 12h | Unlocks Seek Agent -- reveal enemy Agent activity. | -- |
| Personnel Surveillance Equipment | $1200 | 11h | Unlocks Tail -- reveal enemy Cells. | -- |
| Crew Quarters Expansion (2nd) | $3000 | 10h | Increases the Agent limit. | -- |
| Low-Profile Identities | $1450 | 11h | Agents lose Heat faster. | -- |
| Better Cryptography Procedures | $1750 | 8h | Faster Secret File investigation. | -- |
| Body Engineering Expansion | $1400 | 8h | One more Body Engineering slot. | -- |
| Wider Informer Search | $3100 | 9h | More Informers appear on World Map. | -- |
| Interpol Contacts | $1600 | 9h | Reduces combat Heat gain. | Low-Profile Identities |
| MKULTRA Expansion | $750 | 5h | One more MKULTRA slot. | MKULTRA Facility |
| Brainwashing Technology | $1500 | 9h | Unlocks Brainwashing treatment. | MKULTRA Facility |
| Solid Shovels | $750 | 5h | MKULTRA Executions cheaper. | MKULTRA Facility |
| Safer Brainwashing Chems | $3350 | 5h | Fewer perks lost during Brainwashing. | Brainwashing Technology |

### Chapter 3 Part 1 -- unlocks after "Recover Conspiracy cargo from the MI6 safehouse in Glasgow" (KGB path)

| Upgrade | Cost | Time | Effect | Requires |
|---|---|---|---|---|
| Communications Facility | $1500 | 10h | Unlocks Comms (signal-analysis document recovery). | -- |
| Hideout Camouflage | $3000 | 8h | Reduces enemy-Recon impact near HQ. | -- |
| Transportation Network | $2900 | 15h | Increases Agent travel speed. | -- |
| Better Perimeter Recon | $1350 | 9h | Additional Support slot on tactical missions. | -- |
| Major Infirmary Expansion | $1400 | 5h | Two more Infirmary slots. | -- |
| Brainwashing Process Optimization | $750 | 5h | Brainwashing costs less time/money. | -- |
| Interrogation Chemicals' Replacements | $1600 | 6h | Interrogation cheaper. | -- |
| Carefully Selected Informers | $3300 | 9h | Better odds of high-value Informer documents. | -- |
| Real Estate Market Data | $750 | 7h | Hideout candidates appear more often. | -- |
| Information Noise Filtering | $3400 | 14h | Fewer World Map false positives. | Transportation Network |

**This tier is the corpus's current best read on "what's available right now"** -- at the time of writing (Day 28, Ch3, `c3_taipan_capture` not yet done), the player was in the Ch3P1 window. The save's 15 currently-`Unlocked` techs are drawn from this tier plus any earlier tier not yet researched -- no exact id match yet (see mapping note above).

### Chapter 3 Part 2 -- unlocks after "Kidnap Tai-Pan from his HQ" -- **Workshop Upgrades not documented in the substitute source (marked `???`)**

Weapons/armor/blueprints/training/compounds for this tier are listed in the wiki source (and mostly already covered by `weapons.md` / `items/abilities.md`), but the Workshop-upgrade names themselves are a genuine gap here, not a spoiler-gating choice. Flagged in `../limitations.md`.

### Chapter 4 Part 1 onward -- name + effect only, no cost/time in the source; **not expanded here**

The wiki continues through Chapter 7 Part 2 with the same structure (Stakeout Equipment, Marquis Device, Conversion Technology, Major Workshop Expansion, MKULTRA Expansion tiers, Control Phrase/Saboteur/Conversion cost-reduction upgrades, evac/travel speed upgrades, and more) but without cost/time figures, and it is several chapters past the player's current position. **Not transcribed into this file** to avoid parking a wall of future-chapter content in the player's default corpus read -- ask directly ("what unlocks in Chapter 5") if you want to look ahead.

## Bonus finding: Training catalog is larger than previously documented

`../items/abilities.md` previously listed only 3 known trainings (unresearched beyond those). The same Fandom fetch surfaced training names per chapter: Contact Tactics, Urban Operations I, Basic Firearms Drill (Ch1P1); Fire and Movement Tactics, Covert Operations (Ch1P2); Intermediate Firearms Drill (Ch2); Rapid Dominance Tactics (Ch3P1); Night Operations, Advanced Firearms Drill (Ch3P2); Shock Tactics, Warzone Operations (Ch4P1); Specialist Firearms Drill (Ch4P2); Skirmish Tactics (Ch5); Guerilla Operations (Ch6); Expert Firearms Drill (Ch7P1); Black Ops Firearms Drill (Ch7P2). **Names only** -- no per-training effect/proficiency detail pulled this pass (that's `items/abilities.md`'s job to integrate properly; flagged there and in `../limitations.md`, not done here to stay scoped to the tech-tree ask).

_source: live-play WebFetch 2026-08-22 (same Fandom fetch) · capture: web_fetch · confidence: medium (names only, not cross-checked against in-game tooltips) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_

## Sources

- Phantom Doctrine Fandom Wiki, "Technology Tree" page (English, community-wiki, fetched 2026-08-22).
- LordRedStone, "Tech Upgrades Flowchart" (113 elements), Steam guide (English, 2018-2026) -- **REMOVED from Steam Community as of 2026-08-22, author-only visibility now.** Kept as a citation for the 113-element/15-category count (recovered from the page's surviving text summary) but no longer fetchable for detail.
