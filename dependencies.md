# Dependencies -- Phantom Doctrine
<!-- hintforge · stitch pass · last run: 2026-08-18 -->
<!-- Every stitch run re-audits ALL existing edges + adds new ones. The per-edge convergence audit (open each cited source, verify the specific value) applies to every row in this file on every run, not just new candidates. A game patch, DLC, or new ingestion phase can change facts that existing edges cite -- only a full re-audit catches that. See `stitch_and_zipper.md` Phase B "Re-run scope: always full." Inconsistencies (cited source contradicts edge text) land in the `## Corpus inconsistencies` section; the edge row stays in place. -->

## Cross-system edges

| Edge ID | System A | System B | Dependency description | Confidence | Source files |
|---------|----------|----------|------------------------|------------|--------------|
| DEP-001 | HQ facility build order (MK-ULTRA/interrogation) | Chapter 1 CIA tactical mission outcome | The MK-ULTRA/interrogation facility does not exist until Chapter 3 (story-mandatory build); this is why the Chapter 1 CIA morgue mission requires killing Aguirre rather than capturing him -- no facility exists yet to process a captured body. | high | mechanics.md, nav/architecture.md, nav/cia_c1_morgue.md, paths/cia.md |

## PoNR / lockout edges

| Edge ID | Trigger | Locked out | Notes | Source files |
|---------|---------|------------|-------|--------------|
| PON-001 | Strategic Hideout mole-hunt event flags an existing roster agent as "Undertow" | Story progression halts until the flagged agent is executed via the MK-ULTRA facility | Notorious progression-bug hotspot if Investigation Board dossiers are unsolved or the flagged agent is away in training when the event fires; MK-ULTRA itself is not available until Ch3 (story-mandatory build, see DEP-001's System A). | mechanics.md, npcs/undertow.md |

## Missable / sequencing dependencies

_None met the write threshold this pass -- corpus's existing PoNR/missable content (Glasgow trap, Boldface rescue, Gdansk prompt, etc.) is already single-directory-converged (`achievements.md` + `sections/missables.md`, the latter an explicit non-independent aggregation of the former) and did not clear the 2-independent-directory bar this run._

## Stitch run log

| Date | Scope | Edges written | Edges proposed (pending) | Inconsistencies surfaced | Model |
|------|-------|---------------|--------------------------|--------------------------|-------|
| 2026-08-18 | full | 2 | 0 | 2 | sonnet-class |

<!-- Inconsistencies surfaced: count from the per-edge convergence audit (stitch_and_zipper.md Phase B). Counts must be derived by reading this file, not recalled. A non-zero count requires an explicit chat call-out and at least one populated row in the Corpus inconsistencies section below. -->

## Corpus inconsistencies

Stitch's per-edge convergence audit (see [`stitch_and_zipper.md`](https://github.com/hintforge/builder/blob/main/stitch_and_zipper.md) Phase B) populates this section when a candidate edge's cited sources contradict each other. Each row records the contradiction; resolving it is the user's call (or a follow-up doctor / ingestion run). Edges blocked on an unresolved entry are NOT written to the tables above until the inconsistency is closed.

_Both inconsistencies found this run were resolved immediately per stitch's mandatory 5b resolution step -- no open rows remain._

| Detected | Files | Conflicting values | Suspected authoritative source | Status |
|----------|-------|--------------------|--------------------------------|--------|

<!-- Status vocabulary: open (just surfaced) | resolved (user picked authoritative value + corrected the other file) | accepted (user accepted both -- rare; usually means the claim is genuinely ambiguous in-game). When status flips to resolved, the next stitch run can re-evaluate the edge. -->
