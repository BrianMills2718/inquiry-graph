# Reasoning-episode view: first operational test

Status: working evaluation, 2026-10-05.

## Question

Can one higher-order view recover the same reasoning roles across materially different inquiry regimes without adding new core Inquiry Graph node or relation types?

The tested roles are:

1. salient condition;
2. frame;
3. candidates;
4. evaluation;
5. commitment;
6. action or test;
7. update.

## Implementation

`inquiry_graph.episode_view` defines a small **projection profile** over existing graph object IDs. It does not change the V1 graph schema.

A profile assigns existing graph records to cross-case roles and `project_episode` returns a role-oriented view.

This is deliberately a projection, not semantic authority:

- it does not infer hidden intent;
- it does not assert that every inquiry has all seven roles;
- it does not make `ReasoningEpisode` a core ontology type;
- it does not permit the projection to overwrite graph truth.

## Three-regime test

The same profile shape is exercised against minimal fixtures representing:

### Organizational / ill-structured inquiry

```text
project feels stalled
  -> feedback/control frame
  -> candidate simplification / role clarification
  -> evaluate interventions
  -> commit to reframing experiment
  -> test smaller frame
  -> revise active frame
```

### Technical diagnosis

```text
validator failure
  -> expected-vs-observed diagnostic frame
  -> candidate architecture diagnosis
  -> compare causes against evidence
  -> commit to repair
  -> rerun validator
  -> revise diagnosis/model
```

### Entrepreneurial opportunity

```text
aspiration + available means
  -> opportunity frame
  -> candidate bounded engagement
  -> evaluate fit/downside/learning value
  -> commit
  -> deliver and measure
  -> update future feasible space
```

The same seven-role profile applies to all three without modifying the V1 graph ontology.

## What this establishes

It establishes only a **representational possibility**:

> a common reasoning-episode view can be layered over heterogeneous inquiries.

It does not yet establish that the roles can be recovered automatically or reliably from real conversation graphs.

That distinction matters. A projection profile may merely move bespoke interpretation from prose into a sidecar.

## Current design consequence

Do not add a core `ReasoningEpisode` record yet.

The cheapest adequate design is currently:

```text
V1 Inquiry Graph
    +
optional reasoning-episode projection profile
    =
cross-case episode view
```

This follows the repository's broader rule: prefer a projection/profile over a core ontology extension until a real query or workflow requires stronger semantics.

## Next falsifier

The next test should use **real captured graphs**, not hand-authored minimal fixtures.

For at least three real inquiry graphs, attempt to answer:

1. What made the inquiry salient?
2. What frames were considered?
3. What candidates did each frame generate?
4. What evidence/values evaluated those candidates?
5. What was selected or committed to?
6. What action/test occurred?
7. What changed afterward?

Measure:

- how many roles can be recovered directly from existing typed relations/moves;
- how many require analyst-only interpretation;
- whether two reviewers produce materially different episode profiles;
- whether the view improves resumption, motif mining, or another named use.

A core episode construct is warranted only if the profile repeatedly loses material semantics or produces costly/unstable reconstruction.
