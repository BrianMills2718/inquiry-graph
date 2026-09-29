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

### Current stable research architecture

The research layer now has executable reference regimes for positive support, defeasible argumentation, graded support, deduction, measurement, testimony, finite-class statistical learning, and strategy selection.

Candidate generation has been mapped to mature work in synthesis/CEGIS, MIL, anti-unification, HR theory formation, conceptual blending, blackboard systems, multistrategy learning, algorithm selection, hyper-heuristics, algorithm configuration, PRODIGY, Soar and reflection.

Guarantee transport has been mapped to institution theory, DOL/Hets, MMT/LF theory morphisms, abstract interpretation and contract/refinement theory.

The integrated native-Windows repository verification is green: 138 tests passed, 8 artifacts matched, graph validation has 0 errors / 0 warnings, and dependency checks are clean.

### Current research priority

The main foundational frontier is **acceptance licensing and warrant composition** (issue #34):

- define acceptance/commitment/use-for-action precisely;
- compare proof-standard, decision-theoretic, argumentation, belief-revision and acceptance literature;
- avoid one universal confidence threshold;
- treat acceptance policies as explicit warrantable policies/meta-regimes;
- study how heterogeneous typed guarantees compose without premature scalarization.

A second technical task is to audit the strategy-performance benchmark for multiple-comparison and optional-stopping conditions before interpreting it as a general adaptive-selection guarantee (issue #39).

### Empirical / representation priority

The inquiry graph remains a curated first-pass reconstruction.

Priority product/research work is:

1. reconcile the full conversation export and adjudicate the 798 proposed annotations (issue #3);
2. define and run a concrete inquiry-navigation/auditability usefulness test (issue #38);
3. compare the graph-assisted workflow against reading the transcript directly;
4. only then expand UI, storage, automation, or learned reasoning policies.

### Scope control

Do not add a new foundational layer merely because adjacent literature exists.

Reopen architecture only when a concrete benchmark/use case cannot be represented without distortion.

Keep the documented escalation paths dormant unless triggered:

- issue #17: first-class derivation/subargument structure;
- issue #18: full ABA+ / set-to-set hyperargumentation.

Hosted CI restoration (issue #2) is lower priority than research/product work because integrated local verification is already green.

Do not let answering every foundational philosophy question become a release prerequisite for a useful representation tool.
