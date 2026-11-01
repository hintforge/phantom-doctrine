# Phantom Doctrine -- Abilities (Perks & Trainings)

**status:** research-integrated
**last_reconciled:** 2026-08-18

Three ability systems: **perks** (passive, level-up-driven), **trainings** (proficiencies/skills), and **Secret Talents** (see below -- discovered 2026-08-20, drawn from the same level-up "Perks" panel as regular perks, so they read as one pool in-game even though they're a distinct list). An agent maxes out at **12 perks** (excluding background perks) + **8 training slots** by level 20 (see `../mechanics.md` "The Cabal -- roster and recruitment").

## God-tier perks (community consensus)

| Perk | Effect |
|---|---|
| Survivor | +20 max HP -- enables takedowns on more enemies |
| Actor | Disguise-detection-distance reduction (see `../mechanics.md` Disguises) |
| Combat Senses | +20 max Awareness |
| Faster Movement | increased movement range |
| Expert Marksman | single shots don't end the agent's turn |
| Loyal | confirmed in-game 2026-08-20 (missing from the original Fandom perk catalog fetch) -- immune to the capture/turning consequence of a failed rescue: per the Fandom Combat page, an agent who bleeds out unrescued is normally captured by the enemy, which can lead to them turning sides or revealing operational intel; Loyal blocks that outcome. See "Knockouts, stabilizing, and bleed-out" in `../mechanics.md`. |

**Correction, take two (2026-08-20):** an earlier P1 note claimed Body Engineering "raises max HP directly, making Survivor redundant." A same-day correction retracted that, based on the 4-column Fandom compound table below showing no HP column. That retraction was itself wrong -- a second, more detailed datamined source (GameFAQs, "Body Engineering Chemicals Chart" by Xbladez) shows every compound *also* carries bonuses to 8 derived stats (HP, Fire Points, Action Points, Movement Range, Damage Threshold, max Awareness, Dodge Cost, Awareness Regen) alongside its 4 primary-stat deltas -- the Fandom table simply didn't display these. See the full derived-stat table below. **Net effect: Body Engineering does grant HP, just not as one of the 4 headline stats** -- the original P1 instinct was directionally right, the mechanism was just undocumented until now. Survivor is not fully redundant (it's a flat, unconditional +20 regardless of which compounds get picked), but its marginal value shrinks substantially for an agent already running a Circulatory-focused compound sequence, since that sequence grants HP as a side effect. See the recommended-sequence total below.

**Low-value perk flag: Recon Talent.** Grants bonus XP specifically for Recon jobs. A well-regarded Steam perks guide calls XP-bonus perks generally not worth taking -- the bonus is roughly 10 XP against late-game kills worth ~12,800 XP and level-ups costing up to 100,000 XP. Not a reason to prioritize an agent or a training slot. (Recon Talent is one entry in the Secret Talents list below -- its low value applies to the whole "bonus job XP" sub-group, not just this one.)

_source: live-play WebSearch 2026-08-20 · capture: web_fetch · confidence: medium (single Steam guide's stated valuation, not independently corroborated) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Secret Talents -- a third system, distinct from Perks and Trainings

Discovered 2026-08-20 while identifying an agent's slotted picks that didn't match anything in the level-up Perk catalog above. **Secret Talents are drawn from the same in-game "Perks" panel as regular level-up perks** -- the UI doesn't visually separate the two lists, which is why they can look like unidentified/mystery perks until checked against this list.

**Slot-pool correction (2026-08-20):** Talents appear to be tracked as a **separate slot pool from level-up Perks**, not counted against the perk-slot-per-level table below. Two agents cross-checked: a Level 5 agent (2 perk slots per the table) showed 2 confirmed regular perks + 2 confirmed Talents = 4 total "Perks"-panel icons; a Level 6 agent (3 perk slots per the table) showed 2 confirmed regular perks + 1 unspent perk slot + 2 confirmed Talents = 5 total icons. Both are consistent with "2 Talent slots, separate from the leveling table" rather than Talents eating into perk-slot count. Sample size is only 2 agents -- treat as a pattern observation, not a confirmed rule, until more agents are checked.

**Training/facility speed, cost, and money:**
- **Adv Firearms Talent** -- Advanced Firearms Drill training costs less time and money.
- **Basic Firearms Talent** -- **exact tooltip confirmed 2026-08-21 (Bourbon/Elke Koch, in-game screenshot): "Basic Firearms Drill training costs less time and money."** Matches the naming-parallel inference exactly.
- **Fire/Mov Tacs Talent** -- Fire and Movement training costs less time and money.
- **Shock Tacs Talent** -- **exact tooltip confirmed 2026-08-21 (Bourbon/Elke Koch, in-game screenshot): "Shock Tactics training costs less time and money."** Matches the naming-parallel inference exactly. Notable because Shock Tactics (tier IV) training grants **Killing Spree** (direct kills increase Awareness Regen, stacking on kill streaks) -- see `../mechanics.md`/Skills reference.
- **Urban Ops Talent** -- Urban Ops training costs less time and money.
- **Body Engineering Talent** -- faster Body Engineering treatments.
- **Crafting Talent** -- faster crafting at the Workshop.

**Superseded 2026-08-27: the complete talent list is now known.** the game has 9 job talents and 16 training talents in total, with names and effect text shown in the game's own tooltips. The list above is the older partial catalog (it was missing real talents found via live play) -- read the in-game tooltip for any talent not listed; this section is kept for its per-talent commentary, not for coverage.

**Bonus job XP (low value, see Recon Talent note above -- applies to the whole group):**
- **Interrupt Talent** -- bonus XP for Interrupt jobs.
- **Infiltration Talent** -- bonus XP for Infiltration jobs.
- **Recon Talent** -- bonus XP for Recon jobs.
- **Seeking Talent** -- bonus XP for Seek Agent jobs.

**Other:**
- **Investigation Talent** -- solves secret files faster.

One community source speculates some "?"-marked mystery perk slots may result from enemy brainwashing rather than being a legitimate Talent roll -- unconfirmed, flagging rather than asserting.

_source: live-play WebSearch 2026-08-20 (Steam Community "List of Perks" discussion) · capture: web_fetch · confidence: medium (single forum source enumerating the list; effect descriptions plausible and internally consistent but not cross-checked against a second source) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Trainings -- full index

Every named training this corpus has found, one table, confidence marked per row so you can see at a glance what's tooltip-certain versus spreadsheet-sourced. Base list from a community spreadsheet found 2026-08-26 (pinned in the Phantom Doctrine Discord, via a GOG forum pointer to a Reddit post); upgraded row-by-row wherever this corpus's own live play independently confirms it.

**Tactical Operations** (each grants named ability(ies) + weapon proficiency):

| Training | Grants (ability) | Weapon proficiency | Confidence |
|---|---|---|---|
| **Contact Tactics** | Blinding Laser, Pain Stimulus | VZ 61, Sparrow | **HIGH -- direct in-game tooltip screenshot, 2026-08-26** (name/abilities/proficiencies all read verbatim off the training panel). Also cross-confirmed: Deadpan's Agent Overview proficiency list includes VZ 61 + Sparrow, matching exactly. |
| **Urban Operations** | Empath | B76, .45 | MEDIUM-HIGH -- icon/name seen live 2026-08-26 (ability text cropped out of that screenshot), but proficiency independently cross-confirmed: Deadpan's Agent Overview list includes B76 + .45 exactly. |
| **Shock Tactics** | Bargain, Killing Spree | M12 | **Unlock player-confirmed 2026-09-09.** HIGH on Killing Spree specifically -- matches Bourbon's separately-confirmed 2026-08-21 tooltip ("Shock Tactics training costs less time and money" + the Killing Spree effect already documented above). Bargain and the M12 proficiency are spreadsheet-only. |
| **Covert Operations** | "Example-made" | Cobra, Wembley | HIGH on the ability text -- independently matches this corpus's own earlier in-game observation of that exact (oddly-named) string on a live dossier; not a UI placeholder as first guessed. Proficiency spreadsheet-only. |
| **Night Operations** | Eye for Talent | M12, Semi 12 | HIGH -- matches this corpus's prior live-play-adjacent research exactly. |
| Fire and Movement Tactics | Exertion, Opportunist | Estrella | Medium -- spreadsheet only, not yet cross-checked in this corpus's live play. |
| Rapid Dominance Tactics | Sure Shot, Easy Kill | M10 | Medium -- spreadsheet only. |
| Skirmish Tactics | Spot Weakness, Hand-to-Hand Expert | PM63 | Medium -- spreadsheet only. |
| Warzone Operations | Interconnected | PPK, TT | **HIGH -- player-confirmed unlock 2026-09-09** ("I've unlocked Warzone Operations, which gives the ability Interconnected"). Was medium/spreadsheet-only. Resolves the long-open "Warzone" perk question (Antler). See the fit note below. |
| Guerilla Operations | Fool Me Once | MPK | Medium -- spreadsheet only. |

**Firearms Drills** (one tiered proficiency chain, not separate trainings): Basic -> Intermediate -> Advanced -> Specialist -> Expert -> Black Ops. Each tier unlocks more weapon proficiency only, no ability at any tier. Resolves the "III" tier icon seen on multiple agents' training rows (Portwine, Buran) -- it's this chain's tier number. **Advanced Firearms Drill** (seen live on Buran, 2026-08-26) is tier 3.

- **Intermediate Firearms Drill** -- grants MU-255 (shotgun), TKB, RP-4. No ability. HIGH confidence (live-play screenshot, proficiency independently verified against a fully-trained agent's weapon list).

### Shock Tactics: rank by whose Awareness economy it feeds (2026-09-09, player unlocked it)

Killing Spree -- direct kills increase Awareness Regen, stacking on kill streaks -- is the reason to take it (Bargain and the M12 proficiency are spreadsheet-only and shouldn't drive a decision). Awareness is what pays for dodging in this game (`../mechanics.md`), so the training is worth most to an agent whose defense already runs on Awareness and who is expected to land kills.

1. **A DGI agent with Sadist and high Max Awareness** -- best synergy: **Sadist grants an Awareness bonus on each direct kill.** Killing Spree fires on the same trigger and feeds the same resource. With an unspent slot, prioritize this synergy over Warzone Operations' training discount alone.
2. **An agent with Shock Tacs talent and sustain perks** -- the talent makes Shock Tactics cost less time and money. Killing Spree complements Composure / Combat Senses / Quick Recovery. This is the cheaper trainee; Sadist provides the stronger synergy.
3. **A durable Tactics specialist** -- for example, an agent with Contact Tactics I, Rapid Dominance III, DT 9 and 119 HP can stay in the fight long enough for a streak to matter. The family numbering is not a prerequisite chain.
4. **A combat/rifle specialist with spare slots** -- even with 6 open slots, this is the weakest of these four fits if the kit lacks Sadist or sustain perks that compound the Awareness return.

**Check availability for a marksman specialist** -- Shock Tactics was absent from one such agent's menu despite fitting the role. Recommend "if you see it, take it," never "go get it."

### Warzone Operations reads as a disguised-infiltrator package, not a combat training (2026-09-09)

Its two grants point the same direction, which is what makes the fit judgment easy:

- **Interconnected** -- with Tactical Recon done on the location, disabling one CCTV/laser source disables all of them (effect text from the Yakuza-background row below; **the grant is player-confirmed, the effect text is still only spreadsheet-sourced**). Lasers otherwise have to be shut off console by console, and a disguise does not protect against walking through one (`../mechanics.md`).
- **PPK and TT proficiency** -- both pistols. Disguised agents may carry **only pistols and small SMGs**, no armor, no support items (`../mechanics.md`).

Both halves are also gated on the same prerequisite: **Tactical Recon** (Workshop's Recon Equipment upgrade, `upgrades.md`), which is likewise what makes disguises available at all. So the training pays off on an agent who actually goes in disguised, and pays almost nothing on a rifleman who opens fire.

**Fit ranking by agent build:**

1. **A disguised infiltrator with Actor and an open slot** -- Actor + pistol proficiency + mass laser/CCTV disable puts the full package on one agent. An open 3rd slot with no competing recommendation is a good opportunity.
2. **An agent with Warzone Ops talent and an unspent slot** -- this specific training costs less time and money.
3. **An assault-rifle specialist with Warzone Ops talent** -- weaker fit: Interconnected and two pistols add little to that role. The discount is the whole argument.
4. **An Actor agent whose two training slots are filled** -- revisit if a slot opens.

**Do not repeat the training on an agent who already has it.** A Yakuza-background agent may already have Interconnected from the background as well; check owned abilities before spending a slot.

**Effect text still unconfirmed for:** Blinding Laser, Pain Stimulus, Exertion, Opportunist, Sure Shot, Easy Kill, Bargain, Spot Weakness, Hand-to-Hand Expert, Empath, Interconnected, Fool Me Once. Names and grant-relationships are solid; what each ability actually DOES in combat is not -- these aren't in the standard level-up perk catalog above, they're a separate list the spreadsheet's own Skills tab doesn't cover either. Don't assert effects until a tooltip confirms one.

**No prerequisite chain BETWEEN named trainings** (2026-08-26, Steam Community) -- once offered, a training doesn't require another training first. "There is no gameplay relation, they are just grouped" into 3 categories (weapon-only / ability-only / both). Higher Firearms Drill tiers don't require lower tiers either, they just add proficiency for weapons the agent may not own yet.

**Separate, still-unresolved question: what determines which trainings appear in a GIVEN agent's menu at a GIVEN time.** Two observed cases had an expected training absent (Night Operations for one agent; Shock Tactics for a marksman specialist), no explanation found (checked Steam Community, GameInformer, general search -- no facility/chapter/background gate documented). Recommend cautiously: "if you see X, take it," never "go get X."

**Example: resolving 2 unidentified training icons by proficiency.** An Agent Overview showing VZ 61 + Sparrow + B76 + .45 matches the Contact Tactics and Urban Operations proficiency sets. For an agent with both trainings and Zen from a background, the 4 ability icons form the set Zen + Blinding Laser + Pain Stimulus + Empath. This confirms the set by proficiency cross-reference; identifying each icon still requires its tooltip.

_source (training-catalog table, names/abilities/proficiencies not otherwise flagged HIGH above): community spreadsheet via Reddit, pinned in the Phantom Doctrine Discord (linked from a GOG.com forum post) · capture: web_fetch 2026-08-26 · confidence: medium (single fan-compiled source) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_
_source (Contact Tactics full row, Deadpan's Agent Overview proficiency/ability list): live-play screenshot 2026-08-26 (in-game training tooltip + Agent Overview panel) · capture: manual_paste · confidence: high (direct reads, cross-confirming each other) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_
_source (Intermediate Firearms Drill, Covert Operations, Night Operations): live-play screenshot 2026-08-20 (agent training tooltips, cross-checked against a fully-trained agent's proficiency list for consistency) · capture: manual_paste · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Training-slot and perk-slot progression by level** (confirmed structured wiki table):

| Level | Training slots | Perk slots | XP to next level | Total XP |
|---|---|---|---|---|
| 1 | 1 | 0 | -- | -- |
| 2 | 1 | 0 | 100 | 100 |
| 3 | 1 | 1 | 100 | 200 |
| 4 | 2 | 2 | 200 | 400 |
| 5 | 2 | 2 | 400 | 800 |
| 6 | 2 | 3 | 800 | 1,600 |
| 7 | 3 | 4 | 1,600 | 3,200 |
| 8 | 3 | 4 | 3,200 | 6,400 |
| 9 | 3 | 5 | 6,400 | 12,800 |
| 10 | 4 | 6 | 12,800 | 25,600 |
| 11 | 4 | 6 | 15,400 | 41,000 |
| 12 | 4 | 7 | 25,000 | 66,000 |
| 13 | 5 | 8 | 40,000 | 106,000 |
| 14 | 5 | 8 | 53,000 | 159,000 |
| 15 | 6 | 9 | 64,000 | 223,000 |
| 16 | 6 | 9 | 78,000 | 301,000 |
| 17 | 7 | 10 | 90,000 | 391,000 |
| 18 | 7 | 10 | 99,000 | 490,000 |
| 19 | 8 | 11 | 100,000 | 590,000 |
| 20 | 8 | 12 | 100,000 | 690,000 |

_source: live-play WebSearch/WebFetch 2026-08-19 (Phantom Doctrine Fandom wiki "Agents" page, fetched via Firecrawl after direct WebFetch was paywalled -- see `limitations.md`) · capture: web_fetch · confidence: high (single structured wiki table, internally consistent) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Full level-up perk catalog

The "god-tier" list above is the community-consensus subset; the complete perk pool agents draw from at level-up is:

Actor (reduce disguise-detection range by 3 tiles) · Brickhead (stun immunity) · Cold-blooded (-1 turn Focus cooldown) · Combat Senses (+20 max Awareness) · Composure (+10 Awareness regen) · Custom Gear (faster reloads) · Dancer (-5 Awareness cost to dodge) · Expert Marksman (single shots don't end turn) · Faster Movement (+1 movement range) · Fearless (immune to suppression) · Freediver (immune to gas-cloud harm except vision loss) · Gifted (+20 XP per mission) · League Pitcher (grenade throws don't end turn) · Low Profile (better half-cover benefit) · Martial Artist (-10 Awareness cost to takedown) · Masochist (+6 Damage Threshold) · Mild Paranoia (better full-cover benefit) · Paramedic (mobility bonus carrying unconscious agents) · Peripheral Vision (wider Overwatch radius, +2 tiles) · Quick Recovery (exact tooltip, confirmed 2026-08-21: "Increases HP recovery in Hideout") · Revenant (longer bleed-out timer) · Scar Tissue (immune to corrosive Damage Threshold loss) · Stalker (longer Overwatch cone range) · Survivor (+20 max HP) · Vietnam Veteran (wider Overwatch cone).

_source: same Fandom wiki fetch as the level table above, corroborated 2026-08-20 via `/prove` against an independent Steam Community "List of Perks" thread (that source names it "Vietnam Vet," same perk, alternate short form -- no functional discrepancy) · confidence: high (2 independent sources) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Agent backgrounds (starting weapon proficiency + perk)

Every recruited agent has a **Background** (e.g. "Gladio") that grants one fixed starting weapon proficiency and one fixed perk, separate from the level-up perk pool above. Full confirmed list (29 backgrounds):

| Background | Weapon proficiency | Skill (perk) | Skill effect |
|---|---|---|---|
| ASALA | AK | Firm Stance | Bonus firearm damage until this agent moves; resets each turn. |
| BND | MPK | Pickpocket | Replenishes ammo on a successful takedown. |
| Cartels | GAL | Blockade Runner | Damage Threshold bonus while moving. |
| CIA | .44, BM | Zen | Improved Awareness regeneration. |
| DGI | TKB | Sadist | Awareness bonus on each direct kill. |
| DGSE | French DAO | Vigilance | Extended circular Overwatch range. |
| Freelance (no fixed nationality) | MG51 | Warn Ally | Restores another character's Awareness. |
| GBU | AUG | Proximity Stimulus | Awareness + Movement bonus when attacked at close range. |
| **Gladio** | **AUG** | **Team Player** | **Extra Awareness regen near team members.** |
| IJO | AK | Coup de Grace | Instantly kills an enemy below ~33% HP. |
| IRA | GAL | Lucky Break | First hit taken each mission grants a free dodge. |
| KGB | TT, Sparrow | Coup de Grace | Instantly kills an enemy below ~33% HP. |
| Mafia | B76 | Buckshot | Cone-AoE damage. |
| MI6 | LMG 26 | Sniper's Delight | Immediate Awareness boost on a landed headshot. |
| MIT | AK | Vigilance | Extended circular Overwatch range. |
| Mossad | Sparrow, Estrella | Buckshot | Cone-AoE damage. |
| MSS | M10 | Sniper's Delight | Immediate Awareness boost on a landed headshot. |
| NSA | .44, .38 | Heartbeat Sensor | Reveals enemies in an AoE without line of sight. |
| PSIA | M10 | Proximity Stimulus | Awareness + Movement bonus when attacked at close range. |
| RAF | MPK | Buckshot | Cone-AoE damage. |
| SAS | EIW | Eye for Talent | Reveals Talents of teammates on the mission. |
| SAVAK | RP-4 | Coup de Grace | Instantly kills an enemy below ~33% HP. |
| SB | PM63 | Die Hard | Survives one fatal hit per mission and replenishes Awareness. |
| SEAL | AAR | Heartbeat Sensor | Reveals enemies in an AoE without line of sight. |
| Securitate | VZ 61 | Warn Ally | Restores another character's Awareness. |
| Spetsnaz | TKB, AK | Die Hard | Survives one fatal hit per mission and replenishes Awareness. |
| Stasi | PPK | Zen | Improved Awareness regeneration. |
| Triads | GAL | Lucky Break | First hit taken each mission grants a free dodge. |
| USMC | M16 | Sure Shot | Next shot from this agent cannot be dodged. |
| Yakuza | M10 | Interconnected | With Tactical Recon done, disabling one CCTV/laser source disables all of them. |

**Buckshot exact tooltip, confirmed 2026-08-21 (Bourbon/Elke Koch, RAF background, in-game screenshot):** "Deals damage in an area of effect" -- applies to all three backgrounds sharing it above (Mafia, Mossad, RAF).

**Recruitment note** (single-source, not corroborated by the wiki table above): recruitment odds reportedly favor Western-aligned backgrounds, with unaffiliated "Freelance" agents making up roughly a third of available recruits.

_source: live-play WebSearch/WebFetch 2026-08-19 -- primary table from the Phantom Doctrine Fandom wiki "Agents" page (fetched via Firecrawl; direct WebFetch returned HTTP 402, see `limitations.md`), corroborated against an independent Steam Community discussion thread for the entries both sources cover (Gladio/AUG/Team Player also triple-confirmed against this player's live save screenshot) · capture: web_fetch · confidence: high (structured wiki table + independent forum corroboration on overlapping entries; the recruitment-odds note stays medium, forum-only) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Body Engineering (chemical compounds)

Chemical compounds are unlocked via mission rewards + informer reveals (randomized) and applied at the Body Engineering facility. Each compound has a fixed set of four stat deltas (Circulatory/Sensory/Respiratory/Motoric -- can be negative) plus dependency rules: it may **require** an earlier compound first, and applying it **blocks** one or more other compounds permanently for that agent -- but the block relationship is one-directional (A blocking B does not mean B blocks A), so sequencing order determines your final available set, not just your final stat total. Agent base stats (before any compound) are usually 50-60 per stat, occasionally 60-70; total across all four stats averages ~220.

**AP/FP stat thresholds:** 3 Action Points needs 100 Motoric, 4 AP needs 140 Motoric (209 still only gives 4, so there's no 5th tier via Motoric alone). 2 Focus Points needs 150 Circulatory, 3 FP needs 200 Circulatory.

**Full compound table** (stat deltas; Requires = prerequisite compound; Blocks = compound(s) this permanently locks out; Ch = chapter it unlocks):

**Column correction (2026-08-21): the Sensory and Respiratory columns as originally fetched were TRANSPOSED relative to the game.** Verified by a 3-agent screenshot cross-check against save base stats (Reza: computed 92/67/75/75 = dossier exactly; Elke at 1-compound time: Circ 71 / Sens 74 = dossier; Adel: computed 79/82/82/84 = dossier exactly -- none of the three fit the original column labels). The same solve fixed the earlier "residual delta closest to BMA but not exact" puzzle: with the swap, AMPEA+BMA matches the hire-pool delta exactly. Headers below are now in the corrected order (which is also the in-game dossier layout order: Circ, Resp, Sens, Moto); the cell values are unchanged from the source fetch. Full derivation: `../save_schema.md`.

| Compound | Circ | Resp | Sens | Moto | Requires | Blocks | Ch |
|---|---|---|---|---|---|---|---|
| AMPEA | +14 | +7 | +15 | +8 | -- | Calusterone | 1-2 |
| THG | +17 | +17 | +14 | +8 | -- | ARGOXY, Raloxifene | 5 |
| TST | +7 | +13 | +15 | +9 | -- | Gonadorelin | 4-1 |
| BMA | +9 | +15 | +10 | +16 | -- | Danazol, AMPK | 3-1 |
| Bolasterone | -1 | +11 | 0 | -1 | -- | Stanozolol, Formoterol | 3-2 |
| DXAMPEA | +8 | +7 | +11 | +11 | -- | XENOXY, Albumin | 3-2 |
| Gonadorelin | +2 | +1 | -4 | +16 | -- | Anadrol | 3-1 |
| EPO | +13 | 0 | 0 | -2 | AMPEA (re-confirmed 2026-08-21, see below) | THG | 3-1 |
| Danazol | -2 | 0 | +15 | +2 | DXAMPEA | FGF | 3-2 |
| DHEA | +13 | +12 | +9 | +19 | BMA | Formebolone | 4-2 |
| Anadrol | +17 | +14 | +11 | +14 | TST | Mannitol | 6 |
| Bolandiol | -2 | +8 | +1 | -3 | Bolasterone | FGF | 5 |
| Calusterone | 0 | +10 | 0 | -2 | Bolandiol | Cyclofenil | 7-1 |
| Cyclofenil | +18 | -19 | +29 | +20 | Bolandiol | Anadrol | 4-2 |
| Formebolone | -1 | +2 | +10 | +3 | Danazol | DHEA | 4-2 |
| Mannitol | +38 | +24 | 0 | -10 | Danazol | XENOXY | 7-1 |
| ARGOXY | +10 | -1 | 0 | 0 | EPO | Formebolone | 4-2 |
| AMPK | +22 | 0 | -10 | +32 | Raloxifene | BMA | 5 |
| Raloxifene | 0 | +19 | -15 | -10 | ARGOXY | DHEA | 4-1 |
| XENOXY | +17 | 0 | 0 | -4 | ARGOXY | TST, Formoterol | 7-1 |
| Albumin | -10 | +24 | +30 | +6 | AMPK | TST | 6 |
| IGF-1 | -10 | +19 | +28 | +31 | Albumin | Formoterol | 7-2 |
| FGF | -5 | +1 | +3 | +8 | Gonadorelin | Stanozolol, Raloxifene | 5 |
| Formoterol | +2 | 0 | +2 | +14 | FGF | AMPK | 6 |
| Stanozolol | 0 | 0 | +9 | +5 | Formebolone | Albumin | 6 |

**Best-known full sequences** (agent must have Circulatory + Motoric both >=51 to start these -- 14 compounds, ends at 4 AP / 3 FP):
- `DXAMPEA -> Danazol -> Mannitol -> THG -> TST -> Anadrol -> Bolasterone -> Bolandiol -> Cyclofenil -> Calusterone -> AMPEA -> BMA -> DHEA -> EPO` -- totals [149 Circ, 130 Sens, 119 Resp, 89 Moto] *(Sens/Resp corrected per the 2026-08-21 column fix; arithmetic re-verified against the table)*.
- Circulatory-maximizing alternative (no THG needed): `AMPEA -> Bolasterone -> Bolandiol -> EPO -> ARGOXY -> TST -> XENOXY -> DXAMPEA -> Danazol -> Mannitol -> Anadrol -> Cyclofenil -> Raloxifene -> AMPK` -- totals [159 Circ, 72 Sens, 83 Resp, 66 Moto] *(Sens/Resp corrected 2026-08-21; re-verified)*.
- Best Motoric-focused series: `AMPEA -> Bolasterone -> EPO -> ARGOXY -> Gonadorelin -> Raloxifene -> AMPK -> FGF -> Bolandiol -> Cyclofenil -> TST -> Albumin -> DXAMPEA -> Danazol -> IGF-1` -- totals [64 Circ, 118 Sens, 90 Resp, 127 Moto] *(Sens/Resp corrected 2026-08-21; re-verified)*.
- **BMA-carrier route (derived 2026-08-22, first for this corpus):** for an agent who already has BMA applied -- BMA blocks Danazol and AMPK, ruling out all three sequences above as-is. `DHEA -> EPO -> ARGOXY -> DXAMPEA -> TST -> Bolasterone -> Bolandiol -> Cyclofenil` (DHEA's prerequisite is BMA itself, so it's always the open door for this agent class) -- totals from a BMA-already-applied baseline: **+66 Circ, +65 Sens, +31 Resp, +53 Moto** *(delta only -- add to the agent's post-AMPEA+BMA stats, not their raw base)*. Checked pairwise-consistent against the requires/blocks table (no two steps conflict, each prerequisite met by an earlier step or by BMA).

  **Live-confirmation status: ZERO steps confirmed.** In the validation sample, **DHEA, ARGOXY, TST, Bolandiol and Cyclofenil had not been applied to any agent** -- five of the route's eight steps have no in-game data, including its opening step. The proposed first test agent still had only AMPEA+BMA. Treat every delta in this route as derived-only.

  **What BMA carriers actually did instead (live save, 9 agents).** Every one opens `AMPEA -> BMA`, then takes some order of **EPO / Bolasterone / DXAMPEA** -- compounds the route either places late or omits:

  | Agent | uniqueid | Applied order |
  |---|---|---|
  | Lamster | `story_agent_lamster` | AMPEA, BMA, Bolasterone, DXAMPEA, EPO |
  | Agent A | `generated_agent_57` | AMPEA, BMA, EPO, Bolasterone, DXAMPEA |
  | Agent B | `generated_agent_98` | AMPEA, BMA, DXAMPEA, Bolasterone, EPO, **`compound_17` (unmapped)** |
  | Agent C | `generated_agent_104` | AMPEA, BMA, DXAMPEA, Bolasterone, EPO |
  | Agent D | `generated_agent_76` | AMPEA, BMA, EPO |
  | Agent E | `generated_agent_91` | AMPEA, BMA, DXAMPEA |
  | Agent F | `generated_agent_107` | AMPEA, BMA, DXAMPEA |
  | Agent G | `generated_agent_123` | AMPEA, BMA, DXAMPEA |
  | Agent H | `generated_agent_58` | AMPEA, BMA |

  Order is not fixed by the game: Lamster and agent A reach the same five compounds by different paths, so the route's *sequence* is a preference, not a prerequisite chain. Prerequisites still bind; ordering among already-unlocked steps does not.

  **An unmapped compound such as `compound_17`** in an agent's 6th slot makes current stats **not computable** -- `save_extract.py` returns null for that agent. If it is present in every available save slot, its application cannot be dated from those saves; resolve it with that agent's dossier screenshot (mapping procedure: `../save_schema.md` "Compound id mapping").
- **Card builders published before 2026-08-27 enforce Blocks BIDIRECTIONALLY and are wrong** -- they refuse a step whose Blocks list names an already-applied compound, which this line says is legal. Blocks are one-directional (forward-only), as the table above applies them. Consequence in play: the full 15-step Motoric series below cannot be clicked through on those cards, though the series itself is valid.
- Requires/Blocks validity of all three orderings re-checked 2026-08-21: every prerequisite precedes its dependent, and every Blocks relationship only fires against compounds either absent from the sequence or already applied (blocks are one-directional/forward-only). Do NOT reorder a sequence without re-checking blocks -- e.g. in the Circulatory route, TST must precede XENOXY (XENOXY blocks future TST) and Mannitol must precede Anadrol.
- **BMA-carrier warning (2026-08-21): none of these sequences are valid for an agent who already has BMA applied** (hire-pool agents commonly arrive with AMPEA+BMA baked in -- **9 of 21 hired agents in the validation sample**). BMA blocks **Danazol** (killing the Danazol -> Mannitol +38 Circ leg) and **AMPK** (+22 Circ) -- roughly -58 Circulatory vs the Circ-max chain. In exchange BMA enables **DHEA** (requires BMA; strong all-rounder, see its table row; must be taken BEFORE Raloxifene, which blocks it). A properly optimized BMA-carrier sequence has not been derived yet -- check an agent's applied compounds (`save_extract.py`) before quoting any chain at them.
- "Remove All" (reset an agent's compounds back to base stats) unlocks Chapter 4-1.

### Derived-stat bonuses (the hidden layer -- see correction above)

Every compound also carries bonuses to 8 derived stats, on top of its 4 primary-stat deltas above. These do NOT show on the Fandom wiki's compound table -- only on a separate, more detailed datamined chart. All 25 compounds:

### Danazol closes the corpus's "worst derived-table error" -- it was never an error (2026-09-16)

This file's earlier derived-stat notes recorded Danazol's Max Awareness as **"+7 documented, -1 actual -- the worst derived-table error confirmed on this corpus."** It is not an error in the measurement and it is not a table mistake of that kind: **`0.5 x Danazol's -2 Circulatory = -1, exactly.`** The table recorded a Circulatory-derived value as though it were a compound constant, which is the same structural mistake as the HP, MaxAware, AP and FP columns generally.

**This is the cleanest data point on record**, for two reasons:

- **`dCirc` is -2, an even number**, so the rule predicts exactly `-1` with no rounding ambiguity. Durand's popup: **Max HP 106 -> 105 and Max Awareness 119 -> 118. Both exactly -1.**
- **Sensory +15 moved neither stat** -- a second falsifying-test-class case after Bolasterone's Respiratory +11, now covering a different primary. Big non-Circulatory changes do nothing to Max HP or Max Awareness.

**Max HP is fully predictable from Circulatory**, absolutely and not just as a delta. For Durand, `Max HP = 89 + 0.5 x (Circ - 69)` reproduces **every** popup he has generated:

| after | Circ | predicted | popup |
|---|---|---|---|
| AMPEA | 83 | 96.0 | **96** |
| Bolasterone | 82 | 95.5 | **96** |
| EPO | 95 | 102.0 | **102** |
| DXAMPEA | 103 | 106.0 | *(popup unseen)* |
| Danazol | 101 | 105.0 | **105** |

That table also **caught an application nobody reported**: Danazol requires DXAMPEA, and the Danazol popup's "before" HP of 106 is exactly what DXAMPEA predicts. **DXAMPEA is inferred, not save-confirmed** -- the newest save predates these treatments; the next save settles it.

**Delta rule: now 16 for 16.**

### Gonadorelin costs 2 Movement Range -- confirmed on two agents (2026-09-16)

**`Movement Range -2` is real and repeatable**, observed identically on Archer (2026-08-22) and Samurai (2026-09-16). The sourced table records `0`. It remains the only compound confirmed to REDUCE Movement Range, and it is a genuine trade-off to weigh, not a rounding artifact: on Samurai it bought +1 Action Point at the cost of 2 tiles of movement. `Dodge cost -3` also held on both.

**The `AP` and `FP` columns of the derived table below are artifacts too, like HP and MaxAware.** Action and Fire Points are not granted by any compound -- they come from the Motoric (100 / 140) and Circulatory (150 / 200) breakpoints. Samurai's Gonadorelin popup showing `MAX ACTION POINTS 2 -> 3` is her Motoric crossing 100 (86 -> 102), not a property of Gonadorelin. **Only Move, Damage Threshold, Dodge cost and Awareness regen are genuinely per-compound** -- and Awareness regen varies between agents even for the same compound (Gonadorelin: +1 on Archer, +2 on Samurai).

### Max HP and Max Awareness are DERIVED FROM CIRCULATORY, not granted by the compound (2026-09-16)

**The rule: `delta Max HP` and `delta Max Awareness` each equal `0.5 x delta Circulatory`, rounded.** Fits **9 of 9** treatment-popup readings on record, across 3 different compounds and 5 agents:

| Agent | Compound | dCirc | 0.5 x dCirc | dMax HP | dMax Aware |
|---|---|---|---|---|---|
| Durand | AMPEA | +14 | +7.0 | **+7** | **+7** |
| Portwine | EPO | +13 | +6.5 | **+7** | **+6** |
| Samurai | EPO | +13 | +6.5 | **+6** | **+6** |
| Deadpan | EPO (preview) | +13 | +6.5 | **+6** | **+7** |
| Archer | Gonadorelin | +2 | +1.0 | -- | **+1** |

Every case where `dCirc` is **even** lands exactly on the half-value; every case where it is **odd** lands one side or the other of `.5`. **That is the whole of the "popup anomaly" this corpus has been chasing since 2026-08-20** -- the +-1 wobble on these two columns is rounding, not a bug, not a table error, and not a per-agent difference. It also retires "EPO's MaxAware column is wrong": EPO grants no Max Awareness of its own, it raises Circulatory by 13 and Max Awareness follows.

**Consequence: the HP and MaxAware columns of the derived table below are conceptually wrong** -- they record as per-compound constants something that is a function of Circulatory. Compute them instead. Same goes for the recorded "errors" they produced, including Gonadorelin's MaxAware (+1 observed against a documented -2: `0.5 x (+2) = +1`, exactly right).

**The falsifying test was run 2026-09-16 and the rule PASSED.** Bolasterone on Durand is the needed case -- **Resp +11 with `dCirc` of only -1**. Predicted `0.5 x -1 = -0.5`, i.e. 0 or -1 on each stat. Observed: **Max HP 96->96 (0), Max Awareness 106->105 (-1)** -- both in range, and **the +11 Respiratory moved neither**. These two stats track **Circulatory specifically**, not primary stats in general.

**RETRACTED, same day: the "fractional `K + 0.5 x Circ`" model written earlier that day.** It fitted Durand's first two readings exactly and looked settled. His third (EPO) broke it: **his Max Awareness popup reads `-> 105` after three consecutive different treatments**, with "before" fields of 98, 106 and 99. That is not a running value, so no absolute-value model can be fitted to it. Two data points produced a wrong model; the third killed it. *(Second time that day that happened -- see the EPO Dodge/AwareRegen retraction below.)*

**What survives, and it is the useful part -- the DELTA rule, now 12 for 12** across 4 agents (Durand, Samurai, Portwine, Archer) and 4 compounds (AMPEA, EPO, Bolasterone, Gonadorelin), including the falsifying test:

| Agent | Compound | dCirc | dMax HP | dMax Aware | predicted |
|---|---|---|---|---|---|
| Durand | AMPEA | +14 | +7 | +7 | +7 |
| Durand | Bolasterone | -1 | 0 | -1 | 0 or -1 |
| Durand | EPO | +13 | +6 | +6 | +6 or +7 |
| Samurai | EPO | +13 | +6 | +6 | +6 or +7 |
| Samurai | Bolasterone | -1 | 0 | -1 | 0 or -1 |
| Portwine | EPO | +13 | +7 | +6 | +6 or +7 |
| Archer | Gonadorelin | +2 | -- | +1 | +1 |

**Max HP is trustworthy in absolute terms too** -- Durand's chains perfectly across all three popups (89->96, 96->96, 96->102). **Max Awareness is not**: use its *delta* and get the absolute value from a dossier. This is a sharper form of the rule already in `../save_schema.md` -- it is not just the "before" field that is unreliable, it is the whole Awareness readout in that popup.

**Dodge cost and Awareness regen are NOT modelled** and are genuinely inconsistent between agents (EPO moved Portwine's by +1/-1 and Samurai's not at all; Bolasterone moved neither on Durand, while Damage Threshold went +1). Do not predict those.

**EPO live-confirmed on application, 2026-09-16 (Portwine treatment-complete popup, player-supplied).** First *applied* EPO read -- the 2026-08-20 numbers were an in-game preview, not an application. Popup: AP 2->2, FP 1->1, DmgThresh 3->3, Move 8->8, HP 98->105 (+7), MaxAware 84->90 (+6), Dodge 27->28 (+1), AwareRegen 24->23 (-1).

A third reading (Samurai, EPO, same day) then **corrected an over-confident reading of the first two**: Samurai's Dodge and Awareness regen did not move at all where Portwine's did, so EPO has no fixed value in those columns. AP/FP/Move/DmgThresh are confirmed 0 on all three. HP and Max Awareness are explained by the Circulatory rule above, not by EPO.

**Never quote a MaxAware or Max HP figure from the table below as fact** -- compute it from Circulatory, or read it off a dossier.

**Reliability correction (2026-08-20):** live-play confirmation of AMPEA on this player's protagonist matched the table on HP and MaxAware exactly, but **did not match on Move, DmgThresh, Dodge, or AwareRegen** (actual: Move +1, DmgThresh +0, Dodge -2, AwareRegen +1 -- see corrected row below). A second compound, EPO, was then previewed in-game (pending application, not yet confirmed applied): primary-stat deltas matched exactly (Circ +13, Moto -2), but derived HP was off by one (actual +7, table said +6 -- corrected below). **Pattern so far: primary 4-stat deltas have been exact on both compounds checked; derived-stat deltas have been off on at least one column for both.** The GameFAQs chart (2019, single source) should be treated as directionally useful but not precise on derived stats specifically until more compounds are verified against real play.

| Compound | AP | HP | FP | Move | DmgThresh | MaxAware | Dodge | AwareRegen |
|---|---|---|---|---|---|---|---|---|
| AMPEA | 0 | +7 | 0 | **+1** | **+0** | +7 | **-2** | **+1** |
| BMA | 0 | +4 | 0 | +1 | +1 | +5 | -3 | +1 |
| DXAMPEA | 0 | +4 | 0 | 0 | +1 | +5 | -2 | +1 |
| TST | 0 | +3 | 0 | +1 | +1 | +7 | -1 | 0 |
| DHEA | 0 | +6 | 0 | +1 | +1 | +4 | -3 | +1 |
| THG | 0 | +8 | 0 | +1 | +2 | +7 | -1 | 0 |
| EPO | **0** (n=3) | +6 or +7 -- **not a constant**, see the rule below | **0** (n=3) | **0** (n=3) | **+0** (n=3) | +6 or +7 -- **not a constant**, see the rule below | 0 or +1 (Samurai 0, Portwine +1) | 0 or -1 (Samurai 0, Portwine -1) |
| ARGOXY | 0 | +5 | 0 | 0 | 0 | 0 | 0 | 0 |
| Bolasterone | 0 | -1 | 0 | 0 | +1 | 0 | 0 | 0 |
| Bolandiol | 0 | -1 | 0 | 0 | +1 | 0 | 0 | 0 |
| Danazol | 0 (n=2) | **-1, Circulatory-derived** (n=2) | 0 (n=2) | 0 (n=2) | 0 (n=2) | **-1, table's +7 is WRONG; Circulatory-derived** (n=2) | -1 (Durand) | 0 (n=2) |
| Formebolone | 0 | -1 | 0 | 0 | 0 | +5 | 0 | 0 |
| Gonadorelin | **breakpoint, not a grant** -- see note | +1 (n=2) | 0 (n=2) | **-2, table's 0 is WRONG** (n=2) | 0 (n=2) | **+1, table's -2 is WRONG** (n=2) | -3 (n=2) | +1 (Archer) / +2 (Samurai) -- varies |
| FGF | 0 | -3 | 0 | 0 | 0 | +1 | -1 | 0 |
| Raloxifene | 0 | 0 | 0 | +1 | +2 | -7 | +2 | -1 |
| Cyclofenil | 0 | +9 | 0 | 0 | -1 | +14 | -4 | +2 |
| AMPK | 0 | +11 | 0 | 0 | 0 | -5 | -6 | +3 |
| Albumin | 0 | -5 | 0 | +1 | +2 | +15 | -1 | 0 |
| Formoterol | 0 | +1 | 0 | 0 | 0 | +1 | -2 | +1 |
| Anadrol | 0 | +8 | 0 | +1 | +1 | +5 | -2 | +1 |
| Calusterone | 0 | 0 | 0 | 0 | +1 | 0 | 0 | 0 |
| XENOXY | 0 | +8 | 0 | 0 | 0 | 0 | 0 | 0 |
| Stanozolol | 0 | 0 | 0 | 0 | 0 | +4 | -1 | 0 |
| IGF-1 | 0 | -5 | 0 | +1 | +2 | +14 | -6 | +3 |
| Mannitol | 0 | +19 | 0 | +1 | +2 | 0 | +2 | -1 |

None of the 25 compounds carry a direct AP or FP derived bonus -- those two still come only from the primary Circulatory/Motoric thresholds noted above, not from this hidden layer.

**Two live-play corrections on EPO, 2026-08-20 (player screenshot, Haystack's Body Engineering treatment-complete screen):**
1. ~~**EPO does NOT require AMPEA first.**~~ **RETRACTION RETRACTED 2026-08-21 -- EPO DOES require AMPEA; the original table was right.** Two independent proofs from the player's screenshot archive: (a) the in-game Agent Treatment tooltip for EPO literally lists "REQUIRES COMPOUNDS: AMPEA / BLOCKS COMPOUNDS: THG" (also: price $50, duration 3H); (b) the 2026-08-20 premise "Haystack had nothing else applied" was false -- her Munich-era dossier reads exactly base + AMPEA (64/58/66/60), and her save lists AMPEA before EPO, so her EPO application never tested the no-prerequisite claim. Every observed EPO application (Reza, Haystack, Rogue, Grimoire, Buran) had AMPEA applied first. Sequence advice reverted accordingly: AMPEA must precede EPO.
2. **EPO's actual derived-stat delta differs from the sourced datamined table.** Screenshot showed: HP +6 (table said +7), max Awareness **+7** (table said 0 -- a real miss, not rounding), Dodge Cost +1 (table said 0), Awareness Regen -1 (table said 0), Damage Threshold +0 (table agreed). This is consistent with the ongoing pattern of this derived-stat table drifting from live confirmation on individual compounds (see the Body Engineering perk note in `abilities.md`'s god-tier table above) -- keep verifying compound-by-compound as more get applied rather than trusting the table wholesale.

_source: live-play screenshot 2026-08-20 (Haystack, EPO applied) · capture: manual_paste · confidence: high (both findings are a direct read of an in-game confirmation screen) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Third EPO confirmation, 2026-08-21 (Buran/Adel Youssef treatment-complete screenshot):** HP **+7** (matches the originally-sourced table value exactly, not Haystack's +6 reading -- HP may vary slightly per-agent, or Haystack's screenshot had a rounding/read quirk; treat +7 as the more likely true value now that it's 2-for-2 against the table vs. Haystack's lone +6), max Awareness **+7** (matches Haystack's live finding exactly, now 2-for-2 -- confidently overrides the old sourced "0"). Dodge Cost, Awareness Regen, and Damage Threshold all read unchanged on this screen (0 delta each), consistent with Haystack's Dodge/AwareRegen deltas being small enough to be agent-noise rather than a confirmed nonzero effect.

_source: live-play screenshot 2026-08-21 (Buran, EPO applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen, second independent agent) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Screenshot-archive sweep additions, 2026-08-21 (two more EPO data points + a full AMPEA confirmation):**
- **Grimoire's EPO treatment screen: HP 91->98 (+7), Max Awareness 91->98 (+7)**, Dodge/AwareRegen/DT unchanged -- third clean +7/+7. EPO derived tally now: HP +7 (3 of 4; Haystack's lone +6), MaxAware +7 (3 of 4; Rogue's screen showed +6). Treat +7/+7 as the standard values.
- **Deadpan's AMPEA treatment screen confirms the corrected AMPEA derived row EXACTLY** (HP 87->94 +7, Move 6->7 +1, MaxAware 75->82 +7, AwareRegen 21->22 +1, Dodge 32->30 -2, DT 1->1 +0) -- second live confirmation, zero deviation.
- **Treatment-popup Awareness anomaly (n=4 -- Rogue, Haystack, Grimoire, Buran):** the popup's "before" Awareness consistently reads dossier-value-minus-delta while the same-era dossier already shows the higher number. Cause unresolved; rule: never chain popup Awareness values with dossier values (`../ui_reference.md` "Treatment Complete popup").

**Fourth live confirmation -- DXAMPEA, 2026-08-22 (Deadpan/Reza Golshani treatment-complete screenshot).** Derived deltas read: **HP +4 (table +4), DmgThresh +1 (table +1), AwareRegen +1 (table +1), AP 0, FP 0, Move 0 (all matching), Dodge -3 (table -2), MaxAware +4 (table +5)**. **6 of 8 columns exact** -- the closest agreement any compound has produced against the 2019 chart on this corpus, and both misses are single points rather than category errors. This materially softens the running "derived-stat deltas have been off on at least one column for every compound checked" framing: the pattern is now better described as *within +/-1 on most columns, with occasional larger misses (EPO's MaxAware +7 vs. 0)*, not as wholesale unreliability.

**Open flag from the same screen:** the popup's Max Awareness "before" read **84** while his pre-application dossier read **82** -- a +2 gap in the OPPOSITE direction from the n=4 treatment-popup Awareness anomaly recorded below (which has popup-before reading LOWER than dossier). Cause not determined; do not merge it into that anomaly's tally without another data point.

_source: live-play screenshot 2026-08-22 (Deadpan, DXAMPEA applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Fifth live confirmation -- Danazol, 2026-08-22 (Deadpan treatment-complete screenshot).** **7 of 8 derived columns exact** (HP -1, DmgThresh 0, Dodge 0, AwareRegen 0, AP 0, FP 0, Move 0 -- all matching), but **Max Awareness read -1 against the table's +7**: wrong sign, 8 points out, and the **worst single derived-table error confirmed on this corpus**. Treat Danazol's MaxAware row as **-1, not +7**.

**Chapter-gate trap worth stating explicitly (2026-08-22): Anadrol (Ch6) blocks Mannitol (Ch7-1).** The ordering constraint above ("Mannitol must precede Anadrol") is correct but understates the hazard -- the game offers Anadrol a full chapter BEFORE Mannitol becomes available, so a player following the sequence by availability rather than by the written order will destroy Mannitol's +38 Circ / +24 Resp without warning. **Hold Anadrol at Ch6 until Mannitol is applied at Ch7-1.**

**Max Awareness drift, unexplained (2026-08-22, same agent, 2 applications).** Observed chain: `dossier 82 -> DXAMPEA popup before 84 -> after 88 -> Danazol popup before 96 -> after 95` = **+10 across the two applications that the compound rows do not account for**, and running OPPOSITE to the n=4 popup-Awareness anomaly recorded above (popup-before lower than dossier). Cause not determined; recorded as its own open flag rather than merged into that tally.

_source: live-play screenshot 2026-08-22 (Deadpan, Danazol applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Sixth live confirmation -- AMPEA (again), 2026-08-22 (Canasta/Judith Allen treatment-complete screenshot), and a retraction of "zero deviation."** Derived deltas read: AP +0, HP **+7** (table +7, match), FP +0, Move **+1** (table +1, match), **Damage Threshold +1 (table +0, mismatch)**, Max Awareness **+7** (table +7, match), **Dodge Cost -1 (table -2, mismatch)**, **Awareness Regen +0 (table +1, mismatch)**. 5 of 8 columns match -- **this retracts the earlier claim that Deadpan's application confirmed the corrected AMPEA row "EXACTLY, zero deviation."** Treat AMPEA's derived row as no more reliable than the corpus's typical +/-1 drift, not as a fully solved case. **Separately:** this screen's "before" Max Awareness read 97 against Canasta's own prior dossier value of 96 -- a +1 mismatch, then her immediately-following EPO screen (same session) showed "before" Max Awareness as 97 again rather than the 104 her AMPEA screen had just set as "after" -- the EPO popup's before-field appears to not have refreshed off the AMPEA change at all. Per the existing rule, never chain popup Awareness values -- only the AFTER value of the latest screen (104, confirmed) is trusted as her current Max Awareness.

_source: live-play screenshot 2026-08-22 (Canasta, AMPEA then EPO applied) · capture: manual_paste · confidence: high (direct read of two in-game confirmation screens) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Seventh live confirmation -- Bolasterone, 2026-08-22 (Archer/Eita Tanaka treatment-complete screenshot).** Derived deltas read: HP -1 (table -1, match), DT +1 (table +1, match), Move +0 (match), MaxAware +0 (table 0, match), AwareRegen +0 (match), AP/FP unchanged (match) -- **Dodge +1 the one miss (table documents 0).** 7 of 8 columns match, reinforcing that Bolasterone's HP/DT dip pattern (first narrowed on Deadpan, v31) is a real, table-matching effect, not an anomaly -- only Dodge drifts, and by a different single point than any other compound's typical miss.

**Separately, on the same agent:** his Bolasterone screen's "before" Max Awareness read 108, against an original dossier read of 88 taken earlier the same session -- a +20 gap, much larger than any previously logged popup-Awareness discrepancy. No compound or perk change is recorded between the two reads. Kept as its own note rather than folded into the existing popup-anomaly tally, since the magnitude doesn't fit either direction seen before.

_source: live-play screenshot 2026-08-22 (Archer, Bolasterone applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**First live confirmation -- Gonadorelin, 2026-08-22 (Archer/Eita Tanaka treatment-complete screenshot), and the first confirmed compound-caused Movement Range LOSS on this corpus.** Derived deltas read: HP +1 (table +1, match), DT +0 (match), Dodge -3 (table -3, match), AwareRegen +1 (table +1, match) -- 4 of 8 solid. **Move read -2 against the table's documented +0**, and **Max Awareness read +1 against the table's documented -2** (wrong sign, 3 points out). The Move result is unusually trustworthy as a real effect rather than screen noise: Movement Range had held steady at 7 across this same agent's prior two treatment screens (Bolasterone, EPO), so the drop coincides exactly with this compound, not with popup drift. Also notable: this application pushed his Motoric from 92 to 108, crossing the 100/3-AP breakpoint -- confirmed live via Max Action Points stepping 2->3 on the same screen -- the first tracked agent on this roster to reach 3 AP.

_source: live-play screenshot 2026-08-22 (Archer, Gonadorelin applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen; Move result cross-checked against 2 prior stable readings on the same agent) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Eighth live confirmation -- Bolasterone (3rd that day), 2026-08-22 (Sunspot/Lee Yu treatment-complete screenshot), and a reliability downgrade.** Derived deltas read: AP +0 (match), HP +0 (table -1, MISS), FP +0 (match), Move +1 (table 0, MISS), **DT +2 -- double the table's documented +1 (MISS)**, MaxAware +0 (match), Dodge +0 (match), AwareRegen +0 (match). Only 5 of 8 columns match. **This is the 3rd Bolasterone application tracked that day (after Canasta's and Archer's), and all three have deviated on a DIFFERENT set of columns** -- Canasta missed only HP, Archer missed only Dodge, Sunspot misses HP+Move+DT. Bolasterone's derived row can no longer be treated as "mostly reliable with occasional 1-point noise" -- across 3 samples it has now missed on 5 distinct columns (HP, DT, Dodge, Move) with no consistent pattern, including one 2x-magnitude miss (DT) and the corpus's first-ever unexpected Move gain from a compound documented as 0.

_source: live-play screenshot 2026-08-22 (Sunspot, Bolasterone applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Ninth live confirmation -- Bolasterone (4th that day), 2026-08-22 (Pony/Samuel Durand treatment-complete screenshot).** Derived deltas read: HP +0 (table -1, MISS), DT +1 (table +1, match), Move +0 (match), MaxAware -1 (table 0, MISS), Dodge +0 (match), AwareRegen +0 (match), AP/FP unchanged (match). 6 of 8 match. **4 tracked Bolasterone applications that day now, 4 different miss-patterns** (Canasta: HP only; Archer: Dodge only; Sunspot: HP+Move+DT; Pony: HP+MaxAware) -- confirms this isn't agent-specific noise, the compound's derived row itself is unreliable across the board.

_source: live-play screenshot 2026-08-22 (Pony, Bolasterone applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Tenth live confirmation -- Bolasterone (5th in the corpus), 2026-08-26 (Bourbon/Elke Koch treatment-complete screenshot).** Derived deltas read: AP +0 (match), HP +0 (table -1, MISS), FP +0 (match), Move +1 (table 0, MISS -- matches Sunspot's own Move+1 miss exactly), DT +1 (table +1, match), MaxAware net 0 (table 0, match -- see popup-before flag below), **Dodge +1 (table 0, MISS -- matches Archer's own Dodge+1 miss exactly)**, **AwareRegen -1 (table 0, MISS -- first AwareRegen deviation recorded for this compound)**. 4 of 8 columns match. **5 tracked Bolasterone applications this corpus now, and two of Bourbon's four misses repeat prior agents' exact misses** (Move+1 = Sunspot's miss; Dodge+1 = Archer's miss) rather than adding a fifth distinct pattern -- suggests the derived-row unreliability clusters around a small set of recurring alternate values (HP -1/0, Move 0/+1, Dodge 0/+1) rather than being fully random per application.

**Popup Max Awareness anomaly, second data point (2026-08-26):** Bourbon's Bolasterone screen showed popup "before" Max Awareness as **102**, against her last-confirmed dossier value of **82** -- a **+20 gap**, matching Eita Tanaka/Archer's own **unexplained +20 gap** on his Bolasterone screen exactly. Two independent agents, same compound, same +20 magnitude -- strong enough to stop treating this as one-off screen noise and start suspecting a **Bolasterone-specific popup quirk** rather than agent-specific noise. Still doesn't fit the established n=4 anomaly (`../ui_reference.md` "Treatment Complete popup"), which runs in the opposite direction (popup-before reads LOWER than dossier, not higher) -- keep this as its own tracked pattern, watch for a third Bolasterone data point before calling it confirmed. Per the standing rule, only the AFTER value is trusted: her current Max Awareness is unchanged at **82** (net delta 0, matching the table).

_source: live-play screenshot 2026-08-26 (Bourbon, Bolasterone applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Eleventh live confirmation -- DXAMPEA (2nd this corpus), 2026-08-26 (Buran/Adel Youssef treatment-complete screenshot).** Derived deltas read: AP +0 (match), FP +0 (match), DT +1 (table +1, match), Dodge -2 (table -2, match), HP +4 (table +4, match), AwareRegen +1 (table +1, match), MaxAware +4 (table +5, MISS by 1 -- same direction and magnitude as Deadpan's own DXAMPEA miss), **Move +1 (table 0, MISS -- first-ever Move deviation for this compound; Deadpan's and Rich Grey's DXAMPEA applications both read Move unchanged, matching the table).** 6 of 8 columns match. **Popup note:** this screen's "before" Max Awareness read 87 against Buran's last-confirmed value of 86 -- a +1 gap in the same direction as Deadpan's own +2 DXAMPEA-screen mismatch, not the n=4 anomaly's usual direction; too small a sample to fold into either tracked pattern yet.

_source: live-play screenshot 2026-08-26 (Buran, DXAMPEA applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Twelfth/Thirteenth live confirmation -- Bolasterone (6th this corpus) and DXAMPEA (3rd/4th this corpus), 2026-08-26 (Uncle/Plamena Karailieva and Bourbon/Elke Koch, three more treatment-complete screenshots).**
- **Uncle's Bolasterone:** DT +1 (table +1, match), all others (AP/FP/HP/Move/MaxAware/Dodge/AwareRegen) read unchanged -- 8/8 columns match, cleanest Bolasterone application confirmed yet (contrast the 4-of-5 prior applications, all with 3+ misses).
- **Uncle's DXAMPEA:** DT +1 (match), Dodge -2 (match), HP +4 (match), AwareRegen +1 (match), AP/FP unchanged (match), **Move +0 (table 0, MATCH)**, MaxAware +4 (table +5, miss by 1, same as Deadpan's/Buran's). 7/8 match.
- **Bourbon's DXAMPEA** (her 4th compound, after AMPEA/Bolasterone/EPO): same pattern as Uncle's -- DT+1, Dodge-2, HP+4, AwareRegen+1, AP/FP unchanged all match; **Move +0 (match)**; MaxAware +4 (table +5, miss by 1). 7/8 match.
- **Reassessing Buran's lone Move+1 deviation (Eleventh live confirmation, above):** with these two new data points, DXAMPEA's Move column now reads 0 (matching the table) on 4 of 5 tracked applications (Deadpan, Rich Grey, Uncle, Bourbon) against Buran's single +1 outlier -- downgrades that miss from "possible new pattern" to most likely agent-specific screen noise, not a real second Move-affecting quirk on this compound.

_source: live-play screenshots 2026-08-26 (Uncle, Bolasterone+DXAMPEA applied; Bourbon, DXAMPEA applied) · capture: manual_paste · confidence: high (direct read of in-game confirmation screens) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Fourth EPO confirmation, 2026-08-26 (Bourbon/Elke Koch treatment-complete screenshot, her 3rd compound after AMPEA+Bolasterone).** HP +6 (table +7, matches Haystack's own +6 reading, not Buran's +7), Max Awareness +7 (table live-corrected +7, match), Move/DT/Dodge/AwareRegen all read unchanged (0, matching the table). 7/8 match (only HP off, and only by the same 1-point margin already seen on Haystack). **Popup note:** this screen's "before" Max Awareness read 95 against her last-confirmed value of 82 -- a +13 gap, yet another magnitude on top of the already-recorded +1/+2/+9/+20 popup-Awareness mismatches logged elsewhere on this corpus. The standing rule (never chain popup values, trust only the latest AFTER) is doing real work here -- the magnitudes are too inconsistent to read as one pattern.

_source: live-play screenshot 2026-08-26 (Bourbon, EPO applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Third Danazol confirmation, 2026-08-26 (Uncle/Plamena Karailieva treatment-complete screenshot), and the cleanest yet.** Using the corrected row (HP -1, MaxAware -1, all else 0 -- see the "Fifth live confirmation" correction above): HP 120->119 (-1, match), Max Awareness 94->93 (-1, match), DT/Dodge/Move/AwareRegen/AP/FP all unchanged (match). **8 of 8 columns match** -- the third independent agent (after Deadpan and Canasta) to confirm the corrected row exactly, with zero deviation this time. **Popup note:** this screen's "before" Max Awareness read 94 against her own last-confirmed value of 85 (her own DXAMPEA screen's AFTER, immediately prior in this same session) -- a +9 gap, another distinct magnitude for the same never-chain-popup-values caveat above.

_source: live-play screenshot 2026-08-26 (Uncle, Danazol applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Fourth Danazol confirmation, 2026-08-26 (Bourbon/Elke Koch treatment-complete screenshot), her 5th compound (after AMPEA/Bolasterone/EPO/DXAMPEA).** Using the corrected row (HP -1, MaxAware -1, all else 0): HP 100->99 (-1, match), Max Awareness 116->115 (-1, match) -- both reconfirm the correction. **Two new misses:** Dodge Cost 32->31 (-1, table 0, MISS) and Awareness Regen 31->32 (+1, table 0, MISS) -- the first Danazol application to deviate on columns other than the already-corrected HP/MaxAware pair. DT/Move/AP/FP all unchanged (match). 6 of 8 columns match.

_source: live-play screenshot 2026-08-26 (Bourbon, Danazol applied) · capture: manual_paste · confidence: high (direct read of an in-game confirmation screen) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Recomputed totals for the Circulatory-maximizing sequence** (`AMPEA -> Bolasterone -> Bolandiol -> EPO -> ARGOXY -> TST -> XENOXY -> DXAMPEA -> Danazol -> Mannitol -> Anadrol -> Cyclofenil -> Raloxifene -> AMPK`): **+78 HP, +5 Movement Range, +8 Damage Threshold, +40 max Awareness, -13 Dodge Cost, +6 Awareness Regen** -- on top of its primary [+159 Circ, +72 Sens, +83 Resp, +66 Moto]. *(Re-derived 2026-08-21 on a consistent basis: the corrected AMPEA row plus EPO's live-confirmed values (HP +7, MaxAware +7, Dodge/AwareRegen 0). The previous figures (+77/+4/+9/+33/-12/+5) mixed pre- and post-correction values -- in particular they missed EPO's confirmed +7 max Awareness, understating the Awareness total by 7. Whole block stays directional: only AMPEA and EPO are live-verified; the other 12 compounds' derived rows are the medium-low-confidence 2019 chart.)* It substantially outperforms Survivor (+20 HP) on HP alone, and its +8 Damage Threshold exceeds the Masochist perk's +6 -- worth weighing before spending perk picks on either for an agent already committed to this route.

_source: live-play WebFetch/Firecrawl 2026-08-20 -- GameFAQs "Body Engineering Chemicals Chart" (PS4) by Xbladez, v1.0/2019-03-15, cross-checked against the primary 4-stat numbers already sourced from the Fandom wiki table (exact match on all 25 compounds, confirming same underlying datamine) · capture: web_fetch · confidence: high on HP/MaxAware columns (live-play confirmed exact on AMPEA 2026-08-20); medium-low on AP/FP/Move/DmgThresh/Dodge/AwareRegen columns (AMPEA's live-play result deviated from this table on 4 of those 6 -- see correction above; unverified for the other 24 compounds) · enemy-tier: 0-1 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Build implication:** the combat build's 150-200 Circulatory target (see `builds.md`) is best hit via the Circulatory-maximizing sequence above -- note it deliberately skips THG so it can take EPO without conflict, and skips Gonadorelin so Anadrol stays open (Gonadorelin permanently blocks Anadrol, which is load-bearing for every high-Circulatory chain).

**Related achievements:** *Scientist* = apply 50 compounds; *Syndicate Engineering* = engineer an agent with all four core stats >=140.

_source: live-play WebSearch/WebFetch 2026-08-20 -- primary table from the Phantom Doctrine Fandom wiki "Body Engineering" page (fetched via Firecrawl; direct WebFetch returned HTTP 402, see `limitations.md`), which itself credits a Steam Community guide and the raszpl/Phantomdcompounds GitHub datamining tool · capture: web_fetch · confidence: high (structured datamined table, internally consistent, supersedes the earlier single-chain P1 note below) · enemy-tier: 0-1 (compound mechanics = tier 0, general-purpose; specific chains require mission-reward/informer unlocks = tier 1) · puzzle-tier: 0 · category: mainline · spoiler: none_

**Superseded note (kept for provenance):** P1 research (2026-08-18, gameranx.com) originally reported a single "best circulatory chain" of THG -> AMPEA -> EPO -> DXAMPEA -> Danazol -> TST -> Anadrol -> BMA -> DHEA -> Bolasterone -> Bolandiol -> Cyclofenil for 2 FP / 4 AP. The fuller table above shows THG blocks ARGOXY and Raloxifene, meaning that chain forecloses some higher-Circulatory alternatives -- treat the new sequences above as the better-sourced recommendation.

## Sources

- LordRedStone, "The best perks," Steam guide (English, 2018-2026).
- gameranx.com -- Body Engineering compound chains (English, editorial; superseded, see note above).
- github.com/raszpl/Phantomdcompounds -- compound dependency data (English, datamining).
- Phantom Doctrine Fandom Wiki -- Agents, Body Engineering pages (English, community-wiki; fetched via Firecrawl 2026-08-19/20 after direct WebFetch paywalled).
- Phantom Doctrine General Discussions, Steam Community (English, forum; agent backgrounds thread).
