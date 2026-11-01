# Nav -- World Map

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** hub (strategic/mission-select layer)
**Linear?:** no
**Chapter:** all

## Entry

Reached from `hideout_hub` via the `M` key, or automatically presented on mission completion.

## Exit

To any available mission zone via edge `(world_map, <mission-zone-id>)`. **Type:** hub-spoke. **Point of no return:** none at the World Map layer itself (individual missions carry their own PoNR flags).

## Outgoing edges

- `(world_map, hideout_hub)` -- hub-spoke, always available.
- `(world_map, <any available mission zone>)` -- hub-spoke, available once the mission is unlocked (see `architecture.md` edges + Optional Content tables).

## What happens here

The World Map is both the strategic layer and the mission-launch layer -- there is no separate fast-travel system. The player advances in-game time, investigates suspicious activities (which surface new missions and Investigation Board leads), and launches missions directly from the map. On mission completion the player returns automatically to `hideout_hub`. Starting cash is difficulty-scaled ($15,000 Easy / $10,000 Normal / $5,000 Hard); passive income is ~$40/hour, which is why forging and base relocation matter economically.
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 2 sources, 1 language]

## Common confusions

- "How do I fast-travel?" -- there is no separate fast-travel mechanic; missions are launched directly from here.

## Sources

- gamepressure.com general tips / gameplay mechanics guides (English/Polish origin, editorial, 2018).
- TV Tropes, VideoGame/PhantomDoctrine (English) -- economy figures.
