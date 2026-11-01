# Nav -- Rescue Omikron

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone (first shared zone, all three factions converge here)
**Linear?:** yes
**Chapter:** 2

## Entry

From any Chapter 1 finale (`kgb_c1_submarine`, `cia_c1_beirut`, or `mossad_c1_diplomatique`) via their respective story-gate edges. File `LGen_Story_Tac01`.

## Exit

To `c2_glasgow` via edge `(c2_omikron, c2_glasgow)`. **Type:** story-gate. **Point of no return:** none noted beyond normal mission completion.

## Outgoing edges

- `(c2_omikron, c2_glasgow)` -- story-gate, one-way, always.

## Entry tips (3 max)

1. This is where all three starting-agency campaigns converge -- from here on the zone graph is identical regardless of path chosen.
2. Rescuing Omikron uses the handcuff/release ability, **not** an attack -- clicking "rescue" no longer auto-frees him.
3. `entity: omikron` -- see `../npcs/omikron.md`; he becomes an objective-giver at the Hideout after this mission.

## Sequential gates

1. **Investigate suspicious activities** on the World Map to locate captured Omikron.
2. **Enter the zone.**
3. **Turn off lasers.**
4. **Rescue Omikron** -- use the release/handcuff ability, not an attack.
5. **Evacuate Omikron** with your team.
   - `point_of_no_return:` none noted

_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 3 sources, 1 language]

## Common confusions

- "I can't rescue Omikron, clicking rescue does nothing" -- you must use the release/handcuff ability on him specifically; a normal attack or the generic "rescue" click no longer auto-frees him.

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
- gamepressure.com Ch.2 walkthrough (English, editorial, 2018).
