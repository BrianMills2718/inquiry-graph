# ADR 017 — Use blackboard-style orchestration for heterogeneous candidate generators

## Status

Accepted for the current research architecture.

## Context

After mapping individual candidate-generation frameworks, the remaining question was how heterogeneous generators should interoperate when they have different internal representations, search procedures, evaluators, and control policies.

A landscape review found mature precedents for nearly every part of this problem:

- blackboard systems for shared state plus heterogeneous knowledge sources;
- blackboard control architectures for explicit next-action selection;
- multistrategy learning for task-adaptive integration of inference/learning methods;
- algorithm selection and portfolios for choosing among algorithms;
- hyper-heuristics for selecting or generating heuristics;
- algorithm configuration for tuning search/generator parameters;
- PRODIGY and Soar for integrated planning/learning and procedural knowledge generation;
- computational reflection for modifying reasoning machinery itself.

## Decision

Do not invent a new universal orchestration calculus.

Adopt the architectural pattern:

\[
\boxed{
\text{typed blackboard}
+
\text{generator/evaluator portfolio}
+
\text{explicit controller}
+
\text{reflective transformation}
+
\text{warrant}
}
\]

A project-level orchestration state may be written:

\[
\mathcal C
=
(
\mathbb B,
\mathcal K,
\mathcal P,
\Pi,
\mathcal M,
\mathfrak W
)
\]

where:

- \(\mathbb B\): typed shared blackboard/epistemic state;
- \(\mathcal K\): generators, evaluators and other knowledge sources;
- \(\mathcal P\): representation adapters/projections;
- \(\Pi\): controller / selection / hyper-heuristic policy;
- \(\mathcal M\): reflective transformations of generators, biases and control;
- \(\mathfrak W\): warrant regimes.

## Control

Invocation of a generator is itself an action:

\[
\operatorname{invokeGenerator}(g_i).
\]

Selection can be implemented by established approaches such as:

- blackboard control;
- Rice-style algorithm selection;
- portfolios;
- hyper-heuristics;
- metareasoning.

No one controller is made foundational.

## Operator and bias invention

Generating new operators or search heuristics should reuse:

- heuristic-generation hyper-heuristics;
- genetic programming;
- MIL/metarule learning;
- Soar/PRODIGY-style learned control knowledge.

Parameter tuning should reuse algorithm-configuration machinery such as SMAC-like methods.

## Representation adaptation

Generators may use different native languages.

Each component therefore requires an adapter:

\[
p_i:
\mathbb B
\rightleftarrows
L_i.
\]

When formal semantics are available, MMT/institution-style theory morphisms remain the preferred substrate for semantic translation.

## Warrant boundary

The unresolved cross-framework issue is not generic orchestration.

It is how guarantees survive translation and composition.

If:

\[
g_i:
x\mapsto y
\]

has native guarantee \(G_i\), and:

\[
p_i:
L_i\to\mathbb B,
\]

then the system needs to determine what guarantee:

\[
G_i'
\]

is justified after transport.

This is a warrant-transport problem, likely drawing on:

- institution satisfaction conditions;
- proof translation;
- refinement;
- abstract interpretation soundness;
- assume-guarantee contracts.

## Consequences

The project should not build a generic generator runtime merely to reproduce classical blackboard/portfolio functionality.

If a product implementation is pursued, begin with a small typed blackboard and a few heterogeneous generator adapters.

Candidate-generation foundational work should pause unless a concrete case exposes a failure in:

- adapter semantics;
- guarantee transport;
- provenance through composition;
- heterogeneous objective/control policies.

## Related documents

- [candidate-generation-cross-framework-glue.md](../candidate-generation-cross-framework-glue.md)
- [candidate-generation-framework-mappings.md](../candidate-generation-framework-mappings.md)
- [candidate-generation-landscape.md](../candidate-generation-landscape.md)
- [formal-epistemic-reasoning-metamodel.md](../formal-epistemic-reasoning-metamodel.md)
