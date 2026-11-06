# Problem recognition: three-case synthesis

Status: working synthesis, 2026-10-05.

This note compares the three pressure tests now recorded in Inquiry Graph:

1. organizational / ill-structured problem framing;
2. technical diagnosis;
3. entrepreneurial opportunity under uncertainty.

## Cross-case result

The strongest result is negative:

> **Problem is not a universal root object for goal-directed inquiry.**

The three cases begin differently.

| Case | Natural trigger | First major generative object | What action does |
| --- | --- | --- | --- |
| Organizational / ill-structured | dissatisfaction, tension, ambiguous failure | candidate problem frames | tests frames and interventions |
| Technical diagnosis | conflict with expected behavior | candidate diagnoses | discriminates causes and repairs |
| Entrepreneurial opportunity | aspiration + means + possibility | candidate opportunities/goals/experiments | can create information and expand feasibility |

The common structure is not "problem -> solution."

A better cross-case pattern is:

```text
something becomes salient
        ↓
frame what is going on
        ↓
generate relevant candidates
        ↓
evaluate / select under uncertainty
        ↓
act / experiment / inquire
        ↓
observe consequences
        ↓
revise beliefs, frames, goals, methods, or candidate space
```

"Something becomes salient" is deliberately role language, not a proposed ontology primitive. It can be:

- a discrepancy;
- an anomaly;
- a question;
- an unresolved uncertainty;
- an aspiration;
- an opportunity;
- an external assignment or demand;
- a surprise.

## Refined praxeological picture

The earlier chain:

```text
ideal -> problem -> goal -> task -> method -> plan -> action
```

is useful for one class of problem-driven episodes but too narrow as the general architecture.

The pressure tests support:

```text
VALUES / IDEALS / INTERESTS
        +
WORLD / SELF / SITUATION MODEL
        ↓
SALIENT CONDITION
(problem, anomaly, question, opportunity, aspiration, surprise...)
        ↓
FRAMING
what is this?
what matters?
where are the boundaries?
whose perspective?
        ↓
CANDIDATE GENERATION
frames, explanations, goals, strategies, experiments, interventions
        ↓
EVALUATION / SELECTION
value, feasibility, uncertainty, cost, risk, information value
        ↓
COMMITMENT
selected goal / task / experiment / strategy
        ↓
METHOD / PLAN / ACTION
        ↓
OUTCOME + OBSERVATION
        ↓
LEARNING / REFRAMING
        ↺
```

This preserves the useful distinction between ideals and goals:

- **ideal/value** guides evaluation;
- **goal** is one possible committed target generated within an episode;
- goals do not need to exist before inquiry begins.

## Where entrepreneurship fits

Entrepreneurial reasoning is especially visible in two places:

1. **candidate-space transformation** — questioning assumptions, combining means, changing constraints, finding partners, inventing new methods;
2. **action under uncertainty** — experiments and commitments can change what becomes feasible.

So "achievability" is endogenous in many episodes.

The system should not only ask:

> Which known goal is feasible?

It should also be able to ask:

> What action would teach us what is feasible, or make a valuable state more feasible?

## Where diagnosis fits

Diagnosis is one method family for episodes where there is a model-relative anomaly.

```text
expected behavior + observation
  -> conflict
  -> candidate explanations
  -> discriminating test
  -> repair / model revision
```

It should not be generalized into the architecture for all inquiry.

## Where problem framing fits

For ill-structured situations, a problem frame is itself a candidate representation.

```text
ambiguous situation
  -> candidate frame A
  -> candidate frame B
  -> consequences of each frame
  -> revise / select / hold multiple frames
```

A frame matters when it changes what evidence, goals, interventions, or success criteria follow.

## Inquiry Graph design consequence

The three cases do **not** justify adding universal core node kinds for:

- Problem;
- Anomaly;
- Diagnosis;
- Opportunity;
- Ideal.

The stronger candidate gap is higher-order:

> Can Inquiry Graph reliably represent and query a **reasoning episode** with an initiating salient condition, active/candidate frames, generated candidates, selection/commitment, action/test, and updates?

V1 can reconstruct much of this from:

- questions, goals, claims, hypotheses, methods, examples;
- moves such as ask, reframe, hypothesize, decompose, test, propose;
- relations such as motivates, candidate_for, reframes, depends_on, supports, challenges, supersedes;
- stance and question-status history.

The open issue is whether reconstruction is sufficiently faithful and cheap for the intended uses.

## Next evaluation

Do not add a new core construct yet.

Instead, evaluate one concrete query set across the three fixtures:

1. What made this inquiry salient?
2. What frames were considered?
3. What candidates did each frame make available?
4. What evidence or values were used to evaluate them?
5. What was selected or committed to?
6. What action/test occurred?
7. What changed afterward: belief, frame, goal, strategy, or candidate space?

If these queries are unreliable or require extensive bespoke reconstruction in all three regimes, then a higher-order `ReasoningEpisode` / `InquiryEpisode` profile or record becomes justified.

If current V1 records answer them adequately, keep the core small and implement the episode as a projection/view rather than ontology expansion.
