# Nav -- Assault the Broadsword Numbers Station (Munich)

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P2 (2026-08-18)

**Type:** main-story zone
**Linear?:** yes (with Extended-only variant)
**Chapter:** 5

## Entry

From `c5_terrorcell` (chapter continues). File `L010_WIIR_numbers_station`, Munich.

## Exit

To `c6_turncoat` (chapter transition). **Type:** story-gate. **Point of no return:** chapter-bound.

## Outgoing edges

- `(c5_numbers_station, c6_turncoat)` -- story-gate, one-way, chapter continues.

## Entry tips (3 max)

1. A 6-turn timer forces combat -- pace your plant-explosives objective accordingly.
2. Requires the Communications/telecommunications Workshop upgrade beforehand or the station cannot be traced at all -- see `architecture.md` Locks and Keys.
3. Broadsword the person is typically only present and killable in the Extended (NG+) campaign variant of this mission.

## Sequential gates

1. **[Prerequisite] Install the Communications/telecommunications Workshop upgrade** or the station cannot be traced.
   - `lock:` Communications Workshop upgrade (HARD story-tech key) -- see `architecture.md` Locks and Keys.
2. **Analyze the Broadsword dossier**, then a special mission at NATO HQ Brussels.
3. **[Extended variant only] Kill Broadsword.** `entity: broadsword`, `entity-status: hostile`, `entity-hidden: yes` -- this is the mission where the P1 open question resolves. See `../npcs/broadsword.md` for the full identity writeup: Broadsword is BOTH a NATO civil-defense modernization program codename AND a specific Beholder-agent person, present and killable only in the Extended variant.
4. **Plant explosives** (x3, simultaneously).
5. **Evacuate.**
   - `point_of_no_return:` chapter-bound

Achievements: *Explosive Measures* (destroy the Broadsword facility, HIDDEN); *Death of a Citizen* (kill Broadsword in Munich, Extended only). (P2's raw research said "Extreme Measures" -- reconciled to *Explosive Measures* per P1's achievements.md, sourced from a verbatim Steam achievement-name fetch and higher authority than P2's incidental mention.)
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 (gates/facility); enemy-tier: 3 (Broadsword person-identity reveal) · puzzle-tier: 0 · category: mainline · spoiler: progression (gates); spoiler: story (Broadsword identity resolution)_ [Confirmed: 3 sources, 2 languages]

## Common confusions

- Players expecting to kill Broadsword-the-person in the regular campaign will usually not find him present -- that outcome is reliable only in the Extended variant. See `../npcs/broadsword.md`.

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12).
- Phantom Doctrine Fandom wiki, Broadsword page (English, community-wiki, via search snippet).
- Steam Community discussions -- Broadsword identity threads (English, forum).
