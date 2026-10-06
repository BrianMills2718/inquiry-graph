# Problem recognition landscape

Status: working synthesis, 2026-10-05.

Current question: how does an ideal/evaluative frame plus an observed state become a recognized problem that motivates candidate generation and action?

## Mature regimes

### Control / self-regulation
When the relevant variable and reference are already defined:

reference or desired state + observed state -> comparator -> discrepancy -> corrective action -> feedback.

This covers discrepancy reduction well, but assumes the frame is already given.

### Model-based diagnosis
Expected behavior is generated from a model and compared with observation. A mismatch motivates candidate diagnoses and discriminating tests. An anomaly is not itself a diagnosis.

### Problem structuring / Soft OR
For wicked or ill-structured situations, the problem is not pre-given. Problem Structuring Methods and Soft Systems approaches make stakeholder perspectives, boundaries, values, uncertainty, and alternative formulations part of the inquiry.

### Design framing
Schön/Dorst-style framing treats reframing as changing how an observed situation, an aspired value, and possible working principles are connected. Reframing can therefore change the candidate solution space.

### Entrepreneurship
Opportunity-recognition traditions treat some opportunities as discoverable; opportunity-creation/effectuation traditions emphasize acting under uncertainty in ways that can change what becomes feasible.

## Working factorization

```text
ideal / value / reference
        +
observed or estimated state
        ↓
comparison / interpretation
        ↓
discrepancy, anomaly, tension, surprise, unmet value
        ↓
problem formulation
        ↓
explanation / diagnosis hypotheses
        ↓
candidate goals / strategies / experiments
        ↓
selection or reframing / generative-space transformation
        ↓
action
        ↓
feedback and revision
```

This is a workflow factorization, not a claim that every domain contains universal primitives with these names.

## Inquiry Graph implication

V1 already has questions, goals, hypotheses, methods, examples, challenges, reframes, tests, candidate_for, motivates, depends_on, and supersedes.

Do not add universal core node kinds such as Problem, Anomaly, Ideal, Diagnosis, or Opportunity yet.

Test the need across at least three different cases:
1. technical diagnosis;
2. contested organizational/wicked problem;
3. entrepreneurial opportunity under uncertainty.

Promote shared semantics only if the same missing distinction repeatedly changes a material query or downstream use.

Useful evaluation queries:
- Which observations or discrepancies motivated a problem formulation?
- Which frames were considered and superseded?
- Which diagnoses explain an anomaly and which tests discriminate them?
- Which candidate goals appeared only after reframing?
- Which actions changed the feasible/candidate space rather than moving within it?

## Current recommendation

Treat problem recognition as a family of related regimes:

```text
discrepancy detection
diagnosis
problem structuring / framing
opportunity recognition / creation
```

Let method-specific semantics remain with the mature method. Use Inquiry Graph to record the inquiry trajectory and let repeated representation failures determine whether a cross-regime abstraction is earned.


## First pressure test: organizational / ill-structured case

The first pressure test uses an earlier second-brain reasoning conversation. The case starts with weak progress / burnout-like symptoms but proceeds through alternative frames involving feedback and perceived control, problem definition and complexity, and identity conflict.

Result: the simple `desired state - current state = problem` model is underfactored for this case. The same observed condition supports multiple candidate problem frames, and those frames change what evidence, interventions, and success criteria become relevant.

Working refinement:

```text
observed condition
  -> interpreted discrepancy / tension
  -> candidate problem frames
  -> candidate diagnoses / explanations
  -> candidate interventions
  -> test / action / feedback
  -> reframe or revise
```

Inquiry Graph V1 can represent this with questions, hypotheses, moves, and existing relations, but a stable problem-frame object must currently be reconstructed. That is now a representation-gap candidate to test in the technical-diagnosis and entrepreneurial-opportunity cases; it is not yet a schema proposal.

See `docs/evaluation/problem-recognition-organizational-pressure-test.md`.


## Second pressure test: technical diagnosis

The AutoCoder validation-failure case provides a contrasting regime in which expected behavior is comparatively well specified. A real validator produced 0% validation success, and the historical investigation recorded candidate explanations including a mock-versus-real validator gap, stream-versus-RPC architecture mismatch, and wrong component abstractions.

Result: here the anomaly is relatively stable before diagnosis begins.

```text
expected behavior + observation
  -> anomaly / conflict
  -> candidate diagnoses
  -> locate failure level
  -> candidate repair
  -> test
  -> revise
```

Inquiry Graph V1 represents this more comfortably than the organizational case. The semantics of anomaly detection and diagnosis appear naturally method-specific; no universal Anomaly or Diagnosis node kind is currently warranted.

The cross-case distinction is now sharper:

- organizational / ill-structured inquiry may need **candidate problem frames before diagnosis**;
- technical diagnosis can often begin from a relatively stable anomaly and search over explanations.

See `docs/evaluation/problem-recognition-technical-pressure-test.md`.


## Third pressure test: entrepreneurial opportunity

The archived paid-engagement capability loop supplies a case that can begin without a failure signal. Its natural starting point is an aspiration plus available means under uncertainty; bounded engagements both deliver value and generate evidence that can change future capability and feasibility.

Result: this case falsifies **Problem as the mandatory root of goal-directed inquiry**.

A more general cross-case entry role is a salient condition: problem, anomaly, question, aspiration, opportunity, surprise, or similar trigger. That role is not proposed as a new ontology primitive.

Across all three cases, the stronger candidate abstraction is a higher-order reasoning episode that connects:

```text
salient condition
  -> framing
  -> candidate generation
  -> evaluation / selection
  -> action / experiment
  -> feedback / revision
```

Whether that deserves a core record, a profile, or merely a projection remains an empirical/query question.

See:
- `docs/evaluation/problem-recognition-entrepreneurial-pressure-test.md`
- `docs/design/problem-recognition-three-case-synthesis.md`
