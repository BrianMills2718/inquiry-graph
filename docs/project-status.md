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

The 2026-09-30 continuation adds the later meta-model closeout, prior-art/adoption stance, candidate-generation landscape and framework mappings, cross-framework orchestration, certified guarantee transport, and handoff/update requests. These remain curated excerpts rather than a full export.

## Priority 1 — empirical usefulness

Track: issue #38.

**Status 2026-09-29:** a first pilot with an AI model as the reader is done ([results](../evaluation/usefulness_pilot/results.md)). The raw transcript beat the graph report (0.81 vs 0.65 key points covered; the plain excerpts scored 0.59). The graph lost mainly on the reasons behind decisions and what happened to side lines. Next: record decision reasons/outcomes and deferred-branch rationale, rerun the AI-reader pilot, then move to multi-conversation histories that exceed any single model context. **Do not add a human-reader evaluation track; the intended reader is AI.**

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

## Priority 3 — hosted CI

Track: issue #2.

Hosted jobs fail before runner execution. Local verification is green, so this is lower-priority infrastructure debt.

## Separate open PR stack

PR #8 and stacked PR #15 are intentionally separate historical trajectories.

Do not merge them automatically.

## Theory split

All Formal Epistemic Reasoning Meta-Model theory and executable warrant reference regimes now live in `BrianMills2718/epistemic-warrant`.

If product experiments need them, depend on that package explicitly rather than duplicating code.

## Verification

Last fully executed post-split product verification on reviewed `main`:

- Python 3.14.7 / native Windows;
- **60 tests passed**;
- seed rebuild succeeded;
- **8 artifacts** checked;
- graph validation: 0 errors / 0 warnings;
- dependency check clean.

See `docs/verification.md`. The 2026-09-30 seed continuation was structurally cross-reference checked in the GitHub update path, but the execution device was offline, so `examples/build_seed.py`, artifact reproduction, and the full test suite still need to be rerun once an executable environment is available.

## Stop rules

- no ontology expansion without a concrete product/evaluation failure;
- no silent semantic identity merging;
- no user-belief inference from assistant text;
- no claim of source completeness before reconciliation;
- no polished UI before usefulness is demonstrated;
- no theory duplication after the repository split.

## One-line status

**The next meaningful result should be evidence that Inquiry Graph helps an AI recover Brian's attributed positions, rationale, open questions and cross-conversation tensions when the full history cannot fit in context.**
