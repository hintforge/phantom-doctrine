# Nav -- Chemical Weapons Lab (Mossad intro)

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone (tutorial)
**Linear?:** yes
**Chapter:** 1-Mossad

## Entry

Campaign start (Mossad path -- unlocked only after finishing one full CIA or KGB playthrough; this is base-game content, not the Investigators expansion). File `L033` (chemical weapons lab).

## Exit

To `mossad_c1_smugglers` via edge `(mossad_c1_chemlab, mossad_c1_smugglers)`. **Type:** story-gate. **Point of no return:** chapter-bound.

## Outgoing edges

- `(mossad_c1_chemlab, mossad_c1_smugglers)` -- story-gate, one-way, always.

## Sequential gates

Gate-by-gate detail for the chemical weapons lab itself was not itemized by P2 research beyond its existence and file ID -- see the optional "Rescue journalist" side content below, which is documented as running alongside this leg of the Mossad opening.

1. **Complete the chemical weapons lab objective** (detail not itemized at P2 -- flag as a gap if the player asks for gate-by-gate breakdown).
2. **Evacuate.**
   - `point_of_no_return:` chapter-bound

## Optional branches / shortcuts

- **Rescue journalist (Mossad)** -- optional rescue running alongside the Ch1-Mossad leg (file `Lgen_vendor`). See `architecture.md` Optional Content table. Missable.

_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: medium (single-source) · enemy-tier: 2 · puzzle-tier: 0 · category: mainline · spoiler: story (the Mossad-unlock gating fact); progression (the mission's existence and gates)_ `[Single source -- verify · class:steam-guide]`

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
