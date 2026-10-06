# Real reasoning-episode reconstruction evaluation

Status: empirical representation check, 2026-10-05.

## Question

Can the seven-role reasoning-episode view be reconstructed from real captured Inquiry Graphs rather than only synthetic fixtures?

Roles:

1. salient condition;
2. frame;
3. candidate;
4. evaluation;
5. commitment;
6. action/test;
7. update.

## Cases

Three existing captured graphs were profiled without changing their V1 ontology.

| Graph | Roles recovered | Direct | Reconstructed | Missing |
| --- | ---: | ---: | ---: | ---: |
| Founding candidate-generation episode | 7/7 | 5 | 2 | 0 |
| Operational-games compositional-world episode | 7/7 | 6 | 1 | 0 |
| 2026-10-05 semantic-modeling fixture | 5/7 | 3 | 2 | 2 |

The profiles are checked into `evaluation/reasoning_episode_profiles/` and validated against the canonical graph objects in tests.

## Recovery meanings

- **direct** — the graph already contains an explicit typed object that naturally fills the role;
- **reconstructed** — the graph contains adequate explicit records, but assigning the episode role requires a higher-order grouping/interpretation;
- **analyst** — the role would require content not adequately represented in the graph.

No tested role was marked analyst-only. That is encouraging, but profile construction itself is still manually curated.

## Main finding 1: frame is consistently reconstructed

The `frame` role was reconstructed rather than direct in all three cases.

Examples:

- candidate-generation interface as the working frame for the founding episode;
- compositional causal/mechanical world model as the frame for the operational-games episode;
- candidate-generation-under-transformable-feasibility as the frame for the current semantic-modeling episode.

This is the strongest repeated representational friction so far.

It does **not** yet prove Inquiry Graph needs a core `Frame` node kind. A frame can remain a role played by an existing claim, hypothesis, question cluster, or method in a particular episode.

## Main finding 2: complete episode recovery depends on capture coverage

The 2026-10-05 semantic-modeling fixture recovers only 5/7 roles. It lacks:

- evaluation;
- update.

This is not primarily an ontology failure. The fixture was intentionally captured before later pressure tests and repository changes occurred.

That is important for the self-improvement loop:

> episode completeness is partly a **capture lifecycle** problem, not merely a schema problem.

A conversation graph may need an explicit continuation/update pass after downstream actions occur.

## Main finding 3: the profile is useful as a view

The same role vocabulary successfully organizes materially different inquiries:

- candidate-generation theory building;
- architectural reframing plus executable validation;
- semantic/practical framework construction.

The view therefore appears to be a useful **megamodel/projection layer** over V1.

Current evidence favors:

```text
V1 graph
  + episode-role profile
  + lifecycle update
  -> reasoning-episode view
```

over:

```text
add seven new core ontology types
```

## Current diagnosis of Inquiry Graph

### Representation gap: frame role

Repeated but currently manageable with a projection.

Status: keep under observation.

Promotion gate: show that frame reconstruction is materially ambiguous or expensive across independent reviewers/use cases, or that a concrete query cannot be served reliably without first-class frame identity.

### Workflow gap: post-conversation continuation

A graph captured at conversation time can become stale relative to actions and outcomes that happen afterward.

Status: stronger evidence than before.

Candidate repair: add a lightweight continuation mechanism that can append later action/result/update evidence to the same inquiry without rewriting the historical graph.

This is consistent with the existing append/history discipline.

## Next test

The next useful experiment is **reviewer agreement**, not more ontology design.

Give the same real graph and seven-role query to two independent annotators/agents and compare:

- episode boundary;
- selected frame;
- role bindings;
- missing-role judgments.

If agreement is high, keep `ReasoningEpisode` as a derived view.

If disagreement clusters specifically around frame/boundary reconstruction and harms a named use such as resumption or motif mining, then stronger episode/frame representation may be warranted.
