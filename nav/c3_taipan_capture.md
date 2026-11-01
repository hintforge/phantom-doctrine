# Nav -- Capture Tai-Pan to Brainwash Him

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone
**Linear?:** yes (with optional branches)
**Chapter:** 3

## Entry

Reached from `world_map` within Chapter 3, gated behind researching the Control Phrase in the Workshop (see `architecture.md` Locks and Keys). File `L007_WSCC_asian_food_place`.

## Exit

To `c4_boldface` per `architecture.md`'s edges (brainwash Tai-Pan, get intel -> chapter-bound). **Type:** story-gate. **Point of no return:** chapter-bound (uses control-phrase tech).

## Outgoing edges

- `(c3_taipan_capture, c4_boldface)` -- story-gate, one-way, chapter-bound (per `architecture.md`).

## Entry tips (3 max)

1. Tai-Pan's position is static -- he does not react to downed guards, so clear the map first for a clean stealth run.
2. Requires the Control Phrase researched in Workshop beforehand -- see `architecture.md` Locks and Keys.
3. This mission is best planned last among the chapter's flexible missions per community guidance.

## Sequential gates

1. **[Prerequisite] Research the Control Phrase in Workshop.**
   - `lock:` Control Phrase (item -> flag -> tech chain) -- see `architecture.md` Locks and Keys.
2. **Knock out Tai-Pan.** `entity: tai-pan`, `entity-status: convertible` -- see `../npcs/tai-pan.md`.
3. **Optional: find the hostage** (basement freezer).
4. **Optional: maintain stealth** (achievement *No One Noticed*).
5. **Evacuate Tai-Pan** with your team.
   - `point_of_no_return:` chapter-bound

_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

## Common confusions

- Two missions share this same map, reused later at `c8_killtaipan` (Ch8, Extended/NG+) -- distinct objectives (capture vs. kill).

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
- gamepressure.com Ch.3 walkthrough (English, editorial, 2018).
