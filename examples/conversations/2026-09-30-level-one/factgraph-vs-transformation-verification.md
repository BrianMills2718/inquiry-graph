# Factgraph vs transformation-verification tooling — pressure test

> **Question:** Is Factgraph's remaining niche—source-aware transformation-preservation auditing—already better covered by mature model-transformation verification/testing tools?

## Mature field result

A 2025 systematic review analyzed **202 studies** on model transformation/property preservation. It identifies established techniques including:

- formal verification;
- theorem proving / model checking;
- transformation-rule verification;
- static analysis;
- system testing;
- regression testing;
- test generation;
- mutation testing.

The review lists tools such as anATLyzer, Vitruvius, ProB, GROOVE, SPIN, eMoflon, DSLTrans/SyVOLT, VIATRA and others.

Sources:
- Journal of Systems and Software 230 (2025), 112508;
- ACM Computing Surveys, *Model Transformation Testing and Debugging: A Survey*.

## Strong external precedent: DSLTrans / SyVOLT

SyVOLT verifies structural pre/post-condition contracts on model transformations. The published method can:

- express transformation contracts;
- prove contracts exhaustively for the supported DSLTrans fragment;
- return counterexample input models when a contract fails.

A 2026 DSLTrans result adds a cutoff theorem and SMT/CEGAR workflow for a tractable fragment, reporting hundreds of proved properties and concrete counterexamples.

This is strictly stronger than finite Factgraph witnesses when the transformation can be represented in the supported formalism.

## Other external precedents

- OCL transformation contracts: source/target pre/post conditions over model transformations;
- USE/OCL: executable validation of model constraints and operation contracts;
- anATLyzer: static analysis of ATL transformations;
- graph-transformation/model-checking families: GROOVE, SPIN, ProB, VIATRA, eMoflon;
- mutation/model-transformation testing literature: established test-quality technique rather than Factgraph novelty.

## Where Factgraph loses

Factgraph should **not** claim to own:

1. transformation contract theory;
2. general property-preservation verification;
3. counterexample generation as a foundational idea;
4. mutation testing;
5. model-transformation testing methodology;
6. exhaustive preservation proof.

For transformations expressible in a mature formal verification stack, use that stack directly and register its proof/counterexample as the mapping certificate.

## Residual Factgraph niche

Factgraph still has a narrower engineering role when the real transformation is **not available as a formally modeled transformation**.

Examples:

- third-party generator CLI + opaque generated SQL;
- ORM pipeline whose mapping semantics are partly implicit in implementation;
- external schema artifact with an explicit hand-bound semantic-to-physical map;
- live database behavior that must be observed rather than inferred from transformation rules.

In those cases, Factgraph can act as **black-box/gray-box semantic differential testing**:

source obligation
→ discriminating source-valid/source-invalid populations
→ lower through an explicit mapping
→ execute the actual external artifact/system
→ observe whether the semantic distinction survives
→ retain provenance/evidence.

That is closer to model-based testing / differential testing / property-based testing than to model-transformation theory.

## Revised disposition

### Prefer formal verification when possible

If the transformation and property can be expressed in DOL/Hets, CQL, DSLTrans/SyVOLT, OCL/ATL verification, abstract interpretation, lenses, or another mature formalism:

**use the formalism; do not route through Factgraph.**

### Use Factgraph-like auditing only when necessary

Use an executable witness harness only when:

- the transformation is opaque or external;
- no adequate formal certificate exists;
- the target is executable;
- the semantic obligation can be operationalized into discriminating examples;
- live evidence would materially reduce uncertainty.

### Archive threshold

If general-purpose property/model-based testing tools plus OntoCanon provenance can express the external-pipeline cases with comparable effort and evidence quality, archive Factgraph as:

- research prototype;
- benchmark/corpus;
- donor of semantic-witness patterns.

## Architectural integration

OntoCanon mapping records should support **multiple certificate kinds**:

- formal proof/certificate;
- static transformation analysis;
- model checker result;
- test/witness evidence;
- live target observation;
- unresolved/unsupported.

Factgraph is then one optional producer of the last two kinds, not a required layer.

## Current verdict

Factgraph does **not** survive as unique transformation-preservation machinery.

Its only plausible retained role is a reusable harness for **opaque external transformations where formal verification is unavailable**.

That role should still be compared against generic model/property-based testing libraries before retaining custom code.
