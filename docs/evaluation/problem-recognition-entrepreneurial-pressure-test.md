# Entrepreneurial opportunity pressure test: paid-engagement capability loop

Status: working evaluation fixture, 2026-10-05.

Source: the archived Vision synthesis for Agentic Capability Architecture, which records a paid-engagement operating loop and an intended first business test of 5–10 materially similar paid engagements. This is used here as a bounded entrepreneurial/opportunity case, not as current planning authority.

## Why this is a useful counterexample

The organizational and technical cases both begin with something going wrong:

- an ambiguous organizational situation that must be framed;
- a technical anomaly against an expected model.

This case can begin without a failure signal.

The starting condition is closer to:

```text
aspiration:
turn a capability ecosystem into useful paid work

available means:
existing capabilities
existing tools and interfaces
ability to perform client work
ability to measure delivery/reuse economics

uncertainty:
which capabilities fit real engagements?
does composition actually reduce local work/cost?
what should become reusable?
```

There need not be a prior abnormality to motivate inquiry.

## Opportunity structure

The operating loop is:

```text
paid task
  ↓
isolated engagement + capability snapshot
  ↓
discover / select / reject / compose capabilities
  ↓
implement residual local gap
  ↓
deliver + measure
  ↓
generalize evidence
  ↓
update capability ecosystem
```

The intended business test is explicitly empirical: run several similar paid engagements and measure whether reuse/composition rises while local implementation, rework, human effort, and cost fall.

That makes each engagement both:

1. an attempt to create value now; and
2. an experiment that changes knowledge and future capability.

## Why "problem" is not the natural root object

A problem-driven rendering would have to invent something like:

```text
Problem: we do not yet have paid engagements.
```

That is possible, but it is semantically awkward. The motivating object is more naturally an aspiration/opportunity:

```text
ideal / aspiration:
cumulative capability ecosystem supports economically useful delivery

current means:
capabilities + tools + potential engagements

candidate opportunity:
serve a paid task using composition/reuse

experiment:
accept bounded engagement and measure economics

result:
delivery evidence + new knowledge + potentially expanded future capability
```

The inquiry is not merely reducing a discrepancy. It is exploring and partly creating a feasible path.

## Generative-space change

This case directly exhibits the earlier candidate-generation distinction.

Before an engagement, the feasible set contains the capabilities and compositions currently known.

During and after an engagement:

- a new capability combination may be validated;
- a rejected fit becomes useful negative evidence;
- a residual local implementation may remain local;
- repeated use may justify promotion to a reusable capability;
- economic evidence may change which future engagements are attractive.

So action can change the future candidate space.

```text
current generative / feasible space
  ↓ choose bounded engagement
action + delivery
  ↓
evidence / new composition / local gap knowledge
  ↓
transformed future generative / feasible space
```

This is more than selecting among static options.

## Can Inquiry Graph V1 represent this?

Mostly yes.

Useful existing constructs:

- `goal` for aspirations or target outcomes;
- `question` for business/feasibility questions;
- `hypothesis` for expected reuse/economic effects;
- `method` for the engagement operating loop;
- `example` for individual engagements;
- `candidate_for` for candidate approaches relative to a goal/question;
- `depends_on`, `supports`, `challenges`, and `supersedes`;
- moves such as `propose`, `test`, `connect`, `reframe`, and `generalize`.

A first-class `Opportunity` node kind is not required to record the reasoning trajectory.

## Where V1 is strained

### 1. Opportunity vs problem motivation is not explicit

V1 can represent both as goals/questions/hypotheses, but cannot directly ask:

> Which inquiry episodes were initiated by a perceived problem versus a newly noticed opportunity?

This may or may not be a useful generic query.

### 2. Action that changes the option space is indirect

An engagement can create new evidence, validated compositions, and reusable capabilities. V1 can record the before/after claims and moves, but "this action expanded/transformed the future candidate space" is not a dedicated relation.

That seam is already better owned by the candidate-generation/generative-system work unless repeated Inquiry Graph queries require it.

## Comparison across all three cases

| Case | Natural trigger | What is generated first? | Role of action |
| --- | --- | --- | --- |
| Organizational / ill-structured | tension / dissatisfaction / ambiguous failure | candidate problem frames | tests frames and interventions |
| Technical diagnosis | conflict with expected behavior | candidate diagnoses | discriminates diagnoses / repairs |
| Entrepreneurial opportunity | aspiration + means + possibility | candidate opportunities/goals/experiments | can create information and expand feasibility |

## Result

This case falsifies any architecture in which **Problem** is the mandatory root of goal-directed inquiry.

A more general entry point is:

```text
salient trigger
  ├─ problem / discrepancy / anomaly
  ├─ question / uncertainty
  ├─ aspiration / value
  └─ opportunity / possibility
        ↓
frame the situation
        ↓
generate candidates
        ↓
evaluate / select under uncertainty
        ↓
act / experiment
        ↓
feedback
        ↓
revise beliefs, frames, goals, and possibly the candidate space
```

"Problem" remains important, but it is one class of motivating trigger rather than the universal start state.

## Inquiry Graph implication

Do not add `Problem` or `Opportunity` as universal V1 node kinds on the basis of these cases.

The stronger candidate abstraction is not a new content type but a **reasoning-episode structure** that distinguishes:

- what made the inquiry salient;
- the active frame;
- the candidates generated;
- the evaluation/selection;
- the action/experiment;
- the resulting updates.

The next step should synthesize the three cases and test whether that episode structure can be reconstructed reliably with current V1 records or whether a higher-order episode/profile construct is warranted.
