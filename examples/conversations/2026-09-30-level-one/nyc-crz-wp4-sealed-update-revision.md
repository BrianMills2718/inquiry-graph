# NYC CRZ WP4 — sealed-update revision test

## Revealed update

Primary source:

- New York City Department of Health and Mental Hygiene
- *Air Quality Impacts of Congestion Relief Zone Tolling*
- published 2026-08-14
- selected and sealed before WP0/WP1 baseline analysis

The source describes a full-year air-quality evaluation using an interrupted-time-series design with a control site and adjustment for weather and longer-term/seasonal trends.

Its reported findings include:

- inside the CRZ, measured pollution decreased slightly or stayed the same in 2025 compared with 2024;
- the analysis reports no statistically significant pollution difference attributable to congestion pricing inside the CRZ;
- at the monitored environmental-justice neighborhood sites, it reports no overall increase in pollution attributable to congestion pricing;
- one BQE result showed one pollutant did not improve as much as expected relative to the control;
- the report itself makes a broader judgment that reduced congestion, transit improvements and mitigation investments demonstrate overall program benefit.

The last item is retained as a **source judgment**, not automatically adopted as this analysis's policy conclusion.

## Dependency-aware revision

| Baseline artifact / claim | Reopen? | WP4 result |
|---|---|---|
| Agency 13.4% vehicle-entry prediction | no | historical source claim unchanged |
| Frozen 11.39% descriptive vehicle-entry arithmetic | no | different outcome and evidence stream; remains unchanged |
| Claim that CRZ caused an 11.39% reduction in vehicle entries | no direct resolution | air-quality study does not establish the vehicle-entry causal estimand |
| One hearing passage raising medical-access costs | no | update does not address medical appointment travel-cost burden |
| Claim that medical-access burden is widespread/realized | no direct resolution | remains needsSupport |
| Missing six-hearing qualitative Describe | no | still missing; update cannot substitute for method-owned hearing synthesis |
| Air-quality / environmental-health criterion | **yes** | materially new evaluated evidence added |
| Distribution/equity criterion | **yes, partially** | new evidence concerning monitored EJ-neighborhood air quality; other equity dimensions remain open |
| Broad program desirability / policy choice | **yes as evidence context, not settled** | new favorable evidence enters the appraisal, but values, other consequences and accountable authority remain separate |

## New claims introduced by the update

### Source-reported air-quality evaluation result

> The NYC Health evaluation reports that pollution at monitored CRZ and environmental-justice sites was not significantly higher because of congestion pricing under its stated design, with a noted BQE-specific caveat.

Standing: **supported as a source-reported evaluation finding**.

This record does not independently reproduce or validate the full causal analysis.

### Stronger universal air-quality claim

> Congestion pricing caused no adverse air-quality effect anywhere in New York City.

Standing: **needsSupport**.

The published study has explicit monitored sites, pollutants, methods and scope. Do not widen that scope silently.

### Source policy judgment

> The program's documented benefits clearly demonstrate its overall benefit.

Standing here: **source judgment / decision-relevant input**, not the analysis's own recommendation.

It mixes empirical findings with a broader evaluative conclusion and therefore does not bypass the explicit criteria/value/authority boundary.

## Trade-off surface after update

| Criterion | Before update | After update |
|---|---|---|
| Traffic reduction | accepted descriptive reduction direction; causal effect unresolved | unchanged |
| Medical-access burden | one concern in admitted record; magnitude/prevalence unresolved | unchanged |
| Environmental health | insufficient in baseline | materially improved evidence: official full-year evaluation reports no significant attributable worsening at monitored sites |
| Distribution/equity | unresolved beyond bounded hearing concern | narrower uncertainty: monitored EJ-neighborhood air-quality harm is less supported; non-air-quality equity concerns remain unresolved |
| Evidence quality | strong custody, limited causal evidence in baseline | gains one methodologically richer official outcome evaluation |
| Net desirability | unresolved | still unresolved as an accountable decision; evidence mix changed, authority/value problem did not disappear |

## Revision correctness test

The thin federated dependency profile behaves correctly if it does all of the following:

1. adds a new source/evaluation artifact rather than overwriting the baseline;
2. opens the air-quality and distribution/equity appraisal nodes;
3. leaves the historical prediction and frozen traffic arithmetic unchanged;
4. leaves the medical-access claim unresolved;
5. leaves NYC-QC-1 missing;
6. distinguishes the Health Department's source-level overall-benefit judgment from an accountable policy decision;
7. preserves the study's scope and BQE caveat;
8. records that the stronger universal air-quality claim remains unsupported.

All eight conditions are satisfied by the explicit dependency mapping in this revision record.

## Result for the integration hypothesis

WP4 provides the first concrete evidence that the thin federation adds value:

> **selective reopening is easier and less error-prone when dependencies and claim-standing boundaries are explicit.**

But the useful capability remains narrow.

What earned further retention:
- cross-artifact dependency/index links;
- claim-standing/refusal state;
- immutable version/revision lineage.

What still did not earn a new ontology:
- universal O2A relations;
- universal evidence graph;
- universal policy-decision schema;
- universal method model.

## Current conclusion

For the NYC case, the smallest useful integration layer is best viewed as a **revision-aware index over native artifacts and mature donor semantics**.

It should answer:
- what changed?
- what claims/criteria depend on it?
- what remains valid?
- what must be re-warranted?
- what is still missing?

It should not become the authority for the underlying method, evidence, meaning or decision.
