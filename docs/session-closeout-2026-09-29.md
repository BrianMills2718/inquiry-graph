# Session Closeout — 2026-09-29

## Purpose

This is the final cross-project checkpoint for the long session that began by developing a formal meta-model of epistemology/inference and later added a source-grounded inquiry representation and product direction.

The work is now deliberately split into two repositories:

- `BrianMills2718/epistemic-warrant` — Formal Epistemic Reasoning Meta-Model and executable reference regimes.
- `BrianMills2718/inquiry-graph` — per-conversation inquiry representation and product/usefulness experiments.

A third downstream direction, `onto-canon6`, owns cross-source identity/alignment, governed assertions and tension/conflict integration. Inquiry Graph should feed it rather than becoming a second cross-conversation canonical store.

## What the session accomplished

### Formal theory

The session moved away from a flat deduction/induction/abduction taxonomy toward a factorized architecture separating representation, candidate generation, support/provenance, argument/defeat, warrant, current license, epistemic action/update and strategy/control.

Candidate generation was then compared with mature work rather than treated as a blank-slate problem. CEGIS/program synthesis, Meta-Interpretive Learning, anti-unification, HR theory formation and conceptual blending fit the typed generative-system interface. Cross-framework orchestration was aligned with blackboard systems, multistrategy learning, algorithm selection, hyper-heuristics, configuration, PRODIGY, Soar and reflection. Guarantee transport was aligned with institutions/DOL/Hets, MMT morphisms, abstract interpretation and contract/refinement theory.

The theory was split into `epistemic-warrant`. Its current correctness gate is **epistemic-warrant#2**; after that the main foundational question is **epistemic-warrant#1 acceptance licensing and warrant composition**.

### Inquiry representation

Inquiry Graph developed an executable source-grounded model of:

- content/questions;
- typed relations and inquiry moves;
- actor-relative stance;
- question-status history;
- exact source grounding/provenance;
- review state;
- deterministic rendering/query/validation workflows.

The founding curated seed currently contains 219 source excerpts, 229 content nodes, 250 relations, 185 inquiry moves, 58 stance events, 76 question events, 54 questions and 798 proposed annotations.

### Useful-system direction

The product goal was clarified: **the reader is an AI, not Brian**. The graph should help an AI recover Brian's attributed positions, rationale, open questions, dependencies and tensions across histories too large to fit in one context window.

The first AI-reader usefulness pilot is already complete. On the single-conversation test, the raw transcript outperformed the graph report (0.81 vs 0.65 key-point coverage; plain excerpts 0.59). The graph's main losses were decision rationale and side-line outcomes.

Therefore the immediate product plan is not more ontology or UI. It is:

1. capture decision reasons/outcomes and deferred-branch rationale better;
2. rerun the AI-reader pilot;
3. move to multi-conversation histories that exceed a single model context;
4. test cross-conversation integration downstream rather than duplicating it in Inquiry Graph.

## Current plans by repository

### Inquiry Graph

**P0 — issue #38: empirical usefulness.** Default next product track.

**P1 — issue #3: source reconciliation.** Continue exact source reconciliation; full export is still needed for the remaining voice-mode excerpts.

**P2 — machine-consumable workflow.** Only after P0 identifies which retrieval/representation operations actually help the AI reader.

**Maintenance — issue #2: hosted CI.** Lower priority while local verification remains green.

**Separate old trajectory — PR #8 and stacked PR #15.** Do not merge casually. PR #15 is based on #8 rather than main.

### Epistemic Warrant

**P0 — issue #2: semantic correctness.** Fix/enforce flat ABA, target binding and preference semantics with regression tests.

**P1 — issue #1: acceptance licensing + warrant composition.** Main foundational research frontier after P0.

**P2 — issue #5: systematic comparison/adoption matrix.** Normalize terminology and reuse mature frameworks; novelty is not the goal.

**Escalation only — issues #3/#4.** First-class derivation/subargument structure and full ABA+/hyperargumentation only when concrete semantics require them.

## Verification baselines

### Inquiry Graph

Fresh post-split native-Windows verification:

- Python 3.14.7;
- 60 tests passed;
- seed rebuild succeeded;
- 8 artifacts checked;
- graph validation 0 errors / 0 warnings;
- dependency check clean.

### Epistemic Warrant

Fresh post-split native-Windows verification:

- Python 3.14.7;
- 82 tests passed;
- dependency check clean.

The green theory suite does **not** resolve the semantic defects in epistemic-warrant#2.

## Important stop rules

- Do not merge the theory and product repositories back together casually.
- Do not copy theory code into Inquiry Graph; use an explicit package dependency if product experiments need it.
- Do not expand ontology/formalism without a concrete failed benchmark or product requirement.
- Do not optimize for novelty; prefer mature off-the-shelf theory.
- Do not infer Brian's stance from assistant text.
- Do not silently merge semantically similar nodes.
- Do not treat the curated seed as source-complete.
- Do not build a polished human UI; the intended reader is AI.
- Do not transport guarantees across representations without a preservation certificate.
- Do not treat green tests as proof of semantic correctness.
- Do not merge Inquiry Graph PR #8/#15 without an explicit architecture decision.

## Fresh-agent routing

If assigned **product/usefulness**, start in this repository with `docs/new-agent-handoff.md` and issue #38.

If assigned **source integrity**, start with issue #3.

If assigned **formal theory**, switch immediately to `BrianMills2718/epistemic-warrant` and follow its `docs/new-agent-handoff.md`; start with issue #2.

If assigned **paper/framework comparison**, work `epistemic-warrant#5`.

If assigned **old hypergraph/formal-inquiry integration**, inspect Inquiry Graph PR #8 and stacked #15 but do not merge them by default.

## Bottom line

The session has reached a clean handoff boundary.

The theory is no longer in broad architecture-discovery mode; it has a concrete semantic-correctness gate and a narrowed acceptance/warrant-composition frontier.

The product is no longer in schema-building mode; it has an empirical result showing exactly where the current representation underperforms the transcript and a concrete next experiment.

The next agent should choose one track and work from the corresponding repository's handoff rather than reconstructing this conversation.
