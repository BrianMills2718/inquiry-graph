# Roadmap and Scope Control — Inquiry Graph

> Formal epistemic theory lives in `BrianMills2718/epistemic-warrant`.
> This repository is the inquiry-representation/product project.

## Delivered

V1 provides source-grounded content/questions, typed relations and inquiry
moves, actor-relative stance/question history, active-branch import, validation,
merge/query/render workflows, and curated example trajectories.

Hosted CI is restored. The extended founding and operational-games fixtures have
been rebuilt and validated; use [verification.md](verification.md) for evidence.

## Product direction after the 30-chat result

The measured retrieval campaign did **not** justify Inquiry Graph as a superior
general answer-retrieval route. For that workload, archive-search-then-read is
the default.

Continue the graph only for capabilities that are structurally distinct:

- topic/inquiry maps across conversations;
- attributed positions and provenance;
- open-question, rationale and revision traces;
- resumable inquiry state;
- downstream handoff into canonical identity/alignment systems.

Do not schedule another benchmark without explicit approval.

## Source reconciliation

Track issue #3. The curated fixtures are substantive source-grounded
reconstructions, not full-export reconciliations. When original message IDs are
available, reconcile without fabricating IDs/timestamps and preserve review
history.

## Operational-games / compositional-world continuation

The current conceptual record is
[examples/operational-games-2026-09-30](../examples/operational-games-2026-09-30/README.md).

Important current decisions:

1. the base game concept may intentionally be broad;
2. game/model choice is coupled to objectives and hypotheses, not a standalone
   foundational selector;
3. candidate generation already has mature prior-art coverage in
   `epistemic-warrant`; reuse it rather than reopening the problem;
4. UGD/open-game work is a semantic contract, not automatically the runtime;
5. the executable composition direction is a small common wiring syntax, typed
   semantic contracts, backend-specific execution, and explicit preservation
   obligations.

## Downstream integration

Cross-source identity, alignment, governed assertions and tension/conflict
handling belong in OntoCanon/downstream canonicalization, not a second store in
Inquiry Graph.

## Historical branch stack

PRs #8 and #15 remain separate historical trajectories. Do not merge them
casually.

## Stop rule

A new schema, runtime layer, candidate-generation theory, or evaluation campaign
requires a concrete unmet need. Prefer reuse and first-principles analysis.

## Theory dependency

One hop is integrated: `tools/warrant_adapter.py` runs the committed operational-games graph through `epistemic-warrant`'s grounded-dialectical regime as an external package (never copied code); see [warrant-adapter.md](warrant-adapter.md) for the mapping and the unmapped fields.
