# Inquiry Graph — Project Status

> **Repository:** `BrianMills2718/inquiry-graph`  
> **Role:** source-grounded inquiry representation and future useful Inquiry System.  
> **Theory repository:** `BrianMills2718/epistemic-warrant`.

## Current phase

For the final cross-project checkpoint from the long founding session, see [session-closeout-2026-09-29.md](session-closeout-2026-09-29.md).

The foundational theory has been split out.

This repository should now answer: **does a source-grounded inquiry graph provide useful capabilities beyond the transcript itself?**

## Product goal (Brian, 2026-09-29)

The reader is always an AI, never Brian. The graphs exist so an AI can understand everything Brian is interested in and his positions, and can identify gaps, open questions and conflicts across **all** his conversations. Do not design for human reading: no dashboards, UI polish or human-reader tests.

The 2026-09-29 pilot showed that one conversation fits in a model's context, and there the raw transcript beats the graph. The graph's case is therefore across many conversations: Brian's attributed positions (kept separate from assistant proposals), open questions and conflicts, where no model can read everything.

**Division of labour with onto-canon6.** onto-canon6 owns cross-source identity, alignment, governed assertions and tension (conflict) detection. Its proposed general-kernel PRD already requires preserving stance and speaker, lists `StanceEvent`, and uses both inquiry-graph trajectories (including open PRs #8 and #15) as round-trip acceptance cases. inquiry-graph should be the per-conversation producer (conversation to attributed stances, questions, moves and rationale) feeding that kernel, not a second cross-conversation store.

Do not expand the ontology by default.

## Current product

V1 supports conversation/export import, active-branch preservation, typed content/questions/relations/moves, actor-relative stance and question-status histories, exact quote/offset grounding, review state, validation, merge/query workflows, and Mermaid/DOT/Markdown/offline-HTML rendering.

Current seed:

- 247 curated source excerpts/messages;
- 250 content nodes;
- 250 relations;
- 204 inquiry moves;
- 68 stance events;
- 86 question events;
- 59 questions;
- 858 proposed annotations.

The founding seed's 2026-09-30 continuation adds the later meta-model closeout, prior-art/adoption stance, candidate-generation landscape and framework mappings, cross-framework orchestration, certified guarantee transport, and handoff/update requests. These remain curated excerpts rather than a full export.

A separate [operational-games continuation](../examples/operational-games-2026-09-30/README.md) records the next visible research trajectory without silently folding it into the founding fixture: **115 selected excerpts, 108 nodes, 85 relations, 89 moves, 66 stance events, and 33 question events**. It now covers the deliberate universalization of the game concept, top-down decomposition from rich game formalisms, perspectival/self-attributed goals, open-game reuse, the compositional-executable-world reframing, game/decision coupling, and the correction that candidate generation is already substantially mapped to mature prior art.

## Priority 1 — empirical usefulness

Track: issue #38.

**Current status 2026-09-30:** the 30-chat scale campaign is complete and independently signed off for a bounded retrieval-direction decision. On 13 valid cross-chat questions, archive-search-then-read (A) averaged **0.67** key-point coverage, positions + typed links (B) **0.63**, and positions only (C) **0.61**. On the seven source-heldout-reference questions, A scored **0.702**, while B and C both scored **0.595**. Typed links therefore did not show a useful answer-quality gain over positions alone in this sample, and the graph route did not beat archive search. No route satisfied the full source-citation/verbatim-quote answer contract.

The bounded decision is: **use archive-search-then-read as the default answer-retrieval route for this measured workload; retain the linker data for a separate future topic-map phase; do not productize the current graph answer route as superior retrieval.** This does not establish broad generalization beyond the measured 30-chat corpus. See [results](../evaluation/cross_conversation_scale/results.md) and [independent signoff](../evaluation/cross_conversation_scale/signoff.md). **Do not add a human-reader evaluation track; the intended reader is AI.**

Build the smallest machine-consumable representation/workflow needed to test whether an AI can recover:

- open questions;
- revisions and rationale;
- assumptions/dependencies;
- actor commitments;
- rejected/deferred branches;
- enough context to resume a long inquiry.

Prefer task-level evaluation before UI polish.

## Priority 2 — source reconciliation

Track: issue #3.

When the full export is available, reconcile the curated seed against exact message IDs/branches/offsets and review the 798 proposed annotations.

Until then, the seed is not source-complete.

## Hosted CI — acceptance met, issue cleanup pending

Track: issue #2.

PR #67 restored ordinary hosted CI execution: Python 3.11 and 3.13 both reached runners and passed installation, fixture rebuild, tests, graph validation, artifact drift checks, and dependency checks after the workflow stopped installing the private optional `llm_client` adapter in the ordinary test job. Live-LLM integration remains a separate optional path and is not exercised by hosted CI. Issue #2 should therefore be closed once its stale body is reconciled with this evidence.

## Separate open PR stack

PR #8 and stacked PR #15 are intentionally separate historical trajectories.

Do not merge them automatically.

## Theory split

All Formal Epistemic Reasoning Meta-Model theory and executable warrant reference regimes now live in `BrianMills2718/epistemic-warrant`.

If product experiments need them, depend on that package explicitly rather than duplicating code.

## Verification

Latest executed product verification on current `main`:

- Python 3.14.7 / native Windows;
- **67 tests passed**;
- founding seed rebuild: 250 nodes / 250 relations / 204 moves;
- operational-games continuation rebuild: 103 nodes / 80 relations / 84 moves / 61 stance events / 33 question events;
- both graphs: 0 errors / 0 warnings;
- **8 founding artifacts** checked;
- dependency check clean.

See `docs/verification.md`. The run also repaired two invalid provisional move labels already present in the founding curation (`name` -> `clarify`, `refine` -> `reframe`) without widening the V1 move vocabulary.

## Stop rules

- no ontology expansion without a concrete product/evaluation failure;
- no silent semantic identity merging;
- no user-belief inference from assistant text;
- no claim of source completeness before reconciliation;
- no polished UI before usefulness is demonstrated;
- no theory duplication after the repository split.

## One-line status

**The 30-chat result does not justify the graph as a better answer-retrieval route; archive-search-then-read is the current default for that workload. Continue Inquiry Graph only where it provides a distinct capability—such as structured topic/inquiry mapping, source-grounded provenance, or another task that earns the representation's added complexity.**
