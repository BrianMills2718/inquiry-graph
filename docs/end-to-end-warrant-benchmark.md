# End-to-end warrant benchmark

> **Status:** current integration benchmark. The purpose of this benchmark is to test whether the research layers compose, not to add more ontology.

## 1. Target pipeline

The architecture should support cases of the form:

\[
\boxed{
\text{support}
\to
\text{candidate/argument}
\to
\text{attack}
\to
\text{preference resolution}
\to
\text{defeat}
\to
\text{acceptability}
\to
\text{warrant}
\to
\text{license}
}
\]

while preserving the distinctions between those stages.

The benchmark intentionally asks:

> can the pieces compose without hidden category errors?

rather than:

> does the project already have a universal theory of rational belief?

## 2. First executable warrant regime

The first executable regime is:

\[
\mathfrak W_{\mathrm{grounded\text{-}dialectical}}.
\]

It is deliberately narrow.

A certificate argument must be grounded-IN under the current binary defeat graph.

The regime only warrants defeasible actions such as:

\[
\operatorname{retainCandidate}(h),
\]

\[
\operatorname{raiseSupport}(h),
\]

or:

\[
\operatorname{useDefeasibly}(h).
\]

Its guarantee kind is:

\[
G=
\text{defeasible acceptability under grounded semantics}.
\]

It does **not** license unconditional acceptance, deductive truth, or arbitrary epistemic actions merely because an argument is accepted.

## 3. Warrant versus license in the executable model

The executable distinction is:

### Conditional warrant

A warrant assessment asks whether the typed certificate is adequate under the selected regime:

\[
\mathfrak W;A\vdash_\pi a:G.
\]

For the first regime this requires:

- the action kind belongs to the regime;
- the guarantee kind belongs to the regime;
- certificate argument \(\pi\) is grounded-IN.

### License

A license additionally requires the current context to satisfy the applicability assumptions:

\[
C\models A.
\]

The first implementation uses exact set inclusion:

\[
A\subseteq C.
\]

That is an intentionally weak executable approximation to general context entailment.

Therefore:

\[
\boxed{
\text{conditionally warranted}
\not\Rightarrow
\text{currently licensed}.
}
\]

## 4. Executable vertical-slice cases

The current unit/integration suite contains the following end-to-end cases.

### E1 — unchallenged defeasible support

\[
e\Rightarrow h.
\]

No defeater exists.

Expected:

- support for \(h\) exists;
- certificate argument is grounded-IN;
- typed defeasible warrant succeeds;
- license to raise support for \(h\) is present.

### E2 — successful counterargument

\[
e\Rightarrow h,
\]

and:

\[
c\Rightarrow\overline e.
\]

Expected:

- positive support for \(h\) still exists as provenance;
- certificate is grounded-OUT;
- warrant is not adequate;
- no license is produced.

This tests:

\[
\text{support exists}
\neq
\text{warrant survives}.
\]

### E3 — preference blocks weaker counterargument

As in E2, but:

\[
c<e.
\]

Under the current binary normal-attack preference regime, the counterattack is blocked.

Expected:

- positive support graph is unchanged;
- defeat graph changes;
- certificate becomes grounded-IN;
- license is restored.

This tests:

\[
\text{preference change}
\to
\text{defeat change}
\to
\text{license change}
\]

without rewriting support provenance.

### E4 — applicability condition missing

The certificate is grounded-IN, but the warrant has an applicability assumption such as:

\[
\text{sensor-calibrated}.
\]

The current context lacks that assumption.

Expected:

- conditional warrant remains adequate;
- current license is absent.

This tests warrant/license separation.

### E5 — one of two support routes is defeated

Suppose:

\[
e_1\Rightarrow h
\]

and:

\[
e_2\Rightarrow h.
\]

A counterargument attacks only \(e_1\).

Expected:

- the \(e_1\)-certificate is grounded-OUT;
- the \(e_2\)-certificate remains grounded-IN;
- one warrant route fails;
- another can still license defeasible support for \(h\).

This tests preservation of alternative provenance rather than proposition-level all-or-nothing status.

### E6 — preference does not mutate positive support

Evaluate a preference-sensitive conflict before and after adding a strict assumption preference.

Expected:

\[
\lambda_{\mathrm{before}}(h)
=
\lambda_{\mathrm{after}}(h),
\]

while defeat/acceptability/license may differ.

This explicitly tests the factorization:

\[
\boxed{
\text{support provenance}
\neq
\text{dialectical status}.
}
\]

## 5. Additional warrant-unit cases

The warrant suite also checks:

- grounded-OUT certificate implies no warrant/license;
- grounded-UNDECIDED certificate implies no skeptical grounded warrant;
- grounded-IN certificate with unmet context assumptions implies warrant but no license;
- regime mismatch is rejected;
- missing certificate is rejected;
- grounded acceptability cannot license an out-of-scope unconditional-accept action;
- grounded acceptability cannot masquerade as a deductive guarantee.

The last two are important.

Without action/guarantee typing, an accepted argument could accidentally become a universal epistemic permission.

The implementation explicitly prevents that.

## 6. Benchmark matrix

| Case | Domain | Current status | Main invariant |
|---|---|---|---|
| D1 | deductive proof | executable in strict-Horn fragment | checked proof can license derive relative to premises, not premise acceptance |
| F1 | defeasible unchallenged | executable | accepted certificate can license defeasible support |
| F2 | defeasible defeated | executable | support may remain while warrant fails |
| F3 | preference-sensitive defeat | executable | preferences change defeat, not support provenance |
| F4 | unresolved dialectical cycle | executable at warrant-unit level | skeptical grounded regime does not license undecided certificate |
| C1 | applicability assumptions | executable | warrant and current license differ |
| A1 | alternative support routes | executable | one defeated route need not erase another |
| G1 | graded/probabilistic support | executable for grade recording | computed support probability can license recording the grade, not accepting the proposition |
| S1 | statistical/PAC guarantee | executable finite-class bound | theorem-level population-loss bound remains conditional on i.i.d./bounded-loss setup |
| M1 | measurement/testimony | executable narrow regimes | measurement records uncertainty/calibration; testimony records model-relative posterior without acceptance |
| T1 | transition/action guarantee | formal interface only | pre/post guarantee distinct from proposition support |
| R1 | strategy selection | formal interface only | strategy performance warrant needs task/resource scope |
| W1 | warrant-of-warrant | representable, not closed | assumptions/checkers may themselves become warrant targets |

## 7. What this benchmark tells us

The project now has one complete vertical slice:

\[
\boxed{
\text{minimal support}
\to
\text{ABA argument}
\to
\text{attack}
\to
\text{preference-filtered defeat}
\to
\text{grounded acceptability}
\to
\text{typed defeasible warrant}
\to
\text{license}.
}
\]

That is enough to test whether the architecture composes.

It is **not** enough to claim that all epistemic warrant has been formalized.

## 8. Next benchmark expansions

The next additions should be selected because they exercise genuinely different guarantee types.

Priority order:

1. strategy-performance regime;
2. only then any decision policy that consumes graded support values.

Each new regime should instantiate the same action-targeted warrant interface rather than add a new top-level ontology.

## 9. Stop condition for foundational expansion

Do not add another major formal layer unless one of the benchmark cases cannot be represented without distortion.

The current research task is now:

\[
\boxed{
\text{expand benchmark coverage}
>
\text{expand ontology}.
}
\]

Failures in the benchmark should drive the next formal revision.


## 10. Executable graded-support case

The independent-Bernoulli support regime now supplies a second executable warrant specialization.

Given symbolic support \(P_h\) and an explicit independent-Bernoulli model \(M\), the certificate computes:

\[
\rho_M(P_h).
\]

The regime may warrant only:

\[
\operatorname{recordSupportGrade}(h,\rho_M(P_h)).
\]

It does not warrant:

\[
\operatorname{accept}(h)
\]

or:

\[
\operatorname{useForAction}(h).
\]

Even a value such as:

\[
0.99
\]

does not become an acceptance threshold by convention.

Any regime that consumes this value to license another action must state its own assumptions, decision rule and guarantee.

This is ADR 010.


## 11. Executable deductive case

The strict-Horn deductive regime supplies a checked proof fragment.

A certificate states:

\[
(\Gamma,R,h)
\]

where \(\Gamma\) is the explicit premise set, \(R\) is a finite set of strict Horn rules, and \(h\) is the conclusion.

The checker computes the least closure:

\[
\operatorname{Cl}_R(\Gamma).
\]

The certificate is valid iff:

\[
h\in\operatorname{Cl}_R(\Gamma).
\]

The warrant regime may license only:

\[
\operatorname{derive}(h)
\]

with guarantee:

\[
\text{truth preservation relative to the explicit premises}.
\]

A valid proof does not license accepting \(\Gamma\). If the current context omits a premise, the conditional warrant can remain valid while the current license is absent.

This is ADR 011.


## 12. Executable measurement case

A measurement certificate records:

\[
(q,v,u,\text{unit},\text{calibration reference},\text{model reference})
\]

where \(u\) is a non-negative standard uncertainty.

The measurement warrant regime may license only:

\[
\operatorname{recordMeasurementResult}(q).
\]

Its guarantee is that the recorded result carries explicit uncertainty and calibration provenance.

It does not warrant accepting an exact proposition such as:

\[
q=v.
\]

That stronger move would require a separate interpretation/conformity/decision regime.

## 13. Executable testimony case

A positive testimonial report is modeled through:

\[
P(R^+\mid H)
\]

and:

\[
P(R^+\mid\neg H)
\]

for an explicit source and reference class.

Given prior \(P(H)\), the certificate computes:

\[
P(H\mid R^+)
=
\frac{P(R^+\mid H)P(H)}
{P(R^+\mid H)P(H)+P(R^+\mid\neg H)P(\neg H)}.
\]

The testimony regime may warrant only recording this posterior under the declared source model.

It does not warrant:

\[
\operatorname{accept}(H).
\]

The source's reliability parameters are explicitly reference-class relative; the same source may have different reliability models in different domains.

This is ADR 012.
