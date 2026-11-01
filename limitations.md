# Phantom Doctrine -- Limitations & Blocked Sources

Sources I found that look useful but couldn't fully fetch -- paywalls, Cloudflare, age gates, video-only content, etc. URLs preserved so the player (or another contributor) can open them in a real browser.

## How to read this file
- Each entry: topic, URL, block type, what I could glean, best alternative I did get to.
- Each per-topic file (in `npcs/`, `factions/`, `items/`, `sections/`) also lists its own blocked sources at the bottom -- the player rarely needs to come hunting here.
- This file is the catch-all for sources that didn't fit a specific topic.

## Block types
- **paywall** -- content gated behind a subscription or article limit
- **cloudflare** -- Cloudflare bot challenge / 403 / 503 from WebFetch
- **video-only** -- YouTube or other video where the answer is shown visually; no readable text equivalent
- **age-gate** -- content blocked behind age verification
- **cookie-wall** -- popup or consent flow that broke the fetch
- **search-snippet-only** -- search engine returned a snippet but the page itself wasn't reachable
- **dead-link** -- URL was in another source but no longer resolves

## Entries

### Giant Bomb -- character wiki -- STILL BLOCKED as of P1
- Source: https://www.giantbomb.com/phantom-doctrine/3030-61188/characters/
- Block type: cloudflare (HTTP 403 Forbidden from WebFetch)
- Why I think it has the answer: dedicated characters page.
- What I could glean: nothing, at Stage 0 or P1 -- P1's deep-research pass does not cite Giant Bomb anywhere in its source list, so the block was never worked around.
- Best alternative: Fandom wiki + NamuWiki (see below -- resolved) covered the roster gap instead.

## Resolved at P1 (2026-08-18)

### Phantom Doctrine Fandom wiki -- character roster / Cabal membership -- RESOLVED
- Originally blocked at Stage 0: https://phantom-doctrine.fandom.com/wiki/The_Cabal , https://phantom-doctrine.fandom.com/wiki/Character_Customization (HTTP 402 Payment Required from WebFetch).
- **P1's deep-research pass successfully fetched** The Cabal, Valhalla, Cardinal, and Timeline pages from the Fandom wiki (cited throughout `npcs/`, `factions/`, and `sections/story_notes.md`) -- the original block did not recur, likely because the research tool used a different capture path than the setup-time direct `WebFetch`. The `Character_Customization` page specifically was never needed for base-scope roster facts and was not re-attempted.
- Korean-language **namu.wiki** was used as a secondary roster/mechanics source and filled gaps English-only sources missed (weapon tiers, support roles, Beholder structure).

### TV Tropes -- general page resolved; character-specific page unconfirmed
- Originally blocked at Stage 0: https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/PhantomDoctrine (HTTP 403).
- P1's source list cites "TV Tropes, VideoGame/PhantomDoctrine" directly (starting cash, handlers, support roles, brainwashing) -- the main page fetched successfully. Whether a dedicated character-breakdown sub-page exists and was separately blocked was not distinguished in the P1 result.

## Resolved at P2 (2026-08-18)

- **"Broadsword" identity -- RESOLVED.** Both a NATO civil-defense program codename AND a specific person (a Beholder agent, present and killable only in the Extended/NG+ variant of `c5_numbers_station`). See `npcs/broadsword.md`.
- **Undertow's discovery mechanism -- RESOLVED.** Not a fixed character -- a randomly-selected existing roster agent, flagged via strategic Hideout mole-hunt events (polygraph fail, illness/isolation, drunk-spouse accusation), executed in MK-ULTRA. Plays out entirely at the Hideout, not a tactical mission. See `npcs/undertow.md` and `mechanics.md` "Mole hunt (Undertow)".
- **Locks-and-keys table -- RESOLVED (P2 primary deliverable).** Minimal traditional item-keyed gating -- one true in-mission item key (Glasgow); real "keys" are story-flag gates (solved dossiers, Workshop tech). Full table in `nav/architecture.md` Locks and Keys.
- **"Turncoat" characterization -- SUBSTANTIALLY RESOLVED.** Turncoat is the Cabal's name for whichever starting-agency handler (Fender/Cyclone/Delilah) is revealed as a Beholder sleeper agent at `c2_glasgow`; hostile encounter at `c6_turncoat`. See `npcs/turncoat.md`. Remaining gap: no personal motive/backstory beyond the handler role surfaced.

## Open research gaps (P2 could not resolve)

- **Misplaced Trust achievement's exact trigger** -- still unconfirmed. The `c2_glasgow` handler-betrayal reveal (Turncoat) is a plausible fit ("witness an agent betrayal during a tactical mission") but P2 research did not explicitly name it as this achievement's trigger -- don't present as confirmed. See `achievements.md`.
- **`c7_iceberg`'s "the traitor"** -- the finale's optional kill-the-traitor objective (51,200 XP) is described as "background-dependent" but no name is confirmed; possibly resolves to Turncoat or Undertow depending on playthrough. Needs P3 research or a direct game-file check.
- **Wizard** (rescued at `c3_mkultra_plans`) -- P2 research did not confirm a recurring post-rescue role. Not promoted to an `npcs/` entity file; flag if a future pass surfaces a recurring role (parallel to Omikron/Lamster).
- **Evelyn Pococke** (`c6_penthouse` observation target) -- single-line mention, no further characterization; deliberately kept generic per the corpus's named-individual rule, not an entity file.
- **"Make Items Available" button (Loadout/mission-launch screen)** -- live-play flag, 2026-08-20. A red button next to "Remove All Agents" / "Remove All Support" on the pre-mission squad Loadout screen; clicking it triggers an ambush-related warning/confirmation. Effect and actual consequence (if any) not documented anywhere found -- checked trade contract/vendor mechanics, mission-prep warning-icon guides, the Fandom wiki, and multiple Steam Community threads, no match. **Context pinned 2026-08-21 (from a screenshot):** it sits top-right of the LOADOUT screen as the third button in the bulk-action group `REMOVE ALL AGENTS / REMOVE ALL SUPPORT / MAKE ITEMS AVAILABLE`, which suggests a bulk gear-pooling action (make equipped items available to other agents) -- consistent with the ambush warning firing because it would strip the squad. Still unconfirmed; needs a direct in-game test.

- **Tai-Pan post-capture intel/information mechanic -- UNRESEARCHED, player-facing gap surfaced 2026-08-22.** Player asked about "waiting on Tai-Pan to deliver information" mid-session; nothing in `npcs/tai-pan.md`, `mechanics.md`'s interrogation/MK-ULTRA section, or a live `save_extract.py` pull supports a queued intel-delivery flow tied to him -- current corpus coverage is limited to the Ch3 capture mission and the Ch8 Extended-campaign kill mission, both one-time events, not an ongoing information source. Possibilities not yet checked: a post-capture Analytics/Interrogate payout the corpus's interrogation section doesn't itemize per-NPC, a story beat P1/P2 research didn't surface, or player conflation with a different mechanic/NPC. **Needs a research pass (web search or direct game-file check) to confirm whether this content exists at all before it's written up.** If it does, spoiler-gate it at minimum `story` (existence/role) per this corpus's tier scheme (`warning_tiers.md`) -- do not integrate at a lower tier without checking whether it touches Ch3-capture or Ch8-Extended story beats first.

- **Chapter 3 Part 2 Workshop Upgrades -- unnamed, 2026-08-22.** The Fandom wiki's "Technology Tree" page (used as a substitute for the removed LordRedStone Steam flowchart, see `items/upgrades.md`) documents every other chapter's Workshop-upgrade names but leaves this one tier blank (`???` in the source itself). Needs a different source or an in-game screenshot at that story beat to fill.
- **Per-training effect/proficiency detail -- unresearched, 2026-08-22.** The same Fandom fetch surfaced ~16 training NAMES across all chapters (see `items/upgrades.md` "Bonus finding"), well beyond the 3 previously known in `items/abilities.md`, but no mechanical detail (proficiency granted, stat effect, cost) for the newly-named ones. Needs a dedicated research pass before `items/abilities.md`'s Trainings section can be expanded properly.

## Zone-graph reconciliation judgment calls (P2 ingestion, 2026-08-18)

P2's raw research used its own zone-id scheme that didn't always match P1's canonical `nav/architecture.md` ids or zone count. Reconciliation calls made during ingestion (see `nav/architecture.md`'s zone-list note and Harness changelog for full detail):

- **3 zones added to the canonical list beyond P1's original 26:** `c4_vancouver`, `c4_gdansk`, `c6_penthouse`. None carry a confirmed mission-file ID (unlike every P1-sourced zone) -- their existence is `[Confirmed: 2 sources, 1 language]` but the file-ID linkage is unconfirmed. If a future pass finds these don't correspond to distinct playable missions, they may need to be folded into a neighboring zone instead.
- **`c1_mossad_vendor`** (raw P2 id) kept as an entry in `architecture.md`'s Optional Content table ("Rescue journalist (Mossad)"), not promoted to its own nav zone -- its `LGen_` file-prefix pattern suggests a repeatable/generic archetype rather than a unique story zone.
- **Undertow's mole-hunt** (raw P2 id `c6_undertow_hunt`) is explicitly NOT a nav zone -- it's a Hideout strategic-layer mechanic, routed to `mechanics.md` instead. See `nav/architecture.md`'s "Shared-name / confusion flags."

## Always-blocked categories

- **Save file contents -- READABLE as of 2026-08-18** (this entry previously said the opposite; the earlier call was wrong). `.PDSave` is plain UTF-8 XML obfuscated with a repeating XOR keystream, `key[i] = (0x45 + i) & 0xFF`, identical in every save -- obfuscation, not encryption. `save_watcher.py` in this guide now decodes it and reports chapter, day, hideout location, current map, cash, danger, difficulty, ironman flag and agent count; `python save_watcher.py --xml` dumps the whole document. The earlier "encrypted/compressed" claim (Stage 0, 2026-08-17) rested on "no readable strings in the first 16KB and no zlib/gzip/PK magic" -- evidence that a file is not plaintext, but not evidence of encryption. It was overturned by XOR-ing two saves together: the result is 100% below 0x80 with ~134 distinct values, which only happens when two 7-bit-ASCII plaintexts share one keystream. **Remaining real limit:** the decoded values are internal ids (`place_000`, `ChapterName_02`, `L031_WMMR_nuclear_test_site`), not player-facing names, so mapping them to corpus zone ids is still unfinished work -- the save tells you *which* map, not what the corpus calls it.
