# Factgraph keep / borrow / delete decision — 2026-09-30

> **Rule:** assume a better mature version exists until a concrete comparison proves otherwise.
> **Scope:** Factgraph's role in the representation-interoperability program, not a product endorsement.

## Bottom line

Factgraph should **not** become the program's mapping theory, transformation language, schema language, model repository, or universal semantic authority.

Its useful local role is much narrower:

> **evidence-oriented audit harness around mappings owned by other formalisms/tools.**

Even that role should be treated as provisional because model-transformation property preservation is already a mature research/tooling field.

A 2025 systematic review covers 202 studies from 2000–2024 and identifies mature families including formal verification, theorem proving/model checking, static analysis, transformation-rule verification, system/regression testing, test generation and mutation testing.

## Keep

Keep only capabilities that provide local empirical evidence and are cheap to replace.

| Factgraph capability | Why keep locally | Boundary |
|---|---|---|
| explicit source semantic obligation IDs/readings | ties evidence to what was actually claimed | consume imported/native semantics; don't make Factgraph authoring authority |
| explicit semantic→physical mapping trace | useful audit provenance | mapping semantics belong to CQL/QVT/DOL/etc. or explicit external adapter |
| discriminating valid/invalid populations | useful executable evidence technique | not a proof of general property preservation |
| real-target execution | distinguishes predicted preservation from observed backend behavior | use mature test/data-contract engines where equivalent |
| evidence levels: declared / structural / witness / live | excellent anti-overclaim discipline | generic evidence vocabulary, not new transformation theory |
| explicit loss/unknown statuses | prevents false equivalence | align to formalism-specific preservation claims |
| mutation controls | checks that the auditor notices deliberately weakened mappings | standard testing technique, not project novelty |
| provenance pinning of source/tool/target versions | necessary for reproducibility | integrate with OntoCanon custody |

## Borrow, don't own

| Current/local capability | Better-established owner |
|---|---|
| conceptual/fact modeling | ORM/Factum, LinkML, domain modeling standards/tools |
| schema/model transformation | CQL/schema mappings, QVT/ATL/Epsilon, DOL/Hets as appropriate |
| property-preservation theory | model-transformation verification literature; formal methods |
| target schema/data conformance tests | Data Contract CLI/ODCS, dbt, native DB validation, SHACL/etc. |
| model validation | OCL/EVL/SHACL/native validators depending metamodel |
| model repository/versioning | Git, EMF/CDO, registry infrastructure |
| schema migration safety | Atlas, DB-native migration ecosystems, U-Schema/Orion research |
| interchange formats | LinkML/Ossie/ODM/DOL/native standards |
| n-ary semantic database target | TypeDB and domain-native stores |
| registry/catalog | ISO 11179/MFI-aligned OntoCanon registry |

Current examples of mature operational tooling:
- Data Contract CLI imports/exports many schema formats and runs real schema/quality checks across many backends.
- LinkML publishes a generator compliance dashboard derived from actual compliance tests.
- TypeDB directly enforces typed relation/role/cardinality/value constraints.

## Delete / freeze as active direction

Do not invest further in Factgraph as:

1. a general modeling language;
2. a universal intermediate representation;
3. a universal metamodel;
4. a generic model repository;
5. a general migration platform;
6. a generic transformation engine;
7. a broad compiler generating more targets;
8. a replacement for data-contract/schema-validation tooling;
9. a source of new universal property-preservation theory.

Factgraph's own strategic rereview already reached much of this conclusion.

## Hypergraph Schema IR versus Factgraph

### Hypergraph Schema IR

Disposition: **historical donor**.

Useful artifacts: compact n-ary/role-aware schema representation; explicit round-trip loss reports; bounded self-generated reverse readers; four-valued constraint verdict (holds / violated / unevaluated / not applicable).

Do not revive it.

### Factgraph

Disposition: **active donor / possible thin audit harness**.

It adds semantic obligations as first-class audit units, explicit transformation traces, generated discriminating witnesses, mutation testing, real external pipeline audits, a live-observation boundary, and provenance-locked external artifacts.

This is materially more useful, but it is still mostly **integration/test engineering over mature theory**, not a new foundational layer.

## Strongest local idea worth retaining

native source semantic obligation
+ native/external mapping artifact
+ target artifact/system
→ formal/structural preservation claim
+ discriminating executable witness where appropriate
→ observed evidence
→ typed preservation/loss record

That could become an **optional validation adapter** attached to an OntoCanon mapping record.

It should not become mandatory for mappings with stronger formal certificates. A DOL/Hets satisfaction-preserving theorem or CQL functorial law should retain its formal certificate directly; a database mapping without a suitable proof may benefit from Factgraph-style executable falsification.

## Integration boundary

### OntoCanon owns
- mapping artifact registration;
- exact source/target/version identity;
- provenance and authority;
- certificate/evidence references;
- preservation/loss claim records;
- audit status/history.

### Native mapping formalism/tool owns
- mapping semantics;
- composition semantics;
- formal preservation theorem;
- transformation execution.

### Factgraph-like auditor may own
- testable obligation extraction for supported domains;
- counterexample/witness generation;
- target execution;
- empirical falsification evidence.

It must **never upgrade empirical evidence into a stronger formal guarantee than the mapping regime supports**.

## Practical disposition

**Keep Factgraph alive only if there is a named consumer for evidence-oriented mapping audit.**

Otherwise preserve it as research/reference, mine its witness/evidence/provenance patterns, and integrate mature external tools directly.

## Next test before adopting Factgraph

Pick one real mapping in the wider program that lacks a formal preservation certificate, has a meaningful executable target, and has a semantic obligation whose loss would matter.

Then compare Factgraph against Data Contract CLI/native target testing and an established transformation-verification tool appropriate to the mapping. Retain only functionality that materially improves the evidence.
