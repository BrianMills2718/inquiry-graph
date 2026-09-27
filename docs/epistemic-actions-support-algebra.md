# Epistemic actions, support provenance, and graded support

> **Status:** current research draft. This document follows [warrant-license-interface.md](warrant-license-interface.md) and addresses two open questions: what should count as an epistemic action target for warrant, and how should multiple supports/warrants interact with graded support \(\rho\)? The answer is intentionally interface-level rather than a claim that one universal numeric uncertainty calculus exists.

## 1. Main result

The next factorization is:

\[
\boxed{
\text{epistemic action}
\neq
\text{support provenance}
\neq
\text{graded interpretation}
\neq
\text{license aggregation}
}
\]

and, within the action layer:

\[
\boxed{
\text{primitive action vocabulary}
\text{ should not be assumed globally canonical.}
}
\]

The more stable abstraction is a **typed partial state transducer with explicit preconditions, outputs, and effect footprint**.

The more stable abstraction for combining support is **symbolic provenance first, quantitative interpretation second**.

## 2. Why a fixed action taxonomy is probably the wrong target

Several mature traditions point in the same direction.

### 2.1 AGM belief revision

AGM studies expansion, contraction, and revision of belief sets. Revision can be constructed from contraction plus expansion through the Levi identity:

\[
K*p=(K\div\neg p)+p.
\]

This already warns against treating every familiar update verb as primitive.

### 2.2 Katsuno–Mendelzon update versus revision

Katsuno and Mendelzon distinguish:

- **revision**: new information about a world treated as static;
- **update**: information reflecting that the world itself changed.

So even superficially similar input assimilation has different semantics depending on what changed.

### 2.3 Dynamic Epistemic Logic

Dynamic Epistemic Logic represents epistemic events with explicit preconditions and model-transforming update semantics. An action is not merely a verb such as “learn” or “announce”; it has a structured applicability condition and state-transforming effect.

These precedents suggest that the project should not search for one global MECE list such as:

\[
\{\text{accept},\text{retract},\text{reweight},\ldots\}.
\]

Instead, action identity should be relative to the declared state representation and composition algebra.

## 3. Epistemic state interface

Let the relevant reasoning state be abstracted as:

\[
S=
(\mathcal F,
K_{\mathcal F},
\Gamma,
Q,
\Pi)
\]

where:

- \(\mathcal F\): formal representation substrate;
- \(K_{\mathcal F}\): persistent support/epistemic overlay;
- \(\Gamma\): temporary assumption environment;
- \(Q\): current query/task;
- \(\Pi\): current strategy/control state when relevant.

This is an analysis interface, not a claim that cognition literally stores one tuple.

## 4. Epistemic action as a partial transducer

Define an epistemic action instance as:

\[
\boxed{
a:S\rightharpoonup S\times O_a
}
\]

where:

- the function is partial because an action may have preconditions;
- \(O_a\) is the action's observable/readout output type;
- the returned state may equal the input state.

This includes both mutating and non-mutating actions.

### 4.1 Readout action

Deduction can be:

\[
a_{\mathrm{derive}}(S)=(S,h).
\]

The state need not change.

### 4.2 Hard epistemic update

Acceptance/retraction may mutate \(K_{\mathcal F}\).

### 4.3 Graded update

A probabilistic or ranking update may change only the graded-support interpretation.

### 4.4 Context action

A white-box reasoning step may change:

\[
\Gamma\to\Gamma'.
\]

### 4.5 Query/control action

A reasoning-control move may change \(Q\) or strategy state \(\Pi\).

This gives one common target type for the warrant judgment:

\[
\mathfrak W;A\vdash_{\pi}a:G.
\]

## 5. Preconditions and effect footprints

Each action can expose:

\[
\operatorname{Pre}(a)
\]

and an effect footprint:

\[
\boxed{
F(a)\subseteq
\{
\mathcal F,
K_{\mathcal F},
\Gamma,
Q,
\Pi,
O
\}.
}
\]

This avoids another false partition.

Examples:

- derive a consequence:
  \[
  F(a)=\{O\};
  \]
- raise graded support:
  \[
  F(a)=\{K_{\mathcal F}\};
  \]
- introduce new vocabulary:
  \[
  F(a)=\{\mathcal F,K_{\mathcal F}\};
  \]
- switch temporary assumptions:
  \[
  F(a)=\{\Gamma\};
  \]
- change the active question:
  \[
  F(a)=\{Q\};
  \]
- select a new strategy:
  \[
  F(a)=\{\Pi\}.
  \]

A compound action can touch several coordinates.

## 6. What “primitive” now means

Primitive action should be defined **relative to an action algebra**.

Let:

\[
\mathcal A=(A,\circ,\oplus,\ldots)
\]

be a set of actions with available composition operators such as sequential composition, guarded choice, or iteration.

A generator set \(B\subseteq A\) is sufficient when:

\[
A=\langle B\rangle_{\mathcal A}.
\]

Then the meaningful questions are:

- does \(B\) generate every required action?
- is any generator redundant?
- is decomposition unique?
- which equivalence relation identifies two action programs with the same effect?
- does a smaller basis exist?

This is exactly the canonical-factorization strategy applied to epistemic actions.

There is no current claim that one representation-independent minimal basis exists.

## 7. Support provenance before graded support

The second problem is how multiple supports combine.

The ATMS-style support state already preserves minimal assumption environments:

\[
\lambda(h)=
\{\Gamma_1,\ldots,\Gamma_k\}.
\]

Before assigning numbers, retain a symbolic representation of *how* \(h\) is supported.

Introduce support tokens:

\[
X=\{x_1,x_2,\ldots\}
\]

for primitive support sources/assumptions.

Define symbolic positive support expressions with:

\[
\oplus
\]

for **alternative derivations/support routes**, and

\[
\otimes
\]

for **joint use of support**.

For example:

\[
P_h
=
(x_a\otimes x_b)
\oplus
x_c
\]

means:

> \(h\) has one support route requiring \(a\) and \(b\) jointly, and another route through \(c\).

This is closely related to both ATMS labels and semiring provenance.

## 8. Provenance semirings as an existing abstraction

Green, Karvounarakis, and Tannen's provenance-semiring framework uses:

- addition for alternative derivations;
- multiplication for joint use;
- symbolic provenance polynomials as a general provenance representation;
- homomorphisms into other semirings to obtain application-specific interpretations.

That structure is highly relevant here.

However, this project should **not** claim that every epistemic-support algebra is literally the free commutative semiring \(\mathbb N[X]\).

Why not?

- ATMS environments use set-like minimality and absorption;
- repeated derivations need not add epistemic strength;
- defeat/negation is not handled by a purely positive semiring;
- probabilistic interpretation becomes nontrivial when support routes overlap or are dependent.

So the project adopts a weaker claim:

\[
\boxed{
\text{positive support provenance should preserve alternative and joint support symbolically before numerical collapse.}
}
\]

A semiring is one important implementation family.

## 9. Bridge from ATMS labels to symbolic provenance

For intuition, an ATMS label

\[
\lambda(h)=
\{
\{a,b\},
\{c\}
\}
\]

can be rendered as the positive support expression:

\[
P_h=
(x_a\otimes x_b)
\oplus
x_c.
\]

This correspondence is schematic.

If support semantics treat duplicate/absorbed environments idempotently, the appropriate algebra should encode those laws.

The important property is that alternative and joint support remain distinguishable.

## 10. Graded support as a typed interpretation

The earlier scalar-looking symbol \(\rho\) was too weak.

Replace it conceptually with an indexed family of interpretations:

\[
\boxed{
\rho=
\{\rho_\eta\}_{\eta\in I}
}
\]

where each \(\eta\) names an uncertainty/evaluation regime and:

\[
\rho_\eta:
\mathsf{Prov}
\to
V_\eta.
\]

Examples of \(V_\eta\):

- Boolean derivability;
- probabilities;
- belief/plausibility intervals;
- ordinal rankings;
- costs;
- reliability scores;
- other regime-specific values.

This does **not** mean all of these should be stored simultaneously.

It means \(\rho\) is typed and regime-indexed rather than presumed to be one universal scalar.

## 11. Probabilistic ATMS precedent

Laskey and Lehner showed a formal relationship between ATMS reasoning with probabilities on assumptions and Dempster–Shafer belief functions. They emphasized that dependencies between derived nodes can be handled through the underlying assumption structure.

Liu and Bundy likewise showed how probabilities on assumptions can be combined with ATMS-style labels through extended incidence calculus.

These results strongly support the architecture:

\[
\boxed{
\text{symbolic support structure}
+
\text{uncertainty model over assumptions}
\to
\text{graded support}.
}
\]

They argue against assigning independent scalar confidence numbers directly to derived nodes without preserving their common provenance.

## 12. Why naïve numeric combination is unsafe

Suppose:

\[
P_h=x_a\oplus x_b.
\]

It is tempting to say:

\[
\rho(h)=\rho(a)+\rho(b).
\]

That is generally unjustified.

If \(a\) and \(b\) overlap, are correlated, or derive from the same source, naïve addition double-counts evidence.

Likewise:

\[
\rho(a\otimes b)=\rho(a)\rho(b)
\]

requires independence or another explicit interpretation rule.

Therefore:

\[
\boxed{
\text{symbolic composition first;}
\quad
\text{numeric evaluation only under an explicit uncertainty model.}
}
\]

## 13. Graded updates are warrant-regime specific

Bayesian conditioning and Jeffrey conditionalization are useful examples.

Simple conditioning is appropriate under specific assumptions about learning an event with certainty.

Jeffrey conditionalization handles a class of uncertain-learning cases by imposing posterior probabilities on a partition while preserving specified conditional probabilities.

These are not generic definitions of “increase support.”

They are particular update actions:

\[
u_\eta:\rho_\eta\to\rho'_\eta
\]

whose use must itself be warranted under a regime:

\[
\mathfrak W_\eta;A_\eta
\vdash_{\pi}
u_\eta:G_\eta.
\]

Thus:

\[
\boxed{
\Delta\rho
\text{ is not one primitive operation;}
\text{ it is a typed family of update rules.}
}
\]

## 14. Multiple warrants for one action

For an epistemic action \(a\), define the currently applicable undefeated warrant set:

\[
\boxed{
\mathcal L_C(a)=
\{
(\mathfrak W,A,\pi,G)
\mid
C\models A,\;
\mathfrak W;A\vdash_\pi a:G,\;
\pi\text{ is undefeated}
\}.
}
\]

This is the **license basis** for the action.

Important: \(\mathcal L_C(a)\) need not collapse to one score.

### 14.1 Alternative warrants

Two independent proof/argument routes may each be sufficient for the same guarantee.

Keep them as alternative provenance.

### 14.2 Joint warrants

Some license may require several conditions/certificates jointly.

Preserve joint composition explicitly.

### 14.3 Defeated warrant

A defeater can remove/block an otherwise applicable warrant derivation according to its warrant regime.

### 14.4 Heterogeneous guarantees

A statistical guarantee and a deductive guarantee do not automatically combine.

Keep them typed and parallel unless a meta-regime defines a valid aggregation.

## 15. License aggregation versus action selection

Even when an action has licenses, execution is a separate decision.

Let:

\[
\delta
\]

be an optional control/decision policy:

\[
\delta(
S,
a,
\mathcal L_C(a)
)
\to
\{
\operatorname{execute},
\operatorname{defer},
\operatorname{reject},
\operatorname{seekMoreSupport}
\}.
\]

This preserves the earlier distinction:

\[
\boxed{
\text{licensed}
\neq
\text{executed}.
}
\]

Resource constraints, risk preferences, task priorities, or competing licenses may enter here.

Those are not automatically part of the warrant itself.

## 16. Conflicting warrant regimes

Suppose:

\[
\mathfrak W_1;A_1\vdash_{\pi_1}a:G_1
\]

while:

\[
\mathfrak W_2;A_2\vdash_{\pi_2}\neg a:G_2
\]

or licenses a competing action.

If \(G_1\) and \(G_2\) are incommensurable, there is no justified default scalar aggregation.

The system should preserve:

- both warrant derivations;
- their regimes;
- their guarantees;
- their defeaters;
- the meta-level rule, if any, used to resolve the conflict.

This creates a new target for warrant:

\[
\text{warrant for the aggregation/selection rule itself}.
\]

The regress is again explicit rather than hidden.

## 17. Revised end-to-end architecture

The current research stack becomes:

\[
\boxed{
\begin{array}{c}
\textbf{Formal representation}\\
\mathcal F
\\[4pt]
\downarrow
\\[4pt]
\textbf{Symbolic support provenance}\\
J,\lambda,\mathsf{Prov}
\\[4pt]
\downarrow
\\[4pt]
\textbf{Typed graded interpretations}\\
\{\rho_\eta\}
\\[4pt]
\downarrow
\\[4pt]
\textbf{Reasoning state}\\
S=(\mathcal F,K_{\mathcal F},\Gamma,Q,\Pi)
\\[4pt]
\downarrow
\\[4pt]
\textbf{Epistemic actions}\\
a:S\rightharpoonup S\times O_a
\\[4pt]
\downarrow
\\[4pt]
\textbf{Warrant / license}\\
\mathfrak W;A\vdash_\pi a:G
\\[4pt]
\downarrow
\\[4pt]
\textbf{Control / execution}\\
\delta(S,a,\mathcal L_C(a))
\end{array}
}
\]

Candidate generation remains upstream as the mechanism by which draft/formal objects and candidate actions can be proposed.

## 18. Consequences for the previous notation

### Old

\[
K_{\mathcal F}=(N,A,J,\lambda,\rho).
\]

### Refined interpretation

Keep this notation if convenient, but read \(\rho\) as:

\[
\rho=\{\rho_\eta\}
\]

rather than one scalar field.

And read \(J,\lambda\) as preserving symbolic support structure that should generally precede quantitative evaluation.

### Old epistemic action list

Lists such as derive / accept / retract / reweight / select strategy remain useful named action schemas.

They are **not yet a canonical primitive basis**.

Primitive status is relative to the chosen state/action algebra.

## 19. What this resolves

The research supports the following current commitments:

1. epistemic actions should be typed state transducers rather than assumed globally primitive verbs;
2. effect footprints are compositional and can replace a false MECE action taxonomy;
3. primitive action bases are representation-relative generator sets;
4. support provenance should be preserved symbolically before graded collapse;
5. alternative and joint support are distinct composition modes;
6. \(\rho\) should be typed/indexed by an uncertainty regime;
7. probabilities on derived claims must respect shared provenance/dependence;
8. graded update rules such as Jeffrey conditioning are warrant-regime-specific actions;
9. multiple warrants need not collapse to one score;
10. heterogeneous warrant conflicts require an explicit meta-level aggregation/selection rule.

## 20. Remaining open questions

1. Which action composition operators belong in the minimal action algebra: sequential composition, guarded choice, iteration, concurrency?
2. Which state coordinates should be considered part of the action footprint in the executable formalization?
3. Which positive support algebra best matches ATMS minimal-environment semantics: Boolean formulas, absorptive/idempotent semirings, provenance polynomials, or another structure?
4. How should negative support/defeat interact with positive provenance without losing explanation structure?
5. Which graded regime should be implemented first for empirical work?
6. How should reliability of sources and measurements be represented without double-counting common provenance?
7. What properties should a meta-regime satisfy when resolving heterogeneous licenses?
8. Can action and support factorizations be given representation theorems analogous to AGM?
