# Nav -- Assault Project Iceberg (Finale, Grenada)

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone (finale)
**Linear?:** yes
**Chapter:** 7

## Entry

From `c7_searstower` via edge `(c7_searstower, c7_iceberg)`. File `L016_WIRR_server_station`, Grenada.

## Exit

Ending (permanent, point-of-divergence) -- *The End?* difficulty achievements (Easy/Normal/Hard). Extended-campaign players continue to `c8_killtaipan` via edge `(c7_iceberg, c8_killtaipan)`.

## Outgoing edges

- `(c7_iceberg, ending)` -- story-gate, one-way, permanent (point-of-divergence).
- `(c7_iceberg, c8_killtaipan)` -- story-gate, one-way, Extended campaign only.

## Entry tips (3 max)

1. Combat starts 1 turn after the reactor is turned off -- pace accordingly.
2. Bring the whole team down the left side; forward doors are locked until power is off (see `architecture.md` Locks and Keys).
3. This is the campaign finale -- the point of no return is permanent from here.

## Sequential gates

1. **Analyze Iceberg intel.**
2. **Reach the server station.**
3. **Reach the reactor** (can precede gate 2).
4. **Disable the power** -- opens the locked forward doors.
5. **Optional: kill the traitor** (background-dependent identity -- unconfirmed which named character this resolves to; possibly Turncoat or Undertow depending on playthrough, see `limitations.md`; 51200 XP).
6. **Find Valhalla.** `entity: valhalla`, `entity-status: hostile` -- see `../npcs/valhalla.md`.
7. **Kill Valhalla and bodyguards.**
8. **Disable the satellite** (x2).
9. **Evacuate.**
   - `point_of_no_return:` permanent (point-of-divergence)

Achievements: *The End?* -- Easy / Normal / Hard (a higher-difficulty clear unlocks the lower ones).
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 (existence, gates); enemy-tier: 3 (Valhalla boss encounter specifics) · puzzle-tier: 0 · category: mainline · spoiler: progression (existence/gates); spoiler: late-game (tactical execution detail -- route/timing guidance)_ [Confirmed: 2 sources, 1 language]

## Common confusions

- The "traitor" killed here is background-dependent and not confidently named by P2 research -- don't assert an identity to the player; see `limitations.md` open gaps.

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
