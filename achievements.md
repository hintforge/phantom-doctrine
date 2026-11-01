# Phantom Doctrine -- Achievements

**status:** research-integrated
**last_reconciled:** 2026-08-18 (P2 -- Broadsword achievement-name reconciliation, Misplaced Trust candidate note)
**stub_source:** vgtimes.com (Stage 0) + P1 deep-research (trigger conditions, rarity, trigger-type classification)
**stub_fetched:** 2026-08-17 / **P1 research:** 2026-08-18

## Why this file exists

This file is the corpus's single source of truth for "what achievements does this game have, and what do I need to do for each one." The reader consults it when the player asks any achievement-class question -- by name, by category, or by "what am I about to miss."

## Coverage check

All 47 achievements: **resolved.** None deferred, none unreachable. Trigger conditions paraphrased -- Steam's own description text is never reproduced verbatim (only the achievement name is verbatim, per platform-lookup convention).

Rarity % are point-in-time Steam globals from Exophase; console/trophy rarities differ (e.g. *The End? - Hard* is the rarest PS4 trophy at 1.6% per MetaGame.guide, vs 3.1% Steam).

**Genre vocabulary:** no corpus-specific `genre:` values declared for this game -- Phantom Doctrine's achievement set doesn't carry social/roguelike/mission/multiplayer/meta/class-style structural patterns beyond the standard trigger-type taxonomy.

---

## Progression

Default-path achievements every player earns by advancing normally.

| # | Name | Hidden | Rarity% | Trigger | PoNR / prereq |
|---|---|---|---|---|---|
| 4 | Once Bitten, Twice Shy | **Yes** | 32.9 | Escape the Glasgow trap (Ch2, `c2_glasgow`) | chapter-bound |
| 5 | Rock the Boat | **Yes** | 20.9 | Recover Marquis cargo (Ch3 houseboat, `c3_houseboat`) | chapter-bound |
| 6 | Communication Noise | **Yes** | 18.8 | Reach the comm-station save-attempt (Ch4, `c4_commstation`); scripted-fail still counts | chapter-bound |
| 7 | Explosive Measures | **Yes** | 17.3 | Destroy the Broadsword facility (Ch5, `c5_numbers_station`) | chapter-bound |
| 9 | The End? - Easy | No | 15.2 | Beat the Iceberg finale on Easy (a Hard clear unlocks all three) | -- |
| 10 | The End? - Normal | No | 8.8 | Beat the finale on Normal | -- |
| 12 | No One Noticed | No | 7.0 | Capture Tai-Pan (Ch3, `c3_taipan_capture`) without raising alarm | missable -- classified `mastery`, see below (execution-skill achievement, listed here for narrative reference only) |
| 14 | Spy | No | 14.8 | Extract intel from Sears Tower (Ch7, `c7_searstower`) | chapter-bound |
| 18 | Blank Slate | No | 27.0 | Brainwash an agent (MK-ULTRA) | needs facility |
| 19 | Tailor | No | 72.9 | Change an agent's identity (Forger) | needs Forger |
| 20 | Conspiracy Revealed | No | 83.8 | Solve one secret file (Investigation Board) | -- |
| 22 | Airborne Extraction | No | 8.0 | Buy helicopter evac for a mission | -- |
| 31 | Bite the Bullet | No | 56.3 | Survive an ambush | -- |
| 33 | Calculated Risk | No | 15.7 | Implant + use a trigger phrase (control an enemy mid-mission) | needs MK-ULTRA control phrase |

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · category: mainline_

## Branch

Mutually-exclusive-path achievements -- earning one within a playthrough forecloses an alternative.

| # | Name | Hidden | Rarity% | Trigger | branch-excludes |
|---|---|---|---|---|---|
| 1 | Comrade Spy | No | 16.5 | Finish Ch1 KGB (submarine mission) | *US Intelligence*, *The Institute* (starting-agency choice is exclusive per playthrough) |
| 2 | US Intelligence | No | 36.7 | Finish Ch1 CIA (Beirut raid) | *Comrade Spy*, *The Institute* |
| 3 | The Institute | No | 4.8 | Finish Ch1 Mossad; Mossad unlocked only after 1 prior campaign clear | *Comrade Spy*, *US Intelligence* |
| 8 | Tip of the Iceberg | **Yes** | 16.1 | Finish Ch6 Almaz on a **regular** (non-Extended) playthrough | excluded entirely on Extended-campaign saves |
| 15 | Same, but Different | No | 4.2 | Recover Marquis cargo from a different safehouse (Extended-only houseboat variant) | mutually exclusive with *Rock the Boat*'s regular-playthrough version within the same save |
| 16 | Death of a Citizen | No | 4.0 | Kill Broadsword in Munich (Ch5, Extended-only variant) | mutually exclusive with regular-playthrough *Explosive Measures* path within the same save |
| 17 | The Whole Truth | No | 3.6 | Finish the Extended campaign (Ch8, kill Tai-Pan) | NG+ only -- excluded entirely on a save that never unlocks/plays the Extended campaign |

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · category: mainline_ **(added at stitch 2026-08-18 -- #17 was present in the raw P1 research result but dropped during P1 ingestion; `nav/c8_killtaipan.md` and `npcs/tai-pan.md` already cited this achievement and pointed here, so the corpus's own Coverage Check claim of "all 47 resolved" was inaccurate until this row was restored.)**

## Mastery

Skill demonstrations or self-imposed restrictions beyond normal play.

| # | Name | Hidden | Rarity% | Trigger / constraint |
|---|---|---|---|---|
| 11 | The End? - Hard | No | 3.1 | Beat the finale on Hard difficulty -- a restriction beyond normal play |
| 12 | No One Noticed | No | 7.0 | Capture Tai-Pan (Ch3) with zero alarm raised -- needs Actor-perk disguised agents, Tai-Pan's corner is static so plan the mission last |
| 13 | Blessing in Disguise | No | 11.6 | Rescue Boldface (Ch4) using a disguised agent specifically -- 1600 XP stealth bonus |
| 32 | Trust No One | No | 4.1 | Complete ALL secret files manually in one playthrough -- never assign Analytics to auto-solve any |
| 42 | Step into the Breach | No | 19.5 | Breach a room with 4+ agents simultaneously |
| 43 | Pacifist | No | 20.2 | Finish a level in infiltration mode without hurting anyone |
| 44 | Sadist | No | 14.1 | Kill six enemies in a single turn |
| 45 | Combined Arms | No | 7.4 | Use four different Support Powers in one turn -- needs support tech unlocked |

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · category: mainline_

## Collection

Finite, named sets the player must complete in full.

| # | Name | Hidden | Rarity% | Trigger | Set |
|---|---|---|---|---|---|
| 21 | Fully Operational | No | 28.2 | Unlock all facilities | 8 HQ facility screens (Crew Quarters, Comms, Forger, Infirmary, Workshop, Analytics, Body Engineering, MK-ULTRA) |
| 23 | Well-equipped | No | 5.4 | Research all tech upgrades in one playthrough | Workshop tech tree, 113 elements |
| 24 | Tactical Support | No | 16.6 | Own one of each Support Power type in a playthrough | Spotter, Sniper support, Grenade launcher, Cleaner (see `items/support_items.md`) |
| 30 | Cold Truce | No | 3.8 | Have a mission squad with CIA + KGB + Mossad + Stasi + SB agents together | 5 named agency-origin agent types; RNG-recruitment-dependent |
| 39 | Lootcrates are Forever | No | 80.4 | Collect all loot + documents on a single level | per-level loot/document set (varies by mission) |
| 47 | Syndicate Engineering | No | 11.0 | Engineer an agent with all four core stats >=140 (via Body Engineering) | 4 named stats |

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high (medium on Cold Truce's RNG-recruitment dependency) · category: mainline_

## Threshold

Cumulative counts with no finite ceiling -- any qualifying unit counts.

| # | Name | Hidden | Rarity% | Trigger |
|---|---|---|---|---|
| 25 | Tinker | No | 12.1 | Craft 50 items (Workshop) |
| 26 | Merchant | No | 11.8 | Buy 50 items |
| 27 | Tactical Espionage | No | 33.3 | Find 50 secrets on tactical levels |
| 28 | Tactical Plunder | No | 37.8 | Loot 50 containers |
| 29 | Top Tier | No | 4.7 | Get an agent to max level (20) |
| 35 | Soldier | No | 37.6 | Kill 100 enemies |
| 36 | Veteran | No | 19.2 | Kill 250 enemies |
| 37 | Licence to Kill | No | 21.2 | Kill 15 enemy **agents** specifically (not generic mooks) |
| 38 | Inside Job | No | 10.2 | Destroy 5 enemy cells using sleeper agents -- needs a planted control phrase |
| 40 | Scientist | No | 13.5 | Apply 50 chemical compounds -- needs Body Engineering |
| 41 | Counterfeit Fortune | No | 4.5 | Forge $500,000 total (Forger) |

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · category: mainline_

## Discovery

Non-obvious interactions -- the trigger's existence, not its execution, is the achievement.

| # | Name | Hidden | Rarity% | Trigger |
|---|---|---|---|---|
| 34 | Misplaced Trust | No | 12.7 | Witness an agent betrayal during a tactical mission | `confidence: low -- still unconfirmed at P2. Candidate but NOT verified: the c2_glasgow handler-goes-rogue reveal (Turncoat) is a scripted in-mission betrayal that fits this description, but P2 research did not explicitly name it as this achievement's trigger -- don't present as confirmed. Verify at P3 or from live play.` |
| 46 | Silent Power | No | 11.3 | Mod a shotgun with a silencer -- non-obvious weapon/mod-type pairing | needs a silencer blueprint |

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: medium (see Misplaced Trust note) · category: mainline_

---

## Verbatim spelling notes

"Once Bitten, Twice Shy" (comma), "Licence to Kill" (British spelling), "Well-equipped" (hyphen, lowercase e), "Same, but Different" (comma), "Lootcrates are Forever" (one word "Lootcrates"), "The End? - Easy/Normal/Hard" (question mark + space-hyphen-space).

## Achievement-name spoiler flag

The 5 hidden entries (Once Bitten, Twice Shy / Rock the Boat / Communication Noise / Explosive Measures / Tip of the Iceberg) reveal mid/late mission beats by name alone -- treat the **names themselves** as `spoiler: late-game`, gated below enemy-tier 2, in addition to their trigger content.

## Sources

- [Phantom Doctrine -- all achievements, trophies, and awards -- vgtimes.com](https://vgtimes.com/games/phantom-doctrine/achievements-and-trophies/) (stub names + hidden flags, Stage 0)
- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12) -- trigger conditions, mission IDs.
- PSNProfiles / TrueAchievements roadmaps, Exophase (Steam rarity), MetaGame.guide (console trophy rarity).
