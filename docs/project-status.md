# Inquiry Graph — Project Status

> **Repository:** `BrianMills2718/inquiry-graph`  
> **Role:** source-grounded inquiry representation and future useful Inquiry System.  
> **Theory repository:** `BrianMills2718/epistemic-warrant`.

## Current phase

The foundational theory has been split out.

This repository should now answer:

[
oxed{
	ext{Does a source-grounded inquiry graph provide useful capabilities beyond the transcript itself?}
}
]

Do not expand the ontology by default.

## Current product

V1 supports conversation/export import, active-branch preservation, typed content/questions/relations/moves, actor-relative stance and question-status histories, exact quote/offset grounding, review state, validation, merge/query workflows, and Mermaid/DOT/Markdown/offline-HTML rendering.

Current seed:

- 219 source excerpts/messages;
- 229 content nodes;
- 250 relations;
- 185 inquiry moves;
- 58 stance events;
- 76 question events;
- 54 questions;
- 798 proposed annotations.

## Priority 1 — empirical usefulness

Track: issue #38.

**Status 2026-09-29:** a first pilot with a model as the reader is done ([results](../evaluation/usefulness_pilot/results.md)). The raw transcript beat the graph report (0.81 vs 0.65 key points covered; the plain excerpts scored 0.59). The graph lost mainly on the reasons behind decisions and what happened to side lines. Next: record decision reasons and outcomes in the graph and rerun the pilot, then test a human reader and a history too long for the context window.

Build the smallest view/workflow needed to test whether the graph helps users or models recover:

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

Fresh post-split product verification on reviewed `main`:

- Python 3.14.7 / native Windows;
- **60 tests passed**;
- seed rebuild succeeded;
- **8 artifacts** checked;
- graph validation: 0 errors / 0 warnings;
- dependency check clean.

See `docs/verification.md`.

## Stop rules

- no ontology expansion without a concrete product/evaluation failure;
- no silent semantic identity merging;
- no user-belief inference from assistant text;
- no claim of source completeness before reconciliation;
- no polished UI before usefulness is demonstrated;
- no theory duplication after the repository split.

## One-line status

**The next meaningful result should be empirical evidence that Inquiry Graph is useful, not another formal layer.**
