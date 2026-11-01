# Nav -- Steal the (Empty) Beholder Cargo (Glasgow trap)

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone
**Linear?:** yes
**Chapter:** 2

## Entry

From `c2_omikron` via edge `(c2_omikron, c2_glasgow)`. MI6 safehouse, codename "Cornerstone." File `L003_WSOM_mi5_safehouse`.

## Exit

To `c3_ivorycoast` via edge `(c2_glasgow, c3_ivorycoast)`. **Type:** story-gate. **Point of no return:** missable-trigger (see gate 6 below).

## Outgoing edges

- `(c2_glasgow, c3_ivorycoast)` -- story-gate, one-way, always.

## Entry tips (3 max)

1. **Soft-lock warning:** clear the map and call evac *before* opening the shipment box, then trigger it and leave immediately.
2. The duty officer's keys are a transferable state flag -- the agent who grabs them doesn't have to be the one who opens the box.
3. Interacting with the shipment box forces combat -- don't do it until you're ready to evacuate.

## Sequential gates

1. **Investigate/solve the dossier** to learn the Glasgow location.
2. **Recon.**
3. **Deactivate lasers.**
4. **Reach the duty officer and get the keys.**
   - `lock:` Duty officer's keys (in-mission item flag) -- see `architecture.md` Locks and Keys.
5. **Get the shipment** -- the key is transferable to another agent.
6. **Discover the cargo is fake** -- springs the trap; your handler goes rogue (revealed as "Turncoat"). This is the narrative reveal, not just a mission beat.
   - `point_of_no_return:` missable-trigger
7. **Evacuate.**

Achievement: *Once Bitten, Twice Shy.*
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression (gates 1-5, 7); spoiler: story (gate 6 -- handler-is-Turncoat reveal, `entity: turncoat`, `entity-hidden: yes` at the moment of this reveal)_ [Confirmed: 3 sources, 2 languages]

## Common confusions

- Two different "Marquis cargo" missions exist across the campaign -- this one (empty cargo, Glasgow) is distinct from the real-cargo houseboat mission (`c3_houseboat`, Ch3). See `architecture.md`'s "Shared-name / confusion flags."

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
- gamepressure.com Ch.2 walkthrough (English, editorial, 2018).
- Phantom Doctrine Fandom wiki, MI6_Safehouse page (English, community-wiki, via search snippet).
