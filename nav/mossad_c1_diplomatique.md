# Nav -- Intercept Abaddon & Komodo (Mossad)

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone
**Linear?:** yes (with optional branches)
**Chapter:** 1-Mossad

## Entry

From `mossad_c1_smugglers` via edge `(mossad_c1_smugglers, mossad_c1_diplomatique)`. File `L011_WSCC_quartier_diplomatique`.

## Exit

To `c2_omikron` via edge `(mossad_c1_diplomatique, c2_omikron)`. **Type:** story-gate. **Point of no return:** chapter-bound (Mossad branch merges into the shared Chapter 2 spine here).

## Outgoing edges

- `(mossad_c1_diplomatique, c2_omikron)` -- story-gate, one-way, requires finishing Ch1 Mossad.

## Sequential gates

1. **Kill Komodo** (mandatory).
2. **Optional: plant a listening device / eavesdrop / disable cameras** (3 stealth sub-objectives).
3. **Evacuate.**
   - `point_of_no_return:` chapter-bound

Achievement: *The Institute* (finish Ch.1 as Mossad) -- per P1 research this is the rarest story achievement in the base list (4.81% Steam rarity), consistent with the Mossad path itself being unlock-gated behind a prior campaign clear. `entity: abaddon` is present in this zone -- see `../npcs/abaddon.md` and its Mossad-only-kill note at `c3_houseboat`.
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: medium (single-source) · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ `[Single source -- verify · class:steam-guide]`

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
