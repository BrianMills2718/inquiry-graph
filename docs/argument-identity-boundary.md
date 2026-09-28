# Argument identity boundary: when support-equivalence is enough

> **Status:** architecture decision. This note resolves whether the current ABA bridge must preserve full derivation trees before preference-sensitive defeat is added.

## 1. Question

The current ABA bridge identifies an argument by:

\[
(\text{conclusion},\text{minimal assumption environment}).
\]

Distinct deductions with the same conclusion and the same minimal support environment therefore collapse into one executable ABA argument.

That loses derivation-tree identity.

The question is whether this information loss is already unsound for the **next intended layer**, namely ABA/ABA+ assumption-based attack and preference handling.

## 2. Literature distinction

The literature separates two relevant semantics.

### ABA / ABA+

ABA defines derivability through finite deductions, but its attack semantics is assumption-centred.

A set of assumptions \(S\) attacks a set \(Q\) when some subset of \(S\) derives the contrary of an assumption in \(Q\).

Thus, for basic ABA attack semantics, a deduction matters extensionally through:

- what it concludes;
- which assumptions support it.

ABA+ adds preferences **over assumptions** and incorporates those preferences into the attack relation, including attack reversal.

It does not require ASPIC+-style last-link comparison of derivation trees.

### ASPIC+

ASPIC+ treats arguments as recursively structured objects.

Its attacks may target:

- ordinary premises;
- conclusions of defeasible subarguments;
- particular defeasible inference steps.

Its argument preferences can depend on internal rule structure, including last-link and weakest-link principles.

Therefore ASPIC+ can distinguish arguments that ABA/ABA+ deliberately treats extensionally.

## 3. The key equivalence

For the semantics currently selected by the project, define:

\[
A\sim_{\mathrm{ABA}} B
\]

when:

\[
\operatorname{Conc}(A)=\operatorname{Conc}(B)
\]

and:

\[
\operatorname{Asm}(A)=\operatorname{Asm}(B).
\]

Under basic ABA, such arguments:

- attack exactly the same assumption sets, because their conclusions are identical;
- are attacked by exactly the same contrary derivations, because their supporting assumption sets are identical.

So they are behaviorally equivalent with respect to ABA attack.

For ABA+ preference handling, preferences are over assumptions. If \(A\) and \(B\) have the same assumption support, they also present the same preference-relevant assumption information.

Therefore:

\[
\boxed{
A\sim_{\mathrm{ABA}}B
\Rightarrow
\text{same ABA/ABA+ dialectical behavior}
}
\]

for the current intended semantics.

This makes the current quotient principled rather than accidental.

## 4. What about defeasible rules?

The project compiles a defeasible rule:

\[
p_1,\ldots,p_n\Rightarrow_r q
\]

to a strict ABA rule guarded by a generated applicability assumption:

\[
q\leftarrow
p_1,\ldots,p_n,\alpha_r,
\]

where:

\[
\alpha_r=\operatorname{applicable}(r).
\]

The generated assumption retains:

- source rule \(r\);
- role = rule applicability;
- attack origin = undercut.

So use of a defeasible rule is visible in the ABA support environment through \(\alpha_r\).

A preference over such a rule can, when desired, be represented initially as a preference over its generated applicability assumption.

This remains within the ABA/ABA+ design rather than requiring argument-tree identity.

## 5. Stress case: same support and conclusion, different proof trees

Suppose two finite deductions produce:

\[
h
\]

from the same assumptions:

\[
\{a,b\}.
\]

One deduction passes through intermediate \(p\); another through intermediate \(q\).

If all attackable defeasible commitments are represented as assumptions/guards, then under the selected ABA semantics:

- both arguments attack the same targets if they conclude the same contrary;
- both are vulnerable to attacks on the same supporting assumptions;
- ABA+ compares the same assumption set.

The internal difference between \(p\) and \(q\) has no effect on the selected dialectical semantics.

Preserving both proof trees would therefore add representation detail without changing current observable behavior.

## 6. Where the quotient would become unsound

The quotient stops being sufficient if the project adopts a semantics in which two derivations with the same conclusion/support can behave differently.

Concrete triggers include:

### ASPIC+ subargument attack

A counterargument attacks an intermediate defeasible conclusion present in one derivation but not another.

### ASPIC+ inference-step attack not represented by a guard

An undercutter targets a particular rule application whose identity cannot be recovered from the assumption environment.

### Last-link preference

Two arguments with the same ultimate assumptions are ranked differently because their top/last defeasible rules differ.

### Proof-sensitive warrant

A warrant regime treats different derivations of the same conclusion from the same assumptions differently—for example because one uses a certified proof object and another uses a heuristic transformation.

### Explanation requirements

A user needs the exact proof/derivation tree rather than only the minimal assumption basis.

Those are explicit escalation conditions.

## 7. Decision

Do **not** refactor the ABA core to first-class derivation DAGs now.

Keep:

\[
\boxed{
\text{ABA argument identity}
=
(\text{conclusion},\text{minimal assumption environment})
}
\]

for the executable ABA/ABA+ bridge.

Treat this as a declared **semantic quotient**, not as a claim that deductions themselves lack internal structure.

The full formal-representation layer may still store derivation/proof objects independently when available.

## 8. Correct layering

The architecture is:

\[
\boxed{
\begin{array}{c}
\textbf{formal derivation objects, when needed}\\
D
\\[4pt]
\downarrow\;\text{projection}
\\[4pt]
\textbf{ABA dialectical quotient}\\
(\operatorname{conclusion},\operatorname{assumption\ support})
\\[4pt]
\downarrow
\\[4pt]
\textbf{ABA / ABA+ attack and preference semantics}\\
\\[4pt]
\downarrow
\\[4pt]
\textbf{Dung acceptability}
\end{array}
}
\]

This preserves the distinction:

\[
\boxed{
\text{derivation identity}
\neq
\text{dialectical argument identity}.
}
\]

The project currently needs the latter for the ABA bridge.

## 9. Relationship to the support algebra

The support antichain remains:

\[
\lambda(h)
=
\operatorname{Min}
\{
\Gamma:
\Gamma\vdash h
\}.
\]

The ABA argument layer selects individual pairs:

\[
(h,\Gamma)
\]

from this relation.

Several proof trees can map to the same pair.

That many-to-one map is acceptable under ABA/ABA+ semantics.

## 10. Relationship to MMT/LF

This resolves an apparent conflict with the earlier formal-representation work.

MMT/LF-like machinery may distinguish proof objects:

\[
d_1\neq d_2
\]

even when:

\[
\operatorname{Conc}(d_1)=
\operatorname{Conc}(d_2)
\]

and:

\[
\operatorname{Asm}(d_1)=
\operatorname{Asm}(d_2).
\]

The epistemic/argumentation overlay is allowed to quotient those proof objects when the selected semantics cannot distinguish them.

So:

\[
\boxed{
\text{formal artifact identity}
\neq
\text{epistemic quotient identity}.
}
\]

This is a feature of the layered architecture, not a contradiction.

## 11. Project-management consequence

The earlier plan to stop preference work and immediately reify derivation DAGs is **rejected**.

It would solve a richer ASPIC+-level problem before the project has evidence that the richer semantics is needed.

The sequence is now:

1. retain the current ABA quotient;
2. implement/test ABA+ assumption preferences;
3. preserve source-rule and attack-origin metadata on generated assumptions;
4. use concrete warrant cases to test whether the escalation conditions occur;
5. only then add first-class derivation/subargument structure if required.

This keeps the project on the shortest path to the foundational warrant problem.

## 12. Regression requirement

The quotient must remain explicit and testable.

Add/retain fixtures showing that:

- two distinct Horn derivation routes with the same conclusion and support collapse to one ABA argument;
- attacks depend on conclusion + supporting assumptions, not hidden derivation history;
- generated rule-applicability assumptions prevent relevant defeasible-rule information from disappearing.

If a later semantics makes one of those collapsed routes behave differently, that fixture becomes the signal to refine argument identity.

## 13. Bottom line

The boundary has been addressed.

The result is **not** “we need proof trees now.”

It is:

\[
\boxed{
\textbf{the current quotient is sufficient for ABA/ABA+,}
}
\]

while:

\[
\boxed{
\textbf{first-class derivation structure is an explicit escalation path for ASPIC+-level semantics or proof-sensitive warrant.}
}
\]

That is the current architecture decision.
