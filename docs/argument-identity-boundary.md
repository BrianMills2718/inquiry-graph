# Argument identity boundary: support equivalence is not argument equivalence

> **Status:** architecture decision. This document stress-tests the current ABA argument identity before preference-sensitive defeat is added.

## 1. Question

The current ABA bridge identifies an argument by:

\[
(\text{conclusion},\text{minimal assumption environment}).
\]

Equivalently, distinct deductions with the same conclusion and the same minimal support environment collapse into one ABA argument.

That quotient is appropriate for the **positive support layer**:

\[
\lambda(h)\in\mathsf{Supp}(X),
\]

because the support algebra intentionally forgets proof multiplicity and retains only minimal assumption environments.

The open question is whether that same quotient is safe for the **structured argumentation layer**.

## 2. Literature constraint

The answer from established structured-argumentation theory is no.

ASPIC+ arguments are structured objects built recursively from premises and strict/defeasible rule applications. Attacks may target:

- an ordinary premise;
- the conclusion of a defeasible subargument;
- a particular defeasible inference step.

Preferences may also depend on argument structure, including last-link and weakest-link principles.

Therefore two arguments can have the same conclusion and the same ultimate support set while differing in:

- subarguments;
- rule applications;
- top/last defeasible rule;
- attackable locations;
- preference ordering.

ABA itself also defines deductions as finite trees; the support set is not the entire deduction object.

So:

\[
\boxed{
\text{support equivalence}
\neq
\text{argument identity}.
}
\]

## 3. Adversarial case A — same support, different last rule

Let \(a\) be one ordinary assumption.

Introduce two defeasible rule guards:

\[
g_1=\operatorname{applicable}(r_1),
\qquad
g_2=\operatorname{applicable}(r_2).
\]

Construct two derivations of \(h\).

### Argument A

\[
a,g_1\Rightarrow_{r_1} p
\]

then:

\[
p,g_2\Rightarrow_{r_2} h.
\]

### Argument B

\[
a,g_2\Rightarrow_{r_2} q
\]

then:

\[
q,g_1\Rightarrow_{r_1} h.
\]

Both arguments have:

\[
\operatorname{Conc}(A)
=
\operatorname{Conc}(B)
=
h
\]

and:

\[
\operatorname{Supp}(A)
=
\operatorname{Supp}(B)
=
\{a,g_1,g_2\}.
\]

The current quotient therefore identifies them.

But their last defeasible rules differ:

\[
\operatorname{LastDef}(A)=r_2,
\]

\[
\operatorname{LastDef}(B)=r_1.
\]

If:

\[
r_1\succ r_2,
\]

a last-link preference can rank the two arguments differently.

Therefore:

\[
\boxed{
(\text{conclusion},\text{support})
\text{ is insufficient for last-link preferences.}
}
\]

## 4. Adversarial case B — same support, different vulnerable subargument

Again let both final arguments conclude \(h\) from the same support environment.

One derivation contains a defeasible subargument concluding \(p\):

\[
A_p
\subset A_h.
\]

Another contains a defeasible subargument concluding \(q\):

\[
B_q
\subset B_h.
\]

Suppose a counterargument rebuts \(p\) but not \(q\).

Then the counterargument attacks \(A_h\) through \(A_p\), but it does not attack \(B_h\) through \(B_q\).

If the two final arguments have already been collapsed by conclusion/support, the system cannot express:

\[
\operatorname{Attack}(C,A_h)
\quad\text{and}\quad
\neg\operatorname{Attack}(C,B_h).
\]

It must either over-attack the collapsed argument, under-attack it, or reconstruct derivations after the fact.

All three are worse than preserving the structured argument identity.

## 5. Adversarial case C — same support, different undercut target

Two arguments may use the same set of rule-applicability assumptions but arrange them in different derivation structures.

An undercutter can target a particular rule application in one argument.

The support set records that the rule guard occurs somewhere, but not necessarily where it occurs, which subargument it governs, whether it is the top inference, or which conclusion depends immediately on it.

For structured explanation and preference semantics, those distinctions matter.

## 6. Decision

The current quotient is retained only for the **support summary**, not for structured argument identity.

Replace:

\[
\boxed{
A\equiv(\operatorname{conclusion},\operatorname{environment})
}
\]

with:

\[
\boxed{
A=(id,\operatorname{conclusion},D)
}
\]

where \(D\) is a first-class finite derivation structure.

Support is a projection:

\[
\operatorname{Supp}(A)
=
\operatorname{Leaves}_{\mathrm{assumption}}(D).
\]

The proposition-level ATMS-style label remains:

\[
\lambda(h)
=
\operatorname{Min}
\{
\operatorname{Supp}(A):
\operatorname{Conc}(A)=h
\}.
\]

Thus multiple structured arguments may project to the same member of \(\lambda(h)\).

## 7. Minimal derivation representation

Use a hash-consed derivation DAG rather than duplicating entire trees.

A derivation node is one of:

### Assumption leaf

\[
D=\operatorname{Assumption}(a)
\]

### Fact/axiom leaf

\[
D=\operatorname{Fact}(f)
\]

### Rule application

\[
D=
\operatorname{Apply}
(
r,
D_1,\ldots,D_n
).
\]

Each application retains:

- rule ID;
- rule type/origin metadata;
- child/subargument IDs;
- conclusion.

From this structure we can derive:

- minimal assumption support;
- all rules used;
- top/last rule;
- defeasible rules used;
- subarguments;
- attack locations;
- proof depth;
- ASPIC+-style last-link/weakest-link inputs.

## 8. Why a DAG, not merely a rule set

A set of used rules is still insufficient.

The adversarial last-link case can use the same rule set:

\[
\{r_1,r_2\}
\]

in both arguments while giving them different top rules.

Likewise attack location depends on parent/child structure.

Therefore:

\[
\boxed{
\text{rule set}
\neq
\text{derivation structure}.
}
\]

A DAG preserves structure while permitting shared subarguments.

## 9. What remains quotiented

We should still quotient away distinctions that are irrelevant to the selected semantics.

For example, two syntactically duplicated construction histories yielding isomorphic derivation DAGs need not be distinct arguments.

So argument identity should be based on a canonical structural representation:

\[
id(A)=
H(
\operatorname{canonicalize}(D)
).
\]

The exact canonicalization/hashing mechanism is an implementation issue; the semantic requirement is structural identity, not chronological construction occurrence.

## 10. Relationship to the positive support algebra

This change does **not** invalidate the antichain support algebra.

Instead it clarifies its role.

The support layer is a many-to-one projection:

\[
\boxed{
\text{structured arguments}
\longrightarrow
\text{minimal support environments}.
}
\]

Several arguments may have the same projection.

That is expected.

The antichain algebra remains the correct answer to:

> what minimal assumption environments support this conclusion?

It is not intended to answer:

> by which structured argument did the conclusion arise?

## 11. Relationship to MMT/formal representation

The distinction also matches the earlier formal-representation work.

A derivation/proof is a formal object, not merely a set of assumptions.

An MMT/LF-like substrate can therefore host or reference the derivation object, while the epistemic overlay records support environment, attack relations, warrant role, and acceptability status.

This is cleaner than reconstructing proof structure from epistemic support annotations.

## 12. Effect on ABA-first decision

The ABA-first architecture remains valid, but the executable ABA bridge needs one correction before preference semantics.

The correct layering is:

\[
\boxed{
\begin{array}{c}
\textbf{ABA deduction/derivation objects}\\
D
\\[4pt]
\downarrow
\\[4pt]
\textbf{support projection}\\
\operatorname{Supp}(D)
\\[4pt]
\downarrow
\\[4pt]
\textbf{typed attacks on structured arguments/subarguments}\\
\\[4pt]
\downarrow
\\[4pt]
\textbf{preference-sensitive defeat}\\
\\[4pt]
\downarrow
\\[4pt]
\textbf{Dung semantics}
\end{array}
}
\]

Do **not** add ABA+ preference semantics to the current collapsed argument identity.

## 13. Implementation sequence

The project sequence is now:

1. refactor the ABA argument object to preserve first-class derivation structure;
2. make positive support a derived projection;
3. add regression fixtures for the three adversarial identity cases;
4. adapt ABA attack construction and the Dung projection to structured argument IDs;
5. only then implement assumption preferences / ABA+ attack reversal;
6. benchmark whether ASPIC+-style last-link/weakest-link preferences require additional rule metadata.

This is a deliberate stop-the-line correction before another semantic layer is added.

## 14. Revisit criterion

The structural argument representation should be considered sufficient when it can distinguish all cases in which attack status, defeat status, preference ordering, or warrant/license status differs even when conclusion and minimal support environment are identical.

If two derivations differ structurally but none of those observable semantics can distinguish them, canonicalization may quotient them.

## 15. Bottom line

The boundary test produces a clear result:

\[
\boxed{
\textbf{first-class derivation structure is required.}
}
\]

But the consequence is **not** to abandon the positive support algebra or the ABA-first architecture.

It is to factor them correctly:

\[
\boxed{
\text{derivation structure}
\neq
\text{support projection}
\neq
\text{dialectical status}.
}
\]

That correction should be made before preference semantics are implemented.
