# Email-Eu-core O2A donor remap

Status: fixture-specific deletion test.

## Result

The Email-Eu-core fixture contains 16 O2A hyperedges. For this fixture, none requires a new universal O2A relation type.

The mature donor stack is:

- W3C PROV for entities, activities, use, generation, derivation and provenance.
- EVI for computations, findings/claims, scientific evidence and challenges.
- SACM and Assurance 2.0 for claims, evidence, structured inference, assumptions, unsupported/defeated states, evidence incorporation, substitution, defeaters and residual doubts.
- Carneades/practical reasoning for proof standards, premise types, goals, actions, consequences, values and critical questions.
- DecProv-O for retrospective decision provenance.
- Native mapping/transformation theories for preservation, loss and invertibility.

## Relation remap

| O2A edge | Donor representation | Disposition |
|---|---|---|
| h-observation | PROV Entity/Activity/Agent plus EVI/domain annotations | delete generic O2A relation |
| h-projection | PROV derivation/activity plus representation profile and mapping/lens certificate | retain profile metadata only |
| h-symmetrize | PROV Activity/Derivation plus native transformation loss/preservation certificate | retain typed transform profile only |
| h-analysis | PROV/EVI computation and generated result | delete |
| h-license-descriptive | Assurance 2.0 evidence incorporation/substitution plus SACM inference/context | delete generic license relation |
| four descriptive license conditions | SACM evidence/claims/context/assumptions and assurance premises | delete |
| h-claim-descriptive | EVI Claim/Finding plus SACM Claim/AssertedEvidence | delete |
| h-license-intervention | assurance argument with unsupported claim, defeaters and assumptions | delete generic license relation |
| h-cond-intervention-impact | EVI challenge / Assurance 2.0 defeater / SACM counter-evidence | delete |
| h-cond-resilience-correspondence | SACM needsSupport/assumption plus unresolved defeater/doubt | delete |
| h-claim-intervention | SACM Claim plus practical/policy argument claim | delete |
| h-belief | redundant in this fixture with claim/assurance status and provenance | delete from fixture |
| h-decision | practical reasoning prospectively; DecProv-O retrospectively | delete generic O2A relation |

## License deletion result

The strongest result concerns LicenseRelation.

Assurance 2.0 already treats evidence incorporation as the bridge from observation or measurement into a claim: the argument must justify why the evidence supports that claim. Its substitution steps can use an external theory to connect measured/model-level claims to useful higher-level claims.

SACM already represents claims, evidence, asserted inference/evidence, context, assumptions, needsSupport and defeated claims. Assurance 2.0 adds defeaters, residual doubts and argument validity/confidence.

Therefore this fixture does not justify local ownership of a generic LicenseRelation.

## Information that still matters

Claim reach remains useful as a claim/profile annotation controlling which warrant or argument regime applies.

World model and purpose remain important context/assumptions for relevance and applicability.

Consequence/stakes class is best treated as domain policy mapping stakes to an applicable proof/evidence standard. Carneades already supports issue-specific proof standards and burdens.

Projection/transformation loss remains important, but native mapping/lens/abstraction theories should own preservation semantics while PROV records derivation.

## Reconstructed fixture

PROV/EVI records dataset, graph transformations, NetworkX computation and finding.

SACM/Assurance records that integrity, rank, cross-department evidence and scope support the narrow descriptive claim.

The same assurance structure records removal counterevidence and unassessed resilience correspondence as defeaters/unsupported premises for the stronger intervention claim.

Practical reasoning uses the supported descriptive claim, objective, alternatives and uncertainty to choose further review/evidence collection.

DecProv-O can record the decision and any later action.

## Count

Hyperedges examined: 16.

New universal O2A relation kinds required by this fixture: 0.

Potential local integration metadata:
1. source-to-donor identifier mappings;
2. claim-reach profile;
3. domain stakes-to-proof-standard policy;
4. mapping preservation/loss certificate references;
5. optional cross-standard query/view.

## Limitation and next test

This fixture has no executed external action and does not exercise all O2A relation types. It does not establish universal deletion.

Next: remap the hardest authentic O2A fixture exercising stakes, reflection, feedback/challenge propagation, or action. Do not add schema machinery before that test.
