# Reflective mutation-policy O2A donor remap

Status: hard-case semantic deletion test.

## Why this fixture

The reflective mutation-policy fixture is the strongest current O2A falsifier because one authentic historical episode contains:

- observation of the project's own methodology;
- analysis and a defeasible claim;
- competing belief;
- decision among alternatives;
- executed revision;
- transformation of the methodology;
- observed effect;
- feedback that revises the earlier methodology.

It therefore tests reflection, action, effect and feedback rather than only result-to-claim licensing.

## Observable contract to preserve

A donor replacement is adequate only if it preserves these task-relevant distinctions:

1. method-v1 and method-v2 remain distinct historical artifacts;
2. the external audit is evidence about method-v1, not method-v2;
3. the claim that v1 missed widening mutations is supported by the audit;
4. the competing "all shipped mutations pass, therefore method is adequate" view remains representable;
5. a decision selects the repair from alternatives for a stated objective;
6. the repair is an actually performed operation, not merely a proposed action;
7. the revision creates exact-set/widening tests while preserving earlier controls;
8. observed post-revision behavior is linked to the performed repair;
9. the observed effect can feed back on the earlier methodology without rewriting history;
10. the whole episode can be about the system's own prior methodology without requiring a special meta-level ontology.

## Donor remap

### Observation and analysis

PROV represents method-v1 as an Entity, the independent audit/classification as Activities using it, and the audit result as generated evidence. EVI can type the result as a scientific/evidential finding and preserve challenge/support structure.

Preserves contract items 1-3.

### Claim, competitor and entitlement

SACM/Assurance 2.0 can represent:
- the claim about the widening blind spot;
- audit evidence supporting it;
- assumptions/context;
- a competing/defeating adequacy claim;
- structured inference/evidence incorporation;
- claim standing and defeaters.

The current O2A LicenseRelation is not required as a separate universal relation for this case.

Preserves contract items 3-4, subject to a profile that records the audit purpose/scope.

### Decision

Practical-reasoning/decision frameworks can represent:
- objective: closed vocabularies stay closed under narrowing and widening mutations;
- alternatives: retain v1 or add exact-set/widening tests;
- chosen alternative: revise;
- supporting beliefs/claims and critical questions.

DecProv-O can record the retrospective decision event and its provenance.

Preserves contract item 5.

### Performed action and transformation

PROV already distinguishes an Activity from the Entity it uses/generates.

Represent:
- method-v1 as input Entity;
- repair execution as Activity;
- method-v2 as generated Entity;
- preserved/created/omitted content as a native patch/diff/transformation certificate or explicit change-set metadata.

DecProv-O can connect the prior decision to the performed repair Activity.

Preserves contract items 6-7 without an O2A ActionRelation/TransformationRelation pair as universal ontology types.

### Effect

The post-revision mutation run is another PROV Activity using method-v2 and generating an observation/result: six widening mutations added, harness 33→39, all killed.

This observed result is evidence concerning the expected consequence of the repair. EVI/SACM can connect it to the corresponding claim.

Preserves contract item 8 without a universal EffectRelation.

### Feedback / revision of prior methodology

Do not mutate the historical method-v1 claim or artifact.

Represent the later result as a new evidence/claim node that challenges/supersedes the earlier adequacy claim or supports the claim that v1 required revision. EVI challenge propagation and assurance defeaters provide the epistemic feedback semantics; PROV preserves temporal derivation.

The target of feedback is therefore an epistemic claim/model standing, not a magical mutable historical fact.

Preserves contract item 9.

### Reflection

PROV, EVI, SACM and practical reasoning do not require a separate type hierarchy when the subject happens to be the system's own methodology. method-v1 is simply the Entity/subject of the audit and decision.

Reflection is relational: the later process is about/uses/evaluates the earlier methodology.

Preserves contract item 10.

## Result

All ten declared observable requirements can be represented using the mature donor stack plus ordinary transformation/change-set metadata.

New universal O2A relation kinds demonstrated necessary by this hard fixture: **0**.

## What remains local or configuration-like

The following still need explicit project mappings/profiles, but do not currently justify universal ontology primitives:

1. purpose/scope profile connecting the audit evidence to the exact claim being evaluated;
2. mapping from decision framework output to DecProv-O retrospective decision record;
3. change-set/loss/preservation certificate for method-v1→method-v2;
4. mapping of EVI challenge/assurance defeater semantics to the project's chosen "revises" presentation;
5. authority/execution metadata if a future case requires distinguishing who was permitted to perform the action.

## Semantic-preservation qualification

This is not a claim of metaphysical or natural-language semantic identity.

The deletion claim is task-relative: for the ten observable requirements above, the donor federation can represent the distinctions and behavior the fixture uses.

A stronger claim of full equivalence between the entire O2A vocabulary and the donor standards has not been established.

## Consequence

The hard reflective/action/feedback fixture does not rescue the O2A ontology as a universal relation vocabulary.

Together with Email-Eu-core, the burden now lies on any remaining O2A construct to demonstrate a real behavior or distinction that cannot be represented by mature provenance, evidence/assurance, practical-reasoning/decision and native transformation machinery.

## Next decision point

Before another fixture-by-fixture remap, inspect the O2A relation inventory and identify only constructs not exercised by these two cases. Then decide whether any remaining construct is important enough to warrant one targeted falsifier. Avoid mechanically testing every fixture if the remaining constructs are already clearly donor-owned.
