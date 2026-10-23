# NYC CRZ WP0/WP1 — capable baseline

Status: bounded neutral baseline over the frozen `NYC-CRZ-MVP-v1` artifacts. This is decision support, not a policy recommendation.

## Commission

### Decision-support question

After the frozen first operating year, what do the admitted public sources support, contradict, or leave unresolved about the program's stated expectations and recorded stakeholder concerns, and what should an accountable decision-maker retain, change, or monitor?

### Frozen baseline

Reuse only artifacts already accepted in the Mixed Methods Workbench history:

- verified agency source material;
- verified public-hearing source material;
- Brian's accepted source-bound prediction wording;
- Brian's accepted source-bound hearing-concern wording;
- Brian's accepted bounded quantitative comparison;
- frozen 2025 vehicle-entry snapshot and receipts.

Do not use post-freeze material in this baseline.

### Authority boundary

The baseline may:
- describe admitted evidence;
- compute/restate accepted descriptive arithmetic;
- identify agreement, difference, silence and unresolved questions;
- expose criteria and trade-offs.

The baseline may not:
- identify a causal policy effect;
- infer population prevalence from one hearing passage;
- reconstruct the agency's counterfactual independently;
- choose the policy for an accountable decision-maker.

## Accepted source-bound propositions

### Pre-implementation prediction

Accepted wording:

> Before implementation, the agency's Phase 1 table projected a 13.4% reduction in daily vehicles entering the Manhattan CBD relative to its No Action basis.

Status: source claim / pre-implementation prediction.

Not an observed result and not causal evidence.

### Medical-access concern

Accepted wording:

> One public-hearing passage raised added travel costs for vulnerable people accessing medical appointments.

Status: source-grounded stakeholder concern.

It establishes that the concern was raised in the admitted record. It does not establish prevalence, representativeness or burden magnitude.

### Quantitative observation/comparison

Accepted wording:

> Within the agency's No Action comparison frame, the frozen January–October arithmetic is approximately 11.39% below its baseline—about 2.01 percentage points below the 13.4% Phase 1 prediction.

Underlying accepted values:

- agency baseline entry events: 189,820,100;
- frozen observed entry events: 168,203,504;
- difference: 21,616,596 entry events;
- arithmetic difference from agency baseline: 11.3879%;
- difference from 13.4% prediction: 2.0121 percentage points.

Status: descriptive arithmetic inside an agency-derived comparison frame.

Not:
- an independently identified causal effect;
- unique-vehicle counts;
- a revenue calculation;
- an independently reconstructed counterfactual.

## Baseline synthesis

### What is supported

1. The admitted agency source contains a 13.4% Phase 1 daily-vehicle reduction prediction relative to its No Action basis.
2. The frozen public-data arithmetic shows fewer entry events than that agency baseline and in the same reduction direction.
3. The magnitude in the accepted January–October comparison is lower than the 13.4% prediction by about 2.01 percentage points.
4. The admitted hearing evidence establishes that at least one speaker raised a concern about added medical-access travel costs for vulnerable people.
5. Exact source/version differences matter: the public data snapshot and publication-time observations differ slightly and remain separate evidence versions.

### What is not established

1. The causal effect of the policy on vehicle entries.
2. Whether the agency-derived No Action baseline is the correct real-world counterfactual.
3. Whether the medical-access concern was common, representative, large in magnitude, or realized after implementation.
4. Net social benefit or harm.
5. A preferred policy option.
6. A comprehensive qualitative account across all six hearings, because the planned method-owned QC artifact is not accepted/complete.

## Trade-off / criteria surface

No aggregate score or hidden weighting is applied.

| Criterion | Baseline evidence | Current standing | Missing before stronger use |
|---|---|---|---|
| Traffic reduction relative to agency frame | accepted 11.39% descriptive difference vs 13.4% prediction | observed arithmetic supports reduction direction; exact prediction not matched | defensible causal/counterfactual design for policy-effect claim |
| Medical-access burden | one accepted hearing passage | concern exists in record | prevalence, realized burden, affected-population magnitude, post-implementation evidence |
| Distribution/equity | bounded concern evidence only | unresolved | broader admitted evidence and explicit value/justice criteria |
| Program desirability | no accepted integrated appraisal | unresolved | explicit objectives/values, broader consequences, authority-owned weighting or decision rule |
| Evidence quality | exact source hashes, accepted review, frozen quantitative receipts | strong for source fidelity; limited for causal interpretation | method-owned qualitative completion; causal design if causal claims are needed |
| Revision readiness | versioned artifacts and stop rules already exist | good | dependency map showing which conclusions reopen after later evidence |

## Possible accountable-decision dispositions

These are decision-support categories, not recommendations:

- **retain** an existing policy feature where the decision-maker judges current evidence and values sufficient;
- **change** a feature where an identified concern plus additional evidence/values supports modification;
- **monitor / gather evidence** where a decision-relevant issue remains materially unresolved.

The baseline does not determine which category should apply to the whole program.

## Baseline refusal

A stronger statement such as:

> The program caused an 11.39% reduction and therefore should be retained unchanged.

is refused.

The first clause exceeds the current causal warrant; the second introduces policy values, alternatives and authority not supplied by the accepted baseline artifacts.

Likewise:

> Medical-access costs are a widespread adverse effect and therefore the program should be modified.

is refused because one hearing passage does not establish prevalence or post-implementation realized burden.

## Baseline architecture result

The capable baseline needed no universal O2A ontology.

It used:

- frozen artifact/source identity;
- human-reviewed source-bound claims;
- deterministic descriptive arithmetic;
- explicit claim limits;
- a human-readable criteria/trade-off table;
- explicit refusal.

This is the baseline the integrated path must materially improve.

## Known missing strand

The planned six-hearing qualitative Describe artifact is unfinished/unaccepted. Do not synthesize a fake substitute.

Its absence is itself a useful integration test: an honest system must carry `missing method-owned result` rather than converting pipeline incompleteness into a finding.

## Baseline pass/partial/fail snapshot

| Dimension | Baseline status | Reason |
|---|---|---|
| Evidence fidelity | pass | exact source custody/review exists for used claims |
| Semantic continuity | pass for used artifacts | source claim, concern, observation and causal limits remain distinct |
| Method fidelity | partial | quantitative slice is bounded; full qualitative method result absent |
| Warrant discipline | pass | causal/prevalence/recommendation overclaims explicitly refused |
| Decision transparency | partial | criteria can be shown, but no accepted integrated appraisal yet |
| Revision correctness | not yet tested | reserved for sealed update |
| Representation interoperability | partial | artifacts are manually joined; no need for universal IR demonstrated |
| Reconstruction | partial/pass | used artifacts trace well; missing qualitative strand limits whole-case reconstruction |
| Automation usefulness | partial | source binding and arithmetic are useful; integration remains manual |
| Total burden | baseline reference | integrated path must beat this rather than merely look more formal |
