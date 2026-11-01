# Nav -- Index

**status:** research-integrated
**last_reconciled:** 2026-08-18

Sequential gate lists per zone. The persona consults files in this folder first for nav-class questions ("what mission is this?", "where do I go next?", "I'm stuck on mission X").

For the cross-zone structural backbone -- zone graph, edges, support topology, locks-and-keys -- see [`architecture.md`](architecture.md). For underlying mechanics (conspiracy board, disguises, HQ management), see [`../mechanics.md`](../mechanics.md). For per-mission missables, see [`../sections/missables.md`](../sections/missables.md). **This folder is routing only.**

## Files in this folder

| File | Type | Linear? | Status |
|---|---|---|---|
| [`architecture.md`](architecture.md) | zone graph + cascade outputs | n/a | research-integrated |
| [`hideout_hub.md`](hideout_hub.md) | hub | no | research-integrated |
| [`world_map.md`](world_map.md) | hub (strategic layer) | no | research-integrated |
| [`kgb_c1_gukos.md`](kgb_c1_gukos.md) | main-story (tutorial) | yes | research-integrated |
| [`kgb_c1_raid.md`](kgb_c1_raid.md) | main-story (raid) | yes | research-integrated |
| [`kgb_c1_submarine.md`](kgb_c1_submarine.md) | main-story | yes | research-integrated |
| [`cia_c1_nuclear.md`](cia_c1_nuclear.md) | main-story (tutorial) | yes (branches) | research-integrated |
| [`cia_c1_morgue.md`](cia_c1_morgue.md) | main-story | yes (branches) | research-integrated |
| [`cia_c1_beirut.md`](cia_c1_beirut.md) | main-story (raid) | yes | research-integrated |
| [`mossad_c1_chemlab.md`](mossad_c1_chemlab.md) | main-story (tutorial) | yes | research-integrated |
| [`mossad_c1_smugglers.md`](mossad_c1_smugglers.md) | main-story | yes (branches) | research-integrated |
| [`mossad_c1_diplomatique.md`](mossad_c1_diplomatique.md) | main-story | yes (branches) | research-integrated |
| [`c2_omikron.md`](c2_omikron.md) | main-story (shared) | yes | research-integrated |
| [`c2_glasgow.md`](c2_glasgow.md) | main-story (shared) | yes | research-integrated |
| [`c3_ivorycoast.md`](c3_ivorycoast.md) | main-story (shared) | yes (branches) | research-integrated |
| [`c3_houseboat.md`](c3_houseboat.md) | main-story (shared) | yes (branches) | research-integrated |
| [`c3_mkultra_plans.md`](c3_mkultra_plans.md) | main-story (shared) | yes (branches) | research-integrated |
| [`c3_warehouse_ambush.md`](c3_warehouse_ambush.md) | main-story (ambush) | yes | research-integrated |
| [`c3_taipan_capture.md`](c3_taipan_capture.md) | main-story (shared) | yes (branches) | research-integrated |
| [`c4_boldface.md`](c4_boldface.md) | optional | yes | research-integrated |
| [`c4_vancouver.md`](c4_vancouver.md) | main-story `[P2-added]` | yes (branch) | research-integrated |
| [`c4_gdansk.md`](c4_gdansk.md) | optional `[P2-added]` | yes | research-integrated |
| [`c4_commstation.md`](c4_commstation.md) | main-story | yes (branches) | research-integrated |
| [`c5_siliconvalley.md`](c5_siliconvalley.md) | main-story (ambush) | yes | research-integrated |
| [`c5_terrorcell.md`](c5_terrorcell.md) | main-story | yes (branch) | research-integrated |
| [`c5_numbers_station.md`](c5_numbers_station.md) | main-story | yes (Extended variant) | research-integrated |
| [`c6_turncoat.md`](c6_turncoat.md) | main-story (ambush) | yes | research-integrated |
| [`c6_penthouse.md`](c6_penthouse.md) | main-story `[P2-added]` | yes (branch) | research-integrated |
| [`c6_almaz.md`](c6_almaz.md) | main-story (Extended variant) | yes | research-integrated |
| [`c7_searstower.md`](c7_searstower.md) | main-story | yes (branches) | research-integrated |
| [`c7_iceberg.md`](c7_iceberg.md) | main-story (finale) | yes | research-integrated |
| [`c8_killtaipan.md`](c8_killtaipan.md) | main-story (Extended/NG+ finale) | yes | research-integrated |

**Per-mission gate-list files were created at P2 ingestion (2026-08-18)**, per framework convention. 31 files total (2 strategic hub nodes + 29 mission zones, 3 of which -- `c4_vancouver`, `c4_gdansk`, `c6_penthouse` -- late-emerged during P2 research beyond P1's original 26-zone count; see `architecture.md`'s zone-list note). **Not a nav file by design:** Undertow's mole-hunt (`c6_undertow_hunt` in the raw P2 research) plays out entirely at the Hideout strategic layer, not a tactical mission -- see `../mechanics.md` "Mole hunt (Undertow)" instead.

## Routing rules (apply to ALL nav files in this folder)

### Localization mechanism for this game: map-system

Phantom Doctrine's strategic map / mission-select screen names each mission directly -- the persona and player both always know exactly which mission is active by name. No landmark-based "what do you see around you" disambiguation is needed (that's the `landmark`/`hybrid` case for other games). `nav/localization.md` is skipped for this corpus per the folder-structure spec.

### Flag the game's save mechanism on entry

Phantom Doctrine uses quicksave/quickload (`F5`/`F9`) plus autosaves (`pdsauto*`, `pdtauto*` slots observed on disk) rather than in-mission checkpoints. Confirm exact autosave triggers during P1/P2 research.

### Hint format on mission entry

When the player starts or asks about a mission, give 2-3 short tips before any tactical solutions: objective type, any known one-way/point-of-no-return risk, and anything the mainstream guides call out as commonly missed. Full tactical/combat solutions live in `../mechanics.md` and (once researched) per-mission content -- this folder stays routing-only.

## Scaffold-file fallback

When the player asks about a mission whose nav content doesn't exist yet, web-search before asking a clarifying question. Nav-class questions default search-first.
