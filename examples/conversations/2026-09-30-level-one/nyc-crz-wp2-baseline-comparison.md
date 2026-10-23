# NYC CRZ WP2 — minimal federated baseline vs capable baseline

## Question

Does explicit federation across mature provenance, assurance/claim-standing and policy-appraisal concepts materially improve the capable baseline?

## Minimal federation used

Only three shared ideas were needed:

1. **W3C PROV-style derivation/version links** for source, computation and revision lineage.
2. **SACM/Assurance-style claim standing** for the distinction between supported descriptive claims and stronger claims that still need support.
3. **Mature policy-appraisal criteria structure** for keeping evidence, criteria, values and accountable decision authority separate.

EVI was not required for this baseline because no deep evidence/challenge propagation is exercised yet. A universal O2A vocabulary was not required.

The authoritative evidence and computations remain in their native Workbench artifacts.

## Comparison

| Dimension | Capable baseline | Minimal federation | Delta |
|---|---|---|---|
| Evidence fidelity | pass | pass | no material improvement; native hashes/review already did this |
| Semantic continuity | pass for used artifacts | pass+ | modest improvement: support/refusal dependencies are explicit rather than only prose |
| Method fidelity | partial | partial | no change; NYC-QC-1 is still missing and federation cannot manufacture it |
| Warrant discipline | pass | pass+ | modest improvement: causal/prevalence/policy-choice overclaims are machine-visible `needsSupport` states |
| Decision transparency | partial | partial+ | criteria/value/authority boundary becomes explicit, but no completed appraisal exists |
| Revision correctness | not tested | ready to test | dependency links make selective reopening possible; actual value depends on WP4 |
| Representation interoperability | partial | pass for this slice | native artifacts are linked without normalization into one IR |
| Reconstruction | partial/pass | pass | clearer chain from evidence → claim standing → criteria/decision boundary |
| Automation usefulness | partial | partial+ | dependency-aware refusal/reopening is automatable; no method inference added |
| Total burden | reference | acceptable only if kept thin | full standards stack would be overkill; thin profile is low-cost |

## Key result

The integrated path **does improve reconstruction, explicit warrant/refusal state and revision readiness**, but it does not improve the actual evidence or method validity.

Therefore the useful integration layer is small:

```text
native artifact identity/provenance
        +
claim-support / needs-support edges
        +
decision-criteria / authority references
        +
dependency links for revision
```

It does not justify:
- a universal epistemic ontology;
- importing every donor vocabulary into every artifact;
- a universal workflow engine;
- a universal representation IR.

## What earned existence

Only one cross-cutting capability clearly earns a trial from this baseline:

> **dependency-aware cross-artifact reconstruction and selective reopening**

That can be implemented initially as a view/index over native artifacts, not a new semantic authority.

## What did not earn existence

- generic O2A relation vocabulary;
- a new evidence graph engine;
- a new warrant calculus;
- universal confidence scoring;
- automatic decision ranking;
- generic method orchestration.

## Gate before retention

The thin federation only survives if WP4 shows that the sealed update can reopen the correct claims/criteria while leaving unrelated baseline artifacts intact.

If the same result is easy to achieve with ordinary human-readable dependency notes, even this thin integration layer should remain optional.
