# Nav -- Assault Turncoat's Hideout (Ambush)

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone (ambush, forced reinforcements on objective interaction)
**Linear?:** yes
**Chapter:** 6

## Entry

From `c5_numbers_station` via edge `(c5_numbers_station, c6_turncoat)`. File `LGen_StoryTac05`.

## Exit

To `c6_penthouse` (chapter continues, unconfirmed direct edge -- see below). **Type:** story-gate. **Point of no return:** none noted.

## Outgoing edges

- Onward edge to the chapter's other zones (`c6_penthouse`, `c6_almaz`) not explicitly confirmed by P2 source -- likely reached via `world_map` within the chapter.

## Sequential gates

1. **Get documents.** Interacting with this objective spawns reinforcements -- don't trigger it until ready for a fight.
2. **Evacuate.**
   - `point_of_no_return:` none noted

`entity: turncoat`, `entity-status: hostile` -- see `../npcs/turncoat.md`. This is the character revealed as your former handler at `c2_glasgow`.
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: medium (single-source) · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ `[Single source -- verify · class:steam-guide]`

## Common confusions

- Generic "hideout assault / ambush" naming shared with `c3_warehouse_ambush` and `c5_siliconvalley` -- distinct missions, don't conflate.

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
