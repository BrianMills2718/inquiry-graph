# Factgraph residual-niche pressure test — generic testing stack

> **Question:** After formal-verification tooling is preferred, does Factgraph still need custom machinery for opaque/black-box transformations?

## Mature testing stack already owns most of the loop

### Property-based testing

Hypothesis/QuickCheck-style tools already provide:

- generated inputs from declarative strategies;
- stateful/model-based action generation;
- shrinking/minimization of failing cases;
- replay of prior failures;
- targeted mutation/search.

Therefore Factgraph should not own a generic random generator, shrinker, state-machine test engine, or failure minimizer.

### Model-based testing

QuickCheck state-machine style testing already asks the user to supply:

- a model state;
- actions;
- preconditions;
- postconditions;
- a transition function;
- concrete execution semantics.

The framework generates action sequences, executes them, checks the model, and shrinks failures.

This is structurally very close to Factgraph's source-model → target-execution testing loop.

### Metamorphic testing

Metamorphic testing exists specifically for cases where a direct test oracle is difficult. Instead of predicting one exact output, the tester supplies relations that should hold across transformed inputs/outputs.

This is a mature black-box/gray-box answer to the oracle problem.

### Differential / compiler-style testing

Csmith and equivalence-modulo-inputs (EMI) are mature precedents for testing transformations/compilers without proving them. EMI was explicitly presented as applicable beyond compilers to program transformation and analysis systems.

Again, Factgraph does not own this idea.

## What generic tools cannot remove

The test-oracle literature makes the boundary explicit: automation can provide generation, execution, shrinking, metamorphic checks, model checking, etc., but some specification of **what counts as correct** must come from a model, contract, relation, reference implementation, or human/domain knowledge.

For our case the irreducible input is:

1. the **source semantic obligation**;
2. a semantics-preserving way to generate source-valid and/or source-invalid examples relevant to that obligation;
3. the **mapping/lowering** from source examples into the opaque target interface;
4. an observation predicate saying whether the target realized or rejected the semantic distinction.

That is domain adapter/specification work, not a generic testing framework.

## Pressure-test verdict

Factgraph's remaining niche collapses again.

It should **not** remain a custom testing platform.

The minimal residual is better described as:

> **semantic-oracle adapters for opaque transformations, executed by mature property/model/metamorphic/differential testing infrastructure.**

## What to replace

| Factgraph-like machinery | Better default |
|---|---|
| input generation | Hypothesis / QuickCheck / domain-native generators |
| shrinking/minimization | Hypothesis / QuickCheck shrinkers |
| stateful sequences | Hypothesis state machines / QuickCheck state machines |
| metamorphic relations | established metamorphic-testing frameworks/patterns |
| differential execution | generic differential-testing harnesses |
| mutation testing | mature mutation-testing tools / transformation-specific mutation frameworks |
| CI/replay | ordinary CI + test-framework example databases/artifacts |
| generic verdict plumbing | test framework + OntoCanon evidence record |

## What may remain local

A tiny semantic-audit profile could define:

```text
obligation_id
source_artifact/version
source_rule_ref
generator/oracle_adapter
mapping_artifact/version
target_executor
observation_predicate
evidence_policy
```

The actual generators can be Hypothesis strategies or calls into domain-native tooling.

The target executor can be PostgreSQL, a CLI, API, simulator, compiler, etc.

OntoCanon can retain the resulting evidence and provenance.

## Consequence for Factgraph

Three increasingly aggressive dispositions are now available:

### A. Keep
Keep Factgraph as a standalone product only if users demonstrably value a bundled semantic-audit workflow enough to justify custom integration.

### B. Extract
Move only the obligation/adapters/corpus into a small library or OntoCanon plugin and replace custom generation/testing machinery with Hypothesis/native tools.

### C. Archive
If there is no named consumer, archive Factgraph as:

- a research prototype;
- a benchmark/corpus of semantic-portability cases;
- donor examples for obligation schemas, witnesses and evidence vocabulary.

**Current external-first recommendation: B if a real consumer exists; otherwise C.**

## Why there is still some unavoidable local work

No off-the-shelf tool can infer arbitrary domain semantics from an opaque transformation. This is the classic test-oracle problem.

So the remaining work is not novel theory. It is unavoidable **specification/adaptation at the boundary**:

> tell mature testing machinery what source semantic distinction matters and how to observe it in this target.

That is the smallest residual 'yeast' I can justify.
