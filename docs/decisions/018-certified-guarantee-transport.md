# ADR 018 — Transport guarantees only through certified preservation relations

## Status

Accepted for the current research architecture.

## Context

The candidate-generation integration work reduced the remaining cross-framework problem to:

> if a generator establishes a guarantee in its native representation and an adapter translates its output into another representation, what guarantee survives?

A literature review found mature frameworks for this problem:

- institution theory and institution morphisms/comorphisms;
- DOL and Hets heterogeneous proof management;
- MMT/LF theory morphisms;
- abstract interpretation;
- refinement / assume-guarantee / contract theories.

These frameworks differ in transport strength.

## Decision

Do not treat artifact translation as guarantee translation.

Represent each adapter with explicit typed preservation information.

For adapter \(\tau\), use a relation:

\[
\operatorname{Preserves}_\tau(G_S,G_T).
\]

A source guarantee may be transported only when a preservation theorem/certificate establishes the relevant relation.

Classify adapter transport strength as:

- **T0:** syntactic/opaque translation — no semantic warrant transport;
- **T1:** provenance/structural correspondence only — provenance survives, semantic guarantee does not;
- **T2:** sound one-way transport — source guarantee can justify a weaker target guarantee;
- **T3:** exact satisfaction/judgment preservation — institution/MMT-style semantic or proof transport;
- **T4:** compositional transport — preservation is also proven for the pipeline operations actually used.

The class is always relative to a guarantee family and required operations.

## Formal logical transport

For heterogeneous formal logics, prefer:

- institution morphisms/comorphisms;
- DOL/Hets logic graphs and heterogeneous proof calculus;
- MMT/LF theory morphisms.

These already supply satisfaction/theorem/judgment preservation machinery.

## Approximate transport

For abstractions and analyses, use established soundness/refinement machinery such as:

- abstract interpretation;
- simulation/refinement relations;
- contract theories.

The target guarantee may be weaker and transport may be one directional.

## Unverified transport

If an adapter lacks an adequate preservation certificate:

\[
\boxed{
\text{translate artifact/provenance only and re-warrant in the target regime}.
}
\]

An LLM or heuristic semantic translation is therefore not automatically a proof translation.

## Warrant composition

No new primitive transport judgment is required.

Transport can be represented as a warranted action using the existing schema.

If:

\[
\mathfrak W_S;A_S\vdash_{\pi_S}a_S:G_S
\]

and the adapter has a warrant/certificate:

\[
\mathfrak W_\tau;A_\tau
\vdash_\chi
\operatorname{transport}_\tau(G_S):G_T,
\]

then a target warrant may be composed only for the mapped action/assumptions/certificate components that the adapter defines.

Unmapped assumptions remain residual obligations.

## Typed assumptions

The transport problem demonstrates that warrant assumptions should be typed.

Some assumptions are formal/internal and can be translated along a theory morphism.

Others are external applicability conditions such as:

- i.i.d. sampling;
- calibration validity;
- source reference-class match;
- deployment-distribution stability.

Adapters may translate only a subset.

This refinement does not require a new top-level coordinate.

## Composition caution

A translation preserving one property does not necessarily preserve:

- composition;
- conjunction;
- hiding;
- quotient;
- refinement;
- other pipeline constructors.

Composition paths are therefore proof obligations, not merely graph reachability.

## Consequences

The project should treat Hets/DOL as a primary off-the-shelf precedent for formal heterogeneous proof/tool integration rather than designing a replacement.

MMT remains the preferred declarative theory/proof substrate.

The remaining project work is largely representational/engineering:

- record preservation certificates;
- select translation paths;
- preserve provenance;
- expose residual assumptions;
- re-warrant when preservation is unavailable.

## Related documents

- [warrant-guarantee-transport.md](../warrant-guarantee-transport.md)
- [candidate-generation-cross-framework-glue.md](../candidate-generation-cross-framework-glue.md)
- [warrant-license-interface.md](../warrant-license-interface.md)
- [formal-epistemic-reasoning-metamodel.md](../formal-epistemic-reasoning-metamodel.md)
