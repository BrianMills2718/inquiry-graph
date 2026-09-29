# Post-V1 research log: from pattern formation back to epistemic transitions

> **Scope:** curator's reconstruction of the visible dialogue after V1 was created. This is public dialogue provenance, not hidden chain of thought. It records proposals, objections, corrections, and reframings because those changes are part of the inquiry.

## 1. The substantive inquiry resumed

The graph project had branched off from an earlier question: whether there is a principled, possibly exhaustive way to classify the moves by which an embedded observer goes beyond immediate observation.

After V1, the dialogue explicitly returned to that substantive thread. The first question was whether the unresolved middle layer was simply **measurement theory**.

The assistant's initial decomposition was:

$$
\text{world} \to \text{measurement} \to \text{patterns over measurements}.
$$

Measurement theory was treated as a candidate for the first arrow: what variables/distinctions become available to the observer. The second arrow—what structures can be recognized over those measurements—was left open.

Brian repeatedly objected that this sounded like well-trodden territory rather than something to reinvent.

## 2. Pattern Theory was found, then bounded

Research turned to Ulf Grenander's **Pattern Theory** and the Brown school around it. A clarification mattered immediately: “Grenander” and “Brown Pattern Theory” are not competing theories; Brown is the program/school in which Grenander's framework was developed and extended.

Pattern Theory appeared highly relevant because it supplies a general language involving generators, configurations, transformations/invariances, probability/variation, observation/interpretation, and pattern inference.

Two corrections followed.

First, Brian flagged the risk of “smuggling Bronstein” into the spine merely because he had mentioned Michael Bronstein earlier. The assistant agreed and explicitly demoted geometric deep learning: symmetry/invariance overlap is real, but Bronstein is not needed for the foundational problem.

Second, a deeper read of Pattern Theory suggested a boundary: it is strong once a representational/generative vocabulary has been specified, but it does not obviously derive the complete space of representations available to an embedded observer from physics alone.

That left the original representational question intact.

## 3. Predictive equivalence was proposed, then demoted

The next research pass examined computational mechanics, predictive-state representations, information bottleneck ideas, and causal feature learning.

A tempting proposal was:

> patterns or effective states are equivalence classes under predictive or causal consequences.

This has a strong formal basis in causal-state constructions and task-relative abstraction, but Brian objected that it sounded like a criterion for a **good/useful model**, not a definition of what an observer can notice at all.

The assistant accepted the objection. The key correction became:

$$
\text{pattern possibility/discovery}
\neq
\text{optimal/sufficient abstraction}.
$$

Predictive equivalence, causal equivalence, sufficient statistics, and information bottlenecks remained useful as **selection/optimization criteria**, but were removed from the role of foundational ontology of patterns.

## 4. Pattern recognition was separated from induction

Brian returned to the black/white dots example. The decisive point was that a relational property can be available only at the level of a joint configuration even if no individual sensor/atom encodes the whole relation.

This exposed an earlier mistake. If the full finite configuration is already observed, then computing a relation such as

> black and white points occupy separated regions

need not be ampliative. It may be a deterministic relational computation over currently available information.

Therefore:

$$
\boxed{\text{pattern recognition is not automatically induction}.}
$$

This correction matters because much of the earlier conversation had loosely used “projection” or “induction” for any move from tokens to a higher-level pattern.

## 5. Integration, IIT, and the temporalized dots example

The dialogue then asked whether the joint-configuration issue is fundamentally an **integration** problem.

The assistant pointed to information synergy / Partial Information Decomposition and, cautiously, IIT-style irreducibility. Brian clarified that any IIT interest was purely algorithmic; he was not invoking its theory of consciousness.

IIT therefore remained only as a possible mathematical language for partitioning a system and measuring irreducible causal/informational organization. It was not promoted to a learning theory.

Brian then temporalized the dots:

- spatial case: several dots are simultaneously visible;
- temporal case: dot, then dot, then dot, then dot.

This suggested that memory can be viewed abstractly as **temporal integration**. A general recurrence

$$
s_{t+1}=F(s_t,x_t)
$$

can integrate information over time just as a downstream representation can integrate information across spatial sensors.

The assistant then tried to distinguish state update from learning of the update rule, but Brian correctly noticed that the dialogue was drifting away from the original epistemic question.

## 6. Explicit reset: back to “warrant of warrant”

Brian stated the reset directly: the original question was how to formalize **warrant of warrant**, and the conversation risked circling through implementation-level theories of perception and learning.

The white-box / black-box distinction was restored.

- **White-box:** stipulate a world/constraint structure for analysis.
- **Black-box:** an embedded observer has partial evidence and fallible model commitments.

Deduction became cleanly relative:

$$
A,E\models h,
$$

where \(A\) are **assumed**, not “known,” constraints. Brian explicitly corrected the language from known constraints to assumed constraints because certainty is not part of the project.

The foundational question was restated without optimization:

> Under what conditions does evidence \(E\) carry information relevant to a proposition \(h\), and what kind of move is made when commitment changes?

The assistant had repeatedly drifted too early into “which model should be preferred?” or “what is the optimal learning strategy?” Brian pushed the inquiry back to the structural taxonomy of moves.

## 7. Constraint language clarified but did not solve the taxonomy

A useful white-box observation survived:

$$
\text{constraint} + \text{partial observation}
\Rightarrow
\text{restriction elsewhere}.
$$

Information theory, possible-world semantics, and constraint propagation all make versions of this precise.

However, the black-box observer does not have the true constraints handed to it. It proposes and revises hypotheses about them.

This created a natural but incomplete picture:

- deduction: derive consequences under assumed constraints;
- induction: perhaps infer/project empirical constraints;
- abduction: perhaps infer latent/generative structure.

Brian noted that induction and abduction had always blurred for him. The conversation stopped treating historical definitions as authoritative and instead asked for a custom formalism that could be made genuinely **MECE** or otherwise uniquely factorizable.

## 8. “MECE” became a design property, not the name of the object

Voice transcription rendered “MECE” incorrectly several times (“mise,” etc.). Brian clarified that he meant **mutually exclusive, collectively exhaustive**.

This mattered because the project goal became more precise:

> Do not defend induction/deduction/abduction. Find a formal representation in which the classification is exhaustive and non-overlapping by construction.

The first genuinely sharp split was:

$$
K\models h
\quad\text{vs.}\quad
K\not\models h.
$$

But the dialogue wanted more than a trivial entailed/non-entailed split.

A useful target taxonomy emerged:

$$
(\Sigma,G,\theta,x)
$$

or later

$$
(L,C,P,S)
$$

for ontology/language, structure/model-class constraints, model parameters, and instance state.

The important correction was that a complex inference can concern several coordinates at once. Brian suggested treating MECE as a **composition space** rather than forcing every inference into one category.

This led to support profiles:

$$
J(h)\subseteq\{L,C,P,S\}.
$$

## 9. Representation dependence blocked an absolute taxonomy

A deeper stress test showed that the four model levels cannot be metaphysically canonical:

- structure can be encoded as a parameter;
- parameters can be encoded as fixed state;
- ontology variation can be encoded inside a super-ontology.

The language was therefore tightened:

> canonical **relative to a representation contract**, not absolutely canonical.

This was a significant conceptual improvement. It changed the project from searching for a unique ontology of nature to defining a normal form with explicit assumptions about representation.

## 10. State-change algebra simplified the move basis

The dialogue then changed the primitive object again.

Instead of asking whether “projection,” “completion,” “model expansion,” etc. form a MECE basis, it represented the epistemic state as a live hypothesis set.

For fixed universe \(\mathcal U\):

$$
H\rightarrow H'.
$$

Set difference gives unique additions and deletions:

$$
A=H'\setminus H,
\qquad
D=H\setminus H'.
$$

Thus every hard state update is exactly some combination of:

- preserve;
- restrict;
- expand;
- replace.

And replace is just add + remove.

This showed that several previously proposed primitive moves were at the wrong layer:

- **deduction/derive** may be a readout with no semantic state change;
- **reparameterization** may be representationally different but semantically conservative;
- **inductive projection** describes how a candidate proposition is generated, while its hard epistemic effect may simply be restriction;
- **abductive explanation** similarly describes candidate generation, not a unique state-update primitive.

## 11. Current state model and changing universes

The state model was generalized to:

$$
\boxed{K=(\mathcal U,H,\mu)}
$$

where:

- \(\mathcal U\): current semantic/model universe;
- \(H\): live hypotheses;
- \(\mu\): optional graded support.

When the universe changes, introduce an alignment map:

$$
\Phi:\mathcal U\rightarrow\mathcal U'.
$$

Then define:

$$
A=H'\setminus\Phi(H),
\qquad
D=\Phi(H)\setminus H'.
$$

The current candidate factorization is therefore:

$$
\boxed{
\Delta K=(\Phi,A,D,\mu\rightarrow\mu').
}
$$

This is the strongest current structural result. The completeness of \(A,D\) is simple set theory **given a fixed semantic alignment**. The hard problem is moved to the semantics of \(\Phi\), not hidden.

## 12. Three layers were separated

The most important endpoint is the separation:

$$
\boxed{
\text{candidate generation}
\neq
\text{warrant/evaluation}
\neq
\text{state update}.
}
$$

Candidate generation:

$$
g:(K,E)\rightarrow\mathcal C
$$

produces possibilities. This is where induction, abduction, analogy, model invention, causal discovery, category formation, and extrapolation most naturally belong.

Warrant/evaluation asks what licenses a change in commitment.

State update records the resulting \(\Phi,A,D,\Delta\mu\).

This separation prevents a named method such as “Bayesian updating” or “abduction” from silently carrying both content generation and its justification.

## 13. Warrant became a conditional certificate

Brian had earlier objected to Bayesian formulations that merely relocate warrant into priors, likelihoods, or model choices. The current warrant layer makes such assumptions explicit.

A proposed warrant certificate is:

$$
\operatorname{Cert}(\tau)=(A_W,G_W,\pi),
$$

where \(A_W\) are assumptions, \(G_W\) is the claimed guarantee, and \(\pi\) is the argument/proof/evidence that the assumptions deliver that guarantee for the move.

Warrant therefore means:

> under these assumptions, this move has this specified justification/guarantee.

It does **not** mean “the proposition is now known with certainty.”

The “warrant of warrant” regress becomes inspectable because the assumptions \(A_W\) can themselves be represented as hypotheses requiring their own support/certificates. The current project does not claim to terminate that regress.

An AGM-style program—postulates followed by representation theorems—and formal-learning-style performance guarantees were identified as useful precedents, not completed results.

## 14. Current endpoint

The working research formulation is now:

> **A representation-contract-relative factorization of epistemic state transitions, plus a separate warrant semantics, while candidate-generation factorization remains open.**

The central open formal problem is:

$$
\boxed{
\text{Can candidate generation }g:(K,E)\rightarrow\mathcal C
\text{ be given a small compositional / uniquely factorizable basis?}
}
$$

The original deduction/induction/abduction question remains visible as provenance, but is now reframed rather than falsely resolved.

## 15. The conversation itself became a candidate-generation test case

After the first documentation update, the inquiry returned to the question of what kind of process the dialogue itself exemplified. The working description became **theoretical model construction under conceptual constraints**.

The important observation was that this conversation is not primarily updating from fresh physical measurements. It repeatedly:

- generates candidate formalisms;
- tests them against counterexamples and desiderata;
- searches existing literature for established machinery;
- changes the question space when the old formulation is too coarse;
- revises the representation language itself.

That made the dialogue a natural adversarial corpus for the still-open candidate-generation layer.

A provisional list such as “differentiate, abstract, compose, reframe, complete, extend, analogy” was immediately treated with suspicion. In particular, Brian objected that **reframe** was doing too much work and that the problem looked more like:

1. how to construct expressions/concepts inside an existing concept space; and
2. how genuinely new conceptual vocabulary enters the space.

This reopened the literature question rather than promoting another informal taxonomy.

## 16. Concept generation stress-tested the meta-model

The next literature-oriented pass connected the inquiry to description logics, Formal Concept Analysis, anti-unification, and inductive logic programming/predicate invention.

The strongest distinction was:

$$
\text{concept construction}
\neq
\text{concept invention}.
$$

A further refinement split three cases:

$$
\boxed{
\text{expression construction}
\neq
\text{definitional extension}
\neq
\text{substantive predicate invention}.
}
$$

This stress test exposed that the old \(\mathcal U\) coordinate was overloaded. It had been used for vocabulary, expressible propositions, model space, and live hypotheses.

An intermediate repair proposed:

$$
K=(\Sigma,T,W,\rho,E,Q),
$$

with \(\Sigma\) for signature, \(T\) for explicit theory/assumptions, \(W\) for compatible models, \(\rho\) for graded support, \(E\) for evidence, and \(Q\) for task/query.

Institution theory was identified as established machinery for the separation:

$$
\mathfrak I=
(\mathbf{Sig},\operatorname{Sen},\operatorname{Mod},\models).
$$

It also supplied a more disciplined replacement for a generic representation map: signature morphisms with induced sentence/model translations and a satisfaction condition.

At this stage, “reframe” was explicitly demoted from foundational primitive to dialogue-level macro. Depending on the case, a reframe might mean \(Q\to Q'\), \(\Sigma\to\Sigma'\), theory revision, or a combination.

## 17. The \(T\) versus \(W\) formulation was corrected by the white-box/black-box intuition

Brian then objected that the intermediate \(T\) language sounded too much like a theory the observer actually commits to.

The intended semantics were closer to:

> assume these propositions for the purpose of this branch of reasoning and inspect what follows.

That forced another distinction:

\[
\boxed{
\text{persistent epistemic state}
\neq
\text{temporary active assumption context}.
}
\]

The black-box observer should be able to maintain multiple alternative assumptions/hypotheses simultaneously. A white-box reasoning move selects or stipulates one set temporarily without promoting it to certainty.

This made **Assumption-based Truth Maintenance Systems (ATMS)** an unusually close existing analogue and motivated a targeted research pass before changing the documentation again.

## 18. ATMS and institution theory supplied orthogonal pieces of the revised meta-model

The ATMS comparison strengthened the model rather than opening another unrelated branch.

ATMS supplies a structure in which:

- multiple alternative assumptions coexist;
- an **environment** is a set of assumptions;
- explicit justifications propagate consequences;
- a datum's **label** records minimal consistent assumption environments that support it;
- one can inspect consequences under a selected environment without treating that environment as the uniquely believed theory.

This maps cleanly onto the white-box/black-box distinction.

The current persistent state is therefore proposed as:

$$
\boxed{
K_\Sigma=(N,A,J,\lambda,\rho)
}
$$

where \(N\) are represented nodes, \(A\) assumable nodes, \(J\) justification/dependency structure, \(\lambda\) minimal supporting environments, and \(\rho\) optional graded support.

A temporary reasoning branch selects:

$$
\Gamma\subseteq A
$$

and obtains:

$$
C(\Gamma)=\operatorname{Cl}_{J}(\Gamma).
$$

The reasoning episode is now:

$$
\boxed{
R=(K_\Sigma,\Gamma,Q).
}
$$

The query \(Q\) is kept outside persistent epistemic state because changing the current problem need not change what the observer represents or supports.

The previous top-level evidence coordinate \(E\) was also demoted. Observation reports, testimony, instrument readings, and research findings can be represented as typed nodes with provenance and dependencies rather than being treated as epistemically privileged merely because they are called “evidence.”

Institution theory and ATMS are therefore **orthogonal**:

- institution theory: what language/models/semantic translations are;
- ATMS: under which assumption combinations a proposition is supported.

Theory graphs remain relevant for later modular-theory engineering, but are not added as another foundational layer yet.

The current architecture is:

$$
\boxed{
\begin{array}{c}
\mathfrak I=(\mathbf{Sig},\operatorname{Sen},\operatorname{Mod},\models)\\
\downarrow\\
K_\Sigma=(N,A,J,\lambda,\rho)\\
\downarrow\\
R=(K_\Sigma,\Gamma,Q)\\
\downarrow\\
C(\Gamma)=\operatorname{Cl}_J(\Gamma)
\end{array}
}
$$

with typed candidate generation still open:

$$
g_i(R)\rightarrow\mathcal C_i.
$$

This is the current endpoint. It preserves the earlier set-difference result as a semantic-state special case, while replacing the flat live-hypothesis set as the primary representation of persistent epistemic organization.

## 19. The seven candidate types were themselves overfactored

The next pass tried to make candidate generation concrete by assigning each generated item a type. That immediately exposed another bad factorization.

The earlier candidate list mixed artifact kinds with epistemic roles. In particular, **assumption** is usually a role played by a sentence or theory in a reasoning context, not the same ontological kind as expression, model, or mapping.

The better representation was a **candidate footprint**: a generated package can involve several formal artifact kinds simultaneously.

This preserved the earlier composition-space lesson. A latent-variable proposal may introduce a declaration, expressions constraining it, and changes to a theory at the same time. Forcing the move into one exclusive category would lose information.

## 20. MMT collapsed the formal artifact taxonomy

A literature check against LF/MMT substantially simplified the representation layer.

An MMT-like theory graph can represent:

- theories;
- declarations/symbols;
- objects, including formulas, terms and proofs;
- morphisms, including theory translations and models.

LF then becomes one possible logical foundation represented inside that modular framework rather than a separate epistemic layer.

This means several previously separate candidate types collapse at the formal-representation level. The new boundary is instead:

\[
\boxed{
\text{draft candidate}
\rightarrow
\text{formal elaboration/checking}
\rightarrow
\text{formal artifact or failure}.
}
\]

The key correction is:

\[
\boxed{
\text{well formed}
\neq
\text{warranted}.
}
\]

Formal type/proof checking cannot tell us whether a candidate should have been invented, trusted, extrapolated, or selected.

## 21. MECE was generalized into primitive-factorization analysis

Brian explicitly identified a recurring thinking pattern: propose primitives, then notice that the decomposition is overfactored or underfactored and repair it.

MECE was therefore demoted from the general method to one special case appropriate to partitions.

The broader strategy became **canonical/primitive factorization**: search for a decomposition that is complete, nonredundant, compositional, sufficiently independent, and—where the representation permits—canonical.

The dialogue developed three diagnostics:

- **underfactored**: one factor bundles distinctions that matter;
- **overfactored**: several factors are redundant or distinctions at the wrong level;
- **misfactored**: the decomposition mixes unlike dimensions, such as formal type and epistemic role.

Canonicality remains relative to a declared representation/equivalence contract.

## 22. Strategy, metareasoning and reflection became explicit

When Brian asked where canonical factorization lives as a cognitive strategy, the inquiry moved above the operator layer.

The resulting distinction is:

\[
\boxed{
\text{operator}
\neq
\text{strategy controlling operators}.
}
\]

A strategy is represented descriptively as a policy over reasoning history and available operators. Rational metareasoning provides a stronger literature-backed specialization in which strategy selection is optimized under costs/resources, but optimization is not required in the base definition.

The later self-application observation introduced **reflection**. Rather than hard-code permanent levels \(L_0,L_1,L_2,\ldots\), meta-level status is treated as relational: one reasoning episode is meta with respect to another artifact or episode when it is explicitly **about** that target.

The key architectural property is **closure under self-description**:

\[
\text{strategies, reasoning episodes and the meta-model itself can be represented as targets}.
\]

This makes it possible to use the same framework both abstractly and empirically:

- define strategies formally;
- instantiate them on conversation trajectories;
- mark reflective episodes;
- later evaluate which strategies and meta-strategies correlate with useful outcomes.

The current extension is documented in [metareasoning-strategy-reflection.md](metareasoning-strategy-reflection.md).

## 23. Candidate generation became a constrained-search interface

The next research pass compared the open candidate-generation problem with program synthesis, CEGIS, meta-interpretive learning and formal abduction.

The key result was another factorization:

\[
\boxed{
\text{generative space}
\neq
\text{construction operators}
\neq
\text{search/control strategy}
\neq
\text{formal checking}
\neq
\text{warrant}.
}
\]

Rather than searching for one universal list of creativity operators, the project now defines a **draft-generation system** for each reasoning episode:

\[
\mathcal G_R=
(\mathcal D_R,d_0,\mathcal O_R,\rightarrow_R),
\]

with reachable draft space

\[
\operatorname{Reach}(R)=
\{d\mid d_0\xrightarrow{\mathcal O_R *}d\}.
\]

A strategy \(\pi\) explores that space. Formal elaboration checks whether a draft can become a valid formal artifact. Evaluators return feedback such as counterexamples, failed constraints, empirical mismatch or warrant requirements. Warrant remains a separate conditional-justification layer.

This reframed the universal object from “the operator set” to **the interface between search space, operators, strategy, elaboration, evaluation and warrant**.

## 24. Canonical factorization became the worked strategy trace

The founding dialogue was then reconstructed as one explicit instance of that interface.

The trace runs through:

1. deduction/induction/abduction as an initial partition;
2. state/parameter/structure/ontology as a target-type decomposition;
3. power-set composition after joint cases broke exclusivity;
4. representation-relative canonicality after recoding counterexamples;
5. add/delete state-delta factorization;
6. ATMS-style persistent support plus temporary assumption contexts;
7. correction of candidate types that mixed artifact type with epistemic role;
8. MMT/LF-style collapse of formal artifact types;
9. recognition of the repeated repair loop as the canonical-factorization strategy itself.

At each stage the dialogue can be represented as:

\[
\text{draft}
\to
\text{evaluation}
\to
\text{diagnostic feedback}
\to
\text{repair operator}.
\]

This is the first complete strategy trace instantiated against the evolving meta-model. It is documented in [candidate-generation-interface.md](candidate-generation-interface.md).

## 25. Warrant was refactored rather than restarted

The later meta-model made the earlier warrant proposal easier to state precisely.

The original certificate

\[
\operatorname{Cert}(\tau)=(A_W,G_W,\pi)
\]

survived, but the old target \(\tau\) had been doing too much work. After separating draft generation, formal elaboration, evaluator feedback, support state, epistemic updates and strategy selection, the warrant question could be normalized around a typed **epistemic action**.

The resulting factorization is:

\[
\boxed{
\text{support}
\neq
\text{warrant}
\neq
\text{license}
\neq
\text{update}.
}
\]

Support records reasons/dependencies. Warrant says those reasons are adequate, under an explicit regime and assumptions, for a specified epistemic action with a specified guarantee. License is the derived context-relative status that the action is permitted. Update is the action actually executed against persistent state.

The proposed judgment is:

\[
\boxed{
\mathfrak W;A\vdash_{\pi} a:G.
}
\]

This reads: under warrant regime \(\mathfrak W\) and assumptions \(A\), certificate/support \(\pi\) warrants epistemic action \(a\) with guarantee or entitlement \(G\).

## 26. Research tightened the warrant factorization

Justification Logic supplied the precedent for explicit reasons of the form \(t:F\). Structured argumentation supplied the missing defeasibility point: an argument can exist while later attack/defeat changes its acceptability. Hoare logic and assume-guarantee contracts closely match the conditional assumption/guarantee shape. Formal learning theory supplies method-level guarantees under explicit problem-class and sampling assumptions.

This research produced two further factorization corrections.

First, “candidate warrant,” “transition warrant,” and “strategy warrant” do not need to be primitive warrant kinds. They become instances of one polymorphic action-targeted judgment, such as accept(h), raiseSupport(h,δ), or selectStrategy(π).

Second, the earlier temptation to add an independent warrant scope field appears overfactored. Scope is normally carried by the applicability assumptions \(A\) and by the quantification/type of guarantee \(G\).

Defeaters are also kept outside the minimal warrant tuple and represented in the support/argument graph, so nonmonotonic warrant can lose a previously derived license when new defeating information arrives.

The current formulation is documented in [warrant-license-interface.md](warrant-license-interface.md).

## 27. Post-warrant literature pass: actions and graded support

After the warrant/license refactoring, the next two open questions were:

1. what should count as a primitive epistemic action; and
2. how should multiple supports/warrants interact with graded support \(\rho\)?

The research pass drew on AGM/Katsuno–Mendelzon belief change, Dynamic Epistemic Logic, provenance semirings, probabilistic ATMS work, and Jeffrey-style uncertain updating.

The main action-side result is that a fixed universal verb list is probably the wrong abstraction. AGM already shows that familiar change operations can be compositionally related, while Katsuno–Mendelzon distinguish revision from update based on the semantics of what changed. Dynamic Epistemic Logic likewise treats actions as structured events with preconditions and model-transforming semantics.

The project now models an epistemic action schematically as a partial state transducer:

\[
a:S\rightharpoonup S\times O_a
\]

with explicit preconditions and an effect footprint over state coordinates. “Primitive” then means primitive **relative to a declared action algebra and representation**, not metaphysically primitive.

The graded-support result is similarly compositional. Instead of attaching an independent scalar to every derived node, preserve symbolic support provenance first. Alternative support routes and joint support are distinct operations:

\[
P_h=(x_a\otimes x_b)\oplus x_c.
\]

This echoes both ATMS labels and provenance-semiring work. Numeric or ordinal support then comes from a typed interpretation:

\[
\rho_\eta:\mathsf{Prov}\to V_\eta
\]

under an explicit uncertainty regime \(\eta\).

Probabilistic ATMS results are especially important here: probabilities can be placed on assumptions while derived-node support is computed through shared label/provenance structure, which avoids pretending derived nodes are independent.

The current synthesis is documented in [epistemic-actions-support-algebra.md](epistemic-actions-support-algebra.md).

This pass intentionally does **not** add new nodes to the source-grounded founding dialogue graph. The research findings are being introduced in the current assistant response rather than recovered from an already-recorded visible turn. Keeping the research note separate avoids fabricating source provenance. A later transcript reconciliation/update can ground these claims once the visible turn exists in the export.

## 28. Positive support algebra was made concrete

The next pass asked which algebra actually matches ATMS-style minimal environments.

For primitive assumption tokens \(X\), define positive support values as finite antichains of finite assumption sets:

\[
\mathsf{Supp}(X)=
\operatorname{Antichain}(\mathcal P_{\mathrm{fin}}(X)).
\]

Alternative support is:

\[
A\oplus B=
\operatorname{Min}(A\cup B),
\]

and joint support is:

\[
A\otimes B=
\operatorname{Min}
\{E\cup F:E\in A,F\in B\}.
\]

This is exactly the irredundant/minimal-witness construction known from provenance work, and it forms the free distributive lattice over \(X\), equivalently positive Boolean provenance modulo logical equivalence.

That makes it a particularly clean fit for ATMS labels, which already store only subset-minimal supporting environments.

The important information-loss boundary is explicit: this algebra preserves minimal support sets but intentionally discards derivation multiplicity, proof-tree identity, and repeated-use counts.

## 29. First concrete graded regime

A small executable reference interpretation was added.

Each primitive assumption \(x\) receives an independent Bernoulli probability \(p_x\). A support antichain denotes the upward-closed event that at least one minimal support environment is present. Minimal nogoods denote inconsistent worlds.

The reference grade is:

\[
\rho_{\mathrm{Bern}}(A)
=
P(
\llbracket A\rrbracket
\mid
\text{no nogood holds}
).
\]

This is deliberately a probability of the **support condition**, not automatically \(P(h)\) for the supported proposition \(h\). Identifying the two requires an additional warrant/semantic adequacy claim.

The implementation is in src/inquiry_graph/support.py, with tests covering antichain normalization, semiring/lattice laws, absorption, overlapping alternatives, and consistency conditioning.

The next algebraic frontier is negative/defeasible support rather than further refinement of the positive-support algebra.

## 30. Defeat was separated from positive support

The next pass checked the obvious existing formalisms before attempting a negative-support algebra.

The result is that “negative support” was the wrong primitive target. Pollock distinguishes **rebutting** defeaters, which support an opposing conclusion, from **undercutting** defeaters, which attack the inferential connection itself. ASPIC+ makes the structure still more explicit by distinguishing rebutting attacks on defeasible conclusions, undercutting attacks on defeasible inference steps, and undermining attacks on ordinary premises. ASPIC+ also separates **attack** from **defeat**, because preferences and attack type can determine whether an attack succeeds.

Assumption-Based Argumentation is especially close to the ATMS-like assumption layer: assumptions have contraries, and an assumption/set is attacked when another supported argument derives one of those contraries.

The architecture is therefore:

[
\boxed{
\text{positive support provenance}
+
\text{structured attacks}
+
\text{attack-to-defeat resolution}
+
\text{abstract acceptability semantics}
}
]

rather than signed support values.

## 31. First executable defeat semantics

A small research module now represents arguments carrying the existing positive SupportAntichain and explicit successful typed defeats.

The first acceptability semantics is Dung grounded semantics:

[
Gr=\operatorname{lfp}(F),
]

where the characteristic function returns arguments whose defeaters are themselves defeated by the candidate defending set.

The implementation intentionally consumes **successful defeats**, not raw attacks. Automatic ASPIC+/ABA attack construction and preference-sensitive attack-to-defeat resolution remain upstream and open.

This keeps the layers clean:

[
\text{argument exists and has positive support}
\neq
\text{argument is dialectically acceptable}.
]

The integration is documented in [defeat-argumentation-integration.md](defeat-argumentation-integration.md).

As with the previous literature-driven passes, this research note is not retroactively inserted into the stored source-grounded dialogue graph; the current live turn can be grounded later during transcript reconciliation.

## 32. ABA versus ASPIC+ was tested as a requirements benchmark

Rather than selecting a framework by general reputation, the next pass encoded six discriminating cases in both families:

1. assumption contrary;
2. conclusion rebuttal;
3. rule undercutting;
4. premise attack;
5. preference-sensitive conflict;
6. strict versus defeasible inference.

The comparison showed that ABA is native for the assumption-centred cases and can systematically encode the richer defeasible cases by reifying rule applicability or defeasible availability as typed assumptions. ASPIC+ represents rebuttal, undercutting, undermining, strict/defeasible rules and preferences more directly.

The key literature comparison agrees with this result: ASPIC+ can represent ABA, while the ABA approach deliberately translates defeasible rules, preferences, rebutting and undercutting behavior into rules plus assumptions so attack reduces to premise attack.

The architectural consequence is not an exclusive framework choice:

[
\boxed{
\text{ABA execution substrate}
+
\text{ASPIC+-compatible semantic metadata}
+
\text{Dung acceptability}
}
]

The important constraint is reversibility. Generated ABA assumptions for defeasible rules must retain typed provenance back to their source rule and semantic role. Otherwise a rule undercut becomes indistinguishable from an ordinary premise attack.

The full benchmark and revisit conditions are documented in [aba-aspic-benchmark.md](aba-aspic-benchmark.md).

## 33. Minimal ABA construction bridge was implemented

The benchmark decision was then instantiated directly rather than left as architecture prose.

The executable ABA layer now contains:

[
mathcal B=(R,A,overline{cdot})
]

with Horn-style rules, explicit assumptions, contraries, and source/role metadata on assumptions generated from richer defeasible structures.

Support propagation reuses the existing antichain algebra. For each derivable conclusion, the framework computes its subset-minimal assumption environments, then constructs one quotient argument per:

[
(	ext{conclusion},	ext{minimal environment}).
]

This deliberately identifies deductions that have the same conclusion and minimal support set. That is consistent with the current support-provenance abstraction, but it is an explicit information-loss boundary: a future framework requiring comparison of distinct proof trees with identical supports would need finer argument identity.

Basic ABA attacks are generated when an argument concludes the contrary of an assumption used by another argument. The attacked assumption carries its reconstructed attack origin (`undermine`, `undercut`, or `rebut`), so the ABA execution substrate does not erase the richer semantic distinction.

A helper compiles a defeasible rule into a strict rule guarded by a typed applicability assumption while retaining the source rule identifier. Basic-ABA attacks then project directly to the already implemented Dung defeat framework.

The Windows repository agent remained offline during this pass, so the new ABA scenarios were replicated and executed independently rather than claimed as a full repository test run.

## 34. The argument-identity boundary was stress-tested before preferences

The next pass revisited an implementation shortcut in the ABA core: distinct deductions with the same conclusion and same supporting assumption environment were being collapsed into one executable argument.

A first instinct was to reify full derivation DAGs before proceeding. A literature check changed that conclusion.

ABA attack semantics is deliberately assumption-centred: an attacking deduction matters through the conclusion it derives, while a target matters through the assumptions it uses. ABA+ adds preferences over assumptions, not ASPIC+-style last-link preferences over derivation trees.

Therefore, for the currently selected ABA/ABA+ semantics, two deductions with identical conclusion and assumption support are dialectically equivalent.

The project now treats:

[
(	ext{conclusion},	ext{assumption support})
]

as an explicit **ABA dialectical quotient**, rather than pretending it is the identity of the underlying proof object.

This preserves the layered distinction:

[
oxed{
	ext{formal derivation identity}

eq
	ext{ABA dialectical argument identity}.
}
]

The richer derivation structure becomes mandatory only if later semantics make the collapsed deductions observably different—for example ASPIC+ subargument attack, unguarded inference-step attack, last-link preferences, proof-sensitive warrant, or exact explanation requirements.

This decision is recorded both in [argument-identity-boundary.md](argument-identity-boundary.md) and ADR 007.

## 35. Preference work exposed a second representation boundary

The planned next step was initially described as "implement ABA+ preferences."

A fresh literature check showed that this would have been too casual.

ABA+ does not merely filter binary attacks. If an attacking deduction relies on an assumption strictly less preferred than the attacked assumption, ABA+ may **reverse** the attack.

Formally, if:

\[
S\vdash\overline a,
\]

then the attack is normal when:

\[
\nexists s\in S:s<a,
\]

and preference-reversed when:

\[
\exists s\in S:s<a.
\]

The important new result is representational. Recent work by Dimopoulos et al. (2026) shows that general ABA+ is naturally set-to-set and does not in general have the ordinary binary Dung instantiation available for basic ABA. Their Hyper Argumentation Frameworks use:

\[
R\subseteq 2^A\times(2^A\setminus\{\varnothing\}).
\]

That makes a naive "reverse this one argument edge" implementation potentially false to ABA+.

The project therefore introduced an explicit preference-regime boundary.

For the current binary Dung pipeline, use only the **normal-attack preference condition**:

\[
A\hookrightarrow_{\mathfrak P_N}B
\iff
A\leadsto B
\land
\nexists\alpha\in\operatorname{Supp}(A):
\alpha<\beta,
\]

where \(\beta\) is the attacked assumption.

Attacks failing this condition are recorded as blocked, not reversed.

This is deliberately not called full ABA+.

Full ABA+ / set-to-set attack semantics is preserved as GitHub issue #18 rather than silently approximated.

## 36. Preference filtering became executable and auditable

The ABA implementation now contains a finite strict preference relation over assumptions.

The relation is transitively closed and rejects cycles.

Every basic ABA attack receives an audit result:

\[
(attack,status,blockingPreferences),
\]

with:

\[
status\in\{\text{defeat},\text{blocked}\}.
\]

Successful attacks can still be projected into the existing Dung defeat framework.

This gives the first explicit preference-sensitive dialectical path while keeping the richer ABA+ branch separate.

The project-management consequence is that the next milestone should now be **warrant/license integration and end-to-end cases**, rather than importing further adjacent argumentation machinery.

The durable "forest" view is now maintained in [project-status.md](project-status.md), while the two richer escalation paths are tracked by GitHub issues #17 and #18.

## 37. Warrant/license became executable for one typed defeasible regime

The next integration pass connected dialectical acceptability to the earlier action-targeted warrant judgment.

A naive rule of the form:

\[
\text{grounded-IN argument}
\Rightarrow
\text{any epistemic action is licensed}
\]

was rejected.

That would collapse argument acceptability into universal epistemic permission.

The first executable regime is therefore deliberately typed:

\[
\mathfrak W_{\mathrm{grounded\text{-}dialectical}}.
\]

It requires:

1. a certificate argument that is grounded-IN;
2. an action kind belonging to the regime's defeasible action vocabulary;
3. guarantee kind = defeasible acceptability.

Current actions include retaining a candidate, raising support, or using a claim defeasibly.

Unconditional acceptance and deductive truth claims remain outside this regime.

The executable license step separately checks current applicability assumptions. The first implementation uses exact set inclusion:

\[
A\subseteq C
\]

as a deliberately weak approximation to:

\[
C\models A.
\]

Thus the code now preserves:

\[
\boxed{
\text{acceptability}
\neq
\text{conditional warrant}
\neq
\text{current license}
\neq
\text{execution}.
}
\]

No epistemic state update is performed automatically.

## 38. The first vertical slice now composes end to end

A regression benchmark now exercises:

\[
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
\text{typed warrant}
\to
\text{license}.
\]

Cases cover:

- unchallenged defeasible support;
- successful defeating support;
- preference-blocked weak counterargument;
- unmet warrant applicability assumptions;
- two alternative support routes where only one is defeated;
- preference changes that alter license while leaving positive support unchanged.

This is the first point at which the project has a complete executable research-layer vertical slice.

The benchmark also makes the remaining gaps concrete rather than ontological: deductive, graded, measurement/testimony, statistical/PAC and strategy-performance warrant regimes still need executable instances.

The project-management rule is now:

\[
\boxed{
\text{expand benchmark coverage}
>
\text{expand ontology}.
}
\]

See [end-to-end-warrant-benchmark.md](end-to-end-warrant-benchmark.md) and ADR 009.

## 39. Numeric support received a deliberately weak warrant regime

The next benchmark gap was graded support.

The positive-support layer already had an independent-Bernoulli interpretation:

\[
\rho_{\mathrm{Bern}}:
\mathsf{Supp}(X)\to[0,1].
\]

The key design question was what epistemic action such a number should license.

The project explicitly rejected an implicit global confidence threshold.

Even:

\[
\rho=0.99
\]

does not, by itself, warrant accepting the proposition.

The first graded-support warrant regime therefore licenses only:

\[
\operatorname{recordSupportGrade}(h,\rho).
\]

Its guarantee is descriptive: the recorded value equals the support-event probability under the explicit independent-Bernoulli model.

Any later action policy that consumes the number must be a separate warrant regime with explicit assumptions, decision rule, risk semantics and guarantee.

This required one useful generalization of the executable warrant interface. The certificate field had been named specifically for argument certificates; it is now regime-neutral so the same warrant schema can target argument IDs, proof objects, support computations, calibration certificates, statistical results or other typed certificate objects.

The compatibility alias for the original dialectical argument field is retained for existing callers.

This is recorded in ADR 010 and the end-to-end benchmark.

## 40. Deductive warrant was instantiated as an actually checked fragment

The next benchmark cell was deduction.

Rather than introducing a boolean field saying a proof had been checked, the project added a small executable strict-Horn checker.

A proof certificate contains:

\[
(\Gamma,R,h),
\]

where \(\Gamma\) is the explicit premise set, \(R\) is a finite strict-Horn rule set and \(h\) is the claimed conclusion.

The checker computes:

\[
\operatorname{Cl}_R(\Gamma)
\]

and accepts the certificate exactly when:

\[
h\in\operatorname{Cl}_R(\Gamma).
\]

The associated warrant regime licenses only:

\[
\operatorname{derive}(h)
\]

with guarantee:

\[
\text{truth preservation relative to the explicit premises}.
\]

The warrant assumptions must include the proof premises, while the license step separately checks whether those assumptions are currently active.

This yields the intended distinction:

\[
\boxed{
\text{valid derivation}
\neq
\text{premises accepted}.
}
\]

The strict-Horn language is a benchmark implementation, not a commitment to Horn logic as the final formal representation. Richer proof checkers can later plug into the same action-targeted warrant interface.

This is recorded in ADR 011.

## 41. Measurement and testimony were added as model-relative evidence-channel regimes

The next benchmark expansion targeted measurement and testimony.

The literature check reinforced a distinction already implicit in the project.

Metrology does not treat a measurement result as an exact truth statement. The GUM/VIM tradition makes measurement result, uncertainty, calibration and traceability explicit parts of the measurement account.

Formal testimony models likewise treat source reliability through an explicit probabilistic model. Reliability is not simply one global scalar attached to a person independently of domain or reference class.

The executable benchmark therefore adds two deliberately weak warrant regimes.

### Measurement

A certificate records:

\[
(q,v,u,\text{unit},\text{calibration reference},\text{model reference})
\]

where \(u\) is standard uncertainty.

The warrant may license only recording the measurement result with its uncertainty/provenance.

It does not license accepting the exact proposition:

\[
q=v.
\]

### Testimony

A source model records, for one explicit reference class:

\[
P(R^+\mid H)
\]

and:

\[
P(R^+\mid\neg H).
\]

Together with an explicit prior it yields:

\[
P(H\mid R^+).
\]

The warrant may license only recording that posterior under the declared model.

It does not license accepting \(H\), and it does not generalize the source's reliability to unrelated reference classes.

This extends the benchmark without adding a new top-level ontology. It is recorded in ADR 012.

## 42. Statistical warrant was instantiated as a finite-class theorem certificate

The next benchmark cell was statistical/PAC warrant.

Rather than attaching a generic “confidence” number to a predictor, the project implemented a standard finite-class uniform-convergence theorem.

For bounded loss in \([0,1]\), finite hypothesis class \(\mathcal H\), sample size \(m\), and confidence parameter \(\delta\), the certificate computes:

\[
\epsilon=
\sqrt{
\frac{\log(2|\mathcal H|/\delta)}{2m}
}
\]

and records the theorem-level bound:

\[
L_D(h)\le L_S(h)+\epsilon
\]

with probability at least:

\[
1-\delta,
\]

simultaneously for all \(h\in\mathcal H\).

The implementation clips the reported upper loss bound at \(1\).

The important architectural point is that the theorem calculation does not establish its own applicability assumptions.

Conditions such as:

- i.i.d. sampling;
- bounded loss;
- declared finite hypothesis-class size;
- no unmodelled train/deployment shift;

remain explicit warrant assumptions/current-context conditions.

The regime may license only recording the generalization bound.

It does not license using the predictor or accepting any proposition about its future performance without an additional decision/warrant regime.

This is recorded in ADR 013.

## 43. Strategy selection became a first-class warrant target

The final planned benchmark family targeted strategy selection itself.

A strategy-performance certificate compares one candidate strategy with one baseline on paired tasks using a declared normalized utility in \([0,1]\).

For task \(i\):

\[
D_i=u_i(\pi)-u_i(\pi_0)\in[-1,1].
\]

Under i.i.d. task sampling, Hoeffding yields a lower confidence bound:

\[
E[D]
\ge
\bar D
-
\sqrt{
\frac{2\log(1/\delta)}{n}
}.
\]

The warrant regime may license:

\[
\operatorname{selectStrategy}(\pi)
\]

only when this lower bound is strictly positive.

Task-distribution stability and adequacy of the utility definition remain explicit warrant assumptions.

The implementation deliberately requires any reasoning cost to be incorporated into the declared normalized utility before evaluation. It does not add raw quality and raw cost quantities with incompatible units.

This is recorded in ADR 014.

## 44. Architecture checkpoint: stop expanding by default

With strategy-performance added, the executable benchmark now spans several genuinely different guarantee types:

- defeasible acceptability;
- preference-sensitive defeat;
- graded support reporting;
- checked deduction;
- measurement uncertainty/calibration;
- testimonial source reliability;
- statistical generalization;
- strategy-performance selection.

The fact that these heterogeneous cases fit the same action-targeted warrant interface is evidence that the factorization is useful enough to test empirically.

The project therefore changes phase.

New formal layers should now require a concrete failing benchmark/use case.

The next work is:

1. integrated verification;
2. benchmark-driven failure analysis;
3. source reconciliation;
4. empirical usefulness evaluation.

The detailed checkpoint is in [architecture-reassessment.md](architecture-reassessment.md).

## 45. Candidate-generation mapping test

The candidate-generation landscape pass was followed by an explicit stress test against five mature frameworks:

1. program synthesis / CEGIS;
2. Meta-Interpretive Learning;
3. anti-unification;
4. HR automated theory formation;
5. computational conceptual blending.

The revised interface:

\[
\mathcal G_R=
(
\mathcal A_R,
\mathcal L_R,
\mathcal D_R,
B_R,
\mathcal O_R,
\to_R,
V_R
)
\]

was sufficient for all five without adding another top-level coordinate.

A concrete generation episode is now distinguished from the reusable regime:

\[
E_G=(R,\mathcal G_R,d_0).
\]

The mapping produced three important refinements.

First, \(\mathcal A_R\) may be a typed heterogeneous artifact ontology. HR interleaves concepts, conjectures, proofs and countermodels.

Second, \(d\in\mathcal D_R\) may be a graph-structured draft state rather than one candidate object.

Third, and most importantly, transformationality is representation-relative. Predicate invention or concept invention is not automatically a \(\mu\)-transition if the current meta-language already supports generation of fresh declarations.

Therefore:

\[
\boxed{
\text{new object-language symbol}
\not\Rightarrow
\text{new generative meta-language}.
}
\]

Use:

\[
\mu:\mathcal G_R\to\mathcal G'_R
\]

only when the represented generative regime itself changes.

The mapping also sharpened the warrant boundary:

\[
\boxed{
\text{generator warrant}
\neq
\text{candidate-content warrant}.
}
\]

Generator warrants may concern coverage, completeness, least-generality, convergence, termination or cost; they do not establish the truth of generated candidates.

This result is recorded in ADR 016 and [candidate-generation-framework-mappings.md](candidate-generation-framework-mappings.md).

## 46. Cross-framework candidate-generation glue is mostly established prior art

After the five-framework mapping, the remaining question was how heterogeneous generators should interoperate.

A dedicated landscape pass found mature precedents for nearly every part of this problem:

- blackboard systems for heterogeneous knowledge sources over shared state;
- Hayes-Roth-style blackboard control for deciding which source/action should run next;
- Michalski multistrategy learning for task-adaptive integration of inference strategies;
- Rice-style algorithm selection and portfolios for choosing algorithms by task features/performance;
- hyper-heuristics for selecting or generating heuristics;
- algorithm configuration for tuning generator parameters;
- PRODIGY for integrated planning plus multiple learning mechanisms over common knowledge structures;
- Soar for impasse-driven subgoaling and learned procedural rules;
- computational reflection for modifying reasoning machinery itself;
- COMPOSER/metareasoning for the utility of learned control knowledge.

The project therefore adopts:

\[
\boxed{
\text{typed blackboard}
+
\text{generator portfolio}
+
\text{explicit controller}
+
\text{reflection}
+
\text{warrant}
}
\]

rather than a new universal orchestration calculus.

This leaves one especially important cross-framework question.

Suppose a generator has a guarantee \(G_i\) in its native representation \(L_i\), and an adapter:

\[
p_i:L_i\to\mathbb B
\]

translates its output into the shared representation.

What guarantee survives the translation?

That is a warrant/guarantee transport problem rather than an orchestration problem.

Likely mature ingredients include:

- institution satisfaction conditions;
- proof translation;
- refinement;
- abstract-interpretation soundness;
- assume-guarantee contracts.

This result is recorded in ADR 017 and [candidate-generation-cross-framework-glue.md](candidate-generation-cross-framework-glue.md).

## 47. Guarantee transport is largely an existing heterogeneous-formal-methods problem

The cross-framework glue pass left one apparently substantive question:

> if a generator establishes a guarantee in its native representation and an adapter translates the output, what guarantee survives?

A dedicated literature pass showed that this is also heavily precedented.

For formal logics, institution theory provides satisfaction-preserving translations through morphisms/comorphisms. Hets and DOL operationalize graphs of heterogeneous logics, first-class translations, tool integration and heterogeneous proof management.

MMT/LF-style theory morphisms provide theorem/judgment preservation.

For lossy translations, abstract interpretation provides sound one-way guarantee transfer.

For component/interface transformations, refinement and assume-guarantee/contract theories provide preservation and composition machinery, while also showing an important caution: preserving refinement does not imply preserving serial composition or every other constructor.

The architecture therefore adopts:

\[
\boxed{
\text{artifact translation}
\not\Rightarrow
\text{guarantee transport}.
}
\]

An adapter must carry a typed preservation relation:

\[
\operatorname{Preserves}_\tau(G_S,G_T)
\]

with a certificate/theorem appropriate to the guarantee family.

Adapters are usefully classified from opaque translation through provenance-only, sound one-way, exact satisfaction/judgment preserving, and composition-preserving translations.

If no preservation certificate exists, translated output is only a candidate and must be re-warranted in the target regime.

This also exposed that warrant assumptions should be typed: formal/representation-internal assumptions may translate through a morphism while external applicability assumptions such as calibration validity or i.i.d. sampling remain residual obligations.

This result is recorded in ADR 018 and [warrant-guarantee-transport.md](warrant-guarantee-transport.md).

## 48. Session closeout and new-agent handoff

A final project-management review separated the work into three related projects:

1. the **Formal Epistemic Reasoning Meta-Model**;
2. the **Inquiry Representation Model**;
3. the future **Inquiry System**.

The review also corrected several stale planning statements.

Candidate generation is no longer treated as the largest general foundational unknown. The landscape, five-framework mapping, cross-framework orchestration survey, and formal guarantee-transport survey now cover the broad problem with mature prior art.

Integrated verification is complete rather than pending.

The main current meta-model frontier is now:

\[
\boxed{
\text{acceptance licensing}
+
\text{warrant composition}
}
\]

tracked in issue #34.

The main inquiry-representation frontier is source reconciliation and annotation adjudication, tracked in issue #3.

The main useful-system question is empirical:

> does the inquiry representation actually help a person or model navigate, audit, resume, or improve an inquiry compared with the transcript alone?

That evaluation is tracked in issue #38.

A separate technical audit of the strategy-performance warrant under multiple comparisons / optional stopping is issue #39.

A systematic comparison against the closest integrated prior frameworks is issue #40. The goal of that comparison is adoption/alignment, not novelty.

A canonical operational handoff now lives in [new-agent-handoff.md](new-agent-handoff.md). It should be the first document read by a future agent.

