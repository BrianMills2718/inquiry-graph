# ADR 016 — Candidate-generation interface survives five-framework mapping

## Status

Accepted for the current research architecture.

## Context

ADR 015 refined candidate generation into a typed generative system:

\[
\mathcal G_R=
(
\mathcal A_R,
\mathcal L_R,
\mathcal D_R,
B_R,
\mathcal O_R,
\to_R,
V_R
)
\]

with strategy/control separate and with generative-system transformation:

\[
\mu:
\mathcal G_R
\rightharpoonup
\mathcal G'_R.
\]

The immediate test was whether this interface could represent mature frameworks without distortion.

The five selected stress tests were:

1. program synthesis / CEGIS;
2. Meta-Interpretive Learning;
3. anti-unification;
4. HR automated theory formation;
5. computational conceptual blending.

## Decision

The interface survives the five-framework mapping.

Do **not** add another top-level coordinate at this stage.

Use:

\[
\boxed{
E_G=(R,\mathcal G_R,d_0)
}
\]

for a concrete generation episode, keeping the reusable generative regime distinct from its episode-specific initial state and task context.

Interpret:

\[
\mathcal A_R
\]

as a typed artifact ontology rather than a single homogeneous candidate type.

Allow:

\[
d\in\mathcal D_R
\]

to be a structured candidate/dependency graph rather than one object.

## Important refinement

The exploratory/transformational distinction is representation-relative.

Generating a fresh predicate, concept or declaration is not automatically a generative-system transformation.

If the existing meta-language already permits such generated declarations, the move may be an ordinary transition:

\[
d\xrightarrow{o}d'.
\]

Use:

\[
\mu:
\mathcal G_R\to\mathcal G'_R
\]

only when the represented generative regime itself changes, such as changing:

- the generative language;
- artifact ontology;
- admissibility bias;
- operator vocabulary;
- evaluator family.

Thus:

\[
\boxed{
\text{new object-language symbol}
\not\Rightarrow
\text{new generative meta-language}.
}
\]

## Framework results

### CEGIS

Fits directly as candidate production plus verifier/counterexample feedback.

### Meta-Interpretive Learning

Fits and stress-tests vocabulary extension. Predicate invention may remain ordinary generation inside a sufficiently expressive meta-language.

### Anti-unification

Fits as a comparatively algebraic/canonical candidate-generation regime with minimal control requirements.

### HR

Fits but requires heterogeneous artifact kinds and graph-structured draft state because concepts, conjectures, proofs and countermodels interact.

### Conceptual blending

Fits with multiple input structures represented in episode state/bias rather than requiring a new coordinate.

## Warrant consequence

The mapping reinforces:

\[
\boxed{
\text{generator warrant}
\neq
\text{candidate-content warrant}.
}
\]

Generator-level warrants may concern:

- coverage;
- completeness;
- convergence;
- least-generality;
- termination;
- expected cost.

They do not establish the truth or acceptance of each generated candidate.

## Remaining frontier

The candidate-generation frontier is now narrowed to:

- equivalence of generative regimes;
- composition of generative regimes;
- composition/equivalence of transformations \(\mu\);
- operator invention;
- bias invention;
- semantics of substantive concept invention;
- generator-level warrant.

The project should not return to a search for universal primitive creativity operators.

## Related documents

- [candidate-generation-framework-mappings.md](../candidate-generation-framework-mappings.md)
- [candidate-generation-landscape.md](../candidate-generation-landscape.md)
- [candidate-generation-interface.md](../candidate-generation-interface.md)
- [formal-epistemic-reasoning-metamodel.md](../formal-epistemic-reasoning-metamodel.md)
