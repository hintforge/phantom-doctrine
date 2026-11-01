# Undertow

**entity-id:** undertow
**class:** npcs
**entity-status:** hostile
**entity-hidden:** yes
**first-encounter-zone:** hideout_hub (strategic layer -- not a tactical-mission zone; see Current status)
**status:** research-integrated
**last_reconciled:** 2026-08-18

## Current status

**P1 open question RESOLVED at P2 (2026-08-18).** Undertow is a mole inside the Cabal -- a Beholder spy embedded among the player's own recruited agents. Unlike every other named NPC in this corpus, **Undertow is not a fixed pre-written character; it's a randomized existing roster agent.** The mechanism:

1. Omikron begins vetting your roster (strategic Hideout event, not a tactical mission).
2. A randomly-selected agent is flagged as the mole "Undertow" through one of several strategic mole-hunt story branches: a failed polygraph, a mysterious illness/isolation event, or a drunk-spouse accusation.
3. Selection is effectively random -- players report even brand-new or previously "loyal" agents being tagged.
4. The mole must be executed in MK-ULTRA to progress the story. (See `../dependencies.md` PON-001.)

This is a **mechanic explanation, not a narrative-identity reveal** -- nothing about Undertow's fixed backstory or motive is disclosed, because there isn't one; the game reassigns the label to whichever agent gets flagged. The mole-hunt plays out entirely at the Hideout (Analytics/MK-ULTRA), never in a tactical mission map -- see `../mechanics.md` "Mole hunt (Undertow)."
_spoiler: progression (mechanism); enemy-tier: 1 (mechanism), enemy-tier: 3 (the fact that the mole must be executed carries the same identity-concealment weight as other hidden-entity reveals, kept at entity-hidden: yes since the "who" is discovered live in-game, not spoiled here)_ [Confirmed: 3 sources, 1 language]

**Soft-lock warning:** Chapter 6 (where this beat typically lands) is a notorious progression-bug hotspot -- players report getting stuck if Investigation Board dossiers are unsolved or if the flagged agent happens to be in training when the mole-hunt triggers.

**Identification, live-play + WebSearch finding (2026-08-20).** The sleeper conditioning is itself stored as one of an agent's hidden ("?") perk-slot entries -- but an unrevealed "?" perk is the default state for many ordinary agents too, not a unique tell. It looks identical to a normal unrevealed perk until something surfaces it. Three ways to reveal it: (1) secret documents/intel directly naming the agent, (2) the Night Operations training's "Eye for Talent" passive, which reveals hidden skills -- sleeper conditioning included -- of squadmates deployed alongside that agent on a mission, (3) Interrogating the agent (confirmed to work on your own roster, not just captured enemies -- see `../mechanics.md` "Interrogation / brainwashing / sleeper agents"). **Risk management:** a flagged/suspected sleeper is reportedly only dangerous if taken into combat -- assigning them to non-combat Hideout/strategic jobs carries no reported repercussions, making that a safe holding pattern while investigating further.

**Refined, 2026-08-20 (WebSearch): the trigger is being deployed on the tactical map when combat starts, not whether the agent personally fights.** Community reports describe sleeper agents activating and switching sides the moment a deployed mission goes to combat -- a support-flavored role within the squad (hanging back, spotting for teammates) does NOT protect against this; presence on the field is what matters, and when they flip they're standing inside your own formation. **The Tactical Spotter / Spotter Support Power** (`../items/support_items.md` -- confirmed via a second independent source, 2026-08-20, as "perched at a vantage point just outside the mission area," not a squad slot) is mechanically distinct from squad deployment: it never puts the agent on the tactical map, so the "deployed when combat starts" trigger doesn't apply. Treated as safe by the same mechanical logic as Hideout/strategic duty -- not separately battle-tested for a confirmed sleeper specifically, but the reasoning is direct, not a stretch.

_source: live-play WebSearch 2026-08-20 (Steam Community threads on identifying/defending against sleeper agents) · capture: web_fetch · confidence: medium (multiple forum threads, broadly consistent, not cross-checked against an editorial source) · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_

**Retracted method (2026-08-20): a save-file attribute, `sidestoryparticipant`, is NOT a reliable indicator of which agent is Undertow.** After the player reloaded, that flag read `false` on the agent already confirmed as the mole and `true` on two unrelated agents -- the flag does not track Undertow status specifically (it's likely shared with unrelated strategic sidestories, e.g. the "tired"/"paranoia" branches also seen in `playedsidestories`). This method was tried once and produced a wrong read; don't reuse it. The only reliable identification paths remain the three listed above (intel, Eye for Talent, Interrogate).

## Recruitment / Access

Not applicable in the normal sense -- Undertow isn't recruited or encountered in a zone; the label attaches to an existing roster agent via the strategic mole-hunt event described above.

## Capabilities

Whatever the flagged agent's existing build/perks were -- Undertow has no distinct kit of its own; it's a state flag on a regular roster agent.

## Quests

Mole-hunt / execution beat -- resolves at the Hideout (Analytics vetting -> flag -> MK-ULTRA execution), not bound to any `nav/<zone>.md` file. See `../mechanics.md`.

## Achievements

No achievement in the current list is confirmed bound to Undertow by name.

## Combat

Not applicable as a discrete encounter -- resolution happens through the MK-ULTRA facility interface, not a tactical mission fight. **Correction (2026-08-20):** this doesn't have to mean execution specifically -- Brainwash is also usable on the flagged agent, though it's unconfirmed whether it satisfies the same story trigger as Execute. See `../mechanics.md` "Mole hunt (Undertow)" for the full split-source writeup.

## Missability

Not confirmed by P2 research whether failing to identify/execute Undertow promptly has consequences beyond the documented progression-stall risk, or whether the beat is guaranteed to eventually trigger regardless of player action.

## Status history

Not applicable in the usual party/convertible sense -- there is no pre-reveal "innocent agent" state to log; the mole label appears already-flagged when the mole-hunt event fires.

## See also

- `../mechanics.md` -- "Mole hunt (Undertow)" mechanic writeup.
- `../nav/architecture.md` -- "Undertow's mole-hunt is not a zone" confusion flag.
- `../limitations.md` -- previously recorded as an open research gap; now resolved, entry updated.

## Sources

- Phantom Doctrine Fandom Wiki: The Cabal page (English, community-wiki).
- Steam Community discussions -- Undertow/mole-hunt threads (English, forum).
- Wikipedia, "Phantom Doctrine" (English).
