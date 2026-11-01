# Phantom Doctrine -- Factions

**status:** research-integrated
**last_reconciled:** 2026-08-18
**class:** factions

## Why this file exists

The corpus's roster for group entities the player has an ongoing relationship with -- which factions exist, and where to read about each one. Per-faction detail lives in `factions/<entity-id>.md`.

## Roster

| entity-id | display name | entity-status | status | first-encounter zone | missable |
|---|---|---|---|---|---|
| cia | CIA | unspecified | research-integrated | cia_c1_nuclear | no (starting-agency choice) |
| kgb | KGB | unspecified | research-integrated | kgb_c1_gukos | no (starting-agency choice) |
| mossad | Mossad | unspecified | research-integrated | mossad_c1_chemlab | no -- unlock-gated (1 prior campaign clear) |
| beholder-initiative | Beholder Initiative | hostile | research-integrated | unknown | no |
| the-cabal | The Cabal | unspecified | research-integrated | hideout_hub | no |

**Note:** the player picks one of CIA / KGB / Mossad as their starting agency at campaign start -- this is a `paths/`-class choice (see `../paths/index.md`), not a mid-game faction-reputation system. P1 research found no evidence of a deeper mechanical reputation layer beyond the starting-agency pick and per-agency recruitment affinity (see `../mechanics.md` "Agency choice") -- no `reputation/` folder warranted.

## Pointer rules

- Per-faction detail lives in `factions/<entity-id>.md`.

## Sources

- Per-faction source citations live in the per-faction files, not here.
