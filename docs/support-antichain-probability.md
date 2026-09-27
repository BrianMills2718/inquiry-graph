# Minimal-support antichain algebra and a concrete probability regime

> **Status:** current research/result note. This document resolves the first concrete support-algebra choice requested by the project. It does **not** claim that this is the universal algebra for all kinds of epistemic support.

## 1. Decision

For **positive ATMS-style support provenance**, use the algebra of finite antichains of finite assumption sets.

Let \(X\) be the set of primitive assumption/support tokens. Define

\[
\mathsf{Supp}(X)
=
\operatorname{Antichain}(\mathcal P_{\mathrm{fin}}(X)).
\]

Each element is a finite set of pairwise-incomparable environments.

For arbitrary finite families of environments, define:

\[
\operatorname{Min}(S)
=
\{E\in S:\nexists E'\in S,\;E'\subsetneq E\}.
\]

Then:

\[
\boxed{
A\oplus B
=
\operatorname{Min}(A\cup B)
}
\]

represents **alternative support**, and

\[
\boxed{
A\otimes B
=
\operatorname{Min}
\{
E\cup F:
E\in A,\;F\in B
\}
}
\]

represents **joint support**.

Identities are:

\[
0=\varnothing
\]

and

\[
1=\{\varnothing\}.
\]

This exactly matches the ATMS practice of storing only minimal supporting environments.

## 2. Why this algebra rather than ordinary provenance polynomials

General provenance polynomials such as \(\mathbb N[X]\) preserve derivation multiplicity, repeated use of the same token, and distinct proof/derivation structure.

ATMS labels intentionally forget much of that.

If:

\[
\{a\}
\]

already supports \(h\), then the larger environment:

\[
\{a,b\}
\]

adds no new minimal support route and is absorbed.

Similarly, using assumption \(a\) twice does not create a distinct ATMS environment.

Therefore the relevant quotient laws include:

\[
x\oplus x=x,
\]

\[
x\otimes x=x,
\]

and absorption:

\[
x\oplus(x\otimes y)=x,
\]

\[
x\otimes(x\oplus y)=x.
\]

The resulting structure is the **free distributive lattice** over \(X\), viewed as an idempotent commutative semiring.

Equivalently, it is isomorphic to positive Boolean formulas over \(X\) modulo logical equivalence, represented in irredundant monotone DNF by their minimal satisfying environments.

This is much closer to ATMS label semantics than \(\mathbb N[X]\).

## 3. Relation to minimal witness provenance

Database-provenance literature independently arrives at the same construction for **minimal witness bases**:

\[
I+J=\operatorname{irr}(I\cup J)
\]

and

\[
I\cdot J
=
\operatorname{irr}
\{
i\cup j:
i\in I,\;j\in J
\}.
\]

That construction is identified with the free distributive lattice and with positive Boolean provenance.

So the project does not need to invent a new positive-support algebra here.

## 4. Relation to ATMS labels

An ATMS label such as

\[
\lambda(h)
=
\{
\{a,b\},
\{c\}
\}
\]

is represented directly as:

\[
P_h
=
(a\otimes b)\oplus c.
\]

Its semantics is the upward-closed set of assumption worlds:

\[
\llbracket P_h\rrbracket
=
\{
\omega\subseteq X:
\exists E\in\lambda(h),\;E\subseteq\omega
\}.
\]

Minimal environments are therefore a canonical antichain representation of a monotone Boolean support condition.

## 5. Important information-loss boundary

This algebra records **which minimal assumption sets suffice**.

It does not record derivation multiplicity, exact proof trees, repeated use counts, negative support or defeat, temporal order, or source reliability values.

Those belong in other layers if needed.

So the choice is intentional:

\[
\boxed{
\text{ATMS-style minimal support}
\Rightarrow
\text{antichain/free-distributive-lattice algebra}.
}
\]

It is **not** a universal replacement for richer proof provenance.

## 6. Concrete graded regime

Instantiate one quantitative interpretation over this symbolic algebra.

Let each primitive assumption \(x\in X\) be an independent Bernoulli variable with:

\[
P(x=1)=p_x.
\]

For a world:

\[
\omega\subseteq X,
\]

define the base probability:

\[
P_0(\omega)
=
\prod_{x\in\omega}p_x
\prod_{x\notin\omega}(1-p_x).
\]

Let \(N\) be the antichain of minimal **nogood** environments.

A world is consistent iff:

\[
\nexists E\in N:\;E\subseteq\omega.
\]

Write the consistency event as \(C\).

For positive support \(A\in\mathsf{Supp}(X)\), define:

\[
\boxed{
\rho_{\mathrm{Bern}}(A)
=
P_0(
\llbracket A\rrbracket
\mid C
).
}
\]

This is the project's first concrete graded-support regime.

## 7. Why conditioning on consistency matters

Suppose:

\[
P(a)=P(b)=1/2
\]

and

\[
\{a,b\}
\]

is a minimal nogood.

The consistent worlds are:

\[
\varnothing,\{a\},\{b\}.
\]

Their unconditioned total mass is:

\[
3/4.
\]

For support:

\[
a\vee b,
\]

the consistent supporting mass is:

\[
1/2.
\]

Thus:

\[
\rho_{\mathrm{Bern}}(a\vee b)
=
\frac{1/2}{3/4}
=
\frac23.
\]

For \(a\) alone:

\[
\rho_{\mathrm{Bern}}(a)
=
\frac{1/4}{3/4}
=
\frac13.
\]

The checked-in reference implementation reproduces these values exactly.

## 8. Why symbolic provenance must come first

Without the symbolic support formula, numeric combination can double count.

For independent \(a,b\) with probability \(1/2\):

\[
P(a\vee b)
=
3/4,
\]

not:

\[
P(a)+P(b)=1.
\]

The overlap world \(\{a,b\}\) is counted only once by the event semantics.

Likewise, if two apparently different support routes share a common primitive source, their dependence is visible in the symbolic representation rather than hidden inside two unrelated confidence numbers.

## 9. What the numeric value means

The reference implementation deliberately names the function support_probability. Semantically it computes:

\[
P(
\text{at least one positive support environment holds}
\mid
\text{consistency}
).
\]

Do **not** silently identify this with:

\[
P(h)
\]

for arbitrary proposition \(h\).

That stronger identification requires the surrounding warrant regime to establish that the support representation is semantically adequate for \(h\).

Thus:

\[
\boxed{
\rho_{\mathrm{Bern}}(\lambda(h))
\neq
P(h)
\quad\text{by definition alone}.
}
\]

## 10. Why this is only one graded regime

The independent-Bernoulli regime assumes a finite assumption set, explicit primitive probabilities, independence before conditioning on nogoods, and positive support semantics.

Other regimes may instead use a supplied joint distribution over assumption worlds, Dempster–Shafer belief/plausibility, ranking functions, possibility measures, source-reliability models, or Bayesian networks over assumptions.

The symbolic antichain support representation can remain unchanged while the interpretation changes.

## 11. Implementation

The experimental module:

src/inquiry_graph/support.py

contains:

- SupportAntichain
- normalization to subset-minimal environments
- alternative support
- joint support
- support satisfaction in an assumption world
- IndependentBernoulliRegime
- consistency conditioning through minimal nogoods

The implementation is deliberately independent of the executable inquiry-graph schema.

That prevents a research-level support calculus from silently becoming part of the dialogue annotation contract.

## 12. Algebraic laws checked

The test suite checks, on finite examples:

\[
x\oplus0=x,
\]

\[
x\otimes1=x,
\]

\[
x\oplus x=x,
\]

\[
x\otimes x=x,
\]

commutativity, associativity, distributivity, and both absorption laws.

The tests also check normalization/subsumption, distinction between alternative and joint support, overlapping-event probability without double counting, probability conditioned on nogoods, and invalid probability/missing-assumption failure cases.

## 13. Current architecture

The support layer can now be written more precisely as:

\[
\boxed{
\lambda:
N
\to
\mathsf{Supp}(X)
}
\]

where:

\[
\mathsf{Supp}(X)
=
\operatorname{Antichain}(\mathcal P_{\mathrm{fin}}(X)).
\]

A graded regime is then:

\[
\boxed{
\rho_\eta:
\mathsf{Supp}(X)
\to
V_\eta.
}
\]

The concrete first regime is:

\[
\rho_{\mathrm{Bern}}:
\mathsf{Supp}(X)
\to
[0,1].
\]

This gives a clear separation between symbolic support provenance, the uncertainty model, warrant for using that uncertainty model, and the epistemic action licensed by the resulting value.

## 14. Next research boundary

The positive-support question is now sufficiently concrete.

The next unresolved algebraic issue is **negative support / defeat**.

A pure positive distributive lattice cannot express rebuttal, undercutting, inconsistent reasons, priority among defeasible rules, or support both for and against a claim.

Possible next directions include signed/dual provenance tokens, bilattices, provenance with negation, and structured-argumentation attack graphs layered over positive provenance.

That should be researched before forcing defeat into the positive-support algebra itself.
