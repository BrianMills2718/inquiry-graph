# ADR 015 — Candidate generation is a typed generative system with separate space transformation

## Status

Accepted for the current research architecture.

## Context

The original candidate-generation interface separated draft space, construction operators, strategy, elaboration, evaluation, and warrant.

A broader literature review shows that this separation has mature precedents in:

- Wiggins/Boden creative-system frameworks;
- program synthesis and CEGIS;
- ILP and Meta-Interpretive Learning;
- anti-unification;
- abductive logic programming;
- HR automated theory formation;
- conceptual blending / concept invention;
- Bayesian program learning.

The main gap in the earlier project interface was that representation-changing generation was only handled informally as an ordinary operator.

That obscures an important distinction between exploring a fixed generative space and transforming the generative system itself.

## Decision

Represent a candidate-generation regime as:

\[
\mathcal G_R
=
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

where:

- \(\mathcal A_R\): artifact ontology / candidate kinds;
- \(\mathcal L_R\): representation/generative language;
- \(\mathcal D_R\): draft/candidate states;
- \(B_R\): generative bias/admissibility constraints;
- \(\mathcal O_R\): construction/traversal operators;
- \(\to_R\): ordinary candidate transition relation;
- \(V_R\): evaluator family.

Strategy/control remains separate:

\[
\Pi_R:
\operatorname{Hist}(R,\mathcal G_R)
\to
\mathcal P(
\mathcal O_R
\cup
\{\operatorname{stop}\}
).
\]

Representation-changing or transformational moves are modeled separately:

\[
\mu:
\mathcal G_R
\rightharpoonup
\mathcal G'_R.
\]

A transformation may alter:

- artifact ontology;
- representation language;
- admissibility bias;
- operator vocabulary;
- evaluator family.

## Rationale

This imports rather than reinvents the key exploratory-versus-transformational distinction from computational creativity.

It also accommodates:

- predicate invention;
- theory extension;
- new abducibles;
- metarule generation;
- conceptual blending;
- operator invention;
- representation change.

without pretending these are merely ordinary candidate transitions.

## Consequences

The project no longer searches for a universal list of primitive candidate-generation operators.

Candidate-generation systems should be compared dimensionally:

\[
\text{artifact}
\times
\text{language}
\times
\text{bias}
\times
\text{transition}
\times
\text{evaluation}
\times
\text{control}.
\]

Specific mechanisms such as anti-unification, abduction, synthesis, blending, or predicate invention should be imported as domain-specific operator/regime families.

Generation provenance should be preserved rather than automatically quotiented by final candidate identity.

## Warrant boundary

A generator can itself receive a warrant for properties such as coverage, completeness, convergence, or search cost.

That is distinct from warranting the content of any candidate it generates:

\[
\boxed{
\text{generator warrant}
\neq
\text{candidate-content warrant}.
}
\]

## Next test

Map at least these mature frameworks into the revised interface:

1. program synthesis / CEGIS;
2. Meta-Interpretive Learning;
3. anti-unification;
4. HR automated theory formation;
5. conceptual blending.

Only add further coordinates if one of those mappings cannot be represented without distortion.

## Related documents

- [candidate-generation-landscape.md](../candidate-generation-landscape.md)
- [candidate-generation-interface.md](../candidate-generation-interface.md)
- [formal-epistemic-reasoning-metamodel.md](../formal-epistemic-reasoning-metamodel.md)
