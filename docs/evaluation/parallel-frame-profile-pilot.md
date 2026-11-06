# Parallel inquiry pilot: minimal Frame profile

Status: first comparative workflow pilot, 2026-10-06.

## Test question

What is the smallest useful representation of a frame for Inquiry Graph?

This pilot compares the earlier sequential path with a deliberately separated two-lane inquiry:

1. **reuse/discovery lane** — search internal repos and mature prior art for existing frame factorizations;
2. **frame/question lane** — derive representational requirements from real Inquiry Graph failures and queries.

This is a workflow pilot inside one research session, **not** an independent multi-agent randomized experiment. The lanes are separated by source/task role, but they are not statistically independent.

## Sequential baseline

Before the parallel pilot, the conversation and landscape work had already converged on a likely profile containing ideas such as:

- frame content;
- frame scope;
- framing/reframing acts;
- assumptions;
- salient questions/candidates.

That was useful but still left a risk of inventing a local frame tuple.

The earlier design question was:

> Can Inquiry Graph represent frame content + frame scope + framing/reframing acts + frame-relative questions/candidates without expensive reconstruction?

## Lane A — reuse/discovery

A targeted internal search found an existing Epistemic Warrant result that had not been brought into the frame discussion:

```text
game/frame = frame(
    model hypothesis,
    goal / criterion,
    boundary + access,
    resources,
    active query
)
```

This result is explicitly participant-relative and already comes from a reuse-first prior-art pass. It is not a universal ontology declaration.

External mature owners reinforce different coordinates:

- Schön / reframing: active frame, reflection, surprise-driven reframe;
- Dorst / Frame Creation: deliberate productive frame construction;
- Problem Structuring Methods: perspectives, values, boundaries, problem construction;
- C-K theory: concept/knowledge co-expansion;
- literature-based discovery: cross-domain knowledge bridging.

### Lane-A contribution

The lane supplied **existing semantic coordinates** instead of requiring a new local decomposition.

## Lane B — frame/question exploration from real graphs

Three real graphs were inspected:

1. founding candidate-generation inquiry;
2. operational-games compositional-world inquiry;
3. current semantic-modeling / adaptive-inquiry conversation.

Across all three, the smallest repeated needs were:

- **content** — what interpretation/configuration is functioning as the frame?
- **applies_to** — what inquiry stretch, goal, example, or reasoning scope does it govern?
- **active_query** — what question is currently being pursued under that frame?

Other coordinates appeared only where the particular inquiry supported them:

- model hypothesis;
- criterion / goal;
- boundary + access;
- resources;
- perspective / actor.

Frame-relative candidate/question consequences were already present elsewhere in the graph and should not be duplicated inside the frame record.

Framing and reframing acts are already represented as moves/relations and likewise should not be copied into the profile.

## Integrated result

The implemented projection therefore has only three required roles:

```text
FrameProfile
  content
  applies_to
  active_query
```

with optional method-/case-specific coordinates:

```text
perspective_actor
model_hypothesis
criterion
boundary_access
resources
```

This is a **projection sidecar**, not a new core `Frame` node kind.

Three real profiles are checked in under `evaluation/frame_profiles/`.

## Why this is better than the sequential baseline

The parallel process materially changed the design.

### 1. It found an internal prior owner

The existing participant-relative game/frame factorization in Epistemic Warrant supplied reusable coordinates that the earlier frame discussion had not surfaced.

### 2. It reduced rather than expanded the proposed abstraction

Instead of storing every plausible aspect of framing in one universal record, the empirical lane showed only three cross-case roles were consistently needed.

The UGD-style coordinates remain optional.

### 3. It avoided duplicating graph semantics

- framing/reframing acts remain moves/relations;
- frame-relative questions/candidates remain graph consequences;
- evidence/warrant remains in its owning layer.

The profile only supplies the missing **frame identity + scope + active-query projection**.

## Pilot comparison

| Criterion | Sequential baseline | Parallel pilot |
| --- | --- | --- |
| Internal prior-art owner found | No specific existing frame factorization surfaced | Epistemic Warrant participant-relative game/frame factorization |
| Required profile fields | Broad candidate set, not yet pressure-tested | 3 cross-case invariant roles |
| Optional method-specific coordinates | Undifferentiated | Explicitly optional and reused from prior work |
| Risk of duplicate semantics | Moderate | Reduced: acts and consequences stay in existing graph structures |
| Residual invention | Undefined Frame profile | Thin sidecar/projection glue only |
| Empirical pressure | Conceptual + earlier episode reconstruction | 3 real frame profiles validated against canonical graph objects |

## What this does not prove

This pilot does **not** establish that the parallel workflow is globally better.

Limitations:

- one research question;
- same overall model/session rather than independent agents;
- no controlled time/token budget;
- no blinded evaluation;
- the sequential baseline had already benefited from earlier landscape work.

The result is therefore **positive process evidence**, not a general workflow theorem.

## Current decision

Keep the Frame profile as a derived projection.

Do not add a core `Frame` node kind.

The next promotion question is now narrower:

> Can independent reviewers bind the same real inquiry to materially similar frame content, scope, and active query?

If agreement is high, the thin profile is probably sufficient.

If disagreement is concentrated in frame identity/scope and harms resumption, motif mining, or candidate-generation analysis, stronger frame semantics may be earned.

## Parallel-workflow hypothesis after the pilot

The first pilot supports a more precise version of the parallel-inquiry idea:

> Run **empirical/problem-pressure** and **reuse/prior-art** lanes concurrently, then integrate by minimizing the residual abstraction.

The integration objective is not “combine everything both lanes produced.”

It is:

```text
requirements exposed by real use
        +
existing mature semantics
        ↓
smallest residual representation / implementation
```

That is consistent with the novelty-frustration policy: a useful creative requirement should increase search pressure, and successful search should delete proposed invention.
