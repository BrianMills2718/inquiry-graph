# Prior-art audit — integrated observation → evidence → warrant → decision → action

> **Question:** Has a mature framework already solved the broader problem of composing heterogeneous observation/analysis workflows with claims/evidence, epistemic entitlement, belief/update, decisions and actions?
> **Posture:** delete local machinery wherever a mature owner exists.

## Bottom line

**No single mature general-purpose framework was found that owns the entire chain.**

But the chain is far more covered by mature work than the current local architecture suggests. The best current picture is a **federation of established standards/frameworks with a small number of explicit joins**, not a new universal metamodel.

```text
observations / computations
    ↓
PROV / Research Objects / FAIRSCAPE
    ↓
EVI / Micropublications / Nanopublications / AIF
    ↓
SACM / GSN / Assurance 2.0 / structured argumentation
    ↓
practical reasoning / GRADE EtD / domain decision frameworks
    ↓
DecProv-O / PROV-AGENT / action provenance
```

Different regimes can substitute for individual layers. The important design rule is not to flatten their semantics.

## 1. Observation, computation and derivation — solved

### W3C PROV

PROV-O is the standard lightweight provenance backbone for entities, activities, agents, derivation, use and generation, and is explicitly intended for specialization across domains.

Disposition: **adopt; do not duplicate provenance semantics.**

### Research Objects / RO-Crate / CWLProv

Research Objects aggregate data, methods, workflow definitions, execution provenance and annotations. The older RO model now recommends RO-Crate for new users; CWLProv packages workflow-run provenance using PROV.

Disposition: **adopt/profile where packaging/reproducibility is needed.**

### FAIRSCAPE

FAIRSCAPE is the strongest direct precedent found for the scientific half of the problem. It creates a machine-interpretable Evidence Graph for each computational result, linking data, software, computations and findings with persistent identifiers. Evidence graphs can be consumed and extended across transformations/workflows.

Disposition: **major donor/adoption candidate; re-evaluate O→A/DIGIMON against it before building scientific evidence lineage.**

## 2. Result → scientific claim/evidence — substantially solved

### EVI Evidence Graph Ontology

EVI extends PROV to model how scientific results are produced and what evidence bears on their correctness. It treats findings as defeasible assertions, supports evidence/challenge graphs and propagation of challenges deep through support structure.

This is substantially closer to O→A's result→claim/evidence join than generic PROV.

Disposition: **adopt/align; delete local evidence-graph machinery that EVI already supplies.**

### Micropublications

Micropublications model claims, data, methods, evidence, arguments, support, challenge and disagreement. Their maximal form is a claim plus its full supporting argument/evidence structure.

Disposition: **strong donor for scientific claim/evidence semantics; do not reinvent scientific argument metadata.**

### Nanopublications

Useful minimal assertion + provenance + publication-info packaging, but intentionally thinner than Micropublications/EVI for rich evidence/challenge structures.

Disposition: **use when minimal citable assertions are appropriate.**

### Argument Interchange Format

AIF provides an interlingua for structured arguments across tools/formalisms, with information nodes and applications of inference/conflict/preference schemes.

Disposition: **adopt/interoperate where generic argument interchange is required.**

## 3. Claim → entitlement/confidence — substantially solved, regime-specific

### SACM / GSN

SACM is the OMG standard for assurance-case argument/evidence exchange; GSN structures claims, strategies, assumptions, contexts and evidence.

Disposition: **adopt for assurance-style structured claims; do not recreate generic claim/evidence argument structure.**

### Assurance 2.0

Provides defeaters, dialectical examination, residual doubts and confidence assessment over structured assurance arguments.

Disposition: **adopt where assurance-style warrant/confidence fits.**

### EVI + structured argumentation

EVI already propagates challenges through evidence graphs. AIF/Carneades/ASPIC+-style frameworks own many defeasible argument structures.

Disposition: **prefer adapters to new challenge/support calculi.**

## 4. Evidence → policy decision — mature, but not universal

### GRADE Evidence-to-Decision

GRADE EtD is a mature, widely used framework for moving from evidence to recommendations/decisions in health/public-health domains. It explicitly separates certainty of evidence from the broader decision criteria: effects, values, resources, equity, acceptability and feasibility.

Disposition: **adopt as a domain-specific reference implementation of evidence→decision reasoning, not as a universal policy ontology.**

### Practical reasoning / computational argumentation

Walton and Atkinson/Bench-Capon provide mature schemes for action-oriented reasoning from circumstances, actions, consequences, goals and values, with critical questions. Carneades 4 includes practical reasoning and multi-criteria decision analysis.

Disposition: **major prior art for the general claim→action argument join; do not invent a generic practical-reasoning scheme.**

### Policy argument literature

National Academies and evidence-informed-policy research explicitly treat science as one input to situated practical/policy argument alongside values, legitimacy, trade-offs and political considerations.

Disposition: **preserve the scientific-conclusion / policy-decision boundary; do not define science as mechanically entailing policy.**

## 5. Scientific evidence → policy argument — unusually close precedent

The 2020 paper *Enhancing COVID-19 decision making by creating an assurance case for epidemiological models* explicitly separates:

1. scientific evidence;
2. scientific conclusions;
3. policy decisions;
4. scientific argument linking evidence to conclusions;
5. policy argument linking conclusions to decisions;
6. confidence argument about evidence/model trustworthiness.

This is extremely close to the high-level O→A architecture and shows that assurance-case machinery has already been applied to the evidence→policy boundary.

Disposition: **treat as a primary architecture donor; compare O→A's joins against it before claiming gaps.**

## 6. Decision → retrospective action lineage — substantially solved

### DecProv-O

DecProv-O specializes PROV to record decisions as causes of actions/use/generation. It explicitly limits itself to decisions already made, not normative future scenarios.

Disposition: **adopt/align for retrospective decision provenance.**

### PROV-AGENT

Extends PROV to connect prompts, responses, agent decisions and downstream workflow effects.

Disposition: **adopt where agentic execution provenance is needed.**

## 7. What is *not* solved by one framework

The search did not find a mature general-purpose standard that simultaneously provides:

- heterogeneous scientific computation/representation semantics;
- evidence/claim support and challenge;
- regime-specific typed warrant guarantees;
- policy/practical reasoning with goals/values/trade-offs;
- prospective decision/action entitlement;
- retrospective decision/action provenance;
- all with one universal composition law.

That absence should **not** be interpreted as permission to invent such a universal formalism. The mature fields deliberately have different semantics.

## 8. What local work may actually remain

The residual problem is narrower:

> **typed interoperability among mature epistemic/decision regimes.**

A local join should exist only when a concrete end-to-end use case needs information to cross a boundary and no existing standard already defines the mapping.

Candidate joins to re-audit:

1. computational result / EVI finding → assurance/practical-reasoning claim;
2. assurance/scientific conclusion → practical/policy argument;
3. policy argument → decision record;
4. decision record → action execution/provenance;
5. preservation of assumptions, scope, claim reach and guarantee type across those joins.

Even these may collapse further under targeted prior-art review.

## 9. Implications for existing repos

### Epistemic Warrant

Keep as a **meta-interface/research synthesis** only where it adds cross-regime typing that the native regimes do not provide. Do not duplicate the internal mathematics of logic, statistics, assurance, argumentation, practical reasoning or decision theory.

### Observation-to-Action

Shrink aggressively:

- PROV/RO/FAIRSCAPE own computation/provenance;
- EVI/Micropublications own much scientific evidence/claim structure;
- SACM/GSN/Assurance 2.0 own assurance argument structure;
- practical reasoning/GRADE own major parts of evidence→decision reasoning;
- DecProv-O/PROV-AGENT own retrospective decision/action provenance.

O→A should retain only joins proven necessary by real cases after direct mappings to these donors.

### OntoCanon

Registry/custody of exact artifacts, profiles, mappings and certificates remains plausible; it should reference these standards rather than absorb their semantics.

## 10. Strongest current architecture hypothesis

Not:

```text
one universal epistemic/action ontology
```

but:

```text
federated native regimes
      +
standard provenance/evidence/argument/decision representations
      +
small typed mappings at demonstrated joins
      +
explicit preservation/loss/warrant transport
```

## 11. Next deletion tests

Before any new O→A schema work:

1. map the existing Email-Eu-core O→A fixture into **PROV + EVI + SACM/GSN + DecProv-O** and count what remains local;
2. map one genuine policy case using **scientific assurance argument + practical reasoning/GRADE-like decision criteria**;
3. search specifically for standards/ontologies covering each surviving join;
4. delete every O→A relation whose semantics are already supplied by the adopted framework.

## Current verdict

**The whole problem is not solved by one off-the-shelf system, but the components and many of the joins are mature.**

The likely contribution, if any, is not a new epistemology or workflow ontology. It is a very thin, typed federation/interoperability layer—and even that has not yet earned all of its current local constructs.
