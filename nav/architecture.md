# Phantom Doctrine -- Architecture

**status:** research-integrated
**last_reconciled:** 2026-08-18
**research_run:** P1 (2026-08-18), P2 (2026-08-18)

Cross-zone structural primitives. The persona reads this file for all cross-zone reasoning -- lookahead warnings, backtrack queries, reachability checks, locks-and-keys notifications. **Per-mission gate lists now exist at `nav/<zone>.md` (P2 ingestion, 2026-08-18)** -- the `Mission notes` column below is P1's original tactical/nav content, carried forward as a compact cross-reference; full gate-by-gate detail lives in the per-zone files.

## Hintforge manifest

```
corpus-core-version: 6
game-version: "latest / fully patched (player's own words at setup -- not a specific build number)"
game-version-platform: "PC / Steam"
game-version-as-of: 2026-08-17
vector-extensions: npcs, factions, paths
```

## Vector extensions

- `npcs/` -- named individual NPCs, indexed by `npcs/index.md`
- `factions/` -- group entities the player has a relationship with, indexed by `factions/index.md`
- `paths/` -- the starting-agency branch (CIA / KGB / Mossad), indexed by `paths/index.md`

## Zone Graph

**Game-type label:** hub-and-spoke-with-dungeons -- **CONFIRMED at P1.** The Hideout (Cabal HQ) is a persistent hub with facility screens; individual tactical missions are self-contained, algorithmically-populated maps reached from the strategic World Map.
_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 5 sources, 2 languages]

**Localization-mechanism class:** map-system -- **CONFIRMED at P1.** A strategic World Map (hotkey `M`) is the mission-select/navigation layer; no landmark-based navigation exists.
_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 4 sources, 2 languages]

**Entry node:** `hideout_hub` (The Hideout / Cabal HQ) -- the strategic hub the player returns to between missions; the very first mission played is whichever Chapter-1 zone matches the player's starting-agency choice (see Chapter <-> Zone Mapping).
**Hub nodes:** `hideout_hub` (The Hideout), reached from any mission via `world_map`.
**Source-language set:** Developer CreativeForge Games is based in Warsaw, Poland. Ships in Polish/English/French/German/Russian/Simplified Chinese/Italian/Spanish. **Correction to Stage-0 guess:** the strongest guide-producing communities are English, Polish (gry-online.pl, eurogamer.pl, interia, gamereactor.pl, redbull.pl), and **Korean** (namu.wiki carries an unusually detailed page) -- Stage 0 had guessed Russian as the #2/#3 non-English community; Russian is present (Steam guides translated to Russian, Russian KGB voiceover as an immersion feature) but thinner than Korean for strategy depth.
_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 5 sources, 3 languages]

**Nodes:** 29 zones total (see Zone list below) plus the two strategic-layer nodes `hideout_hub` and `world_map`. **P2 addition (2026-08-18):** 3 zones late-emerged during P2 per-zone research that P1's datamined mission-file list didn't surface as distinct entries -- `c4_vancouver`, `c4_gdansk`, `c6_penthouse` (see rows below, flagged `[P2-added]`). None carry a confirmed mission-file ID the way the P1-sourced zones do; treat their existence as `[Confirmed: 2 sources, 1 language]` but their file-ID linkage as unconfirmed.

### Zone list (canonical snake_case IDs)

| zone_id | Canonical name | Chapter | File ID |
|---|---|---|---|
| hideout_hub | The Hideout (Cabal HQ) | all | strategic |
| world_map | Strategic World Map | all | strategic |
| kgb_c1_gukos | Arrest the traitor Yukon (KGB intro) | 1-KGB | L000_ESMO_gukos_facility |
| kgb_c1_raid | Raid: They found your hideout | 1-KGB | L065_GIII_raid_industrial |
| kgb_c1_submarine | Sabotage the submarine | 1-KGB | L001_EIMI_submarine_base |
| cia_c1_nuclear | Pakistani nuclear test site (CIA intro) | 1-CIA | L031_WMMR_nuclear_test_site |
| cia_c1_morgue | Sneak into the morgue (Leslie) | 1-CIA | L032_WSRR_morgue |
| cia_c1_beirut | Raid: Leave Beirut | 1-CIA | L066_WSCC_raid_urban |
| mossad_c1_chemlab | Chemical weapons lab (Mossad intro) | 1-Mossad | L033_WMMR_chemical_weapon_lab |
| mossad_c1_smugglers | Assault the smugglers' base | 1-Mossad | L034_EIII_smugglers_base |
| mossad_c1_diplomatique | Intercept Abaddon & Komodo | 1-Mossad | L011_WSCC_quartier_diplomatique |
| c2_omikron | Rescue Omikron | 2 | LGen_Story_Tac01 |
| c2_glasgow | Steal the empty Beholder cargo (Glasgow trap) | 2 | L003_WSOM_mi5_safehouse |
| c3_ivorycoast | Get the Operation Ivory Coast report | 3 | L040_WSOM_embassy_smaller |
| c3_mkultra_plans | Acquire MK Ultra facility plans (rescue Wizard) | 3 | L005_ESRR_brainwashing_facility |
| c3_warehouse_ambush | Ambush: warehouse trap | 3 | LGen_StoryTac02 |
| c3_taipan_capture | Capture Tai-Pan | 3 | L007_WSCC_asian_food_place |
| c3_houseboat | Steal the real Beholder cargo (houseboat) | 3 | L008_ESCI_houseboat |
| c4_boldface | Optional: Rescue Boldface for Cardinal | 4 | L004_EIOC_convention_center |
| c4_vancouver | Beholder base in Vancouver -- infiltrate or destroy (Northstar lead) | 4 | unconfirmed `[P2-added]` |
| c4_gdansk | Optional: Protect Polish opposition leaders (Cardinal's deal) | 4 | unconfirmed `[P2-added]` |
| c4_commstation | Stop the communication (save aircraft) | 4 | L009_EMMM_comm_station |
| c5_siliconvalley | Ambush: Silicon Valley trap | 5 | LGen_StoryTac04 |
| c5_terrorcell | Destroy a terrorist cell in Europe | 5 | LGen_StoryTac03 |
| c5_numbers_station | Assault the numbers/Broadsword station | 5 | L010_WIIR_numbers_station |
| c6_turncoat | Assault Turncoat's hideout (ambush) | 6 | LGen_StoryTac05 |
| c6_penthouse | Retrieve the Iceberg briefcase (Chicago office building) | 6 | unconfirmed `[P2-added]` |
| c6_almaz | Attack the Almaz Control Station | 6 | L013_EMRM_almaz_control_station |
| c7_searstower | Infiltrate the Sears Tower | 7 | L015_WSOO_skyscraper |
| c7_iceberg | Assault Project Iceberg (finale) | 7 | L016_WIRR_server_station |
| c8_killtaipan | Kill Tai-Pan (Extended/NG+ finale) | 8 | L096_WSCC_asian_food_place_revisited |

_source: LordRedStone Steam datamined mission-file guide, 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 5 sources, 1 language]

**Shared-name / confusion flags (persona should proactively disambiguate on request):**
- **Two distinct "Marquis cargo" missions:** "Steal the (empty) Beholder cargo" (Ch2, Glasgow, `c2_glasgow`, achievement *Once Bitten, Twice Shy*) vs "Steal the real Beholder cargo" (Ch3, houseboat, `c3_houseboat`, achievements *Rock the Boat* / *Same, but Different*). Both concern "the Marquis cargo" and both involve a safehouse/boat -- frequently conflated by players.
- **Multiple ambush / "lured you into a trap" missions:** `c3_warehouse_ambush` (Ch3, warehouse), `c5_siliconvalley` (Ch5, Silicon Valley trap), `c6_turncoat` (Ch6, Turncoat's hideout). All generic-named; distinct missions, do not conflate.
- **Two Tai-Pan missions on the same reused map:** "Capture Tai-Pan to brainwash him" (`c3_taipan_capture`, Ch3) vs "Kill Tai-Pan" (`c8_killtaipan`, Ch8 NG+, revisited map).
- **"Cardinal" is a person** (a companion character; also the name of this guide's persona voice), NOT an in-fiction codename system -- Cabal agents use codenames (Deadpan, Kodiak, Hemlock, etc.), Cardinal specifically names one character. See `npcs/cardinal.md`.
- **Halloween DLC confusion:** the free Halloween Scare Tactics DLC only swaps cosmetic destructibles (pumpkins, bat-wing liquor, horror magazines) into existing maps -- no new missions. Any "pumpkin"/spooky content is DLC cosmetic, not base-game.
- **Undertow's mole-hunt is not a zone.** Unlike every other named character beat, Undertow's discovery plays out entirely at the Hideout (Analytics/MK-ULTRA strategic layer) via investigation-branch events, not a tactical mission map. It has no `nav/<zone>.md` file by design -- see `mechanics.md` "Mole hunt (Undertow)" and `npcs/undertow.md`.
- **Two same-city, different-building missions:** `c6_penthouse` (Chicago office building, retrieve the Iceberg briefcase) and `c7_searstower` (Sears Tower, Chicago) are both Chicago missions but distinct buildings and distinct objectives -- confirm which one the player means before giving directions.

**Edges:**

| From | To | Type | Direction | Condition | Point of no return | Notes |
|---|---|---|---|---|---|---|
| hideout_hub | world_map | hub-spoke | two-way | always | none | `M` key opens map |
| world_map | any mission | hub-spoke | two-way | mission available | none | agents dispatched from map |
| kgb_c1_gukos | kgb_c1_raid | story-gate | one-way | always | none | tutorial chain |
| kgb_c1_raid | kgb_c1_submarine | story-gate | one-way | always | none | tutorial chain |
| kgb_c1_submarine | c2_omikron | story-gate | one-way | finish Ch1 KGB (*Comrade Spy*) | chapter-bound | branches merge |
| cia_c1_nuclear | cia_c1_morgue | story-gate | one-way | always | none | tutorial chain |
| cia_c1_morgue | cia_c1_beirut | story-gate | one-way | always | none | tutorial chain |
| cia_c1_beirut | c2_omikron | story-gate | one-way | finish Ch1 CIA (*US Intelligence*) | chapter-bound | branches merge |
| mossad_c1_chemlab | mossad_c1_smugglers | story-gate | one-way | always | none | tutorial chain |
| mossad_c1_smugglers | mossad_c1_diplomatique | story-gate | one-way | always | none | tutorial chain |
| mossad_c1_diplomatique | c2_omikron | story-gate | one-way | finish Ch1 Mossad (*The Institute*) | chapter-bound | Mossad path requires 1 prior campaign clear (NG+ unlock) |
| c2_omikron | c2_glasgow | story-gate | one-way | rescue Omikron | none | -- |
| c2_glasgow | c3_ivorycoast | story-gate | one-way | decrypt evidence | missable-trigger | Glasgow is a scripted ambush |
| c3_ivorycoast | c3_houseboat | story-gate | one-way | get the Ivory Coast dossier | none | `c3_mkultra_plans`/`c3_warehouse_ambush`/`c3_taipan_capture` reached independently from `world_map` within Ch3 -- no confirmed direct chain to/from them |
| c3_taipan_capture | c4_boldface | story-gate | one-way | brainwash Tai-Pan, get intel | chapter-bound | uses control-phrase tech |
| c4_boldface | -- | optional | -- | Cardinal's request; disguised agent | missable | *Blessing in Disguise*, Ch4-only |
| c3_houseboat | c4_vancouver | story-gate | one-way | Beholder comm device installed in Workshop -> Northstar lead | none | Marquis/Beholder cargo device is the key (see Locks and Keys) |
| c4_vancouver | c4_commstation | story-gate | one-way | learn Operation Northstar | none | infiltrate-or-assault branch is cosmetic, not a hard fork |
| c4_gdansk | -- | optional | -- | Cardinal's deal accepted | missable | reported bug: reloading around this beat can hide both the Gdansk and Sakhalin (`c4_commstation`) prompts -- see Common confusions |
| c4_commstation | c5_siliconvalley | story-gate | one-way | always | point-of-divergence | Sakhalin/KAL-007 scripted Foregone Conclusion |
| c5_siliconvalley | c5_terrorcell | story-gate | one-way | always | none | -- |
| c5_terrorcell | c5_numbers_station | story-gate | one-way | always | none | -- |
| c5_numbers_station | c6_turncoat | story-gate | one-way | always | chapter-bound | -- |
| c6_almaz | c7_searstower | story-gate | one-way | finish Ch6 (*Tip of the Iceberg*, regular playthrough only) | chapter-bound | Extended variant plays differently (hold-position); `c6_turncoat`/`c6_penthouse` reached independently from `world_map` within Ch6 -- no confirmed direct chain between all three |
| c6_penthouse | c7_searstower | story-gate | one-way | retrieve the Iceberg briefcase | none | `[P2-added, Single source -- verify]` distinct from the Sears Tower mission despite both being Chicago |
| c7_searstower | c7_iceberg | story-gate | one-way | always | none | -- |
| c7_iceberg | ending | story-gate | one-way | finale | permanent (point-of-divergence) | *The End?* difficulty achievements |
| c7_iceberg | c8_killtaipan | story-gate | one-way | Extended campaign only | permanent | *The Whole Truth* |
| c8_killtaipan | epilogue | story-gate | one-way | finale | permanent | Extended-campaign true ending; fixed team, no named mastermind confirmed by P2 research |

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 4 sources]

**Edge types:** `story-gate` / `one-way` / `optional` / `hub-spoke` / `fast-travel` / `conditional`
**Point-of-no-return subtypes:** `permanent` / `chapter-bound` / `missable-trigger` / `point-of-divergence`

## Chapter <-> Zone Mapping

| Chapter | Zones | Mission notes (P1 tactical/nav content -- carried forward for P2's per-zone files) |
|---|---|---|
| 1-KGB | kgb_c1_gukos, kgb_c1_raid, kgb_c1_submarine | Yukon found dead; follow blood trail to classified docs; investigate Vladivostok police; hideout raid; submarine has 3 sabotage points whose interlocks force combat after 2 turns -- **do sabotage points last.** Finishing = *Comrade Spy*. |
| 1-CIA | cia_c1_nuclear, cia_c1_morgue, cia_c1_beirut | Locate Aguirre across Port Said/Kuwait/Muscat, tail to Aleppo; morgue mission retrieves microfilm from Leslie's false tooth -- **you must kill Aguirre, not capture** (no interrogation room built yet, so his body can't be retrieved this early -- a documented exception to the normal capture-first rule; see `dependencies.md` DEP-001); Beirut raid. Finishing = *US Intelligence*. |
| 1-Mossad | mossad_c1_chemlab, mossad_c1_smugglers, mossad_c1_diplomatique | Chemical weapons lab; optional journalist rescue; smugglers' base (optional kill Ramses, +50 XP); intercept Komodo & Abaddon (kill Komodo; 3 optional stealth objectives worth 33 XP each). Finishing = *The Institute* (4.81% Steam rarity -- rarest story achievement in the base list; Mossad path unlocks only after finishing one campaign). |
| 2 | c2_omikron, c2_glasgow | Rescue Omikron, then the Glasgow "empty cargo" trap: get keys, get shipment -- **interacting forces combat; clear the map and call evac first, then trigger and leave.** *Once Bitten, Twice Shy* (HIDDEN) = escape the trap; key-carrier need not be the box-opener. Story reveal: your handler is a Beholder sleeper who springs this ambush (see `npcs/` handler files). |
| 3 | c3_ivorycoast, c3_mkultra_plans, c3_warehouse_ambush, c3_taipan_capture, c3_houseboat | Ivory Coast: 400 XP for disabling cameras + maintaining stealth (getting caught on the way out is fine). MK Ultra plans/rescue Wizard: optional kill overseers for 400 XP (needs a breach; silenced pistols/SMGs recommended). Capture Tai-Pan: *No One Noticed* = kidnap without alarm -- needs Actor-perk disguised agents; Tai-Pan's corner is static, **plan this mission last** among the chapter. Houseboat: *Rock the Boat* (HIDDEN) = recover cargo; Extended variant = *Same, but Different* (different safehouse); Mossad gets an extra "Kill Abaddon" objective flagged as main but not actually required. |
| 4 | c4_boldface, c4_vancouver, c4_gdansk, c4_commstation | Boldface rescue: *Blessing in Disguise* = rescue with a disguised agent; 1600 XP stealth bonus (enough for a level-up); MISSABLE, Ch4 only. Vancouver `[P2-added]`: ask Tai-Pan about Northstar, then either infiltrate (Workshop upgrade) or assault (2 agents) the Beholder cell -- both routes are valid, infiltration is not a hard gate. Gdansk `[P2-added, optional]`: protect Polish opposition leaders as part of a Cardinal side-deal; **documented bug** -- reloading around this beat can make both the Gdansk and Sakhalin (`c4_commstation`) prompts disappear. Comm station: *Communication Noise* (HIDDEN) = attempt to save 269 lives -- **documented gotcha: the plane is shot down regardless of play; this is scripted and the achievement fires anyway.** |
| 5 | c5_siliconvalley, c5_terrorcell, c5_numbers_station | Numbers/Broadsword station: a timer forces combat after 6 turns; *Explosive Measures* (HIDDEN) = destroy the facility; *Death of a Citizen* = kill Broadsword in Munich (Extended only); use control phrases / Mason Gambit to plant a mole. "Broadsword" naming is ambiguous between facility and person -- see `limitations.md`. |
| 6 | c6_turncoat, c6_penthouse, c6_almaz | Almaz Control Station: *Tip of the Iceberg* (HIDDEN) = finish Ch6, regular playthrough only; the Extended variant plays as a hold-position combat mission (arrive first, survive 5 turns). Penthouse `[P2-added]`: observe Evelyn Pococke, assault the Chicago office building, retrieve the Iceberg briefcase -- distinct from the Ch7 Sears Tower mission despite both being Chicago. Undertow's mole-hunt also resolves somewhere in this chapter's span but plays out at the Hideout, not a zone -- see `mechanics.md`. |
| 7 | c7_searstower, c7_iceberg | Sears Tower: *Spy* = extract intel; 25,599 XP available (3x8533 for stealth + both optionals); interacting with the safe in Valhalla's room forces combat; finish optionals + reach the roof first (reinforcement spawn location depends on whether the roof was already reached). Iceberg (finale): *The End? -- Easy/Normal/Hard* (a higher-difficulty clear unlocks the lower ones); kill the background-dependent traitor (51,200 XP), then find and kill Valhalla. |
| 8 (Extended/NG+ only) | c8_killtaipan | *The Whole Truth* = finish the Extended campaign; fresh squad in Juggernaut Mk2 armor; a documented player report describes finishing this mission silently using a leftover Control Phrase on Tai-Pan despite the game's "go loud" pressure. |

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high (medium on Broadsword identity and Mossad-Abaddon-objective specifics) · enemy-tier: 1-2 (see per-fact tags in `sections/story_notes.md` and `sections/missables.md` for the story/hidden-achievement-tier facts pulled from this table) · puzzle-tier: 0 · category: mainline · spoiler: progression (existence); story/late-game facts embedded here are cross-referenced, not duplicated -- see `sections/story_notes.md`_

## Optional Content

| Name | Type | Unlock condition | Access window | Parent zone | Rec. chapter | Failure mode |
|---|---|---|---|---|---|---|
| Rescue Boldface | side mission | Cardinal's package request | Ch4 | world_map | 4 | missable |
| Protect Gdansk opposition leaders `[P2-added]` | side mission | Cardinal's deal | Ch4 | world_map | 4 | missable -- documented bug can hide this prompt (see `c4_gdansk`) |
| Rescue journalist (Mossad) | side mission | Mossad Ch1 path | Ch1-Mossad | world_map | 1 | missable -- `[P2]` file `Lgen_vendor`; `LGen_` prefix suggests a repeatable/generic archetype rather than a unique story zone, kept as optional content rather than promoted to its own nav zone |
| Rescue-the-informer / Destroy-cell | repeatable | random world-map spawns | continuous | world_map | any | always-available |
| Secret files (Investigation Board) | repeatable | procedurally generated | continuous | hideout_hub | any | always-available (finish all before endgame for *Trust No One*) |
| HQ facility upgrades | upgrades | Workshop tech + story unlocks | continuous | hideout_hub | any | *Fully Operational* / *Well-equipped* |
| Chapter 8 (Extended campaign) | campaign | beat the game once | NG+ | full | NG+ | NG+ only |
| Mossad starting-agency campaign | campaign | beat CIA or KGB once | post-clear | full | unlock-gated |

_source: deep-research P1 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 (0 for the always-available repeatables) · puzzle-tier: 0 · category: mainline · spoiler: progression (none for the always-available repeatables)_ [Confirmed: 4 sources]

## Support Topology

### Save stations

Not zone-based -- Phantom Doctrine uses `F5`/`F9` quicksave/quickload plus autosave slots (confirmed present on disk: `pdsauto0-2`, `pdtauto0-2`), not in-mission checkpoint locations. **Autosave triggers -- CONFIRMED at P2:** an autosave is written at the start of each combat turn during tactical missions (the game "keeps auto saves of the last three combat turns") and on day-advance at the World Map strategic layer (last three game days). Manual mid-mission saving is available except in Ironman mode.
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 2 sources, 1 language]

### Fast-travel network

N/A -- confirmed at P1, re-confirmed at P2 with no exception found. Missions are launched directly from the World Map (strategic layer), not traveled to on foot; there is no separate fast-travel system to document.

### Hub access

Confirmed at P1: the player returns to The Hideout between missions automatically; the World Map (`M` key, two-way hub-spoke edge to every mission and to the Hideout) is the sole navigation layer. **Base relocation -- CONFIRMED at P2 (structural, affects the hub node itself, not just `hideout_hub`'s internal content):** the Hideout is not a fixed node -- danger accumulates toward a threshold; at the cap the base is raided (money lost, agents possibly captured) and the player is prompted to relocate to a new hideout candidate, initiated from Analytics or by clicking a candidate on the World Map. A "clean" hideout costs ~$8000; a candidate with the danger bar already ~halfway is cheaper (~$2000). Once abandoned, a hideout cannot be reused. This means `hideout_hub` is best understood as a persistent *role* in the zone graph (always the one hub node, always reached the same way) rather than a fixed place -- full facility/evolution detail lives in `nav/hideout_hub.md`.
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 3 sources, 2 languages]

## Locks and Keys

**P2 primary deliverable -- CONFIRMED.** Phantom Doctrine has MINIMAL traditional item-keyed gating: it's a mission-select tactics game, not a dungeon crawler. Exactly one true in-mission item key exists (Glasgow); locked doors are always optional convenience routes. The meaningful progression "keys" are story-flag gates (solved Investigation Board dossiers) and required Workshop tech upgrades.

| Lock (zone + description) | Key required | Key source zone | Visible before key obtained? | Notes |
|---|---|---|---|---|
| Glasgow shipment room (`c2_glasgow`) | Duty officer's "keys" (in-mission objective flag) | Same mission (`c2_glasgow`) | Yes (room/box visible) | **Only true in-mission item key.** Transferable state flag -- the agent who grabs it need not be the one who opens the box. Opening the box forces combat. |
| Restricted (red-outlined) zones inside buildings, most missions | Disguise (soft access key) | Pre-mission Recon; disguise capability itself gated behind a Workshop Tactical Recon upgrade | Yes | Lets a disguised agent move in restricted zones without alarm; enemy agents see through it unless the agent has the Actor perk. Soft/access key, not a hard gate. |
| Locked doors / cabinets on tactical maps (any mission) | Lockpick (crafted at Workshop, ~$500-600) | Workshop | Yes | Always optional -- never blocks a mandatory objective; an alternate route always exists. Some locked doors can't be lockpicked at all (e.g. the optional Sakhalin roof door at `c4_commstation`). |
| Broadsword numbers-station trace (`c5_numbers_station`) | Communications/telecommunications Workshop upgrade (story tech) | Workshop | Objective hinted, station not traceable without it | HARD story-tech key -- required, not optional, to trace the station. |
| Kidnapping Tai-Pan (`c3_taipan_capture`) | Control Phrase (researched mind-control device recovered from a Beholder cell) | Beholder cell mission -> Workshop research | Objective visible | HARD chained item -> flag -> tech key: recover device, install, research, then use. |
| Vancouver infiltration path (`c4_vancouver`) | Special Workshop infiltration upgrade | Workshop | Yes | SOFT / optional-path key only -- assault with two agents is a valid alternative. Not a hard progression gate. |
| Next World Map story mission (multiple chapters) | Solved Investigation Board dossier (story flag) | Analytics/Investigation Board (fed by mission intel + informers + Comms) | Partially -- leads shown, location hidden until solved | HARD story-flag keys, e.g. solve Kingfish->Glasgow, Broadsword->NATO/Munich, Lamster->Beholder cell, Iceberg dossier. Unsolved files hard-block progress. |
| Northstar lead (`c4_commstation`'s prerequisite) | Marquis/Beholder cargo device, carried out then installed in Workshop | `c3_houseboat` | Objective visible | HARD item -> flag chain: recover cargo -> install device in Workshop -> Comms produces the Northstar lead -> unlocks `c4_vancouver`. |
| Project Iceberg interior forward doors (`c7_iceberg`) | Disable the reactor/power (scripted switch, not an item) | Same mission | Yes (doors visible, locked) | Doors auto-open after power-off -- a switch flag, not a key item. |
| MK-ULTRA facility build (`c3_mkultra_plans`) | MK-ULTRA blueprints (mission item) | Same mission | n/a | Blueprints unlock the mandatory Ch3 facility build. |

True item-keyed gates: the Glasgow key, the MK-ULTRA blueprints, the Marquis/Beholder cargo device, and the Control Phrase mind-control device. Everything else is a soft gate (lockpick, disguise, money, timer, skill) or a story-flag gate (solved dossiers, required tech upgrades).
_source: deep-research P2 2026-08-18 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Confirmed: 3 sources, 2 languages]

## DLC (out of P1 scope -- named here only)

- Halloween Scare Tactics DLC (free) -- out of P1 scope; covered in P3 if ever run. P3 was skipped at setup (judged low value: this is the only DLC, and it's a small free seasonal pack, not a story/zone expansion). Confirmed at P1: cosmetic-only (swaps pumpkins/bat-wing liquor/horror magazines into existing maps; no new missions).
- Deluxe Edition Upgrade (soundtrack + artbook) -- not gameplay content, needs no corpus coverage.

## Sources

- LordRedStone, "Every tactical mission in the campaign," Steam Community guide (English, datamining, 2018-12) -- mission file IDs, objectives, achievements, zone graph.
- Phantom Doctrine Fandom Wiki: The Cabal, Valhalla, Cardinal, Timeline pages (English, community-wiki).
- gamepressure.com official guide: chapter walkthroughs (English/Polish origin, editorial, 2018).
- Wikipedia, "Phantom Doctrine" (English) -- plot structure, Extended campaign.
- namu.wiki, "Phantom Doctrine" (Korean, community-wiki). [translated from: Korean]
- gry-online.pl, eurogamer.pl, interia.pl, gamereactor.pl, redbull.pl reviews (Polish, editorial-non-en, 2018). [translated from: Polish]

**P2 additions (2026-08-18):**
- LordRedStone Steam guide, gamepressure.com per-chapter walkthroughs (IDs 45914-46499) -- per-zone gate lists.
- Phantom Doctrine Fandom wiki: Hideout, Technology_Tree, Broadsword, Chapter_4, Omikron, MI6_Safehouse, Deadpan, Timeline, Korean_Airlines_Flight_007 (captured via search snippets -- direct fetch returned HTTP 402/403).
- TV Tropes: main page, YMMV, Auto-Save (English) -- autosave triggers, economy figures.
- PSNProfiles / TrueAchievements trophy guides (English).
- Steam Community discussions: Broadsword, Undertow, base relocation, danger/hideout cost, Omikron, lockpick, mind-control threads (English, forum, 2018-2020).
- GRY-Online.pl base upgrades + Ch1-7 walkthroughs (Polish); Red Bull PL review (Polish); NamuWiki campaign structure (Korean); Eurogamer.de / OneAngryGamer.de base/facility notes (German); yxbao.com / zhihu.com / 3dmgame.com base/campaign notes (Chinese).
