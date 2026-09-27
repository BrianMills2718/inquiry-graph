# Roadmap and scope control

## V1 delivered scope

Executable Pydantic ontology and generated schemas; role-typed relations and reified multi-input/output inquiry moves; exact source grounding; separate actor stance/question state; active-branch ChatGPT import; deterministic offline candidate ingestion; optional official SDK adapter; semantic validation; idempotent conflict-detecting merge; open agenda, trace, dependencies/conflicts; Mermaid, DOT, Markdown and offline HTML inspector; first-pass conversation dataset; tests and reproducible docs/artifacts.

This is a small local-first toolkit, not a deployed application or a learned reasoning system. The provider adapter is mock-tested, not live-validated. The seed is curated and unreviewed, not an independent gold extraction.

## V1.1: source reconciliation and review

Import Brian's full export and reconcile the 197 curated excerpts against actual message IDs/branches. Add an explicit reviewer/annotation-decision log and a focused review UI. Evaluate false closure and actor attribution first. Add extraction-quality fixtures independent of the founding discussion.

## V1.2: cross-conversation identity and incremental updates

Introduce explicit reviewed identity proposals for concepts/questions and actors, with reasons and undo history. Do not silently merge claims based on similarity. Add large-conversation chunking with boundary provenance and a reconciliation policy. Keep graph snapshots reproducible.

## V2: inquiry navigation application

Add a local graph canvas with filters for actor, topic, status and interpretation confidence. Support editing a move and seeing affected questions without losing source history. Select a storage engine only after measuring data/query sizes; a TypeDB adapter can preserve the role structure, but no database is needed merely to justify the schema.

## Research track, separate from product delivery

Evaluate extraction fidelity, inquiry-navigation usefulness, higher-level strategy-episode annotation, and eventually policies over reasoning moves/strategies under held-out tasks and controlled budgets. Investigate links to AIF/IAT, IBIS, provenance, belief revision, metareasoning and discourse models without claiming a unique new universal ontology. Before adding a dedicated StrategyEpisode schema, test whether grounded example episodes plus method strategies, part-of links and the new about relation are sufficient for annotation/review. Do not let answering every foundational philosophy question become a release prerequisite for a useful representation tool.
