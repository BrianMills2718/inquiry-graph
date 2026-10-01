# New Agent Handoff — Inquiry Graph

> **Updated:** 2026-10-01
> **Repository:** `BrianMills2718/inquiry-graph`
> **Purpose:** source-grounded per-conversation inquiry representation for AI
> consumers. Foundational epistemic theory lives in `epistemic-warrant`.

## Read this first

The canonical current-state documents are:

1. [Project status](project-status.md)
2. [Roadmap](roadmap.md)
3. [Verification](verification.md)
4. [Operational-games coverage audit](../examples/operational-games-2026-09-30/coverage-audit.md)
5. [Conversation walkthrough](conversation-walkthrough.md)

The former long 2026-09-29 handoff/closeout instructions are historical. Their
still-useful facts are preserved in
[archive/2026-09-29-handoff-snapshot.md](archive/2026-09-29-handoff-snapshot.md).

## Repository boundary

Inquiry Graph owns source-grounded inquiry history:

- visible source excerpts;
- questions and question-state changes;
- typed relations and inquiry moves;
- actor-relative stance;
- provenance and review state.

It is **not** the canonical truth store and should not duplicate the formal
epistemic theory in `epistemic-warrant`.

Cross-source identity/alignment/governed assertions belong downstream in the
OntoCanon direction. Keep PRs #8/#15 separate unless that historical trajectory
is explicitly resumed.

## Current product result

The graph has **not** demonstrated superior answer retrieval.

For the measured 30-chat workload, archive-search-then-read beat the tested
positions/typed-link routes. Use archive search as the default answer-retrieval
route for that workload. Preserve Inquiry Graph where it provides a distinct
capability: structured inquiry/topic mapping, attributed positions, provenance,
open-question/rationale traces, or resumable research state.

Do not restart a benchmark campaign merely because the representation changed.
Benchmarks require explicit approval.

## Current research continuation

The operational-games fixture records the later conceptual thread. The current
settled corrections are:

- describing a game is distinct from optimizing a strategy;
- the base notion of game is intentionally broad;
- game/model choice is **not** a new isolated primitive: it is coupled to the
  active objective/goal and hypotheses about how actions produce outcomes;
- candidate generation is **not** an undefined foundational gap. The mature
  survey in `epistemic-warrant` already maps program synthesis/CEGIS,
  ILP/MIL, anti-unification, HR theory formation, conceptual blending and
  orchestration frameworks to a reusable generative interface;
- do not invent a second candidate-generation theory in Inquiry Graph;
- UGD/open-game work supplies semantic requirements; the executable composition
  direction is a small wiring syntax + typed contracts + backend-specific
  execution + explicit preservation obligations.

See the coverage audit for the exact source-grounded trajectory.

## Current next work

For Inquiry Graph itself, prefer maintenance and distinct-capability work over
schema expansion:

- keep the live conversation trajectory current when requested;
- finish source reconciliation when original export IDs are available;
- use the existing topic/inquiry-map direction for cross-chat structured
  context, without claiming it is better general retrieval;
- keep documentation current when project decisions move.

For foundational candidate generation, warrant, game semantics, or UGD, switch
to `BrianMills2718/epistemic-warrant`.

## Verification

Do not copy old test counts into new status text. `docs/verification.md` is the
append-only evidence record; `docs/project-status.md` states the latest
verified baseline.

## Stop rules

- no ontology expansion without a concrete need;
- no user-belief inference from assistant text;
- no silent semantic identity merging;
- no claim of full-export completeness before reconciliation;
- no theory duplication after the repo split;
- no new candidate-generation framework unless the existing prior-art interface
  demonstrably fails;
- no benchmark without Brian's explicit approval.
