# ADR 012 — Measurement and testimony warrant only model-relative recording actions

## Status

Accepted for the current research architecture.

## Context

Measurement and testimony are both evidence channels, but neither should be treated as a primitive truth oracle.

Metrology distinguishes a measurement result from the underlying measurand and treats uncertainty/calibration as part of the measurement model and traceability story.

Formal testimony models likewise represent source reliability through explicit probabilistic assumptions; reliability is not a context-free property of a source independent of task/reference class.

The project therefore needs executable reliability cases without collapsing them into proposition acceptance.

## Decision

Add two narrow warrant regimes.

### Measurement-result regime

A measurement certificate contains:

- measured quantity;
- numeric value;
- standard uncertainty;
- unit;
- calibration reference;
- optional measurement-model reference.

The regime may warrant only:

\[
\operatorname{recordMeasurementResult}(q,v,u).
\]

Its guarantee is that the recorded result carries explicit uncertainty and calibration provenance.

It does **not** warrant accepting a proposition such as:

\[
q=v
\]

without an additional interpretation/decision regime.

### Testimony-posterior regime

A testimonial reliability model is explicitly relative to a source and reference class.

For a positive report it records:

\[
P(R^+\mid H)
\]

and:

\[
P(R^+\mid\neg H).
\]

Together with an explicit prior:

\[
P(H),
\]

the certificate computes:

\[
P(H\mid R^+)
=
\frac{P(R^+\mid H)P(H)}
{P(R^+\mid H)P(H)+P(R^+\mid\neg H)P(\neg H)}.
\]

The regime may warrant only recording that posterior under the declared model.

It does **not** warrant accepting the claim or treating the source as globally reliable across reference classes.

## Rationale

This preserves:

\[
\boxed{
\text{measurement/report}
\neq
\text{truth}
}
\]

and:

\[
\boxed{
\text{model-relative reliability estimate}
\neq
\text{unconditional epistemic license}.
}
\]

It also keeps reliability/reference-class assumptions explicit rather than hiding them inside a scalar confidence attached to a claim.

## Consequences

The warrant interface now has executable examples for:

- defeasible grounded acceptability;
- graded support reporting;
- checked deduction;
- measurement result recording;
- testimony posterior recording.

Stronger actions require separate regimes.

## Escalation

Measurement should gain richer models when benchmark cases require:

- correlated uncertainty components;
- nonlinear measurement models;
- calibration hierarchies;
- traceability chains;
- conformity assessment.

Testimony should gain richer models when benchmark cases require:

- multiple dependent sources;
- learning source reliability from past reports;
- adversarial/deceptive source models;
- reference-class uncertainty;
- source dependence;
- testimony combined with non-testimonial evidence.

Those should extend the certificate/model layer rather than changing the generic warrant judgment.

## References

- JCGM GUM / VIM metrology guidance.
- Bovens & Hartmann, Bayesian Epistemology, chapters on reliability and testimony.
- Merdes, von Sydow & Hahn, “Formal models of source reliability.”

## Related documents

- [warrant-license-interface.md](../warrant-license-interface.md)
- [end-to-end-warrant-benchmark.md](../end-to-end-warrant-benchmark.md)
- [project-status.md](../project-status.md)
