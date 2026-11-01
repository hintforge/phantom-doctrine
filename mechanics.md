# Phantom Doctrine -- Mechanics Reference

**status:** research-integrated
**last_reconciled:** 2026-08-18 (P2)

Core game-system rules. Phantom Doctrine is a turn-based tactical espionage game (CreativeForge Games, 2018) built around several interacting systems -- the Investigation Board, agency choice, disguises, interrogation/brainwashing, roster management, HQ facilities, crafting, and difficulty all cross-reference each other in play.

## Action Points & Fire Points

Two separate per-turn resources, both shown on every agent dossier:

- **Action Points (AP)** -- spent on movement and general actions. Every agent starts with 2.
- **Fire Points (FP)** -- spent specifically on combative actions, most commonly firing a weapon; some abilities cost both AP and FP together. Every agent starts with just **1**. Weapon fire modes cost FP at different rates (e.g. a single aimed shot costs 1 FP + ammo; full-auto costs 1 AP + 1 FP) -- the practical effect is that a 1-FP agent can generally only take one real offensive action per turn before running dry, even with AP left over.
- FP (and AP) can be raised past their starting value via **Body Engineering**, not via leveling: 150 Circulatory grants 2 FP, 200 Circulatory grants 3 FP; 100 Motoric grants 3 AP, 140 Motoric grants 4 AP (see `items/abilities.md` "Body Engineering" for the full compound table used to hit these thresholds).

_source: live-play WebSearch 2026-08-20 (gamepressure.com "Action points" / "Gameplay mechanics" guides, Steam Community discussion) · capture: web_fetch · confidence: high (matches the AP/FP thresholds already independently sourced in the Body Engineering compound table) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Combat resolution -- what determines a hit vs. a graze (player question, 2026-08-21)

Phantom Doctrine doesn't show a hit-percentage the way XCOM does. Every weapon instead has **two damage values: a maximum (full hit) and a minimum (graze)** -- there's no clean miss against a target with line of sight; every shot lands as one or the other.

- **Which one you get is gated by the target's Awareness, not a die roll against your gun.** A target with Awareness left in the tank can attempt to dodge; succeeding drops the shot to the weapon's **minimum** damage ("grazed!") instead of its **maximum** ("dodged!" also appears as a message, per the in-game manual text quoted in the community thread below -- the two terms seem to cover the same outcome: reduced, not zero, damage). Failing (or having no Awareness left) means the shot lands for full/maximum damage.
- **Dodging costs the target Awareness** -- every successful dodge attempt drains some of the target's Awareness pool (their "dodge cost" stat, tracked per-agent -- see the roster files' Vitals). Enough incoming fire eventually burns a target's Awareness down to where they can no longer dodge at all.
- **Point-blank (adjacent-tile) shots skip the dodge check entirely** -- guaranteed full/maximum damage, no matter the target's Awareness.
- **Weapon type shapes how much a graze actually costs you.** Automatic weapons have a comparatively high minimum damage, so they stay dangerous even on a grazed hit; single-shot weapons (pistols, sniper rifles) have very low minimum damage, so a dodge against them is a near-total whiff.
- **Community-reported, less certain:** cover, suppression, and flanking are also said to shift the effective damage/dodge math, and a bonus "headshot" damage tier is mentioned in player discussion (one commonly cited example: 7 graze vs. 70 headshot on the same weapon) -- but the exact formulas for cover/suppression/flanking, and how a headshot is actually triggered (a separate aimed action vs. a random outcome), weren't consistently explained across sources and aren't asserted here as confirmed.

_source: live-play WebSearch 2026-08-21 (Steam Community "Hit chance?" and "How does the mechanics of damage and awareness work?" discussions, the second directly quoting the in-game manual: "Minimum damage is how much damage is dealt if the enemy dodges; maximum damage is how much is dealt if they don't dodge" and "Awareness is vital to both your offensive and defensive strategies; it allows Agents to dodge or reduce damage") · capture: web_fetch · confidence: medium-high on the core dodge/graze/point-blank mechanic (corroborated across multiple independent threads plus a quoted manual excerpt), low on cover/suppression/flanking specifics and the headshot trigger (community-reported only, not consistently explained) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Range -- does it affect the gun? (player question, 2026-08-21)** Yes. Range isn't shown as an explicit number in-game, but the community consensus across several independent threads is that every weapon class has an effective-range band, and damage drops off once a target is beyond it: roughly **pistol/shotgun (short, loses effectiveness past ~10 tiles) < SMG < assault rifle/LMG < sniper rifle**, with **sniper rifles the outlier -- effectively unlimited range, no falloff at all**, full damage at any distance.

**Is a sniper less likely to hit at point-blank than a pistol? No.** Per the point-blank rule above, dodge is skipped entirely at adjacent range for *any* weapon -- hit-vs-graze isn't weapon-dependent, so a sniper and a pistol are equally guaranteed to connect at point-blank. What differs is just each gun's own damage/FP-cost/ammo numbers, not its odds of landing the shot.

**Should you always use a pistol, then?** Not on accuracy grounds -- that part's a wash at point-blank. The real reasons pistols are the go-to for up-close/stealth work are practical, not mechanical-hit-chance: they cost less FP per shot, take a silencer well (keeping a takedown from raising the alarm -- see alarm trigger #2 above), and are cheap/plentiful early. A handful of community threads claim a pistol is specifically *more effective* than a sniper rifle at point-blank -- this wasn't consistently explained (possibly conflating a "headshot" bonus some players associate with pistols) and isn't asserted here as a confirmed mechanic; treat "pistol for stealth work" as the well-supported takeaway, not "sniper is mechanically worse up close."

_source (range): live-play WebSearch 2026-08-21 (Steam Community "Unlisted stat: weapon ranges" discussion, gameplay.tips "General Weapons Guide") · capture: web_fetch · confidence: medium (consistent range-tier ordering across two independent community sources; exact tile numbers are community-estimated, not datamined or patch-note confirmed) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Conspiracy / investigation board (`B` key)

The signature deduction mechanic: a physical pinboard where intel files (from informers, mission loot, or the Comms facility) are connected via keyword cues to reveal enemy agents, new missions, agent candidates, trade contacts, and compounds. Double-click a file to open it, click highlighted keywords in the document text, then link matching cues on the board; solving a "secret file" yields a reward. Board arrangement is **not saved between sessions.**

**Common English-guide gap:** many players never realize files without pre-set keywords must be decrypted at the **Analytics** facility before their cues appear -- the board simply won't let you link them, which reads as a bug rather than a missing prerequisite.

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 5 sources, 1 language]

## Agency choice (CIA / KGB / Mossad)

Two options available from campaign start (CIA "Deadpan", KGB "Kodiak"); Mossad "Hemlock" (the Israeli Nazi Hunter) unlocks only after finishing one campaign. See `paths/index.md` for the full per-agency breakdown; summary of what diverges:

1. Different protagonist + entirely different Chapter 1 missions (three unique openings).
2. A unique handler, later revealed as a brainwashed MKULTRA traitor -- see `npcs/fender.md` (CIA), `npcs/cyclone.md` (KGB), `npcs/delilah.md` (Mossad).
3. Voiceover language (KGB agents speak Russian).
4. Recruitment affinity -- KGB recruits Stasi/SB (communist-bloc agencies) more easily; CIA and Mossad recruit each other more easily.
5. Subtle facility/upgrade unlock-timing differences and some mission variations.

From Chapter 2 onward the storylines converge into "The Cabal." Per developer CFG_Hitch on Steam (verbatim): "each background provides healthy several hours of content, with the entire game estimated at 40+ hours."

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 0 (the choice mechanic itself) · puzzle-tier: 0 · category: mainline · spoiler: none. The handler-traitor reveal (item 2) is `spoiler: story`, enemy-tier 3 -- see the linked npcs/ files, gated separately from this mechanic-level summary._ [Confirmed: 5 sources, 1 language · class:official-pr+community-wiki]

## Disguises & cover/awareness

Agents start missions in Infiltration mode. Restricted (red) zones trigger combat if a guard/civilian/camera sees you -- unless you wear a disguise. Disguises can only be assigned to a limited number of agents (difficulty-dependent: up to 4 on Easy, 3 on Medium) and **only if Tactical Recon was completed on that location first.** Disguised agents may carry only pistols/small SMGs, no armor, no support items.

The **Actor perk** reduces the distance at which enemy agents detect a disguise (post-patch: a *reduction*, not total immunity -- a documented nerf from launch behavior, later made a toggleable option in the Halloween update). Guards have zero Awareness during infiltration; enemy agents start at full Awareness and can detect disguises.

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 5 sources, 1 language · class:editorial-en+forum]

## Alarms, opposition types & body disposal

**Opposition categories.** Restricted-zone opposition splits into enemy agents, militia, and police -- police are the odd one out because they trigger the "agent hasn't reported back" alarm chain if taken down carelessly. Recommended takedown order during infiltration: enemy agents first, then militia, then police last.

**The "hasn't reported back" chain.** Every takedown -- civilian, local guard, militia/enemy, or police -- counts against a shared hidden tolerance, but not equally: drain scales by unit type, **civilian < local guard < enemy < agent**, so an agent takedown burns far more tolerance than a civilian one. Total budget is roughly 2-4 before something happens, scaling with difficulty (Easy tolerates more, Hard fewer; exact per-run threshold reported as inconsistent). The watcher is specifically **enemy Agents**, not regular guards -- ordinary guards don't notice colleagues or civilians going missing on their own. Once an Agent's tolerance is crossed, that Agent goes vigilant and actively searches for the missing person. Clearing enemy Agents from the map first is the standard opener for two stacked reasons: it removes the watcher (nothing left to track the count) AND it clears the most expensive unit type off the meter first. With no Agents present, guards/civilians can be worked through freely. Can also be used deliberately: leave someone quiet and ambush the Agent sent to investigate while they're isolated from their post.

**Alarm triggers -- five ways an alarm starts:**
1. Being seen in a restricted (red) zone without a valid disguise.
2. A guard/civilian/camera witnessing a hostile act (takedown, kill, forced entry).
3. A guard or civilian finding an unconscious or dead body.
4. **Walking through an active laser barrier -- unconditional, live-play + WebSearch finding 2026-08-20.** Unlike trigger #1, a valid disguise does NOT prevent this -- lasers raise the alarm regardless of disguise status. Lasers are tied to a **console**, not a guarding agent; killing whichever enemy agent is on the mission does not disable them. The only way through is finding and interacting with the console (see the per-zone `nav/` files that list "turn off lasers" as an objective) -- or, with the Yakuza background's Interconnected ability (or an equivalent Tactical Recon setup), disabling one laser/CCTV terminal can disable all of them at once instead of hunting each console individually.
5. **"Force Majeure" -- a scripted/forced alarm with no in-fiction cause, player-reported 2026-08-21.** The game's own on-screen label when an alarm triggers for no player-visible reason -- not tied to being seen, a witnessed act, a found body, or a laser. Two flavors, per multiple corroborating Steam Community threads: (a) **story missions** where a specific objective is scripted to trigger it regardless of how quietly everything before it was done; (b) certain **randomly-generated recon missions**, where one of the mission's random variants is "agents start compromised, alarm coming soon" and Force Majeure is just that variant playing out. **There is nothing to do about it when it happens** -- it isn't caused by a mistake, and community consensus is it can't be avoided or undone once that mission variant/story beat is live. The only reported workaround is technical and story-mission-inapplicable: deleting `PhantomDoctrine\IWTB\Content\Data\Design\MissionLogic\Lgen_scout_alarmsoon.xml` removes it from randomly-generated missions only, not scripted story alarms -- a file edit, not something to do mid-mission.

_source (trigger #5, Force Majeure): live-play WebSearch 2026-08-21 (multiple corroborating Steam Community threads: "What is Force Majeure?", "Force Majeure - Not compromised", "FORCE MAJEURE NEEDS TO GO AWAY", "Force Majeure", "Force Majeur") · capture: web_fetch · confidence: medium (consistent explanation across several independent community threads, not developer/patch-note confirmed) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Body disposal.** Takedown drops the body where it falls; the separate Disposal ability is required to make it vanish before a patrol or civilian walks past it. On **Hard difficulty, Disposal is unavailable entirely** -- a dropped body will eventually be found regardless of positioning.

_source: live-play WebSearch 2026-08-19, corroborated across a second independent pass same day · capture: web_fetch · confidence: high (unit-type tolerance weighting and agents-first strategy independently confirmed across gamepressure.com, GameInformer, Fandom Tips, and multiple Steam Community threads) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 6+ sources, 1 language · class:editorial-en+community-wiki+forum]

**Breach mechanic and civilians in the room -- live-play question + WebSearch finding, 2026-08-20.** A breach (2+ agents entering a room together, opening fire simultaneously) auto-assigns agents to nearby *hostile* targets -- civilians present are NOT auto-targeted and are not killed by the breach itself if left alone. Civilians CAN be manually right-click-selected as breach targets, but every source calls this a mistake: killing a civilian raises the Hideout's Danger meter (community-reported figures cluster around +30 to +40 per civilian, not confirmed to an exact current-patch number). All-suppressed weapons on every breaching agent keep the breach from raising an alarm, matching alarm-trigger #2 above (a witnessed hostile act) -- civilians left untargeted and out of the shooters' line of sight don't react to a clean, suppressed breach.

**Known limitation once combat starts:** panicked civilians can become impossible to interact with non-lethally -- multiple Steam reports describe them as unremovable except by lethal means (e.g. a grenade) after a fight begins, even when they're blocking a path to an objective. If a civilian needs to be out of the way without dying, the reliable move is a **takedown before breaching**, while still in Infiltration mode -- not an in-combat fix.

**Player-confirmed, 2026-08-20: facing direction matters, not just distance.** A suppressed breach was run on a room where the civilians were facing away (toward a filing cabinet) -- they never noticed / never triggered an alarm. This confirms "witnessing" for the alarm-trigger-#2 rule above is gated on the civilian's actual line of sight/facing at the moment of the act, not merely being present in the room or even in the same room as an unsuppressed sound would carry. Positioning a breach so civilians are back-turned is a working alternative to a pre-breach takedown when repositioning them isn't practical.

_source: live-play WebSearch 2026-08-20 (gamepressure.com "Breach mechanic" guide; Steam Community "Help with Civilians" thread) + live-play confirmation same day (facing-direction finding) · capture: web_fetch + manual_paste · confidence: medium (breach targeting and suppressor behavior corroborated by an editorial guide; exact Danger-per-civilian figure and the panic/uninteractable behavior are community-reported, not patch-note confirmed) / high (facing-direction gates witnessing -- player-confirmed in this playthrough) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## No-alert vs. combat -- the real tradeoff, not just reinforcements (live-play + WebSearch finding, 2026-08-20)

Beyond avoiding the reinforcement countdown, staying in Infiltration mode (no alarm ever triggered) has a genuine economic upside, traded against a genuine downside:

- **Combat mode generates Heat on your agents just by being entered -- outcome doesn't matter.** Per a Steam Community thread on Heat mechanics, Heat accrues from being in combat at all, not from kills or how the fight goes. Staying in Infiltration avoids this entirely. Heat isn't free to clear either -- it requires a new identity at the Forger (~$500 baseline per agent, see "Economy note" below), so avoiding it is a real cash saving, not a cosmetic one.
- **Danger risk is lower too** -- Danger accrues partly from civilian kills and a compromised evac, both far more likely once a mission goes loud.
- **The tradeoff: combat-mode kills are worth more XP than infiltration-mode kills.** Per a mission-rewards breakdown, kills made in Combat earn more XP than the same kill made in Infiltration. Pure stealth isn't strictly better on every axis -- it's an explicit trade of some XP efficiency for avoided Heat/Danger cost, not a free lunch.
- **Heat vs. Danger priority:** one Steam thread frames it plainly -- Heat is always the lesser evil because it's fixable (Forger identity change); Danger is harder to walk back (base relocation is the main lever, and it's expensive). If a mission is going sideways, prefer letting Heat rise over letting Danger rise.

**Community disagreement, not settled consensus (2026-08-20).** The "stealth = less Danger" framing above isn't unanimous. A counter-report on Steam claims the opposite causal story: going loud and clearing a mission *fast* can generate **less** overall Danger than a long, careful stealth run, because Danger accrues partly from how long a Beholder cell sits exposed on the map -- a quick loud clear ends that exposure sooner than a drawn-out infiltration. This suggests **mission duration/lingering may matter for Danger at least as much as combat-vs-infiltration mode itself**, which the framing above doesn't capture. Practical middle ground reported by an experienced player: gear half the squad for stealth, half for combat, and switch to guns if a stealth attempt stalls rather than forcing it. Separately, players report reinforcement waves can dump 8+ enemies at once with cover only reducing (not blocking) damage -- a practical reason to keep loud engagements short regardless of which side of this debate you land on.

_source: live-play WebSearch 2026-08-20 (Magic Game World "Mission Rewards" guide; Steam Community "Heat, kills and cleaners," "Hideout Danger Levels and Heat? How to avoid?," "Do you have to stealth?") · capture: web_fetch · confidence: medium (consistent across an editorial guide and multiple forum threads, not independently verified against this playthrough's own data; the duration-vs-mode disagreement specifically is single-source and unconfirmed) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Knockouts, stabilizing, and bleed-out (in-mission) -- live-play finding, not previously documented

When an agent (yours or an enemy's) hits 0 HP via non-lethal means (takedown, knocked below 0 by gunfire), they fall **incapacitated** rather than dying outright, and a turn-count "bleeding out" timer starts. Three ways this resolves:

- **Stabilize them** (an ability, usable by another agent) -- this removes the bleed-out timer. They stay alive and unconscious indefinitely; carrying them also pauses the timer. A stabilized body left behind (not extracted) survives -- you simply don't get the capture, but nothing forces you to retrieve it.
- **Leave them unstabilized** -- they bleed out and die within a few turns on their own. You don't have to wait out the timer: ending/leaving the mission with them still down and unstabilized counts them as dead.
- **There is no in-mission "finish off" action for an already-stabilized body.** Stabilizing is specifically what removes the kill-by-bleedout path -- once done, the only way found in research to guarantee a kill is to not stabilize in the first place, or skip the knockout flow entirely and use a lethal method (e.g. a headshot) which has no incapacitated/bleed-out state at all. **Correction 2026-08-22: "breach charge" was previously listed here as a second example and is unverified -- a targeted re-check found no evidence this game has a "breach charge" item at all. Retracted; do not cite it.**
- **Failing to rescue one of your own downed agents has a consequence beyond losing them -- confirmed 2026-08-20 via Fandom Combat page.** If a stabilized-but-unrescued agent isn't extracted successfully, they're captured by the enemy, which can lead to them turning sides or revealing operational intel about your organization. The **Loyal** perk (confirmed on this player's protagonist, not in the original perk-catalog fetch -- see `items/abilities.md`) makes an agent immune to this specific consequence.

**Extraction doesn't require carrying the body into the zone -- confirmed high-confidence, 2026-08-20.** Setting a downed/captured body down inside the evac zone is sufficient; it does not need to be held by an agent at the moment extraction completes. Corroborated by two independent sources: a Steam Community thread asking this exact question, and the Fandom wiki's Combat page confirming the same for downed agents generally. Timing still matters if unstabilized -- most evacs take ~3 turns, bleed-out is ~5, so there's a buffer but not a large one.

**Practical takeaway:** decide before you knock someone out whether you intend to extract them. If you don't expect to make it to extraction, either don't stabilize (they'll die on their own, no timer-babysitting required) or kill them outright instead of taking them down non-lethally.

**Untested against this corpus's own play:** whether attacking an already-stabilized incapacitated body a second time does anything (e.g. re-triggers a kill). No source found confirms or denies this -- flagging as an open question rather than asserting either way.

_source: live-play WebSearch/WebFetch 2026-08-20 (Phantom Doctrine Fandom wiki "Combat" page + Steam Community discussion "Anyway to kill enemy Agents bleeding out") · capture: web_fetch · confidence: high (stabilize/bleed-out mechanic, corroborated across wiki + forum) / unconfirmed (re-attacking a stabilized body) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Line of sight -- no XCOM-style move/shot preview

**Confirmed absent, 2026-08-20 WebSearch.** Phantom Doctrine has no hotkey, hold-key, or UI toggle that previews which enemies an agent will have line-of-sight to shoot at *before* confirming a move (the XCOM-style blue-silhouette-during-movement feature). Two independent Steam Community threads discussing LOS mechanics were checked; neither mentions such a feature existing, and one player explicitly complains about its absence ("A game in which LoS is so crucial to success is unplayable if i cant tell if my agents are in LoS or not").

What the game does offer instead:
- **Infiltration phase:** enemies have a visible, limited LOS cone -- stepping into it triggers detection. You can click an enemy to preview their next move.
- **Combat/battle phase:** no LOS cone limit is enforced the same way; shots are evaluated after you commit to a position, not previewed during movement.
- **Overwatch:** dragging out a watch direction paints the covered ground live as you set it up (visual preview of *that* ability's coverage, not of movement-to-shot LOS).
- **Community workaround:** enemies (and you) can shift a tile or two to gain LOS mid-turn, then shift back -- don't assume standing next to a window/doorway is safe just because you can't currently see through it.

_source: live-play WebSearch 2026-08-20 (2 Steam Community discussion threads on LOS mechanics) · capture: web_fetch · confidence: medium (negative finding -- absence confirmed across 2 forum threads, not an official patch-notes/manual source) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Interrogation / brainwashing / sleeper agents

Captured enemy agents (knocked out while at lower HP than your attacker, then bodies retrieved) go to holding cells. The **MK-ULTRA facility** offers:

- **Interrogate** -- intel, reveals perks/aliases/candidates; costs money once MK-ULTRA is built. **Not enemy-only, confirmed 2026-08-20:** works on your own roster agents too, including flagged sleeper suspects, with the same reward types as an enemy interrogation. One-time per agent -- no repeat payout from interrogating the same person twice.
- **Brainwash** -- erases hidden control phrases/sleeper conditioning at risk of destroying perks; used defensively on your **own** suspected agents.
- **Conversion** -- turns an enemy agent into a recruit.
- **Control Phrase, Mason Gambit, and Saboteur are three distinct MK-ULTRA treatments, not variants of one mechanic (corrected 2026-08-21):**
  - **Control Phrase** -- manual activation. An agent with line of sight uses the ability mid-mission to flip the conditioned agent to your side; works in both Infiltration (an instant disguised agent) and Combat (an extra gunner).
  - **Mason Gambit** -- automatic. Flips the agent to your control the moment combat starts, no activation needed. Does nothing during Infiltration -- pure combat trigger.
  - **Saboteur** -- doesn't grant control at all. Wires the agent to attack the first hostile they encounter once things go loud, turning on their own side rather than joining yours.
  All three: implant via MK-ULTRA, then release the agent back into the field to plant the effect (*Calculated Risk* achievement for using the technique; *Inside Job* for destroying 5 cells via sleepers turned this way).

**Base costs, player-reported 2026-08-22: Control Phrase $2000, Mason Gambit $500** -- a real 4x price gap, buying Control Phrase's manual timing and Infiltration-mode value on top of the combat-only automatic flip. Not yet cross-checked against a second source or screenshot; treat as this playthrough's observed price until corroborated (both scale down with their respective Workshop cost-reduction upgrades -- Control Phrase Improvements, Miniaturized Abdomen Explosives -- see `items/upgrades.md`).

_source (Control Phrase/Mason Gambit/Saboteur distinction): live-play WebSearch 2026-08-21 (Steam Community "What's the difference between control phrase and mason gambit?" and "Control Phrase vs Converting the agent" discussions) · capture: web_fetch · confidence: high (consistent, specific mechanical distinction across multiple independent threads) · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Hideout personnel events (agent crises -- illness, arrest, etc.)

**Own roster agents can randomly trigger a personal-crisis event** (illness, arrest by local police, other personal trouble) that surfaces a choice screen with 2-3 response options at different costs (a free/cheap option like a "care package" vs. a paid option, e.g. $200 or $1000+danger). Community-reported outcomes: the agent can return **loyal** (sometimes with a bonus perk), return **compromised** (functions as a mole), or be **lost permanently** -- and which outcome lands depends on the option picked, not simply "pay more = safer" (one player's cheaper option outperformed the expensive one). **"Missing" is a temporary in-progress state, not a resolved loss -- CORRECTED 2026-08-22.** Live-play, 2026-08-21: Lamster (Rich Grey) hit an arrest event, the free "care package" option was chosen, and he showed as missing with no immediate recovery action visible. The prior write-up treated that as the final (bad) outcome -- wrong. **2026-08-22: he returned on his own after roughly a day, with +$1000 and his Loyal perk confirmed/granted** -- the "care package" pick's actual payoff, not a loss. Treat a "missing" agent as pending resolution (check back next Hideout visit) rather than lost, unless further play shows a genuinely permanent case. **Second confirmed data point, 2026-09-15: Archer (Eita Tanaka) also returned Loyal** after a personnel-crisis arc -- which response option was picked this time is not recorded, so it corroborates the "returns Loyal" outcome existing but not yet which choice drives it.

_source: live-play 2026-08-21+2026-08-22 (Lamster, full arc: event -> missing -> returned+$1000+Loyal) + live-play 2026-09-15 (Archer, returned+Loyal, option choice not recorded) + WebSearch (Steam Community "Agents leaving / returning" discussion) · capture: web_fetch + manual_paste · confidence: medium (two independent live-play data points now confirm the "returns Loyal" outcome itself; which response option drives it is still one-sample on the "care package" branch, not cross-checked) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Documented exception to "brainwash = mind control":** Brainwashing does **not** convert enemies -- Conversion does that. Brainwashing an enemy and then releasing them produces a ~30-day "zombie" state on the enemy list instead.

**Recruit-screening as routine practice -- live-play + WebSearch finding, 2026-08-20.** Running new hires (and returned/recovered agents) through MK-ULTRA to check for Beholder sleeper conditioning before trusting them is a recognized community strategy, not just a reactive-investigation move. Cost-benefit split by tool: **Interrogate/Brainwash** costs money and is only considered worth it on an agent you intend to keep long-term (or one you already suspect) -- not worth spending on someone you'll execute or use disposably anyway. **Night Operations training's Eye for Talent** passive is the free alternative -- deploying an agent who has it alongside a new hire on a mission reveals that hire's hidden skills at no MK-ULTRA cost.

_source: live-play WebSearch 2026-08-20 (Steam Community discussions) · capture: web_fetch · confidence: medium (consistent across multiple forum threads, not cross-checked against an editorial source) · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 2 · puzzle-tier: 0 · category: mainline · spoiler: late-game_ [Confirmed: 5 sources, 1 language · class:community-wiki+forum]

**MK-ULTRA cost -- CONFIRMED at P2, danger half CORRECTED 2026-09-09.** Before the facility is built, captured agents are interrogated and executed free and instantly. After the build (story-mandatory in Ch3), interrogation costs roughly $1500 and execution roughly $500.

**The "adds danger" clause was wrong for a patched game -- retracted 2026-09-09 on the player's challenge.** Three corrections, in order of importance:
1. **A patch removed it.** Captured agents *being interrogated* no longer generate danger. The pre-patch figure was +20 danger per interrogation, which is where this corpus's unsourced "(adds danger)" came from. This guide is built against the fully-patched game (`nav/architecture.md` manifest), so the retraction applies here.
2. **The danger was never from the act of interrogating.** It came from *holding* captured enemy agents in the Hideout -- a continuous drip for as long as they sit there, which is why the pre-patch advice was to capture only as many as you can process at once. **Faraday Cages (Ch4) remove it entirely.**
3. **None of it applies to interrogating your own roster agent.** There is no prisoner being held, so there is no holding cost -- the recruit-screening use above costs money and nothing else.
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_

> **Cross-system dependency** -- see `dependencies.md` DEP-001: MK-ULTRA not existing until Ch3 is why the Ch1 CIA mission forces a kill instead of a capture. [Confirmed: 3 sources, 1 language]

## Mole hunt (Undertow)

**Strategic Hideout mechanic, confirmed at P2 (2026-08-18) -- resolves a P1 open question.** At some point in the mid-late campaign, Omikron begins vetting the player's roster. A randomly-selected existing agent is flagged as the Beholder mole "Undertow" through one of several strategic story branches: a failed polygraph, a mysterious illness/isolation event, or a drunk-spouse accusation. Selection is effectively random -- even brand-new or previously "loyal" agents can be tagged. `entity: undertow`, `entity-status: hostile`, `entity-hidden: yes` -- see `npcs/undertow.md`. This entire beat plays out at the Hideout (Analytics/MK-ULTRA); it is never a tactical mission, and has no `nav/<zone>.md` file.

**Correction (2026-08-20): "must be executed" overstated the certainty here.** MK-ULTRA's Brainwash option (erases an agent's sleeper conditioning/allegiance, at risk of destroying their existing perks) is mechanically usable on the Undertow-flagged agent, same as any suspected-own-agent -- it is not an Execute-only interaction. Community reports are split on whether Brainwash also satisfies the story trigger: one player reports brainwashing the flagged agent and continuing to use them with no issue; another claims the specific "Undertow burial scene" story beat requires the agent actually processed as a kill through MK-ULTRA, not just brainwashed. No confirmed tie-breaker found. **If avoiding a progression stall matters more than keeping the agent, Execute is the documented-safe path** (it's what the rest of this corpus's story-progression research assumes); Brainwash is a real option if you'd rather keep the agent and are willing to risk a possible stall and perk loss.

**Soft-lock warning:** this beat is a notorious progression-bug hotspot -- players report getting stuck if Investigation Board dossiers are unsolved, or if the flagged agent happens to be away in training when the mole-hunt event fires. Keep dossiers current and avoid leaving agents mid-training if progression stalls here.

See `npcs/undertow.md` for the full entity writeup.
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 3 sources, 1 language]

> **Cross-system dependency** -- see `dependencies.md` PON-001: the flagged mole must be executed via MK-ULTRA before the story can progress.

## The Cabal -- roster and recruitment

Max roster with all upgrades, per developer CFG_Hitch on Steam (verbatim): "The maximum number with all upgrades is 40 agents on easy, and 35 agents on hard." A practical hireable ceiling, per Steam user Cahos Rahne Veloza: "Max number of Agents you can hire is 38 which also includes the ones you can 'convert.' Once you have 38 you can only add more by capturing them and making them sleeper Agents." Agents cap at **level 20** with 8 training slots and 12 perks (excluding background perks). Candidates come from solved secret files, strategic jobs, and rescued informants. The main character cannot die without triggering game-over; other agents are expendable.

See also `factions/the-cabal.md` for The Cabal as an organization.

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 5 sources, 1 language · class:official-pr+forum]

**The $10 hire trio -- a hard-coded, pre-authored offer (save-verified 2026-09-16).** Three candidates can appear at a flat **cost 10**: **Clover (Melika Shajarian, SAVAK)**, **Luna (Ai She, Freelance)**, **Wraith (Dinh Xuan Phu, Triads)**. They are not part of the random hire pool -- their uniqueids are `player_agent_tp1/tp2/tp3`, the **only three `player_agent_*` entries in the entire save**, and they were already present as `NotInitialized` with the same names and `cost=10` in the 2026-08-20 dump, i.e. sitting in the campaign from the start. Ordinary hire-pool candidates are `generated_agent_*` at ~$1760. They also carry `XPWorth=0` where generated candidates carry 1200. **Why the price is 10 is not determined** -- nothing in the save explains it; don't invent a reason.

**Their advertised stats are already compound-boosted.** All three arrive with **AMPEA + BMA + DXAMPEA pre-applied**; raw bases are ordinary (62/61/61/61, 69/61/64/60, 67/64/60/61) and the dossier figures reproduce exactly as base + those three. **Because they carry BMA they are locked out of Danazol and AMPK from the moment you hire them** -- BMA-carrier route only, unless Remove All is spent on them. Completed trainings, from `completedtrainings` (reliable): Clover -- Warzone Operations (`training_11`); Luna -- **Night Operations (`training_08`, grants Eye for Talent)**; Wraith -- Advanced Firearms Drill (`training_09`).

**Their OWNED perks are not recorded here, and must not be read from `levelupperks` -- see the trap note in `save_schema.md`.** Each dossier shows 4 filled perk tiles plus 3 unrevealed slots; naming the filled ones needs a tooltip read in-game. What `levelupperks` does give is each one's **next level-up draw** (all three sit at 600/6400): Clover would be offered Scar Tissue / Peripheral Vision / Composure / Survivor; Luna, Combat Senses / Survivor / Low Profile / Vietnam Veteran; Wraith, Scar Tissue / Masochist / Paramedic / Expert Marksman.

_source: live save read 2026-09-16 (`pdsauto0.PDSave`) cross-checked against `the player's save file (via save_extract.py)` 2026-08-20 + player dossier screenshots · capture: save XML + manual_paste · confidence: high (save-verified) for the roster facts, **not determined** for the reason behind the price · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Hire Danger -- live-play finding, not previously documented.** Every hire-candidate dossier shows a red "HIRE DANGER +50" warning next to the Hire button, in addition to the cash cost -- hiring adds directly to the Hideout's Danger meter (see `nav/hideout_hub.md` for what Danger does). Confirmed across all 5 candidates on one hire-list screen (initially misread as 3 of 4 -- corrected 2026-08-20). Checked the live save's XML for a per-candidate danger value and found none; only the global `Danger` meter and `HideoutDanger` threshold exist as save fields. That absence, plus the identical "+50" across every candidate observed, points to this being a **flat cost applied to any hire**, not a per-candidate stat -- factor it into every hiring decision, not just some.

**Hire-candidate pool rotates -- confirmed via editorial source.** The hire list only ever shows a handful of candidates at once (5 observed in one live save, matching the in-game screen); "unlocking" more candidates via Investigation Board / intel work does not add them all to the visible list -- they queue behind it. Per gamepressure.com's tips guide: candidates are **not permanently available** -- after successful tactical/investigative missions you get new candidates to hire, but each candidacy expires after some unspecified time and the candidate then moves to the enemy side, permanently lost. The exact expiry window (real-time, mission count, or specific triggers) isn't stated by this source and remains unconfirmed. Practical read: hire what you want off the visible list promptly rather than treating it as a stable backlog.

A separate, still single-source and unconfirmed claim (a different Steam Community thread): a Workshop tech upgrade may increase how many candidates show at once -- worth checking Workshop options if 5 feels cramped, but not verified against gamepressure or this playthrough.

_source: live-play screenshot 2026-08-20 (Hire Danger) + live save XML read 2026-08-20 + gamepressure.com "General tips" guide, tip on candidate expiry (WebFetch 2026-08-20, editorial) + separate Steam Community thread (pool-size-upgrade claim) · capture: manual_paste + web_fetch · confidence: high (Hire Danger, save-verified; candidate expiry/turnover, editorial source) / low (pool-size-upgrade claim, single forum source, unverified) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Hire dossiers preview perks the candidate already has.** The PERKS row on a hire-candidate screen shows perks already earned by that candidate (same icon set as the level-up Perk panel, `items/abilities.md`), not empty slots to fill. Player-confirmed identification on one candidate: Spade (Hideo Yamada, PSIA background) carries **Actor** (god-tier, see `items/abilities.md`). Other icons seen across the same candidate pool (a running-figure icon, a shield icon, a building/network-style icon) are not yet identified by name -- hover the icon in-game for its tooltip rather than trusting a shape-based guess.

_source: live-play screenshot 2026-08-20, Actor identification player-confirmed · capture: manual_paste · confidence: high (Actor) / unconfirmed (other icons on the same screens) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## HQ facility screens

| Facility | Function |
|---|---|
| Crew Quarters | Roster, perks, equipment |
| Communications (Comms) | Signal analysis, leads (unlocked later) |
| Forger | Forge cash, new identities to reset Heat, appearance/ID customization |
| Infirmary | Healing; buy extra beds early |
| Workshop | Craft items, research the tech tree, unlock facilities |
| Analytics | Decrypt intel / solve secret files automatically |
| Body Engineering | Chemical compounds to boost stats |
| MK-ULTRA | Interrogation / brainwashing |
| Faraday Cages | Reduces danger generated by held prisoners (Ch4) |

Facilities beyond the starting set unlock through Workshop tech + story progression. **Unlock cadence -- CONFIRMED at P2:** Body Engineering (Ch2), MK-ULTRA (Ch3, story-mandatory), Communications (Ch3, last of the chapter-gated facilities to unlock), Faraday Cages (Ch4). Full per-facility detail (cost, build time, danger/relocation mechanics) lives in `nav/hideout_hub.md`.

_source: deep-research P1 2026-08-18, extended P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 5 sources, 2 languages · class:community-wiki+editorial-en]

## Crafting / trading (Tinker / Merchant)

**Workshop crafting** builds items (grenades, silencers, support gear, armor) for cash from unlocked blueprints; *Tinker* = craft 50 items. **Buying** happens via the Vendor/inventory "buy" option (blueprints unlocked from interrogation/trade contacts/loot); *Merchant* = buy 50 items. Money is earned passively per hour and via forging (see Economy note below).

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 4 sources, 1 language · class:community-wiki+forum]

## Difficulty modes (Easy / Normal / Hard)

Difficulty changes **far more than damage/HP.** Per LordRedStone and PSNProfiles:

- **Easy:** you can knock out ANY enemy agent (not just lower-HP ones). Starting cash **$15,000.**
- **Normal:** starting cash **$10,000.**
- **Hard:** you **cannot hide bodies at all**, and takedowns require higher HP than the target. Evac arrives 1 turn later (4 vs 3 turns), enemy reinforcements arrive 2 turns earlier (2 vs 4 turns), enemies have more HP/damage, enemies run more world-map jobs (faster danger/doomsday buildup), informers are slower and more likely to be assassinated, Analytics/investigation work slower, and moles/prisoners generate more danger. Starting cash **$5,000.**

Passive hideout income is roughly $40/hr regardless of difficulty (see Economy note -- distinct from the per-Forger $20/hr figure).

Difficulty also affects starting/max agent count and disguise-slot count (see Disguises section above).

**Community consensus that contradicts "harder is harder throughout":** the game is hardest **early** and easiest **late** -- endgame stats/perks trivialize stealth regardless of difficulty. Ironman is available on every difficulty.

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 5 sources, 1 language · class:forum+community-wiki]

## Economy note (Forger)

The Forger provides base income of **$20 per hour per forger** (per gamepressure's official guide: "Initially, you can hire only one forger who earns $20/hour"), rising with Workshop upgrades that increase forgers allowed and income per forger (players cite ~$40/hr after the printing-press upgrade -- this is a *different* income stream from the passive hideout base income noted in Difficulty above, not a contradiction). Forging is also the primary way to reset an agent's Heat via a new identity ($500 base). *Counterfeit Fortune* = forge $500,000 total.

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**New-identity cost reduced to $460 via Workshop research, 2026-08-27.** Player completed a tech-tree upgrade for cheaper agent identity forging; the per-agent new-identity price dropped from the $500 base noted above to **$460**. Exact tech id not looked up (no `tech_NNN`->name map exists yet, see `save_schema.md`).

_source: live-play, player-reported 2026-08-27 · capture: manual_paste · confidence: high (player-observed in-game price change) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 3 sources]

**Second reduction, 2026-09-16: another Workshop research completed, price dropped from $475 to $410.** Exact tech id not recorded. **Unreconciled discrepancy: this entry's pre-drop price ($475) does not match the $460 this file already had on record from 2026-08-27** -- the price may scale with something else between forges (chapter, heat, or agent count) rather than staying flat, or one of the two player-reported readings is off. Not investigated yet; treat $410 as the current price and flag this gap rather than silently overwriting the $460 note above.

**Checked 2026-09-16: no evidence found that per-agent identity cost scales up per use/check.** WebSearch (Fandom Technology Tree/Forger pages, Steam Community discussions, gamepressure.com) consistently describes a single flat base cost ($500) reduced only by Workshop tech-tree upgrades (e.g. $500 -> $460 for one documented upgrade tier) -- no source describes the price climbing with repeated use, agent count, or any other per-check multiplier. This doesn't explain the $460-vs-$475 discrepancy above (could be a different/undocumented mechanic, a patch change post-dating these sources, or one of the two player reads being off) -- treat "cost increases per use" as unconfirmed, not ruled impossible, since community coverage of this specific detail is thin.

_source: WebSearch 2026-09-16 (Fandom Technology Tree, Fandom Forger page, Steam Community discussions) · capture: web_fetch · confidence: medium (negative finding across several community sources, not an official patch-notes/manual source) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

_source: live-play, player-reported 2026-09-16 · capture: manual_paste · confidence: medium (player-observed price change, but conflicts with the prior recorded price -- see discrepancy note) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Early-game money -- best sources

Four corroborated income moves for the early game: (1) **sell unequipped gear** -- weapons/armor/items sell for roughly 80% of purchase value, a generous rate; rule of thumb is sell anything you're holding more than 2 spares of. (2) **loot every mission**, including documents, and use trading contracts to offload unwanted loot once discovered. (3) **keep every Forger slot manned 24/7** -- this is the steadiest passive income stream (see Economy note above) and idle Forger capacity is pure lost income. (4) **craft high-margin items to resell** -- among quick personal-gear/items crafts, **Decoy tops the tier at $25.00/hr** (with the Crafting perk), edging out lockpicks and all silencer variants; the separate, longer-craft Support Items tier runs higher still, topping out at **Neurotoxin, $25.91/hr** (see tables below). Risk-management note found alongside the above: keep a reserve of roughly **$4,000** rather than spending to zero, since identity changes (Heat reset) and emergency base relocation both need cash on hand.

**Craft-for-profit table, personal gear/items** (time shown as standard/with-Crafting-perk; $/hr columns match):

| Item | Sell | Cost | Profit | Time (std/perk) | $/hr | $/hr (perk) |
|---|---|---|---|---|---|---|
| Flashbang | $650 | $500 | $150 | 12h/8h | $12.50 | $18.75 |
| Smoke Grenade | $715 | $550 | $165 | 12h/8h | $13.75 | $20.63 |
| Acid Cloud | $740 | $570 | $170 | 12h/8h | $14.17 | $21.25 |
| CS Grenade | $755 | $580 | $175 | 12h/8h | $14.58 | $21.88 |
| Blister Gas Bomb | $755 | $580 | $175 | 12h/8h | $14.58 | $21.88 |
| Rimfire Suppressor | $900 | $750 | $150 | 10h/7h | $15.00 | $21.43 |
| Subsonic Ammo | $700 | $500 | $200 | 13h/9h | $15.38 | $22.22 |
| Rifle Suppressor | $925 | $770 | $155 | 10h/7h | $15.50 | $22.14 |
| Lockpick | $830 | $640 | $190 | 12h/8h | $15.83 | $23.75 |
| Monolith Suppressor | $950 | $790 | $160 | 10h/7h | $16.00 | $22.86 |
| Expanding Bullets | $730 | $520 | $210 | 13h/9h | $16.15 | $23.33 |
| Riot Slugs | $755 | $540 | $215 | 13h/9h | $16.54 | $23.89 |
| **Decoy** | **$870** | **$670** | **$200** | **12h/8h** | **$16.67** | **$25.00** (best of this tier) |

_Decoy cost/sell confirmed live-play 2026-08-19: player-reported $670 craft cost / $870 sell price, matching the researched figures exactly._ [_source: live-play confirmation 2026-08-19 · capture: manual_paste · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_]

**Support items tier (higher time investment, higher ceiling):**

| Item | Sell | Cost | Profit | Time (std/perk) | $/hr | $/hr (perk) |
|---|---|---|---|---|---|---|
| Sniper (silenced) | $750 | $500 | $250 | 16h/11h | $15.63 | $22.73 |
| Sniper (loud) | $765 | $510 | $255 | 16h/11h | $15.94 | $23.18 |
| Sweeping Spotter | $795 | $530 | $265 | 16h/11h | $16.56 | $24.09 |
| Grenade Launcher | $810 | $540 | $270 | 16h/11h | $16.88 | $24.55 |
| Smoke Screen | $825 | $550 | $275 | 16h/11h | $17.19 | $25.00 |
| Poison Gas Cloud | $840 | $560 | $280 | 16h/11h | $17.50 | $25.45 |
| Neurotoxin | $855 | $570 | $280 | 16h/11h | $17.81 | **$25.91** (highest $/hr overall) |

Both tables give standard craft time and craft time with the Crafting perk side by side; the $/hr and $/hr(perk) columns match those respectively.

_source: live-play WebFetch 2026-08-19, full tables direct from Steam Community guide "Profit with Workshop items" (steamcommunity.com/sharedfiles/filedetails/?id=1542666251) · capture: web_fetch · confidence: high (single primary source, internally consistent, cross-checked against an earlier WebSearch summary of the same guide -- all overlapping figures matched exactly) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 1 primary source (full table), 1 corroborating summary · class:forum]

## World-map assault missions -- timing

Assault missions dispatch instantly: any agent not already on a mission or in transit can be sent regardless of physical map position, so there's no travel-time reason to delay. Delaying anyway has a real cost -- danger level rises for every turn the mission sits unassaulted, and the enemy can bring in reinforcements (up to heavy weapons/air support) the longer it's left. Net guidance: take an assault mission as soon as a free agent is available to send; there's no benefit to waiting and a real cost to it.

_source: live-play WebSearch 2026-08-19 · capture: web_fetch · confidence: medium (Steam Community + GameInformer + PCGamesN, not deep-research-cascade sourced) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 3+ sources, 1 language · class:editorial-en+forum]

## Third-party modding

Modding is not Steam Workshop-based -- CreativeForge opened up direct CSV-file editing (key game variables) instead, documented in an official modding guide. As of the 2026-08-19 check, ModDB's mod list is thin: one released mod ("Better Trainings," tunes training/weapon proficiency stats), nothing addressing squad/mission-assignment UI or roster-management pain points specifically. Same result for a remaining-loot/document counter -- no mod exists; players have floated it as a wishlist idea for if modding tools ever expand, not something shipped.

**Correction, 2026-08-20: the ModDB-only check above missed Nexus Mods, which has a more active scene.** Standout: **"Gameplay RE-Vision"** (NMKopfkino, still updated as of October 2024) -- a broad QoL overhaul: cuts long wait times/animations, revamps abilities/reactive abilities, shortens training duration to 24h, and makes disabling *enemy* Overwatch sound the alarm if spotted. **No confirmed auto-Overwatch (player-side) mod found** -- the mod's page itself was blocked from direct fetch (403), so this isn't a complete feature-list check, just what surfaced via search snippets.

_source: live-play WebSearch 2026-08-20 (Nexus Mods search results; direct page fetch blocked) · capture: web_fetch · confidence: low-medium (mod's full feature list unverified, snippet-only) · enemy-tier: 0 · puzzle-tier: 0 · category: meta (not in-game content) · spoiler: none_

**Correction, 2026-08-22 (live-play, direct install check): "CSV-file editing" above is wrong -- confirmed against the actual install (the game's Steam install folder).** No `.csv` files exist anywhere in the install. What actually ships loose and editable is **XML** under `IWTB\Content\Data\Design\` -- `MissionLogic\` (per-mission objective/trigger logic, one file per `L###_...` map) and `StrategicLogic\` (`Campaign01`-`Campaign11.xml` + a few standalone files). This is genuinely useful for modding mission/campaign logic, but **does not include Workshop tech-tree definitions** -- checked directly: the only `tech_`-prefixed content in any loose XML is a dev leftover in `StrategicLogic/AnnouncementLogic.xml` (`ab_tech_NN_facilityname` ids under a comment reading "Secret, temp objectives... to be deleted when the actual tech system starts working") -- a different id scheme from the save's `tech_NNN`, and explicitly stale placeholder content, not the live system. **The real tech/item definitions are compiled into two packed Unreal asset archives**, `IWTB\Content\Paks\pakchunk0-WindowsNoEditor.pak` (~9.6 GB) and `pakchunk1-WindowsNoEditor.pak` (~13.6 GB) -- not readable as text; would need an Unreal asset-extraction tool (e.g. FModel, UnrealPak) to pull DataTable contents, which is a materially bigger undertaking than anything else in this corpus's research method. Not attempted this pass -- flagged as a possible future avenue for solving the `tech_NNN` id-mapping gap if the player wants to invest in it, in `save_schema.md`.

_source: live-play direct filesystem check 2026-08-22 (the game's Steam install folder) · capture: manual_paste · confidence: high (files enumerated directly, not inferred) · enemy-tier: 0 · puzzle-tier: 0 · category: meta (tooling, not in-game content) · spoiler: none_

**Built-in alternative (no mod needed):** the pause menu shows per-mission stats, including loot/document counts, in the top-left corner. A full Recon of an area also uncovers the whole map and makes unfound intel glow gold/yellow and loot glow light blue -- loot's glow is reportedly easy to miss even then.

**Why loot/docs still get missed after Recon -- live-play + WebSearch finding, 2026-08-20.** Four community-reported causes, independent of whether Recon was run:
1. **The two glow colors mark different things, not one generic "unfound item" glow:** glowing **blue cabinets/safes** = weapon/armor/mod loot (occasionally intel too); glowing **yellow files** = intel-only. Scanning for one color misses the other category.
2. **Containers get visually hidden behind furniture/walls depending on camera angle.** A single top-down pan across a room is not enough -- rotating the camera through a few angles per room is necessary to catch containers occluded from the default view.
3. **Loot is sometimes placed on rooftops or upper levels**, easy to skip if only the main floor gets checked.
4. **The pause-menu counter itself is reported buggy/miscounting by some players.** If a room-by-room, multi-angle search still doesn't match the counter, that may not be player error.

_source: live-play WebSearch 2026-08-20 (Steam Community: "Finding the last loot or doc on the map," "How to tell where intel/cache are?," "Can't ever seem to find all loot," "Disappearing Documents") · capture: web_fetch · confidence: medium (consistent across multiple independent forum threads, not cross-checked against an editorial source) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

_source: live-play WebSearch 2026-08-19 · capture: web_fetch · confidence: medium (single-pass search, not exhaustive) · enemy-tier: 0 · puzzle-tier: 0 · category: meta (not in-game content) · spoiler: none_ [Confirmed: 2 sources, 1 language · class:community-wiki]

## Sources

- LordRedStone, "The best perks" & "Tech Upgrades Flowchart" (113 elements), Steam guides (English, 2018-2026).
- Phantom Doctrine Fandom Wiki: MK Ultra, Technology Tree, Body Engineering, Agents, Tips, Hideout (English, community-wiki).
- gamepressure.com guide: base upgrades (English/Polish origin, editorial, 2018).
- TV Tropes, VideoGame/PhantomDoctrine (English, editorial) -- starting cash, handlers, support roles, brainwashing.
- Steam Community discussions: difficulty differences, agent cap (CFG_Hitch dev posts), brainwashing, crafting/trading, Undertow/mole-hunt threads (English, forum, 2018-2020).
