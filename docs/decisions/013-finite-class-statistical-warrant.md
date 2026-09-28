# ADR 013 — Statistical warrant records a finite-class uniform-convergence bound

## Status

Accepted for the current research architecture.

## Context

The project already distinguishes graded support from epistemic acceptance. Statistical learning introduces a different kind of guarantee: a theorem-level bound connecting empirical loss to population loss under explicit sampling and hypothesis-class assumptions.

For a finite hypothesis class \(\mathcal H\), bounded loss in \([0,1]\), and an i.i.d. sample of size \(m\), Hoeffding's inequality plus a union bound gives:

\[
P\left(
\exists h\in\mathcal H:
|L_D(h)-L_S(h)|>\epsilon
\right)
\le
2|\mathcal H|e^{-2m\epsilon^2}.
\]

Equivalently, with probability at least \(1-\delta\):

\[
L_D(h)
\le
L_S(h)
+
\sqrt{
\frac{\log(2|\mathcal H|/\delta)}{2m}
}
\]

simultaneously for all \(h\in\mathcal H\).

## Decision

Add an executable finite-class uniform-convergence certificate.

It records:

- selected hypothesis ID;
- finite hypothesis-class size;
- sample size;
- empirical loss;
- confidence parameter \(\delta\).

The certificate deterministically computes:

\[
\epsilon=
\sqrt{
\frac{\log(2|\mathcal H|/\delta)}{2m}
}
\]

and:

\[
U=
\min(1,L_S(h)+\epsilon).
\]

The corresponding warrant regime may license only:

\[
\operatorname{recordGeneralizationBound}(h).
\]

Its guarantee is the finite-class uniform-convergence theorem conditional on the explicit sampling/loss assumptions.

## Required applicability assumptions

The executable theorem calculation does not establish that the empirical sample actually satisfies the statistical assumptions.

The warrant therefore keeps conditions such as:

- i.i.d. sampling from the target distribution;
- loss bounded in \([0,1]\);
- declared finite hypothesis-class size;
- no unmodelled train/deployment distribution shift;

as explicit applicability assumptions/context rather than hiding them inside the numeric bound.

## What the regime does not license

It does **not** by itself license:

- accepting a proposition;
- deploying/using the predictor;
- claiming the sampling assumptions are true;
- treating empirical error as population error;
- applying the theorem after data-dependent hypothesis-class changes that violate the declared setup.

A stronger action such as use-predictor requires a separate decision/warrant regime with task/loss/risk semantics.

## Why this is different from the graded-support regime

The graded-support regime evaluates a symbolic support event under a probabilistic model.

The statistical regime certifies a **generalization theorem** from an empirical sample to population loss under sampling assumptions.

Therefore:

\[
\boxed{
\text{support probability}
\neq
\text{statistical generalization guarantee}.
}
\]

## Escalation

Use richer learning-theory certificates when benchmark cases require:

- infinite hypothesis classes and VC/Rademacher complexity;
- data-dependent model selection;
- dependent/non-i.i.d. data;
- distribution shift;
- PAC-Bayes;
- online learning/regret;
- calibration/conformal guarantees.

The generic warrant interface should remain unchanged.

## References

- Shalev-Shwartz & Ben-David, *Understanding Machine Learning*, finite-class uniform convergence.
- Standard Hoeffding + union-bound finite-class PAC derivations.

## Related documents

- [warrant-license-interface.md](../warrant-license-interface.md)
- [end-to-end-warrant-benchmark.md](../end-to-end-warrant-benchmark.md)
- [project-status.md](../project-status.md)
