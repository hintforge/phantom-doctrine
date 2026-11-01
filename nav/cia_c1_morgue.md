# Nav -- Sneak Into the Morgue for Leslie's Intel (CIA)

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone
**Linear?:** yes (with optional branches)
**Chapter:** 1-CIA

## Entry

From `cia_c1_nuclear` via edge `(cia_c1_nuclear, cia_c1_morgue)`. File `L032_WSRR_morgue`.

## Exit

To `cia_c1_beirut` via edge `(cia_c1_morgue, cia_c1_beirut)`. **Type:** story-gate. **Point of no return:** chapter-bound.

## Outgoing edges

- `(cia_c1_morgue, cia_c1_beirut)` -- story-gate, one-way, always.

## Entry tips (3 max)

1. Rooms are **not labeled** -- check pre-autopsy, post-autopsy, and autopsy rooms in turn.
2. Leslie is specifically in the **pre-autopsy room**, unmarked -- easy to miss.
3. The mission's intermission dialog claims a firefight happened even if the mission was completed in full stealth -- that's dialogue flavor, not a bug.

## Sequential gates

1. **Find Leslie** -- check pre-/post-/autopsy rooms; he is in the pre-autopsy room, unmarked.
2. **Retrieve the microfilm** from his body.
3. **Kill Aguirre.** (Cannot capture -- see `dependencies.md` DEP-001: no interrogation facility exists this early.)
4. **Optional: kill Aguirre's team** (x3 total).
5. **Evacuate.**
   - `point_of_no_return:` chapter-bound

_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

## Common confusions

- "The intermission dialog says there was a firefight but I did this in full stealth" -- that's flavor dialogue, not a bug; it doesn't reflect actual mission outcome.
- Rooms aren't labeled -- don't assume Leslie is in the marked "autopsy" room.

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
- gamepressure.com CIA Ch.1 walkthrough (English, editorial, Aug 2018) -- https://guides.gamepressure.com/phantom-doctrine/guide.asp?ID=45914
