# Warrant and Guarantee Transport Across Representations

> **Status:** literature-driven integration decision following the candidate-generation cross-framework glue survey.
>
> **Purpose:** determine how guarantees established by one generator, prover, analyzer, or epistemic regime can survive translation into another representation or tool context.

## 1. Executive conclusion

The remaining cross-framework problem is also substantially covered by existing formal methods.

The project should **not invent a universal guarantee-transport calculus from scratch**.

Different mature frameworks already handle different transport strengths:

1. **Institution theory / DOL / Hets** — satisfaction-preserving translations across logics and heterogeneous proof management.
2. **MMT / theory morphisms / logical frameworks** — theorem/judgment preservation along formal theory morphisms.
3. **Abstract interpretation** — sound one-way transfer through abstraction/concretization.
4. **Refinement and contract theories** — preservation of assumptions/guarantees through refinement and composition, when the relevant preservation laws are established.
5. **Opaque or empirical adapters** — no formal guarantee transport; translated output must be re-evaluated/re-warranted in the target regime.

The project should therefore classify representation adapters by **preservation strength**, and only transport a warrant when an existing preservation theorem/certificate justifies it.

The default rule is:

\[
\boxed{
\text{artifact translation}
\not\Rightarrow
\text{guarantee translation}.
}
\]

If no preservation result is available, the target artifact is merely a translated candidate and must be warranted again.

---

## 2. Major correction: Hets/DOL already solves much of the formal case

The Heterogeneous Tool Set (Hets) is much closer to the project's formal cross-framework problem than earlier architecture notes acknowledged.

Hets:

- represents multiple logics as institutions;
- treats logic translations as first-class institution morphisms/comorphisms;
- maintains a graph of logics and translations;
- integrates logic-specific theorem provers, model finders and analyzers;
- supports heterogeneous specifications;
- provides a heterogeneous proof calculus and proof-management structure.

The Distributed Ontology, Model, and Specification Language (DOL) further standardizes heterogeneous OMS networks and mappings between them.

Therefore, for formally specified logical artifacts:

\[
\boxed{
\textbf{Hets/DOL should be the default precedent for heterogeneous formal interoperability.}
}
\]

MMT/LF remains valuable as the declarative theory/proof representation layer.

A plausible division of labor is:

\[
\boxed{
\text{MMT/LF}
=
\text{formal theories, objects, proofs, morphisms}
}
\]

and:

\[
\boxed{
\text{Hets/DOL}
=
\text{heterogeneous logic graph, translations, tool/proof orchestration}.
}
\]

The project does not need to reproduce either system.

---

## 3. Exact semantic transport: institutions

An institution is:

\[
\mathcal I
=
(
\mathbf{Sign},
\operatorname{Sen},
\operatorname{Mod},
\models
).
\]

A logic translation connects:

- signatures;
- sentences;
- models;

subject to a satisfaction condition.

Schematically, for translation \(\tau\):

\[
M'
\models'
\tau_{\mathrm{Sen}}(\varphi)
\quad\Longleftrightarrow\quad
\tau_{\mathrm{Mod}}(M')
\models
\varphi.
\]

This is extremely strong.

It means truth/satisfaction is invariant under the translation in the specified direction.

For guarantees that are genuinely semantic consequences in the source institution, institution-theoretic translation provides an established transport basis.

Thus:

\[
\boxed{
\text{satisfaction-preserving morphism/comorphism}
\Rightarrow
\text{semantic guarantee transport}.
}
\]

DOL/Hets operationalizes this style of interoperability across heterogeneous logics.

---

## 4. Proof/judgment transport: MMT and theory morphisms

Theory morphisms provide the proof-theoretic analogue.

If:

\[
\mu:S\to T
\]

is a valid theory morphism, judgments/theorems over \(S\) are mapped to judgments/theorems over \(T\).

Schematically:

\[
\Gamma\vdash_S p:P
\]

implies:

\[
\mu(\Gamma)
\vdash_T
\mu(p):\mu(P).
\]

This yields:

\[
\boxed{
\text{theory morphism}
\Rightarrow
\text{proof/judgment preservation}.
}
\]

Therefore if a candidate generator returns a formally checked proof in a source theory and a certified MMT-style morphism maps that theory into the shared formal substrate, the proof can be transported rather than re-proved from scratch.

This is an existing theorem-preservation mechanism, not a new project invention.

---

## 5. Sound but lossy transport: abstract interpretation

Many adapters are not equivalences.

Abstract interpretation supplies the canonical mature theory for sound abstraction.

A concrete semantic domain \(C\) and abstract domain \(A\) are related through abstraction/concretization maps, often organized as a Galois connection.

The central idea is that the abstract computation safely approximates the concrete one.

Therefore some properties can be transported **one way**.

For example, if an abstract analysis overapproximates reachable states and the abstract result excludes all unsafe states, the corresponding concrete safety property follows.

This motivates a second transport class:

\[
\boxed{
\text{sound abstraction}
\Rightarrow
\text{one-way weakened guarantee transport}.
}
\]

Unlike institution satisfaction preservation, this need not be biconditional.

The target guarantee may be weaker than the source description or may apply only in one inference direction.

---

## 6. Contract/refinement transport

Assume-guarantee and interface theories provide another mature family.

A contract has the rough form:

\[
(A,G)
\]

where the environment is assumed to satisfy \(A\), and the component guarantees \(G\).

Refinement allows one component/contract to safely replace another under specified conditions.

Composition allows system-level guarantees to be derived from component contracts when the composition rules apply.

This is highly aligned with the project's warrant shape:

\[
\mathfrak W;
A
\vdash_\pi
a:G.
\]

However, the contract literature gives an important warning:

\[
\boxed{
\text{preservation of one relation/operator}
\not\Rightarrow
\text{preservation of every operator}.
}
\]

For example, transformations between interface and contract formalisms may preserve refinement while failing to preserve serial composition unless additional assumptions/projections are introduced.

Thus adapter composition must be justified **operation by operation**.

Do not assume:

\[
\tau(g_2\circ g_1)
=
\tau(g_2)\circ\tau(g_1)
\]

merely because \(\tau\) preserves some local correctness property.

---

## 7. Heterogeneous proof management: Hets as a direct model

Hets provides an especially important precedent for the exact use case:

- a theorem exists in one logic;
- a translation connects that logic to another;
- a different prover can be used in the translated logic;
- global heterogeneous proof obligations are decomposed into local ones.

This means the project should not conceptualize every generator/prover as if it needs to speak the shared logic natively.

Instead:

\[
\boxed{
\text{native logic}
\xrightarrow{\text{certified translation}}
\text{logic with appropriate tool}
}
\]

is already a mature tool-integration pattern.

For formal candidate generators, the preferred implementation path is therefore:

1. preserve the native representation;
2. declare the logic/representation formally;
3. declare verified translations where available;
4. transport only the guarantees those translations preserve;
5. recheck locally where transport is not available.

---

## 8. Transport-strength taxonomy

The project should classify every adapter into one of the following transport strengths.

### T0 — syntactic/opaque translation

The adapter maps artifacts:

\[
x\mapsto \tau(x)
\]

but provides no formal preservation theorem.

Result:

\[
\boxed{
\text{no warrant transport}.
}
\]

The target artifact must be re-evaluated.

Examples:

- heuristic natural-language rewrite;
- unverified LLM translation;
- format conversion with unclear semantics.

### T1 — provenance-preserving translation

The adapter preserves source identity/provenance and perhaps structural correspondences, but not semantic correctness.

Result:

- provenance survives;
- semantic warrant does not automatically survive.

### T2 — sound one-way translation

There is a theorem/certificate:

\[
G_S
\Rightarrow
G_T.
\]

Examples:

- sound abstraction;
- safe weakening;
- refinement in a verified direction.

Result:

\[
\text{source guarantee can justify a weaker target guarantee}.
\]

### T3 — exact satisfaction/judgment preservation

There is a strong preservation property such as:

\[
M'\models\tau(\varphi)
\Longleftrightarrow
\tau(M')\models\varphi
\]

or theorem/judgment preservation along a theory morphism.

Examples:

- institution morphism/comorphism under the relevant direction;
- MMT theory morphism.

Result:

\[
\text{formal guarantee is transportable in the preserved fragment}.
\]

### T4 — compositional transport

In addition to local preservation, the adapter is proven to preserve the operations used in the pipeline:

- composition;
- conjunction;
- refinement;
- hiding;
- quotient;
- other required constructors.

This is stronger than T3 for composed generator workflows.

Result:

\[
\text{pipeline-level guarantees may be transported compositionally}.
\]

The classification is cumulative only when the relevant theorems actually hold.

---

## 9. Transport is guarantee-specific

An adapter should not receive one blanket label such as “sound.”

Preservation depends on **which guarantee is being transported**.

For adapter \(\tau\), define a relation:

\[
\operatorname{Preserves}_\tau(G_S,G_T).
\]

Examples:

- preserves theoremhood;
- preserves satisfiability;
- preserves validity;
- preserves refinement;
- preserves a safety invariant;
- preserves probability calibration;
- preserves uncertainty bounds;
- preserves causal interpretation.

An adapter may preserve one property and not another.

Therefore:

\[
\boxed{
\text{adapter correctness is typed by guarantee family}.
}
\]

This aligns directly with the existing typed-guarantee warrant model.

---

## 10. No new primitive warrant judgment is required

The project does not need a second “transport logic.”

Transport itself can be treated as another warrant target.

Suppose source warrant:

\[
\mathfrak W_S;
A_S
\vdash_{\pi_S}
a_S:G_S.
\]

Let translation \(\tau\) have a preservation certificate \(\chi\).

Represent the adapter-level warrant schematically as:

\[
\mathfrak W_\tau;
A_\tau
\vdash_\chi
\operatorname{transport}_\tau(G_S):
G_T.
\]

Then the target warrant is obtained by ordinary warrant composition:

\[
\boxed{
\frac{
\mathfrak W_S;A_S\vdash_{\pi_S}a_S:G_S
\qquad
\mathfrak W_\tau;A_\tau\vdash_\chi\operatorname{transport}_\tau(G_S):G_T
}{
\mathfrak W_T;
\tau_A(A_S)\cup A_\tau
\vdash_{\tau_\pi(\pi_S),\chi}
\tau_a(a_S):G_T
}
}
\]

This is a **schema**, not a claim that every translation supports every mapping shown.

The adapter supplies:

- assumption transport \(\tau_A\) where applicable;
- certificate/proof transport \(\tau_\pi\);
- action mapping \(\tau_a\);
- guarantee mapping/weakening \(G_S\rightsquigarrow G_T\).

If any required mapping is unavailable, target re-warrant is required.

---

## 11. Assumptions do not all translate the same way

The transport problem exposes a useful distinction inside warrant assumptions.

Some assumptions are internal to the formal representation:

- axioms;
- typing assumptions;
- model-class restrictions.

Others are external applicability conditions:

- sample is i.i.d.;
- sensor remains calibrated;
- source reliability model applies to this reference class;
- deployment distribution is stable.

A theory morphism may translate the first category while leaving the second unchanged.

Therefore \(A\) should be treated as a **typed assumption set**.

An adapter may act partially:

\[
\tau_A:
A
\rightharpoonup
A'.
\]

Untranslated external assumptions remain explicit residual obligations.

This does not require a new top-level coordinate; it requires typed assumption metadata.

---

## 12. Transport composition

Suppose:

\[
L_1
\xrightarrow{\tau_1}
L_2
\xrightarrow{\tau_2}
L_3.
\]

A guarantee can be transported through the chain only if the preservation relation composes.

If:

\[
\operatorname{Preserves}_{\tau_1}(G_1,G_2)
\]

and:

\[
\operatorname{Preserves}_{\tau_2}(G_2,G_3),
\]

then:

\[
G_1
\rightsquigarrow
G_3
\]

is licensed only if the relevant preservation certificates compose.

For institution/theory morphisms this may follow from categorical composition.

For contracts or other weaker adapters it may not.

Therefore the controller should treat composed adapter paths as proof obligations, not merely graph reachability.

This is exactly the kind of problem Hets's heterogeneous development graphs already address for logical systems.

---

## 13. Formal vs empirical adapters

The integration architecture should make a sharp distinction.

### Formal adapter

Has a machine-checkable preservation certificate.

Examples:

- institution comorphism;
- MMT theory morphism;
- verified abstraction;
- checked refinement mapping.

Result:

guarantees may be transported according to the certificate.

### Empirical adapter

Reliability is established statistically or experimentally.

Examples:

- learned representation translator;
- LLM semantic converter;
- learned schema mapper.

Result:

the adapter may have its own statistical warrant, but it does not provide deductive guarantee transport.

The target warrant must reflect this weaker regime.

### Unverified adapter

No adequate reliability evidence.

Result:

translation produces only a candidate.

---

## 14. Non-logical guarantees

Not every guarantee lives in a logical institution.

The project's benchmark includes:

- measurement uncertainty;
- testimony posterior;
- PAC bounds;
- strategy-performance bounds.

For these, exact logical translation may be irrelevant.

The same high-level transport rule still applies:

\[
G_S
\xRightarrow[\chi]{\tau}
G_T.
\]

But \(\chi\) may be:

- calibration propagation theorem;
- probability transformation theorem;
- confidence-bound preservation;
- unit conversion proof;
- statistical covariate transformation;
- measurement model propagation.

The key rule remains:

\[
\boxed{
\text{transport only the guarantee that the adapter certificate actually preserves}.
}
\]

---

## 15. Examples

### 15.1 Theorem prover translation

Source:

\[
\Gamma\vdash_S h.
\]

Certified theory morphism:

\[
\mu:S\to T.
\]

Transport:

\[
\mu(\Gamma)
\vdash_T
\mu(h).
\]

This is T3 theorem-preserving transport.

### 15.2 Abstract analysis

Source abstract analyzer proves no abstract bad state is reachable.

Sound abstraction theorem establishes that concrete reachable states are contained in the concretization of abstract reachable states.

Transported guarantee:

\[
\text{concrete system is safe}.
\]

This is T2 one-way sound transport.

### 15.3 LLM-generated translation of a theorem statement

An LLM rewrites a source formula into another formal language.

No verified mapping exists.

Result:

\[
\boxed{\text{translated formula is a candidate only}.}
\]

The theorem must be checked/reproved in the target formalism.

This is T0/T1.

### 15.4 Contract transformation

A translation from interface theory to assume-guarantee contracts is known to preserve refinement but not arbitrary serial composition without extra conditions.

Result:

- refinement guarantees transport;
- serial-composition guarantees do not transport automatically.

This illustrates guarantee-specific preservation.

---

## 16. Revised candidate-generator interoperability architecture

The cross-framework architecture remains:

\[
\mathcal C
=
(
\mathbb B,
\mathcal K,
\mathcal P,
\Pi,
\mathcal M,
\mathfrak W
).
\]

Refine the adapter portfolio:

\[
\mathcal P
=
\{
(\tau_i,\operatorname{Pres}_i,\chi_i)
\}.
\]

Each adapter records:

- source representation/regime;
- target representation/regime;
- artifact translation;
- typed preservation relations;
- preservation certificate/proof;
- residual assumptions;
- supported composition operators.

The controller may prefer an adapter path with stronger preservation:

\[
T4>T3>T2>T1>T0
\]

only relative to the guarantee required by the active task.

---

## 17. Off-the-shelf implementation recommendation

If this architecture is ever implemented, use existing systems before writing custom formal transport machinery.

### Formal multi-logic layer

Use/evaluate:

- DOL;
- Hets;
- institution morphisms/comorphisms;
- MMT/LF theory morphisms.

### Approximation layer

Use abstract-interpretation style soundness certificates.

### Component/contract layer

Use established refinement / assume-guarantee / hypercontract frameworks.

### Unverified/learned adapters

Preserve provenance and require target-side re-warrant.

This should be enough for the first implementation.

---

## 18. What remains genuinely unresolved

After this survey, guarantee transport itself is much less open than previously thought.

The remaining project-specific questions are mainly integration choices:

1. how to represent typed preservation certificates uniformly in the shared graph;
2. how to choose among multiple translation paths with different preservation strengths;
3. how to combine formal and empirical adapter reliability;
4. how to preserve source/proof provenance through heterogeneous pipelines;
5. how to expose residual assumptions after translation;
6. how to handle guarantees that have no natural image in the target regime.

These are important, but they do not currently require a new foundational formalism.

---

## 19. Adoption decision

For formal logical transport:

\[
\boxed{
\textbf{adopt institution/DOL/Hets and MMT-style morphism machinery.}
}
\]

For approximate transport:

\[
\boxed{
\textbf{adopt soundness/refinement certificates.}
}
\]

For unverified translation:

\[
\boxed{
\textbf{transport artifacts and provenance only; re-warrant content.}
}
\]

The project should stop treating warrant transport as a largely unexplored theoretical gap.

The major open problem is now implementation/integration, not foundational semantics.
