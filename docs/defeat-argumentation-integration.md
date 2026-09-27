# Defeat and argumentation integration

> **Status:** current integration note. This pass deliberately reuses established argumentation theory instead of inventing a negative-support algebra.

## 1. Decision

Keep the positive ATMS/minimal-support algebra unchanged.

Add a separate defeasible-argumentation layer:

\[
\boxed{
\text{positive support provenance}
+
\text{typed attack/defeat structure}
+
\text{acceptability semantics}
}
\]

The positive support layer answers which minimal environments support an argument.

The argumentation layer answers which supported arguments survive conflict.

These are different questions.

## 2. Why not signed support numbers

Pollock's rebutting/undercutting distinction and structured-argumentation frameworks show that defeat is not one scalar opposite of support.

A rebuttal attacks a conclusion.

An undercut attacks the inferential connection or rule application.

ASPIC+ additionally distinguishes undermining attacks on ordinary premises.

So negative information should not be encoded by assigning a negative coefficient to a positive-support expression.

## 3. ASPIC+ distinction

ASPIC+ distinguishes three structured attack locations:

\[
\boxed{
\{\text{rebut},\text{undercut},\text{undermine}\}
}
\]

- rebut: conflict with a conclusion of a defeasible inference;
- undercut: attack the defeasible inference itself;
- undermine: attack an ordinary premise.

ASPIC+ further distinguishes attack from defeat: preferences and attack type can determine whether an attack succeeds.

Therefore the current implementation does not infer a defeat merely from an attack-kind label.

## 4. ABA correspondence

Assumption-Based Argumentation is particularly close to the project's assumption/support layer.

In ABA, assumptions have explicit contraries, and a set of assumptions attacks another assumption/set when it derives the contrary of one of those assumptions.

That makes ABA a strong candidate for constructing some defeats directly from assumption environments.

But ABA's construction rules and ASPIC+'s attack-location taxonomy solve somewhat different representational problems.

The current architecture therefore imports the common boundary:

\[
\text{construct structured arguments/attacks}
\to
\text{resolve attacks to defeats}
\to
\text{apply abstract acceptability semantics}.
\]

## 5. Dung layer

Once successful defeats are known, project to a Dung-style abstract argumentation framework:

\[
AF=(Args,\operatorname{Defeat}).
\]

The first implemented semantics is grounded semantics.

For \(S\subseteq Args\), define:

\[
F(S)
=
\{
a:
\text{every defeater of }a
\text{ is defeated by some member of }S
\}.
\]

The grounded extension is the least fixed point:

\[
\boxed{
Gr=\operatorname{lfp}(F).
}
\]

Grounded semantics is a useful first implementation because it is unique and conservative.

It is not the only semantics. Preferred, stable, complete and other semantics remain available when the use case requires them.

## 6. Integration with positive support

Represent an argument schematically as:

\[
A_i=(id_i,P_i)
\]

where:

\[
P_i\in\mathsf{Supp}(X)
\]

is its positive support antichain.

Then:

\[
A_i \xrightarrow{\text{defeat:type}} A_j
\]

records a successful typed conflict.

The support algebra remains monotone:

\[
P_i
\]

does not disappear merely because \(A_i\) is defeated.

Instead, dialectical status is layered on top.

This preserves the distinction:

\[
\boxed{
\text{argument exists and has support}
\neq
\text{argument is currently acceptable}.
}
\]

## 7. Integration with warrant/license

A warrant certificate/support object can be represented by an argument \(A_\pi\).

The warrant layer should require the relevant certificate argument to satisfy the chosen acceptability condition.

Schematic refinement:

\[
\mathfrak W;A
\vdash_{\pi}
a:G
\]

plus:

\[
\operatorname{Acceptable}_\sigma(A_\pi)
\]

contributes to:

\[
\operatorname{Licensed}_{\mathfrak W,C}(a:G).
\]

Under grounded semantics:

\[
A_\pi\in Gr.
\]

This is cleaner than modifying the internal positive support expression whenever an attacker appears.

## 8. Attack construction is intentionally upstream

The checked-in module consumes successful defeats, not raw attacks.

The move from attack to defeat can depend on preference ordering, strict versus defeasible inference, contrary versus contradictory relation, source/rule priorities, or domain-specific admissibility rules.

ASPIC+ explicitly separates attack and defeat for this reason.

The module retains the originating type: rebut, undercut, undermine.

But it does not decide whether a raw attack succeeds.

## 9. Implementation

The experimental module src/inquiry_graph/defeat.py contains:

- Argument
- Defeat
- typed defeat kinds: rebut / undercut / undermine
- DefeatFramework
- Dung characteristic function
- grounded extension
- grounded IN / OUT / UNDECIDED status

Arguments carry the existing SupportAntichain.

This is intentionally separate from the source-grounded dialogue ontology.

## 10. Example

Let:

\[
A\to B
\]

mean \(A\) defeats \(B\).

For:

\[
c\to b,\qquad b\to a
\]

the grounded construction starts with unattacked \(c\).

Since \(c\) defeats the attacker \(b\) of \(a\), \(a\) is defended.

Thus:

\[
Gr=\{a,c\}.
\]

For mutual defeat:

\[
a\leftrightarrow b,
\]

neither argument is grounded-in:

\[
Gr=\varnothing,
\]

and both remain undecided.

## 11. Current architecture

The epistemic-support/warrant path is now:

\[
\boxed{
\begin{array}{c}
\textbf{positive support provenance}\\
\mathsf{Supp}(X)
\\[4pt]
\downarrow
\\[4pt]
\textbf{structured argument construction}\\
Args
\\[4pt]
\downarrow
\\[4pt]
\textbf{typed attacks}\\
\text{rebut / undercut / undermine / ABA contrary attacks}
\\[4pt]
\downarrow
\\[4pt]
\textbf{successful defeats}\\
Defeat
\\[4pt]
\downarrow
\\[4pt]
\textbf{acceptability semantics}\\
\sigma\;\text{(grounded first)}
\\[4pt]
\downarrow
\\[4pt]
\textbf{warrant/license}\\
\mathfrak W;A\vdash_\pi a:G
\end{array}
}
\]

This avoids recreating either argument construction or abstract acceptability theory.

## 12. What is not implemented yet

The current implementation deliberately stops before:

1. automatic ASPIC+ attack construction;
2. preference-sensitive attack-to-defeat resolution;
3. automatic ABA contrary/attack construction;
4. preferred/stable semantics;
5. collective attacks;
6. graded argument strength;
7. attacks on warrant regimes or meta-rules.

Those should be imported from established formalisms only as concrete use cases require them.

## 13. Next boundary

The positive-support and abstract-defeat layers are now both explicit.

The next useful question is not "what is negative support?"

It is:

\[
\boxed{
\text{which structured argument-construction formalism should instantiate attacks first?}
}
\]

Given the current ATMS-like assumption model, ABA is probably the smallest natural first bridge.

Given the need to distinguish rebuttal, undercutting, premise attacks, strict/defeasible rules, and preferences, ASPIC+ is the richer bridge.

The project should test both against concrete warrant examples before committing to one executable structured-argument formalism.
