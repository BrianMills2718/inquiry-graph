# Roadmap and Scope Control — Inquiry Graph

> **Split, 2026-09-29.** Formal epistemic theory moved to `BrianMills2718/epistemic-warrant`. This repository is now the inquiry-representation/product project.

## Delivered V1

- executable Pydantic ontology and generated schemas;
- role-typed/reified relations and inquiry moves;
- exact source grounding;
- actor stance/question-state histories;
- active-branch ChatGPT import;
- deterministic offline candidate ingestion;
- optional provider adapter;
- validation, merge, query and render workflows;
- curated founding-dialogue seed.

## P0 — Usefulness pilot

Track: issue #38.

**Status 2026-09-29:** a first pilot with an AI model as the reader is done ([results](../evaluation/usefulness_pilot/results.md)). The raw transcript beat the graph report (0.81 vs 0.65 key points covered; the plain excerpts scored 0.59). The graph lost mainly on decision rationale and side-line outcomes. Next: record those explicitly, rerun the AI-reader pilot, then test multi-conversation histories that exceed a single context window. Human-reader evaluation is out of scope.

Goal: determine whether the graph earns its complexity.

Compare transcript-only/context-limited vs graph-assisted AI performance on unresolved-question recovery, rationale/revision recovery, attribution, dependency recovery, branch recovery, cross-conversation conflict/tension recovery, and long-context resumption.

Do not build a polished UI first.

## P1 — Source reconciliation

Track: issue #3.

The live thread can now be read through the ChatGPT bridge, so this no longer waits on an export. The partial check on issue #3 matched 136 of 219 excerpts verbatim; about 50 voice-mode excerpts still need the export.

When the full export is available:

- reconcile curated excerpts to exact active-branch messages;
- preserve source/review history;
- audit actor attribution and question closure;
- adjudicate proposed annotations.

## P2 — Machine-consumable product workflow

Only after P0 identifies useful retrieval/representation workflows for an AI reader.

Likely capabilities:

- open-question retrieval;
- revision/rationale traces;
- provenance/dependency retrieval;
- actor/stance filtering;
- strategy/reasoning-history retrieval;
- compact cross-conversation context assembly.

Do not optimize for human-facing UI. Choose storage/query technology only after measuring actual multi-conversation retrieval needs.

## P3 — Downstream cross-conversation integration

Cross-source identity, alignment, governed assertions and tension/conflict detection belong in the downstream `onto-canon6` direction, not in Inquiry Graph.

Inquiry Graph should emit per-conversation, source-grounded attributed structure that can be consumed downstream. When the multi-conversation usefulness experiment reaches this stage:

- test the handoff contract into the downstream canonicalization layer;
- preserve speaker/stance, source provenance, question state, rationale and deferred-branch outcomes;
- measure whether downstream integration recovers cross-conversation tensions without silent semantic merging;
- keep any reviewed identity proposals, reasons and undo history in the downstream owner rather than creating a second canonical store here.

Incremental/chunked processing for larger **individual conversations** may still be added here when evaluation requires it, with boundary provenance preserved.

## Maintenance — hosted CI

Track: issue #2.

Restore hosted Python 3.11/3.13 execution when convenient, but do not block product research while local verification is green.

## Separate old branch stack

PR #8 and stacked PR #15 remain separate.

Review/rebase only if that formal-inquiry/hypergraph trajectory is explicitly resumed.

## Theory dependency

If product experiments need formal warrant/support machinery, depend on `epistemic-warrant` as an external package and make the integration explicit.

Do not copy its code into this repository.

## Current verification baseline

Post-split fresh native-Windows verification:

- 60 tests passed;
- 8 artifacts checked;
- graph valid with 0 errors / 0 warnings;
- dependency check clean.

## Stop rule

A new schema/product layer should be justified by a concrete evaluation or user-workflow need.
