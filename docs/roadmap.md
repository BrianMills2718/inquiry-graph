# Roadmap and scope control

## V1 delivered scope

Executable Pydantic ontology and generated schemas; role-typed relations and reified multi-input/output inquiry moves; exact source grounding; separate actor stance/question state; active-branch ChatGPT import; deterministic offline candidate ingestion; optional official SDK adapter; semantic validation; idempotent conflict-detecting merge; open agenda, trace, dependencies/conflicts; Mermaid, DOT, Markdown and offline HTML inspector; first-pass conversation dataset; tests and reproducible docs/artifacts.

This is a small local-first toolkit, not a deployed application or a learned reasoning system. The provider adapter is mock-tested, not live-validated. The seed is curated and unreviewed, not an independent gold extraction.

## V1.1: source reconciliation and review

Import Brian's full export and reconcile the 219 curated excerpts against actual message IDs/branches. Add an explicit reviewer/annotation-decision log and a focused review UI. Evaluate false closure and actor attribution first. Add extraction-quality fixtures independent of the founding discussion.

## V1.2: cross-conversation identity and incremental updates

Introduce explicit reviewed identity proposals for concepts/questions and actors, with reasons and undo history. Do not silently merge claims based on similarity. Add large-conversation chunking with boundary provenance and a reconciliation policy. Keep graph snapshots reproducible.

## V2: inquiry navigation application

Add a local graph canvas with filters for actor, topic, status and interpretation confidence. Support editing a move and seeing affected questions without losing source history. Select a storage engine only after measuring data/query sizes; a TypeDB adapter can preserve the role structure, but no database is needed merely to justify the schema.

## Research track, separate from product delivery

Evaluate extraction fidelity, inquiry-navigation usefulness, higher-level strategy-episode annotation, and eventually policies over reasoning moves/strategies under held-out tasks and controlled budgets. Investigate links to AIF/IAT, IBIS, provenance, belief revision/update, dynamic epistemic logic, metareasoning, explicit justification, structured argumentation, assume-guarantee reasoning and discourse models without claiming a unique new universal ontology. The positive-support choice is instantiated as finite antichains of minimal assumption environments (free distributive lattice / positive Boolean provenance), with a small independent-Bernoulli reference regime conditioned on nogoods. Defeasible conflict is now kept in a separate argumentation layer with typed rebut/undercut/undermine defeats and Dung grounded semantics. The six-case benchmark selected an **ABA-first executable bridge with ASPIC+-compatible attack-origin metadata**, and the basic ABA core is now implemented: Horn-style rules, assumptions, contraries, minimal-support argument construction, typed attacks, and projection into the Dung defeat layer. The argument-identity boundary is resolved: keep the conclusion + assumption-support quotient for the current ABA dialectical layer and escalate to first-class derivation trees only if ASPIC+-level attacks/preferences or proof-sensitive warrants require them. Preference-sensitive binary defeat is now implemented as a Dung-compatible normal-attack filter with explicit blocked-attack audit records. Full ABA+ reversal is tracked separately because general ABA+ is set-to-set and may require a hyperargumentation layer. The first warrant/license integration and defeasible end-to-end vertical slice are implemented. Graded support now has a separate executable regime that warrants recording the computed support-event probability but not accepting the proposition. The deductive benchmark is executable in a checked strict-Horn fragment, and measurement/testimony now have narrow executable result-recording regimes. The strategy-performance benchmark is now executable as well. The formal warrant benchmark set is broad enough for an architecture reassessment: the next work should be integrated verification, benchmark-driven failure analysis, source reconciliation and empirical usefulness, with new formal layers added only when a concrete case fails. New foundational layers should be added only when a benchmark case cannot be represented without distortion. Action-algebra choices (sequential composition, guarded choice, iteration) and richer quantitative regimes remain separate research tracks. Do not assign independent scalar confidence directly to derived nodes. Before adding a dedicated StrategyEpisode schema, test whether grounded example episodes plus method strategies, part-of links and the new about relation are sufficient for annotation/review. Do not let answering every foundational philosophy question become a release prerequisite for a useful representation tool.

## Current handoff status — 2026-09-29

The repository has moved beyond architecture discovery. The current research/product plan is:

### Foundational research

**P0 — Acceptance licensing and warrant composition.** Track in issue #34. The model can represent heterogeneous warrants but does not yet have a general rule for when they license stronger actions such as acceptance, commitment, use-for-action, revision or retraction.

**P1 — Empirical adequacy.** Test whether the factorization and source-grounded inquiry representation improve real reasoning/audit/navigation tasks. Do not add new formal layers unless a benchmark/use case exposes a concrete failure.

**Deferred escalation only.** Issue #17 preserves first-class derivation/subargument structure; issue #18 preserves full ABA+ / set-to-set hyperargumentation. Do not implement either preemptively.

### Inquiry-representation/product track

**P0 when data is available — Source reconciliation.** Issue #3 now reflects the current 219 curated excerpts and 798 proposed annotations. Reconcile against the full conversation export before treating the graph as source-complete.

**P1 — Useful Inquiry System.** Product work may proceed separately from foundational research: navigation, open-question recovery, provenance/revision inspection, strategy visualization, and evaluation of whether the representation is actually useful.

### Maintenance

**P2 — Documentation/paper normalization.** The canonical notation is in `docs/formal-epistemic-reasoning-metamodel.md`. The paper's top-level notation/priorities are now synchronized to acceptance/composition and the completed candidate-generation/transport surveys. Remaining work is systematic related-work/bibliography normalization and optional migration of older historical docs. PR #36 resolved the strategy-performance multiple-comparison/optional-stopping assumptions; only a fresh independent integrated rerun of current main remains as verification follow-up.

**P3 — Hosted CI.** Issue #2 remains open because GitHub-hosted jobs fail/cancel before runner steps. The last independently executed application-level baseline is local and green: 138 tests, 8 artifacts, graph 0 errors/0 warnings, dependency check clean. PR #36 records 142 passing tests after its strategy-performance fix; a fresh independent rerun of current main is pending.

### Separate open PR stacks

PR #8 (`formal-inquiry-substrate`) and PR #15 (`inquiry-hypergraph-crosswalk`, stacked on #8) predate the current main research line and intentionally keep a second inquiry trajectory / hypergraph crosswalk separate. **Do not merge them automatically.** Rebase/review them as a distinct project decision if that trajectory is resumed.

