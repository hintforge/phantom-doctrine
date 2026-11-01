# Nav -- Steal the Real Beholder Cargo (Houseboat)

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone
**Linear?:** yes (with faction-conditional branch + Extended variant)
**Chapter:** 3

## Entry

From `c3_ivorycoast` via edge `(c3_ivorycoast, c3_houseboat)`. File `L008_ESCI_houseboat`; Extended-campaign variant exists (NG+).

## Exit

Gates the Northstar lead via edge `(c3_houseboat, c4_vancouver)` once the recovered cargo is installed in the Workshop. **Type:** story-gate. **Point of no return:** none noted.

**Unconfirmed:** P2 research did not establish a direct edge from `c3_houseboat` to the chapter's other three zones (`c3_mkultra_plans`, `c3_warehouse_ambush`, `c3_taipan_capture`) -- these are likely reached independently from `world_map` within Chapter 3 rather than chained directly off this mission. Don't assert a specific inter-mission order among the four beyond `c3_ivorycoast -> c3_houseboat` (which the source confirms) until further research pins it down.

## Outgoing edges

- `(c3_houseboat, c4_vancouver)` -- story-gate, one-way, requires installing the recovered Beholder comm device in the Workshop (see `architecture.md` Locks and Keys -- Northstar lead).

## Sequential gates (regular variant)

1. **Search the apartment.**
2. **Search the boat.**
3. **Get the cargo.**
4. **[Mossad only] Kill Abaddon.** `entity: abaddon`, `entity-status: hostile` -- see `../npcs/abaddon.md`.
5. **Wait for evac** (stealth-only path, 2 turns).
6. **Evacuate.**
   - `point_of_no_return:` none noted

Achievement (regular): *Rock the Boat* (corrected at stitch 2026-08-18 -- P2's raw source cited "Clear the Deck," which contradicted the higher-authority P1 `achievements.md` verbatim-Steam-name fetch; see `achievements.md` Progression #5).

## Optional branches / shortcuts

- **Extended variant** -- cargo is at a different safehouse. Achievement: *Same, but Different.*

The recovered cargo (Beholder comm device) is later installed in the Workshop, unlocking the Northstar lead (see `architecture.md` Locks and Keys) -- this is the item that opens `c4_vancouver`.
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

## Common confusions

- Two different "Marquis cargo" missions exist -- this one (real cargo, houseboat) is distinct from the empty-cargo Glasgow trap (`c2_glasgow`, Ch2). See `architecture.md`'s "Shared-name / confusion flags."
- The Mossad "Kill Abaddon" objective is flagged as if it were a main objective in some sources, but is not actually required to complete the mission.

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
- gamepressure.com Ch.3 walkthrough (English, editorial, 2018).
