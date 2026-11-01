# Nav -- Beholder Base in Vancouver (P2-added)

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone
**Linear?:** yes (with a cosmetic infiltrate-or-assault branch)
**Chapter:** 4

**Note:** this zone was not part of P1's datamined 26-zone list; P2 research surfaced it as a distinct beat with no confirmed mission-file ID. Treat existence/gates as `[Confirmed: 2 sources, 1 language]` but the file-ID linkage as unconfirmed.

## Entry

From `c3_houseboat` via edge `(c3_houseboat, c4_vancouver)`, gated by installing the recovered Beholder/Marquis cargo device in the Workshop (see `architecture.md` Locks and Keys -- Northstar lead).

## Exit

To `c4_commstation` via edge `(c4_vancouver, c4_commstation)`. **Type:** story-gate. **Point of no return:** none noted.

## Outgoing edges

- `(c4_vancouver, c4_commstation)` -- story-gate, one-way, learn Operation Northstar.

## Sequential gates

1. **Ask Tai-Pan about Northstar** (single-agent mission/conversation beat). `entity: tai-pan`.
2. **Travel to Vancouver.**
3. **EITHER infiltrate** (requires a special Workshop upgrade) **OR destroy/assault** (two agents).
   - `lock:` Special Workshop infiltration upgrade -- soft/optional-path key only, see `architecture.md` Locks and Keys. Assault is a fully valid alternative; the upgrade is not a hard gate.
4. **Learn about Operation Northstar.**
   - `point_of_no_return:` none noted

## Optional branches / shortcuts

- **Infiltration path** -- stealth-only, requires the Workshop upgrade.
- **Assault path** -- always available, requires two agents, no upgrade needed.

_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

## Sources

- gamepressure.com Ch.4 walkthrough (English, editorial, 2018).
- Steam Community discussions -- Northstar/Vancouver threads (English, forum).
