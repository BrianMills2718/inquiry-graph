# Conversation-to-graph self-improvement loop

**Status:** proposed workflow, 2026-10-05.

## Purpose

Substantive inquiry conversations should do two jobs:

1. leave behind a source-grounded Inquiry Graph of what was asked, proposed,
   challenged, distinguished, reframed, and left open; and
2. use that graph as evidence for whether Inquiry Graph itself represented the
   inquiry well enough for its intended uses.

The second job is a feedback loop, not permission for the repository to rewrite
its own ontology. A conversation can expose a representational or workflow gap;
it cannot silently promote one local workaround into shared semantics.

The governing rule is:

> **self-improving, not self-authorizing**

## Loop

```text
conversation
   ↓
source-grounded inquiry graph
   ↓
representation-fit review
   ├─ what was easy to express?
   ├─ what was lossy or awkward?
   ├─ what required a workaround?
   ├─ what could not be represented?
   └─ what was a capture/workflow failure rather than an ontology failure?
   ↓
diagnosis + candidate repair
   ↓
prior-art / existing-repo check
   ↓
promotion gate
   ↓
smallest justified repo change
   ↓
verification on prior + new cases
   ↺
```

## 1. Capture the inquiry first

Use the existing V1 graph contract. Preserve source excerpts separately from
semantic interpretation. Do not infer hidden reasoning.

Capture, where material:

- content nodes;
- typed semantic/argument relations;
- inquiry moves;
- actor-relative stance and question-state changes;
- unresolved questions and rejected/superseded proposals.

A compact curated excerpt graph is acceptable when the full native transcript
is unavailable, but the coverage note must say so.

## 2. State the graph's purpose for this conversation

A fit judgment is always relative to a use.

Examples:

- recover the conceptual trajectory;
- identify unresolved questions;
- compare alternative factorizations;
- mine recurring reasoning motifs;
- resume the inquiry later;
- inspect how a conclusion changed after a challenge.

Do not call a representation "bad" merely because it omits distinctions that no
current use needs.

## 3. Run the representation-fit review

Each captured conversation may carry a sibling `fit-review.json`, validated by
`inquiry_graph.fit_review.FitReview`.

For every material friction point, ask:

1. **Representability:** Can V1 state the distinction at all?
2. **Fidelity:** Can it state it without replacing a precise relation with
   `related_to`, prose, naming conventions, or analyst memory?
3. **Level:** Is the issue about domain content, a reasoning move, a recurring
   strategy/motif, actor stance, review state, or repository workflow?
4. **Alternative factorization:** Would split / merge / retype / redraw-boundary
   materially change a query, interpretation, extraction, or downstream use?
5. **Capture versus ontology:** Did the schema fail, or did the extraction path
   simply fail to capture something the schema already supports?
6. **Consequence:** What actual use becomes incorrect, impossible, or
   substantially harder because of the issue?

## 4. Diagnose, do not immediately extend

Use the factorization diagnostics as descriptive labels:

- `underfactored` — one construct hides distinctions with different
  consequences;
- `overfactored` — distinctions add complexity without a current consequence;
- `misfactored` — unlike kinds are treated as peers;
- `wrong_level` — content, process, strategy, status, or authority levels are
  conflated;
- `hidden_coupling` — supposedly independent pieces share a dependency;
- `incomplete` — an in-scope case cannot be expressed;
- `non_compositional` — the representation forces exclusive bins where real
  cases combine;
- `capture_gap` — the source/extractor omitted supported information;
- `workflow_gap` — repository process loses or fails to revisit information;
- `representation_gap` — the information exists but the current form makes a
  needed operation materially difficult.

These diagnoses are evidence about the current representation, not new graph
node kinds.

## 5. Prefer reuse and the smallest repair

Before adding a shared construct:

1. check whether the current graph can express the need compositionally;
2. check whether the issue belongs to extraction, review, or a downstream
   projection instead;
3. search mature prior art and related repositories;
4. prefer a profile, sidecar, adapter, or documented convention over a new core
   primitive when it preserves the needed distinction.

A missing name is not enough evidence for a missing primitive.

## 6. Promotion gates

A `fit-review` finding must state its own `promotion_gate`.

Default promotion policy:

- **Documentation/workflow repair:** may be justified by one clear failure if it
  does not change graph semantics.
- **Extraction/tooling repair:** requires a reproducible capture/use failure and
  regression coverage.
- **Core relation/node/move change:** normally requires either:
  - the same material representational failure in at least two independent
    inquiries, or
  - one blocking case plus explicit owner approval and a prior-art/reuse check.
- **New higher-order construct (for example StrategyEpisode):** require a query
  or evaluation that cannot be served adequately by the current
  method-node/example/part_of representation.

Every shared semantic change should replay prior fixtures and explain any
changed interpretation.

## 7. Close the loop

After a repair:

- rerun the case that exposed it;
- rerun representative previous cases;
- mark the finding resolved, rejected, or superseded;
- record whether the repair actually improved the intended use;
- leave the next unresolved inquiry question explicit.

A proposal that makes the ontology more elegant but changes no material use is
not an improvement by default.

## Current conversation as first fixture

`examples/conversations/2026-10-05-semantic-modeling/` is the first explicit
fixture for this loop. It records the inquiry about modeling, metamodeling,
ontology, canonical factorization, ideals/goals, optimization, candidate
generation, reasoning motifs, problem recognition, and this self-improvement
mechanism.

Its fit review deliberately records open gaps without extending the V1 graph
ontology. In particular, this conversation raises but does not yet justify:

- a more precise relation between evaluative ideals, perceived problems, goals,
  and tasks;
- a first-class strategy/motif episode type;
- any new universal problem-recognition primitive.

The next inquiry should investigate problem/anomaly recognition and existing
prior art before deciding whether any of those need shared representation.
