# Assumption-context meta-model — current research endpoint

> **Status:** research draft derived from the visible 2026-09-27 dialogue and a targeted literature check. It refines, rather than erases, the earlier state-delta model in [epistemic-transition-calculus.md](epistemic-transition-calculus.md). It is not an established universal theory of cognition or warrant.

## 1. Why this revision was needed

The earlier working state

$$
K=(\mathcal U,H,\mu)
$$

was useful for proving a simple fact about hard state changes: once a semantic universe and identity map are fixed, additions and deletions uniquely describe how a live set changes.

But \(\mathcal U\) was doing too much. It blurred:

- the vocabulary/signature available to the reasoner;
- the sentences expressible in that vocabulary;
- semantic models/possible worlds;
- candidate hypotheses currently under consideration;
- temporary assumptions used only for one derivation.

The dialogue also clarified that the project should not model an embedded observer as having one committed theory. A reasoner can entertain incompatible alternatives and temporarily stipulate assumptions for a branch of reasoning without endorsing them as certain.

The current refinement therefore separates the **logical substrate**, the **persistent support structure**, and a **temporary reasoning episode**.

## 2. Logical substrate: institution-style separation

Use the abstract shape supplied by institution theory:

$$
\boxed{
\mathfrak I=
(\mathbf{Sig},\operatorname{Sen},\operatorname{Mod},\models)
}
$$

where:

- \(\mathbf{Sig}\) is the class/category of signatures;
- \(\operatorname{Sen}(\Sigma)\) gives sentences expressible under signature \(\Sigma\);
- \(\operatorname{Mod}(\Sigma)\) gives models/interpretations for \(\Sigma\);
- \(m\models_\Sigma\varphi\) is satisfaction.

This supplies a disciplined replacement for the earlier overloaded \(\mathcal U\).

A representation/language change is no longer an arbitrary map \(\Phi\) when a signature morphism is available. Instead use

$$
\sigma:\Sigma\rightarrow\Sigma'.
$$

The logical institution supplies the induced sentence translation and model reduct. The satisfaction condition provides the semantic coherence criterion that the generic \(\Phi\) lacked.

This does **not** claim every representation change encountered in cognition is already an institution morphism. It establishes the preferred formal interface when the change is genuinely a translation/extension between logical signatures.

## 3. Persistent black-box epistemic/support state

For a selected signature \(\Sigma\), use an ATMS-inspired support structure:

$$
\boxed{
K_\Sigma=(N,A,J,\lambda,\rho)
}
$$

where:

- \(N\) is the set of represented propositions, hypotheses, reports, candidate structures, etc.;
- \(A\subseteq N\) is the subset that may function as assumptions;
- \(J\) is the explicit dependency/justification structure;
- \(\lambda(n)\) records minimal assumption environments under which node \(n\) is derivable;
- \(\rho\) is an optional graded-support layer.

An **assumption environment** is a consistent set

$$
\Gamma\subseteq A.
$$

A node may have more than one independent minimal support environment. Schematically,

$$
\lambda(h)=
\big\{
\{a,b\},
\{c\}
\big\}
$$

means \(h\) is supported either by assumptions \(a,b\) jointly or by \(c\) independently.

The ATMS contribution is structural dependency bookkeeping, not probability. The optional \(\rho\) is deliberately separate because the current project still has not chosen one universal algebra of graded support.

## 4. White-box reasoning as a temporary environment

The white-box/black-box distinction can now be stated without certainty language.

### Persistent black-box state

The embedded observer maintains alternatives and their dependency structure:

$$
K_\Sigma=(N,A,J,\lambda,\rho).
$$

It need not select one theory as *the* theory.

### Temporary white-box context

A reasoning episode temporarily stipulates:

$$
\Gamma\subseteq A
$$

and inspects what follows under those assumptions.

Define the consequence/context closure:

$$
\boxed{
C(\Gamma)=\operatorname{Cl}_{J}(\Gamma).
}
$$

Then a deductive readout can be represented schematically as:

$$
h\in C(\Gamma)
\quad\text{or}\quad
\Gamma,J\vdash h.
$$

Selecting \(\Gamma\) does not assert certainty or permanent endorsement. It means:

> for this branch, assume these propositions and inspect the consequences.

This is the formal distinction the earlier notation \(T\) versus \(W\) was trying to reach but described too much like a committed belief theory.

## 5. Reasoning episode and query

A query or problem is not itself part of what the observer believes. Keep it outside persistent epistemic state.

A reasoning episode is therefore:

$$
\boxed{
R=(K_\Sigma,\Gamma,Q)
}
$$

where \(Q\) is the current question/task.

This decomposes the dialogue-level macro **reframe** into several distinct possibilities:

- query transformation: \(Q\to Q'\);
- signature/language transformation: \(\Sigma\to\Sigma'\);
- support-graph change: \(K_\Sigma\to K'_{\Sigma}\);
- assumption-context change: \(\Gamma\to\Gamma'\);
- combinations of the above.

“Reframe” remains useful for dialogue annotation, but is not a foundational epistemic primitive.

## 6. Evidence is not a magical top-level bucket

The previous draft used an undifferentiated evidence coordinate \(E\). That is now demoted.

An observation, instrument report, testimony, or imported research result can instead be represented as a typed node in \(N\) with provenance and explicit dependencies.

For example:

- \(e\): “instrument reports 37.9°C”;
- \(a\): “instrument is calibrated”;
- \(j\): justification connecting \(e,a\) to some diagnostic proposition.

This avoids treating the word “evidence” as self-warranting. Reports can themselves depend on assumptions and can be challenged.

External source provenance remains distinct from semantic warrant. The existing inquiry graph already follows this principle: a grounded utterance establishes what was said, not whether the proposition is true.

## 7. Concept construction, definitions, and concept invention

The candidate-generation work exposed an important three-way distinction.

### 7.1 Construction in an existing language

If the logic already contains a constructor \(f\), then

$$
c=f(c_1,\ldots,c_n)
$$

can produce a new expression without changing the signature or epistemic state.

Example: form \(A\land B\) from existing expressions.

This is candidate/expression construction.

### 7.2 Definitional extension

A fresh name \(C\) can be added with an explicit definition:

$$
\Sigma'=\Sigma\cup\{C\},
$$

$$
C\leftrightarrow A\land B.
$$

If the extension is conservative over the old language, representational convenience increased without adding substantive old-language commitments.

### 7.3 Substantive predicate/concept invention

A genuinely new predicate may not be definitionally reducible to the old language:

$$
\Sigma\rightarrow\Sigma'.
$$

Its semantic role must be learned, proposed, constrained, or otherwise supplied.

This is the domain of predicate invention and related concept-invention problems.

Therefore:

$$
\boxed{
\text{expression construction}
\neq
\text{definitional extension}
\neq
\text{substantive concept invention}.
}
$$

## 8. Candidate generation remains a typed open problem

The earlier notation

$$
g:(K,E)\rightarrow\mathcal C
$$

made “candidate” look like one homogeneous type. It is not.

For a reasoning episode \(R\), a generator may produce candidates of several types:

$$
g_i(R)\rightarrow\mathcal C_i
$$

where \(\mathcal C_i\) may contain:

- expressions/sentences;
- assumptions;
- justifications/dependencies;
- semantic models;
- latent variables or predicates;
- signature extensions;
- mappings/translations;
- queries;
- whole theories or modular theory fragments.

Established operators cover parts of this space:

- logical constructors: within-language expression construction;
- anti-unification / least-general generalization: generalization of structured expressions;
- Formal Concept Analysis: closure and concept-lattice construction from object–attribute contexts;
- ILP / predicate invention: introducing new relations/vocabulary;
- analogy and theory mapping: structural mappings between representations.

The project should import precise existing definitions where possible rather than promote English labels such as “abstract,” “compose,” or “reframe” to primitives.

The major unresolved problem remains:

$$
\boxed{
\text{Can typed candidate generation be factored into a small compositional basis?}
$$

No MECE basis has been established.

## 9. Warrant and support provenance

The earlier warrant certificate remains useful:

$$
\operatorname{Cert}(\tau)=
(A_W,G_W,\pi),
$$

where:

- \(A_W\) are assumptions;
- \(G_W\) is the guarantee being claimed;
- \(\pi\) is the support for the conditional claim.

The ATMS-style support graph gives a concrete data structure for exposing which assumptions support which derived propositions. It does **not** by itself prove that the assumptions are warranted.

Meta-warrant remains recursive:

$$
\lambda(a)=
\{\Gamma_1,\ldots,\Gamma_k\}
$$

may expose support for assumption \(a\); its own supporting assumptions can in turn be queried.

The formalism deliberately permits a chain to terminate in:

- declared axioms;
- observation/report nodes;
- empirical reliability claims;
- circular/coherent support;
- unresolved assumptions.

It does not pretend the regress is philosophically solved.

## 10. Relationship to the earlier state-delta result

The previous fixed-universe result remains valid at its intended semantic level.

If a selected semantic possibility set changes from \(W\) to \(W'\) under a fixed identity relation, then:

$$
A_W=W'\setminus W,
\qquad
D_W=W\setminus W'
$$

uniquely characterize additions and deletions.

What changed is our understanding of **persistent epistemic organization**. A flat live-world set is now treated as a derived or degenerate view of the richer support structure rather than the whole observer state.

Likewise the old generic representation map

$$
\Phi:\mathcal U\to\mathcal U'
$$

is retained only as a fallback abstraction. For logical vocabulary change, institution-style signature morphisms are the preferred formal object.

## 11. Worked micro-example

Suppose the observer represents assumptions:

$$
A=\{a,b,c\}
$$

and has justification rules:

$$
a\land b\Rightarrow h,
$$

$$
c\Rightarrow h.
$$

Then:

$$
\lambda(h)=
\big\{
\{a,b\},
\{c\}
\big\}.
$$

For one reasoning branch select:

$$
\Gamma=\{a,b\}.
$$

Then:

$$
h\in C(\Gamma).
$$

No commitment to \(a,b\) as certainly true is implied.

Now suppose the observer invents a latent predicate \(Z\) not expressible in the current signature. That is a candidate signature extension:

$$
\sigma:\Sigma\rightarrow\Sigma'.
$$

Candidate generation proposes \(Z\), warrant/evaluation assesses the move, and only then is the persistent support structure extended with new nodes/justifications/support.

This one example separates:

1. persistent alternatives;
2. temporary white-box assumptions;
3. deductive consequence;
4. vocabulary invention;
5. evaluation/warrant;
6. persistent state change.

## 12. Relationship to the inquiry graph

The **epistemic meta-model** and the **dialogue inquiry graph** are different layers.

The inquiry graph records public discourse:

- who proposed a candidate;
- what was challenged;
- what was retracted or reframed;
- what question was opened/reopened;
- source provenance.

The epistemic meta-model proposes a formal semantics for hypothetical reasoning and candidate generation.

A dialogue “reframe” move may correspond, at the epistemic layer, to \(Q\to Q'\), \(\Sigma\to\Sigma'\), a support-graph edit, an environment switch, or a composition of these. The inquiry graph should not silently infer which internal operation occurred unless the dialogue supports that interpretation.

## 13. Established machinery now in the spine

Two existing formalisms now play complementary roles.

### Institution theory

Use for:

- signatures;
- sentences;
- models;
- satisfaction;
- semantics-preserving language/signature transformations.

Primary reference: Joseph Goguen and Rod Burstall, “Institutions: Abstract Model Theory for Specification and Programming,” *Journal of the ACM* 39(1), 95–146 (1992), DOI 10.1145/147508.147524.

### Assumption-based Truth Maintenance

Use for:

- simultaneous hypothetical alternatives;
- assumption environments;
- explicit justification dependencies;
- minimal supporting environments;
- cheap conceptual context switching.

Primary reference: Johan de Kleer, “An assumption-based TMS,” *Artificial Intelligence* 28(2), 127–162 (1986), DOI 10.1016/0004-3702(86)90080-9.

The project does not claim to implement either formalism in full.

## 14. Parked but relevant

**Theory graphs / theory morphisms** remain relevant if the system later needs a modular network of theories with explicit imports and knowledge transport. They are not currently required as an additional foundational layer because institution theory already supplies the needed abstraction for language/model translations.

## 15. Current endpoint

The current architecture is:

$$
\boxed{
\begin{array}{c}
\mathfrak I=(\mathbf{Sig},\operatorname{Sen},\operatorname{Mod},\models)
\\[4pt]
\downarrow
\\[4pt]
K_\Sigma=(N,A,J,\lambda,\rho)
\\[4pt]
\downarrow
\\[4pt]
R=(K_\Sigma,\Gamma,Q)
\\[4pt]
\downarrow
\\[4pt]
C(\Gamma)=\operatorname{Cl}_{J}(\Gamma)
\end{array}
}
$$

with typed candidate generation still open:

$$
g_i(R)\rightarrow\mathcal C_i.
$$

The strongest current conceptual commitments are:

1. certainty is not required;
2. persistent black-box state is not one committed theory;
3. white-box reasoning is temporary reasoning under stipulated assumptions;
4. dependency/support provenance should remain explicit;
5. language change should use formal signature/translation machinery when available;
6. candidate generation, warrant/evaluation, and persistent state update remain separate;
7. “reframe” is a dialogue macro, not an epistemic primitive;
8. the next hard problem is the typed algebra of candidate generation.

## 16. Open questions

1. What is the minimal candidate type system?
2. Can candidate generators be given a complete compositional basis relative to a declared representation language?
3. How should \(\rho\) interact with ATMS-style minimal environments?
4. How should inconsistent or paraconsistent environments be represented outside classical ATMS assumptions?
5. Which observation/report types deserve primitive treatment, if any?
6. Which institution or logic should an executable implementation instantiate first?
7. What exact conditions distinguish conservative definitional extension from substantive concept invention in the chosen logic?
8. How should query transformation be formalized without smuggling an optimization objective into the foundation?
9. Which warrant guarantees attach to which candidate-generation operators?
10. How should the current support graph map into the existing inquiry-graph ontology without conflating public discourse with private epistemic state?
