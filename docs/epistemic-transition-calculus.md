# Epistemic transition calculus — current research draft

> **Status:** research draft capturing the current endpoint of the 2026-09-27 dialogue. It is a proposed formalization, not an established theory, and not a claim that the factorization below is representation-independent or a complete psychology of cognition.

## 1. Problem

The target is not certainty and not a theory of “knowledge” in the strong philosophical sense. The target is a compact formalism for the kinds of **epistemic moves** an embedded, black-box observer can make over hypotheses/models, together with a separate account of what licenses those moves.

The motivating distinction is:

- **white-box / stipulated view:** a world model or constraint set is taken as given for the purpose of analysis;
- **black-box / embedded view:** the observer has partial access to the world and operates on fallible, revisable hypotheses.

Accordingly, this document uses **assumed constraints**, **live hypotheses**, **support**, and **warrant** rather than “known true model.” A deduction can be valid relative to assumptions without those assumptions being certain.

The central design goal is not to preserve the folk trichotomy *deduction / induction / abduction*. Those labels are useful historical motifs but overlap. The stronger goal is:

> **Construct a canonical factorization of epistemic state transitions relative to an explicit representation contract, then attach warrant semantics separately.**

“Canonical” here is always relative to a declared semantic representation and identity/alignment rule.

## 2. Why absolute canonicality is unavailable

Earlier in the dialogue, a candidate model normal form was

$$
m=(\Sigma,G,\theta,x)
$$

with ontology/signature, structure, model-level parameters, and instance state. A scope-oriented renaming was

$$
M=(L,C,P,S)
$$

where:

- \(L\): language / expressivity — what can be stated;
- \(C\): model-class constraints / structural form;
- \(P\): model-level degrees of freedom shared across instances;
- \(S\): instance-level degrees of freedom.

This is useful as a **representation contract**, but not metaphysically canonical. Recodings can move information between blocks:

- graph structure can be encoded as a discrete parameter;
- a parameter can be encoded as a state variable constrained to stay fixed;
- ontology variation can be represented inside a larger super-ontology using activation/existence variables.

Therefore no theorem should claim that nature itself uniquely decomposes into \(L,C,P,S\). The defensible claim is conditional:

> Given a declared representation contract, model-target support can be factored relative to that contract.

For a proposition \(h\), a support profile

$$
J(h)\subseteq\{L,C,P,S\}
$$

can record which model coordinates its truth depends on. Joint claims naturally occupy the power set rather than being forced into one category. This target-support view remains useful, but it is secondary to the simpler state-transition factorization below.

## 3. Epistemic state

The current minimal state model is

$$
\boxed{K=(\mathcal U,H,\mu)}
$$

where:

- \(\mathcal U\) is the current semantic universe / language / model space of expressible hypotheses;
- \(H\subseteq\mathcal U\) is the currently live set of hypotheses or possibilities;
- \(\mu\) is optional graded support over \(H\): a probability, plausibility ranking, score, preorder, or other support object.

This is deliberately abstract. It can represent a hard possibility set without \(\mu\), or a graded state when soft updates matter.

A proposition \(p\) denotes some semantic subset \([p]\subseteq\mathcal U\). Relative to \(H\), its logical status is:

$$
\begin{aligned}
H\subseteq[p] &\quad \text{entailed},\\
H\cap[p]=\varnothing &\quad \text{refuted},\\
\text{otherwise} &\quad \text{open}.
\end{aligned}
$$

This partition is useful, but logical status is not itself the state-update basis.

## 4. Fixed-universe state changes

First hold \(\mathcal U\) fixed and ignore \(\mu\). Consider any hard transition

$$
H\rightarrow H'.
$$

Define uniquely:

$$
A=H'\setminus H
$$

and

$$
D=H\setminus H'.
$$

Then

$$
\boxed{H'=(H\cup A)\setminus D}
$$

with \(A\cap H=\varnothing\) and \(D\subseteq H\).

This yields the structural cases:

| Additions \(A\) | Deletions \(D\) | Derived description |
|---|---|---|
| empty | empty | preserve |
| empty | nonempty | restrict |
| nonempty | empty | expand |
| nonempty | nonempty | replace |

The important point is that **replace is not a third primitive**. It is the composition of expansion and restriction. Given fixed semantic identity, the pair \((A,D)\) is unique by set difference.

This is a stronger completeness result than any current claim involving induction or abduction: for hard set-valued epistemic state changes over a fixed universe, add/remove is complete by construction.

## 5. Changing the hypothesis universe

A substantive inquiry can change what is expressible or which model structures are admitted. Then

$$
\mathcal U_t\neq\mathcal U_{t+1}.
$$

Introduce an alignment / representation map

$$
\Phi:\mathcal U\rightarrow\mathcal U'.
$$

The map \(\Phi\) says how old semantic objects are carried into the new universe. It may be a conservative embedding, a quotient, a reinterpretation, or something more complex; its admissible class is an open design question.

Relative to \(\Phi\), define:

$$
A=H'\setminus\Phi(H)
$$

and

$$
D=\Phi(H)\setminus H'.
$$

The hard state transition is then characterized by:

$$
\boxed{(\Phi,A,D)}.
$$

Adding the graded component gives the current full candidate factorization:

$$
\boxed{
\Delta K=
\left(
\Phi:\mathcal U\to\mathcal U',
A,
D,
\mu\to\mu'
\right).
}
$$

Given the representation/alignment map \(\Phi\), the set differences \(A\) and \(D\) are unique.

### What this does *not* prove

It does not prove:

- that there is one privileged \(\mathcal U\);
- that semantic identity across representation change has one uniquely correct \(\Phi\);
- that all cognitive change is literally explicit set manipulation;
- that \(\mu\) has one universal mathematical type;
- that the factorization is a psychology of human or model internals.

It is a normal form for describing epistemic state changes.

## 6. Readout is not necessarily state change

Several moves that looked like candidate primitives disappear once state change is separated from content generation and readout.

### Deductive derivation

If current assumptions entail \(p\), making \(p\) explicit need not change \(K\):

$$
K\vdash p,
\qquad
\Delta K=0.
$$

Deduction can therefore be modeled as a **readout** or derivation over an epistemic state rather than necessarily as a state mutation.

If the system separately stores explicit derived propositions, then a bookkeeping representation can change, but the semantic possibility set need not.

### Semantics-preserving reparameterization

A bijective or otherwise semantics-preserving representational transformation may change syntax without changing empirical commitment. This belongs in \(\Phi\), but should be marked as conservative rather than confused with learning a substantive new hypothesis.

### Inductive projection

Suppose a process generates the proposition \(p=\) “the next case will exhibit the observed regularity.” If \(p\) is hard-accepted, its state effect may simply be

$$
H'=H\cap[p],
$$

which is restriction. If it is only made more plausible, the effect may be entirely in

$$
\mu\to\mu'.
$$

Thus “projection” describes **how candidate content was generated**, not a new set-theoretic state-update primitive.

The same observation applies to many abductive explanations.

## 7. Three layers that must remain separate

The strongest conceptual result of the later dialogue is:

$$
\boxed{
\text{candidate generation}
\neq
\text{warrant/evaluation}
\neq
\text{epistemic state update}.
}
$$

### 7.1 Candidate generation

Let evidence/experience be \(E\). A candidate generator is schematically

$$
\boxed{
g:(K,E)\rightarrow\mathcal C
}
$$

where \(\mathcal C\) is a set of candidate propositions, models, variables, mechanisms, analogical mappings, predictions, etc.

This is where traditional labels such as induction and abduction most naturally live:

- extrapolating an observed regularity;
- filling a latent state in an assumed model;
- proposing a new mechanism;
- analogical transfer;
- introducing a new variable or category;
- proposing a causal structure.

No MECE factorization of candidate generation has yet been established. **This is the principal open formal problem.**

### 7.2 Warrant / evaluation

Given candidate \(c\), evaluation asks what licenses changing epistemic commitment to it.

Warrant is not “certainty” and not “the candidate is now known true.” A minimal warrant certificate is:

$$
\boxed{
\operatorname{Cert}(\tau)=(A_W,G_W,\pi)
}
$$

where:

- \(A_W\): explicit assumptions or restrictions on admissible worlds/environments;
- \(G_W\): the claimed guarantee;
- \(\pi\): a proof, argument, derivation, empirical certificate, or other support that \(A_W\) yields \(G_W\) for the transition/rule.

Write:

$$
A_W\vdash_{G_W}\tau.
$$

Possible guarantees include:

- deductive truth preservation relative to premises;
- consistency preservation;
- convergence under a specified problem class;
- calibration;
- bounded prediction error or regret;
- identifiability under stated causal assumptions.

For genuinely ampliative rules, nontrivial universal guarantees require restrictions on the admissible world/problem class. Those restrictions are part of the warrant, not hidden implementation details.

### 7.3 State update

After generation and evaluation, the agent may:

- keep a candidate merely available: \(A\neq\varnothing\);
- remove incompatible possibilities: \(D\neq\varnothing\);
- reweight support: \(\mu\to\mu'\);
- change the representational universe: \(\Phi\).

Those are state effects, independent of the rhetorical or philosophical label attached to the generating move.

## 8. Warrant of warrant

The original motivating question was “what warrants warrant?”

This calculus does not claim to terminate the regress. Instead it makes it explicit.

If a warrant certificate depends on assumptions \(A_W\), those assumptions can themselves be represented as hypotheses/commitments and subjected to further transitions and certificates:

$$
A_2\Rightarrow A_1\Rightarrow A_W\Rightarrow G_W(\tau).
$$

A system may eventually:

1. mark assumptions as foundational/axiomatic;
2. ground them in measurement/observation commitments;
3. use a coherence relationship;
4. leave the support chain open.

The important engineering property is that **ungrounded assumptions remain inspectable** instead of disappearing inside a named inference method.

An AGM-like research program is relevant here: specify rationality postulates for update operators and seek representation theorems; separately specify empirical/world assumptions and prove performance guarantees. No such general theorem has been established by this project.

## 9. White-box / black-box interpretation

The white-box/black-box distinction is a modeling device, not a certainty claim.

### White-box analysis

For analysis, stipulate some world model \(W\), constraints \(C\), or environment class. Then one can ask what follows, what observations carry information about other variables, or how a proposed rule performs.

### Embedded observer

The observer has only its current \(K\), evidence stream \(E\), and physically/computationally available operations. “Constraint known” should therefore normally be read as **constraint assumed for this derivation**.

The observer can be wrong at every level. The calculus classifies the move and its support structure; it does not certify the world model.

## 10. Relationship to deduction, induction, and abduction

The conversation began by asking whether deduction, induction, and abduction form an exhaustive taxonomy. The current formalism no longer requires that claim.

### Deduction

Most cleanly,

$$
K\vdash p
$$

is a readout/derivation from assumptions. It can leave \(\Delta K=0\).

### Induction

Likely a family of candidate-generation trajectories that extend empirical regularities, estimate model-scoped quantities, or propose general constraints. Its state effect may be restriction, expansion, or reweighting.

### Abduction

Likely a family of candidate-generation trajectories that fill latent states or introduce explanatory/generative structure. It overlaps induction when a new general explanatory structure is inferred from finite observations.

Thus the historical labels may become **motifs over the calculus**, not primitive state-transition types.

## 11. Worked examples

### 11.1 Finite dot configuration

Suppose every dot in a finite visible configuration is measured, and the relational fact

> black and white dots occupy separable regions

is logically computable from those measurements.

Extracting that relational feature need not be ampliative. It may be a deterministic readout/representation computation over currently available information.

This corrects an earlier temptation to call all pattern recognition “induction.”

### 11.2 Temporal dots and prediction

Now observe dots sequentially. Memory/state integration can summarize the past without yet making a claim about an unobserved future dot.

A candidate generator may propose:

> another dot will appear.

If support for that proposition increases, the epistemic state changes through \(\mu\to\mu'\) or, under hard commitment, through restriction.

Spatial integration, temporal integration, candidate generation, and induction therefore need not be identical operations.

### 11.3 Diagnosis

Given an existing diagnostic model, symptoms may generate the candidate:

> the patient has condition \(Z\).

If \(Z\) was already expressible, no universe expansion is required. Evaluation may reweight \(Z\) relative to competitors.

### 11.4 New latent variable

If current \(\mathcal U\) cannot express a proposed latent variable \(Z\), candidate generation can trigger a universe change

$$
\Phi:\mathcal U\rightarrow\mathcal U'
$$

where \(\mathcal U'\) includes models containing \(Z\). Some new models become live through \(A\).

### 11.5 Causal structure

The proposition \(X\to Y\) can be generated from observations plus modeling assumptions. Accepting it may remove model structures that lack the edge, or upweight causal models containing it. The causal interpretation belongs to the candidate content and warrant assumptions; the state effect remains factorizable.

### 11.6 Counterfactual under an assumed SCM

With a structural causal model assumed, many counterfactual conclusions are derivations/readouts after a stipulated intervention transformation. If the SCM itself is uncertain, candidate generation/evaluation over structures occurs before the counterfactual readout.

### 11.7 Analogy

An analogy proposes a mapping between structures. The mapping is generated content. If entertained, it may expand the live model space; if accepted, it may constrain/reweight it. Analogy therefore need not be a primitive state-update operator.

## 12. Earlier detours and what remains useful

Several literatures were investigated because they appeared to supply a missing foundational layer.

- **Measurement theory / psychophysics:** useful for what variables/distinctions are physically or operationally accessible.
- **Grenander/Brown Pattern Theory:** useful as a broad language for generators, configurations, transformations, variation, observation, and inference. It does not by itself derive all observer representations from physics.
- **Computational mechanics / predictive representations / information bottleneck:** useful for optimal or sufficient predictive representations. Their equivalence relations encode a relevance criterion and should not be mistaken for the ontology of all patterns an observer can notice.
- **PID / synergy / IIT mathematics:** potentially relevant to distributed information integration. IIT was considered only as algorithmic partition/irreducibility machinery, not as a consciousness theory.
- **State-space / recurrent computation:** useful substrate for memory and temporal integration. It does not by itself answer the warrant problem.
- **AGM belief revision:** useful precedent for postulates plus representation theorems; not a completed solution for the present calculus.

These are neighboring tools, not the spine of the current formalization.

## 13. Current endpoint

The current research claim is deliberately narrow:

> **Relative to an explicit semantic representation/alignment contract, an epistemic state can be modeled as \(K=(\mathcal U,H,\mu)\), and its state change can be factored into representation change \(\Phi\), additions \(A\), deletions \(D\), and graded-support change \(\mu\to\mu'\). Candidate generation and warrant are separate layers.**

The fixed-universe hard-update component is complete by set difference. The broader “canonical” claim remains conditional on semantic identity and alignment.

The next research target is not another taxonomy of state updates. It is:

$$
\boxed{
\text{Find a useful, ideally uniquely factorizable basis for candidate generation }
g:(K,E)\to\mathcal C.
}
$$

Then specify warrant postulates/certificates that make every non-entailing commitment explicit about its assumptions and claimed guarantee.

## 14. Open problems / falsifiers

1. **Candidate-generation factorization.** Can induction, abduction, analogy, completion, projection, model invention, concept formation, and causal discovery be represented by a smaller compositional basis?
2. **Semantic alignment \(\Phi\).** When \(\mathcal U\) changes, what makes an old and new hypothesis “the same” hypothesis? Multiple alignments may be defensible.
3. **Soft support.** What is the minimal common algebra for \(\mu\)? Probability is too specific; arbitrary scores may be too weak.
4. **Continuous/infinite spaces.** Set difference is conceptually clean, but implementation over measure-theoretic or uncountable model spaces needs care.
5. **Observation versus report.** The inquiry graph records utterances; the epistemic calculus needs a separate account of how measurements/reports enter \(E\).
6. **Warrant postulates.** Which structural postulates should apply to update/evaluation, and which representation theorems follow?
7. **Performance warrants.** Which assumptions support which guarantees for particular candidate generators/update rules?
8. **Meta-warrant.** How should unresolved, foundational, empirical, and circular support chains be represented without pretending the regress is solved?
9. **Representation contract adequacy.** Is \(L,C,P,S\) expressive enough as a descriptive target space, or are there important update dimensions it distorts?
10. **Empirical usefulness.** Does this factorization improve annotation, reasoning analysis, or AI reasoning policies compared with simpler provenance graphs?

These are the appropriate failure points for the next phase.
