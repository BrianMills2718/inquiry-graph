# Candidate-generation interface and worked trace

> **Status:** research draft retained as the first candidate-generation interface. A broader literature-driven refinement is now recorded in [candidate-generation-landscape.md](candidate-generation-landscape.md) and ADR 015. The important correction is to distinguish ordinary exploration within a generative system from transformations that change the generative language, bias, operators, or evaluators.

## 1. Core claim

The mature literature surveyed across program synthesis, CEGIS, inductive logic programming/meta-interpretive learning, and formal abduction suggests a common architecture:

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

Different domains instantiate different operators and biases. The reusable abstraction is therefore an **interface**, not a universal list of creativity primitives.

## 2. Reasoning episode

Retain the current reasoning episode:

\[
R=(\mathcal F,K_{\mathcal F},\Gamma,Q)
\]

where:

- \(\mathcal F\): formal artifact substrate, MMT-like;
- \(K_{\mathcal F}\): persistent support/assumption overlay;
- \(\Gamma\): temporary assumption environment;
- \(Q\): current query/problem.

## 3. Draft-generation system

For a reasoning episode \(R\), define:

\[
\boxed{
\mathcal G_R=
(\mathcal D_R,d_0,\mathcal O_R,\rightarrow_R)
}
\]

where:

- \(\mathcal D_R\): admissible **draft states**;
- \(d_0\): initial/partial draft;
- \(\mathcal O_R\): available construction/refinement operators;
- \(d\xrightarrow{o}_R d'\): applying operator \(o\) transforms draft \(d\) into draft \(d'\).

The reachable draft space is:

\[
\boxed{
\operatorname{Reach}(R)
=
\{d\mid d_0\xrightarrow{\mathcal O_R *}d\}.
}
\]

This is the candidate-generation space for that episode.

The draft space is deliberately broader than the formal-artifact space. A draft may be incomplete, ill-typed, only partly mapped, or otherwise not yet acceptable to the formal substrate.

## 4. Strategy

A strategy controls how the generative transition system is explored.

\[
\boxed{
\pi:
\operatorname{Hist}(R,\mathcal G_R)
\to
\mathcal P(\mathcal O_R\cup\{\operatorname{stop}\})
}
\]

A deterministic strategy chooses one next operator. A stochastic policy can return a distribution. A strategy may also condition on evaluator feedback.

Crucially:

\[
\boxed{
\mathcal G_R \text{ determines what is reachable;}
\qquad
\pi \text{ determines how it is searched.}
}
\]

This prevents the recurring conflation between an operator basis and a reasoning strategy.

## 5. Formal elaboration

A draft is not yet a formal artifact.

\[
\boxed{
\operatorname{Elab}_{\mathcal F}(d)=
\begin{cases}
c\in\mathcal F & \text{if the draft can be elaborated/checked},\\
\bot & \text{otherwise}.
\end{cases}
}
\]

Elaboration may include parsing, name resolution, type reconstruction, proof checking, theory/morphism validation, and structural well-formedness.

And still:

\[
\boxed{
\text{well formed}
\neq
\text{warranted}.
}
\]

## 6. Evaluation and feedback

Let evaluators be:

\[
V_j(R,c)
\to
(\operatorname{status},f_j)
\]

where \(\operatorname{status}\) can be pass/fail/undetermined and \(f_j\) is diagnostic feedback.

Examples include:

- type checker → ill-typed subexpression;
- countermodel search → counterexample;
- constraint checker → violated invariant;
- empirical test → mismatch;
- literature retrieval → relevant prior framework;
- warrant analysis → assumptions required for a guarantee.

The feedback object is itself representable and can alter the subsequent search/control state.

## 7. Warrant remains separate

A warrant claim remains:

\[
\operatorname{Cert}(\tau)=(A_W,G_W,\pi_W),
\]

or an equivalent relation stating that, under assumptions \(A_W\), some move/rule achieves guarantee \(G_W\).

An evaluator may contribute to warrant, but not every evaluator is a warrant checker.

## 8. General loop

The abstract loop is:

\[
\boxed{
R_t
\xrightarrow[\pi]{\mathcal G}
d_t
\xrightarrow{\operatorname{Elab}}
c_t
\xrightarrow{V}
f_t
\xrightarrow{\operatorname{control/update}}
R_{t+1}.
}
\]

The update may modify draft state, available operators, active assumptions, query, support graph, search strategy, or formal representation.

## 9. Canonical factorization as one strategy instance

Canonical/primitive factorization is now an instance of the strategy interface.

### 9.1 Draft state

A draft contains a proposed decomposition:

\[
d=(X,B,\kappa)
\]

where \(X\) is the target object/problem, \(B=\{b_1,\ldots,b_n\}\) is the proposed factor set, and \(\kappa\) is the proposed composition law or normal-form rule.

### 9.2 Operators

A provisional factorization operator set is:

\[
\mathcal O_{\text{fact}}=
\{
\operatorname{split},
\operatorname{merge},
\operatorname{retype},
\operatorname{add},
\operatorname{remove},
\operatorname{change\_composition},
\operatorname{change\_representation},
\operatorname{retrieve\_literature}
\}.
\]

These are strategy-local control actions, not claimed universal cognitive primitives.

### 9.3 Evaluators

Relevant evaluators include:

\[
V_{\text{coverage}},
V_{\text{redundancy}},
V_{\text{independence}},
V_{\text{composition}},
V_{\text{canonicality}}.
\]

### 9.4 Diagnostics

Evaluator feedback can be normalized into:

\[
\{
\text{underfactored},
\text{overfactored},
\text{misfactored},
\text{representation-dependent},
\text{incomplete},
\text{noncanonical}
\}.
\]

These diagnostics are relative to the target representation/equivalence contract.

## 10. Worked trace from the founding dialogue

This is a reconstructed public-dialogue trace, not hidden chain of thought.

### Step 0 — initial partition candidate

Draft:

\[
d_0=
\{
\text{deduction},
\text{induction},
\text{abduction}
\}.
\]

Evaluation finds overlap and ambiguity between induction and abduction.

Feedback:

\[
f_0=\text{misfactored / insufficiently discriminating}.
\]

Control response:

\[
\operatorname{change\_representation}.
\]

### Step 1 — target-type decomposition

Proposed draft:

\[
d_1=
\{
\text{state},
\text{parameter},
\text{structure},
\text{ontology}
\}.
\]

A joint claim such as introducing a latent variable plus causal structure touches several proposed factors simultaneously.

Feedback:

\[
f_1=\text{underfactored composition rule}.
\]

Control response:

\[
\operatorname{change\_composition}.
\]

### Step 2 — composition space

Replace exclusive assignment with:

\[
J(h)\subseteq
\{\Sigma,G,\theta,x\}.
\]

Further stress testing shows structure, parameters and state can be recoded into one another under different representations.

Feedback:

\[
f_2=\text{noncanonical across encodings}.
\]

Control response:

\[
\operatorname{change\_representation}.
\]

### Step 3 — representation-relative factorization

Repair the claim:

\[
\text{absolute canonicality}
\to
\text{canonical relative to a representation contract}.
\]

### Step 4 — state-transition factorization

For fixed live set \(H\):

\[
A=H'\setminus H,
\qquad
D=H\setminus H'.
\]

This yields a provably complete hard-set delta representation relative to fixed identity.

Later, persistent epistemic organization is shown to be richer than a flat set.

Feedback:

\[
f_3=\text{flat state underfactored}.
\]

Control response:

\[
\operatorname{split/retype}.
\]

### Step 5 — assumption/support structure

The persistent state is refined toward:

\[
K_\Sigma=(N,A,J,\lambda,\rho)
\]

with a temporary environment:

\[
\Gamma\subseteq A.
\]

### Step 6 — candidate-type stress test

A proposed candidate taxonomy includes expression, assumption, model, etc.

Evaluation notices that assumption is a role rather than the same sort of artifact as expression.

Feedback:

\[
f_4=\text{misfactored: type mixed with role}.
\]

Control response:

\[
\operatorname{retype}.
\]

### Step 7 — formal representation collapse

MMT/LF-like machinery collapses several formal artifact categories into:

\[
\{
\text{theory},
\text{declaration},
\text{object},
\text{morphism}
\}.
\]

Feedback:

\[
f_5=\text{previous representation overfactored}.
\]

Repair:

\[
\text{draft candidate}
\to
\text{formal elaboration}
\to
\text{formal artifact},
\]

with epistemic warrant kept separate.

### Step 8 — strategy recognition

The repeated repair loop is abstracted into the reusable strategy:

\[
\pi_{\text{canonical-factorization}}.
\]

The meta-model is then used to describe the process that constructed the meta-model, yielding a reflective about relation.

## 11. Why this trace matters

The trace demonstrates that the interface can describe changing candidate spaces, changing composition rules, changing representation contracts, evaluator feedback, repair operators, strategy recognition, and reflective self-application without declaring induction, abduction, reframe, or factorization itself to be a universal primitive operator.

## 12. Implementation guidance

Do **not** yet add a universal CandidateGenerator execution engine.

The next implementation-worthy structures are narrower:

1. a serializable strategy episode only if annotations across more conversations show the current method/example bridge is inadequate;
2. explicit evaluator/feedback records only if repeated traces require first-class feedback provenance;
3. formal artifact references if/when an MMT-compatible representation is actually instantiated;
4. strategy-evaluation datasets once strategy segmentation can be annotated reliably.

The current inquiry graph can already represent the worked trace with method nodes for reusable strategies, example nodes for reconstructed episodes, moves for atomic transformations, part-of/exemplifies/about relations, and claims/hypotheses for draft/failure-state descriptions.

## 13. Remaining hard problems

After this concretization, the frontier is:

1. **draft-generation algebra:** what domain-independent structure, if any, constrains \(\mathcal D,\mathcal O,\to\)?
2. **warrant:** the basic support/warrant/license/update factorization is now specified in [warrant-license-interface.md](warrant-license-interface.md); open work remains on epistemic-action types, warrant composition and graded support;
3. **graded support:** how should \(\rho\) interact with ATMS-style minimal environments?
4. **strategy identification:** can strategy episodes be annotated reproducibly from public reasoning traces?
5. **strategy evaluation:** which strategies help under which tasks/resources without mistaking correlation for causation?
6. **reflection bounds:** how should self-application be typed/guarded in a formal implementation?

The interface is deliberately designed so those questions can be attacked independently.


## 14. Literature-driven refinement

The broader landscape survey found close precedents in Wiggins/Boden creative-system models, program synthesis/CEGIS, ILP/MIL, anti-unification, abductive logic programming, HR theory formation, conceptual blending, and Bayesian program learning.

The original tuple:

\[
\mathcal G_R=
(\mathcal D_R,d_0,\mathcal O_R,\to_R)
\]

should therefore be read as a minimal fixed-space projection of a richer generative regime:

\[
\boxed{
\mathcal G_R
=
(
\mathcal A_R,
\mathcal L_R,
\mathcal D_R,
B_R,
\mathcal O_R,
\to_R,
V_R
)
}
\]

where:

- \(\mathcal A_R\) is the candidate/artifact ontology;
- \(\mathcal L_R\) is the representation or generative language;
- \(\mathcal D_R\) is the draft space;
- \(B_R\) is admissibility/generative bias;
- \(\mathcal O_R\) is the construction/traversal operator family;
- \(\to_R\) is ordinary candidate transition;
- \(V_R\) is evaluation.

Strategy remains separate.

Transformational generation is represented as:

\[
\mu:
\mathcal G_R
\rightharpoonup
\mathcal G'_R.
\]

Thus an ordinary candidate move and a representation-space change are no longer forced into one operator category.

See [candidate-generation-landscape.md](candidate-generation-landscape.md) and ADR 015 for the adoption decision.
