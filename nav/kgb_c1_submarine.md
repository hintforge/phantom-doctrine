# Nav -- Sabotage the Submarine (KGB)

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone
**Linear?:** yes (with tactical-ordering advice)
**Chapter:** 1-KGB

## Entry

From `kgb_c1_raid` via edge `(kgb_c1_raid, kgb_c1_submarine)`. File `L001_EIMI_submarine_base`.

## Exit

To `c2_omikron` via edge `(kgb_c1_submarine, c2_omikron)`. **Type:** story-gate. **Point of no return:** chapter-bound (branches merge into the shared Chapter 2 spine).

## Outgoing edges

- `(kgb_c1_submarine, c2_omikron)` -- story-gate, one-way, requires finishing Ch1 KGB.

## Entry tips (3 max)

1. Do the sabotage **interlocks last** -- they force combat 2 turns after triggered.
2. Read the blueprints early; they reveal the sabotage method for the rest of the mission.
3. This mission is the achievement precondition for *Comrade Spy* (finish Ch.1 as KGB).

## Sequential gates

1. **Read blueprints** to learn the sabotage method.
2. **Sabotage the ballast tanks** (x1).
3. **Sabotage the interlocks** (x2, simultaneously) -- do this LAST; forces combat after 2 turns.
4. **Evacuate.**
   - `point_of_no_return:` chapter-bound

Achievement precondition: *Comrade Spy* (finish Ch.1 as KGB).
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 2 languages]

## Common confusions

- Triggering the interlocks early forces an avoidable early fight -- do ballast tanks first, interlocks last.

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
- gamepressure.com KGB Ch.1 walkthrough (English/Polish origin, editorial, 2018).
