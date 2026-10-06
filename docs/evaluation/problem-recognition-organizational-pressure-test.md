# Organizational problem pressure test: second-brain project

Status: working evaluation fixture, 2026-10-05.

Source: an earlier owner conversation captured in Vision as `AI Ontology for Reasoning.md`. The source conversation moves from a vague symptom ("the second brain project is not working" / burnout and loss of motivation) toward several alternative problem formulations: lack of clarity, weak feedback, low perceived control, excessive complexity, conflicting strategies, unclear roles, and identity conflict. The assistant proposed interventions such as redefining the problem, reducing complexity, reusing existing repositories, and clarifying roles. Treat those assistant formulations as proposed interpretations, not owner-endorsed facts.

## Why this is a good pressure test

A simple control model would encode:

```text
desired project progress
    -
observed project progress
    =
problem
```

But the historical inquiry does something richer. It repeatedly asks whether the apparent problem is only a symptom of a differently framed problem.

## Candidate representations

### Frame A — performance discrepancy

```text
reference: useful second-brain system
observed state: project feels stalled / results are weak
discrepancy: insufficient progress
```

This frame is useful, but does not explain the discrepancy.

### Frame B — motivation / feedback

```text
symptom: burnout / motivation loss
candidate explanation:
  lack of clarity
  + weak visible results
  + low perceived control
```

The problem has shifted from "the system is not working" to "the feedback/control loop is poor."

### Frame C — problem-definition / complexity

```text
lack of clarity
  <- unclear problem definition
  <- excessive solution complexity
  <- conflicting strategies / roles
```

Now the candidate intervention changes: simplify, clarify, and search for reusable components rather than merely work harder on the existing design.

### Frame D — identity conflict

```text
self-concept: strong problem solver / winner
reality signal: project is not succeeding
tension: failure threatens identity
```

This is not a substitute for the project diagnosis. It is another possible explanation for avoidance or distress around confronting the project state.

## What changes when the frame changes?

This is the material test.

| Frame | Main question | Candidate intervention |
| --- | --- | --- |
| Performance discrepancy | Why are results below the reference? | Improve execution |
| Feedback/control | Why does effort not produce useful feedback/control? | Shorten feedback loops; expose progress |
| Problem-definition/complexity | Are we solving the right problem with an overcomplicated design? | Reframe, simplify, reuse, clarify roles |
| Identity conflict | Is the difficulty of confronting the problem partly maintained by self-concept threat? | Separate identity from model quality; make revision safe |

The different frames lead to different evidence requests, candidate causes, interventions, and success criteria. Therefore problem formulation is not cosmetic metadata.

## Can Inquiry Graph V1 represent this?

Mostly yes.

Useful existing constructs:

- `question` for "what problem are we actually solving?";
- `hypothesis` for candidate diagnoses;
- `goal` for desired outcomes;
- `reframes` for replacing one active question with another;
- `challenges` for questioning a frame or causal explanation;
- `depends_on` and `motivates` for weaker semantic connections;
- moves such as `decompose`, `hypothesize`, `challenge`, `reframe`, and `test`.

A sequence of alternative problem frames can therefore be represented without adding a `Problem` node kind.

## Where V1 is strained

### 1. Frame identity is indirect

A problem frame is currently represented through a question/hypothesis cluster plus moves and relations. If a downstream query asks "show every problem frame considered, the assumptions each frame foregrounded, and which frame superseded which," the answer requires reconstruction rather than a first-class object.

This is a **representation-gap candidate**, not yet proof that a new primitive is needed.

### 2. Perspective/stakeholder ownership is weak

The case could involve different views from the user, team members, or organizational roles. Actor stance exists, but "this stakeholder sees X as the problem under these values/boundaries" is not a dedicated construct.

Again, one case is insufficient to extend the core.

### 3. Symptom vs problem vs cause is method-specific

The historical conversation uses terms such as symptom, cause hypothesis, feedback variable, control variable, and identity conflict. V1 can encode these as claim/hypothesis content, but it intentionally does not force them into universal ontology types.

That seems correct so far.

## Verdict

**The simple discrepancy model is underfactored for this case.**

A better workflow distinction is:

```text
observed condition
  ↓ interpreted relative to values / reference
salient discrepancy or tension
  ↓
candidate problem frames
  ↓
candidate diagnoses / explanations
  ↓
candidate interventions
  ↓
tests / action / feedback
  ↓
reframe or revise
```

The important addition is **candidate problem frames** between raw discrepancy and diagnosis.

That does not yet imply a new Inquiry Graph primitive. It implies that the evaluation should test whether problem-frame queries can be served adequately by existing question/hypothesis/move structures.

## Next falsifier

Run the same queries on:

1. a technical diagnosis case where expected behavior is comparatively well specified;
2. an entrepreneurial opportunity case where the feasible set is partly created through action.

If both also require reconstructing a stable "frame" object and the absence materially hurts query quality, then a shared Frame / ProblemFrame abstraction may be earned. Otherwise keep framing method-specific.
