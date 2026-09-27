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
