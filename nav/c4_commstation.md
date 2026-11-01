# Nav -- Sabotage the Soviet Comm Array (Sakhalin, KAL-007)

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone
**Linear?:** yes (with optional branches)
**Chapter:** 4

## Entry

From `c4_vancouver` via edge `(c4_vancouver, c4_commstation)`. File `L009_EMMM_comm_station`, Sakhalin.

## Exit

To `c5_siliconvalley` per Chapter 5's opening ambush. **Type:** story-gate. **Point of no return:** point-of-divergence (scripted Foregone Conclusion -- see below).

## Outgoing edges

- `(c4_commstation, c5_siliconvalley)` -- story-gate, one-way, chapter continues.

## Entry tips (3 max)

1. **This mission cannot be "won" in the usual sense** -- the plane (KAL-007) is shot down regardless of play. This is scripted.
2. The achievement ("Dead Zone" / *Communication Noise*) still fires even though the plane is lost -- don't assume a failed run.
3. One locked door on this map (roof) cannot be lockpicked at all -- it's a dead end, not a bug.

## Sequential gates

1. **Disable the communication.**
2. **Optional: disable short-range comms** to stall air support (1600 XP).
3. **Optional: unlock another path upward** (1600 XP; a door that cannot be lockpicked).
4. **Cut off the power** (x2).
5. **Evacuate.**
   - `point_of_no_return:` point-of-divergence

Achievement: *Communication Noise* / "Dead Zone" (HIDDEN) -- "attempt to save 269 lives."
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression (gates); spoiler: story (the scripted-outcome twist itself)_ [Confirmed: 2 sources, 1 language]

## Common confusions

- **Players think they failed** when the plane is shot down -- it's always shot down, scripted, and the achievement fires regardless. This is a Foregone Conclusion, not a failure state.
- Reloading around the Cardinal/Gdansk beat (`c4_gdansk`) has been reported to make this mission's prompt disappear alongside Gdansk's -- a documented bug, not a sequence-break.

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
- TV Tropes, VideoGame/PhantomDoctrine (English) -- Foregone Conclusion trope entry.
