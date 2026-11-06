# Technical diagnosis pressure test: AutoCoder validation failure

Status: working evaluation fixture, 2026-10-05.

Source: Vision lineage material for the AutoCoder family, including a historical episode in which the real validator produced 0% validation success after earlier mock-validator results appeared materially better. The same source records an architecture mismatch: the system was designed around streams while generated code used RPC-style communication, along with wrong component types.

This case is useful because expected behavior is comparatively well specified. Unlike the organizational case, we do not need to negotiate what "success" means before noticing a failure.

## Initial anomaly

```text
expected:
generated systems validate successfully under the real validator

observed:
0% validation success

anomaly:
observed behavior violates the expected contract
```

At this point, the existence of a problem is comparatively uncontroversial.

## Diagnosis structure

The historical material then distinguishes candidate explanations:

```text
anomaly:
0% validation success
    ↓
candidate diagnosis A:
mock validator had hidden failures
    ↓
candidate diagnosis B:
communication architecture mismatch
(stream design vs RPC-style generated code)
    ↓
candidate diagnosis C:
wrong component-type abstraction
(13 hardcoded types rather than intended primitives)
    ↓
candidate repair:
change the architecture / generation contract, not merely patch outputs
```

This is structurally different from the organizational pressure test.

The technical case starts with a stable anomaly and then searches for a diagnosis. The organizational case first had to decide what should count as the problem.

## Important distinctions

### Anomaly is not diagnosis

"0% validation success" establishes a mismatch against an expected outcome. It does not by itself establish why.

### Diagnosis is relative to a model

Calling "RPC vs streams" the architecture mismatch depends on a model of intended communication behavior. Without that model, it is merely a difference.

### Repair depends on diagnosis level

If the failure were a local code defect, patching generated code might be appropriate.

If the failure is a blueprint/architecture defect, local patches are the wrong-level repair. Later AutoCoder work states this explicitly: if the problem is a blueprint defect, heal the blueprint and regenerate downstream artifacts.

That is a useful general pattern:

```text
symptom / failed check
  -> conflict with expected model
  -> candidate diagnosis
  -> locate failure level
  -> choose repair at that level
  -> rerun check
```

## Can Inquiry Graph V1 represent this?

Yes, more comfortably than the organizational case.

A plausible representation uses:

- claim/example nodes for observations such as validation results;
- question for "why does the real validator fail?";
- hypothesis nodes for candidate diagnoses;
- `supports` / `challenges` for diagnostic evidence;
- `depends_on` for architectural assumptions;
- `candidate_for` for candidate repair relative to the diagnostic question/goal;
- `test` moves for validator runs;
- `hypothesize`, `decompose`, `challenge`, and `reframe` for diagnostic reasoning;
- `supersedes` when a new diagnosis replaces an earlier account.

No dedicated `Anomaly` or `Diagnosis` node kind is needed to preserve the inquiry.

## Where V1 is strained

### 1. Expected-vs-observed relation is generic

The graph can encode the expected behavior and observed failure as claims, but there is no specialized "violates expectation / conflicts with model prediction" relation.

This may be fine if method-specific diagnosis tooling owns that semantics.

### 2. Diagnosis level is implicit

The distinction between output defect, component defect, blueprint defect, and architecture defect matters because it determines the correct repair scope. V1 can express this in content and `part_of` / `depends_on`, but does not have a generic typed notion of fault level.

Again, this looks method-specific rather than obviously core.

## Comparison with organizational case

| Question | Technical diagnosis | Organizational / ill-structured |
| --- | --- | --- |
| Is the anomaly initially clear? | Usually yes | Often contested |
| Is the reference model stable? | Relatively | Often part of the inquiry |
| Main uncertainty | Cause / fault location | What the problem is, then cause |
| Main generative object | Candidate diagnoses | Candidate problem frames + diagnoses |
| Reframing role | Can change diagnosis level/model | Can redefine the problem itself |
| Does V1 need a new primitive? | Not demonstrated | ProblemFrame remains a candidate gap |

## Result

The technical case weakens the case for a universal `Problem` or `Anomaly` primitive in Inquiry Graph.

It supports a layered distinction:

```text
observation
  ↓ comparison against expectation/model
anomaly or conflict
  ↓
candidate diagnosis
  ↓
repair hypothesis
  ↓
test
  ↓
model / diagnosis revision
```

But most of that semantics belongs naturally to the diagnostic method or domain model. Inquiry Graph can record the reasoning trajectory without owning the full diagnosis ontology.

## Next falsifier

The entrepreneurial case is now the most important one.

It should test whether the sequence can begin without a salient anomaly at all:

```text
means / environment / aspiration
  -> noticed or created possibility
  -> candidate opportunity
  -> experiment / commitment
  -> changed feasible set
```

If that case does not require "problem" as the universal starting object, then the broader architecture should probably treat **problem-driven inquiry and opportunity-driven inquiry as sibling modes** rather than forcing one into the other.
