# First end-to-end policy-analysis case — NYC Congestion Relief Zone

Status: selected research case and evaluation rubric. This is a neutral decision-support exercise, not an endorsement of a policy choice.

## Why this case

Use the existing Mixed Methods Workbench NYC Congestion Relief Zone (CRZ) corpus rather than creating a new topic or data pipeline.

Reasons:

- it is already the Workbench's stable MVP example;
- exact source bytes and hashes already exist;
- source-bound structured extraction already exists;
- a frozen quantitative first-year vehicle-entry slice already exists;
- human-review boundaries and claim limits already exist;
- the current Workbench roadmap already names NYC-QC-1 -> NYC-INTEGRATE-1 -> NYC-MVP-REVIEW-1 as the unfinished integration path;
- it is a real policy setting with heterogeneous evidence, affected interests, quantitative observations, uncertainty, and later updates;
- therefore the test pressure is on integration, semantic continuity and revision, not on building a new method or acquiring a new corpus.

Mist Trail remains useful as a bounded policy-appraisal donor/fixture, but should not be the primary case because that appraisal slice already exists.

## Bounded decision-support question

> After the frozen first operating year, what do the admitted public sources support, contradict, or leave unresolved about the program's stated expectations and recorded stakeholder concerns, and how do alternative explicit decision criteria change the trade-offs that an accountable decision-maker would need to consider?

The analysis does **not** choose the policy for the decision-maker.

## Starting corpus

Reuse the existing frozen NYC evidence package and current Workbench artifacts, including:

- exact verified agency source documents;
- exact hearing-source material already admitted;
- source-bound prediction and concern candidates;
- accepted human dispositions already recorded in the Workbench history;
- frozen 2025 vehicle-entry data and its existing deterministic aggregate/comparison artifacts.

Do not reacquire or silently replace frozen baseline sources merely because newer material exists.

## Baseline workflow

### WP0 — commission

Record:

- user/decision-maker role: accountable policy analyst/decision support consumer;
- question and frozen baseline date;
- authorized source corpus;
- affected-interest categories represented in admitted sources;
- decision criteria to be exposed, not silently weighted;
- hard constraints and claim limits;
- output: inspectable evidence/trade-off/revision packet;
- one sealed later update.

### WP1 — capable baseline

Using competent ordinary tools and mature methods, produce the best neutral analysis possible from the frozen corpus **without requiring O2A or a new universal schema**.

Required outputs:

1. source inventory and exact provenance;
2. claims/predictions/concerns actually present in sources;
3. quantitative descriptive results already justified by the frozen data;
4. explicit separation of descriptive observations from causal/policy-effect claims;
5. option/adjustment space only where it is source-grounded or explicitly framed as hypothetical;
6. criteria/trade-off table with no hidden aggregate score;
7. unresolved evidence and questions;
8. decision-support summary with no automated policy choice.

### WP2 — governed evidence and semantic continuity

Use existing owners where they materially help:

- OntoCanon for governed source/assertion identity if needed;
- Workbench/QC for source-bound qualitative material;
- native tabular tooling for quantitative observations;
- PROV/RO-style lineage for derivations;
- EVI/SACM/Assurance-style structures if claim/evidence/warrant joins need explicit representation;
- mature decision-analysis/EtD/MCDA concepts for criteria and trade-offs.

Do not introduce O2A relations merely to make the chain look complete.

### WP3 — policy analysis

Keep at least these distinctions explicit:

- evidence vs values/preferences;
- observation vs causal attribution;
- source claim vs analyst inference;
- descriptive/predictive/counterfactual reach;
- measured consequence vs affected-interest judgment;
- uncertainty vs disagreement;
- option consequences vs criteria/values;
- recommendation/advice vs accountable decision authority.

No universal confidence score or hidden weighted ranking is required.

### WP4 — sealed update and revision

Before the baseline analysis is run, pin one later primary-source update and withhold it from the baseline.

The update must materially change at least one of:

- evidence;
- program circumstances;
- a stakeholder concern;
- an official evaluation/measurement;
- an applicable constraint or policy condition.

After revealing it, the system must identify:

1. which artifacts remain valid unchanged;
2. which claims require reappraisal;
3. which assumptions/conditions changed;
4. which trade-offs change or do not change;
5. what new evidence remains missing.

No silent overwrite of the baseline analysis.

## Evaluation rubric

Score each dimension as **pass / partial / fail**, with evidence. Do not collapse to one overall numeric score.

### 1. Evidence fidelity

Pass when every material factual/source claim can be traced to exact admitted evidence or a clearly identified computation.

Failure examples:
- invented source support;
- stale source silently substituted;
- model-generated statement presented as source fact.

### 2. Semantic continuity

Pass when material changes in framing, construct meaning, scope, unit, representation, assumptions and claim reach remain visible across stages.

Failure examples:
- a stakeholder concern becomes a measured effect;
- a descriptive trend becomes a causal effect without new warrant;
- a representation change silently drops a decision-relevant distinction.

### 3. Method fidelity

Pass when each analytical method retains its native assumptions, inputs, refusal states and permissible conclusions.

Failure examples:
- generic workflow status substitutes for method validity;
- quantitative association is promoted to causal attribution;
- qualitative concern frequency becomes population prevalence.

### 4. Warrant discipline

Pass when stronger claims require stronger evidence/assumptions and unresolved conditions remain unresolved.

Failure examples:
- computation success automatically licenses a policy-effect claim;
- unsupported correspondence assumptions disappear;
- unassessed becomes satisfied.

### 5. Decision transparency

Pass when options, criteria, consequences, values, uncertainty and authority remain distinguishable.

Failure examples:
- hidden weighting;
- an analyst tool makes an accountable policy choice;
- evidence certainty is conflated with desirability.

### 6. Revision correctness

Pass when the sealed update changes only what it should and preserves historical versions.

Failure examples:
- baseline history rewritten;
- unrelated conclusions recomputed without dependency;
- affected claims fail to reopen after a changed premise.

### 7. Representation interoperability

Pass when table/text/graph/argument/decision artifacts can be traversed with identity and provenance intact without a universal IR.

Failure examples:
- conversion loses a material distinction without a loss record;
- native method semantics are flattened for transport.

### 8. Reconstruction

Pass when another analyst can reconstruct:
- what was known;
- what was inferred;
- what remained uncertain;
- what criteria were applied;
- why the analysis changed after the update.

### 9. Automation usefulness

Pass when automation reduces real analyst effort without hiding review or authority boundaries.

Measure:
- repeated manual reconstruction avoided;
- exact evidence reopening;
- bounded recomputation;
- useful refusal/insufficiency outputs.

### 10. Total burden

Pass only if the integrated path is materially better than the capable baseline after accounting for:
- implementation;
- maintenance;
- ontology/schema burden;
- adapter cost;
- analyst cognitive burden.

A technically elegant system that costs more to maintain than the baseline fails.

## Comparison design

Run two conditions over the same frozen case:

### A. Capable baseline

Use ordinary mature tools and human-readable artifacts. No special cross-standard integration layer unless already available off the shelf.

### B. Governed/integrated path

Use only already-owned/adopted infrastructure plus the smallest adapters necessary to preserve identity, lineage and task-relevant semantics.

Compare A vs B on the ten rubric dimensions.

## Architecture admission rule

A new shared concept/interface is admitted only if:

1. the baseline exposes a concrete failure;
2. existing standards/tools cannot represent the required distinction adequately;
3. the integrated path fixes the failure;
4. the distinction matters to at least one evaluation dimension;
5. maintenance cost is justified;
6. preferably a second materially different case later needs the same behavior.

## Stop condition

If mature tools plus narrow adapters can complete the case with good evidence fidelity, semantic continuity, revision and reconstruction, stop.

Do **not** build:
- a universal policy ontology;
- a universal analytical IR;
- a universal workflow engine;
- a new warrant calculus;
- a new decision theory;
- a new provenance model.

The case exists to discover a missing join, not to justify one in advance.
