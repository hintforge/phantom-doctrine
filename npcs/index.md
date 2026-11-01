# Phantom Doctrine -- NPCs

**status:** research-integrated
**last_reconciled:** 2026-08-18 (P2)
**class:** npcs

## Why this file exists

The corpus's roster for named individual NPCs -- who's in the story, and where to read about each one. Per-entity detail lives in `npcs/<entity-id>.md`.

## Roster

| entity-id | display name | entity-status | status | first-encounter zone | missable |
|---|---|---|---|---|---|
| cardinal | Cardinal | friendly | research-integrated | unknown | no |
| valhalla | Valhalla (Sven Galloway) | hostile | research-integrated | unknown (final: c7_iceberg) | no |
| tai-pan | Tai-Pan | convertible | research-integrated | c3_taipan_capture | no (Ch3 mandatory; Ch8 encounter is Extended-only) |
| fender | Fender (CIA handler) | hostile | research-integrated | cia_c1_nuclear (approx.) | no -- CIA-path only |
| cyclone | Cyclone (KGB handler) | hostile | research-integrated | kgb_c1_gukos (approx.) | no -- KGB-path only |
| delilah | Delilah (Mossad handler) | hostile | research-integrated | mossad_c1_chemlab (approx.) | no -- Mossad-path only |
| omikron | Omikron | friendly | research-integrated | c2_omikron | no |
| abaddon | Abaddon | hostile | research-integrated | mossad_c1_diplomatique | yes (Ch3 kill-objective is optional) |
| broadsword | Broadsword | hostile | research-integrated | c5_numbers_station | person-encounter effectively missable in regular campaign (Extended-only) |
| turncoat | Turncoat | hostile | research-integrated | c2_glasgow (reveal); c6_turncoat (combat) | no -- mandatory story beats |
| undertow | Undertow | hostile | research-integrated | hideout_hub (strategic, not a zone) | unknown -- randomized roster agent, see file |
| lamster | Lamster | party | research-integrated | hideout_hub (joins post-c3_taipan_capture) | no |

## Pointer rules

- Per-entity detail lives in `npcs/<entity-id>.md`.
- Claims about an entity continue to route to their primary-vector destination; the entity overlay aggregates in parallel.
- `fender`/`cyclone`/`delilah` are mutually exclusive per playthrough -- only the character matching the player's starting-agency choice is ever encountered in that save.

## Sources

- Per-entity source citations live in the per-entity files, not here.
