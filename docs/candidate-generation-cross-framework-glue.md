# Candidate-Generation Cross-Framework Glue: Existing Work and Adoption Plan

> **Status:** integration landscape following ADR 016.
>
> **Purpose:** identify the mature off-the-shelf frameworks for the remaining candidate-generation integration problems, and determine whether the project needs a new orchestration theory.

## 1. Executive conclusion

The remaining “glue” problem is also heavily precedented.

The project should **not invent a new universal orchestration architecture**.

The closest mature families are:

- **blackboard systems** for heterogeneous knowledge sources cooperating through shared state;
- **blackboard control architectures** for explicit meta-level control over which knowledge source/operator fires next;
- **multistrategy learning** for integrating multiple inferential/learning strategies under task-adaptive control;
- **algorithm selection / portfolios** for choosing among candidate generators or solvers;
- **hyper-heuristics** for selecting or generating heuristics/operators rather than searching directly in the object-level solution space;
- **automated algorithm configuration** for tuning generator/control parameters;
- **integrated planning-learning architectures** such as PRODIGY;
- **reflective architectures / meta-programming** for reasoning about and modifying the system's own procedures;
- **cognitive architectures such as Soar** for impasse-driven subgoaling and learning of new procedural rules.

The best off-the-shelf architectural interpretation for this project is therefore:

\[
\boxed{
\textbf{typed blackboard + explicit controller + generator portfolio + reflective transformation}
}
\]

not a new monolithic generator calculus.

The project's formal representation layer can provide the **typed shared substrate**; existing generators become **knowledge sources/services**; strategy selection, algorithm selection and hyper-heuristics provide **control**; reflective/meta-level actions provide **regime modification**; and the warrant layer evaluates both generated content and generator-selection decisions.

---

## 2. The remaining subproblems and mature precedents

| Remaining project question | Mature prior-art family | Project interpretation |
|---|---|---|
| choose among generators | Rice algorithm selection, portfolios, AutoML | strategy/controller selects generator based on task/context |
| sequence generators/operators | hyper-heuristics, blackboard control | controller chooses next knowledge source/operator |
| generate new operators | heuristic-generation hyper-heuristics, genetic programming, MIL metarule learning | operator candidate generation at the meta-level |
| tune operator/generator parameters | algorithm configuration, SMAC | optimize parameters of \(\mathcal G\) or \(\Pi\) |
| generate/change inductive bias | MIL metarule learning, grammar induction, meta-learning | transform \(B\) and sometimes \(\mathcal L\) |
| integrate heterogeneous generators | blackboard systems, multistrategy learning, PRODIGY | common typed state + adapters + opportunistic control |
| learn procedural shortcuts | Soar chunking, EBL, PRODIGY learning | generate reusable control/operator knowledge |
| manage cost/utility of learned procedures | COMPOSER, rational metareasoning | generator/control warrant over utility/cost |
| reflect on/modify own reasoning machinery | reflective architectures, blackboard control, meta-programming | \(\mu:\mathcal G\to\mathcal G'\) |
| compare generators empirically | algorithm selection/configuration literature | benchmark/task-distribution performance models |
| compare generators formally | automata/process/program equivalence, simulation/bisimulation | optional later formal equivalence notions |

Thus most “open” integration problems are better understood as **selection of the right mature subframework** than invention of new primitives.

---

# 3. Blackboard systems: closest orchestration architecture

## 3.1 Core idea

Classical blackboard systems separate:

- a shared evolving problem-solving state (“blackboard”);
- multiple specialized **knowledge sources**;
- a control mechanism that decides which applicable knowledge source to invoke.

Hearsay-II and subsequent blackboard systems demonstrated heterogeneous expert modules incrementally contributing to a solution without requiring direct pairwise coordination.

Nii's blackboard framework explicitly abstracts this architecture.

For the candidate-generation meta-model, map:

\[
\boxed{
\text{blackboard}
\leftrightarrow
(R,K,\mathcal D,\text{feedback/provenance})
}
\]

and:

\[
\boxed{
\text{knowledge source}
\leftrightarrow
\text{generator/evaluator/operator family}.
}
\]

Examples of knowledge sources in this project could include:

- anti-unifier;
- CEGIS synthesizer;
- MIL hypothesis generator;
- theory-morphism searcher;
- conceptual blender;
- theorem prover;
- countermodel finder;
- literature retriever;
- measurement/testimony evaluator.

## 3.2 Why this matters

The blackboard pattern answers the practical question:

> How can heterogeneous generators interoperate without sharing one internal representation or algorithm?

They exchange **typed artifacts/results through shared state**.

This is almost exactly the cross-framework glue requirement.

## 3.3 Typed refinement

Classical blackboards often use domain-specific shared structures.

Our representation layer suggests a typed version:

\[
\mathbb B
=
(
\mathcal F,
K_{\mathcal F},
Q,
\Gamma,
\text{drafts},
\text{feedback},
\text{provenance}
).
\]

Each generator has an adapter contract:

\[
g_i:
I_i(\mathbb B)
\rightharpoonup
O_i(\mathbb B).
\]

The adapter maps shared formal artifacts into the generator's native representation and maps output back into the shared substrate.

No requirement exists that every generator use the same internal logic.

---

# 4. Blackboard control: meta-level selection is old too

Hayes-Roth's blackboard control architecture makes the control problem explicit:

> which potential action should the system perform next?

It separates domain problem solving from control problem solving and permits the system to reason about its own knowledge and behavior.

This is very close to the project's:

\[
\Pi:
\operatorname{Hist}(R,\mathcal G)
\to
\mathcal P(
\mathcal O\cup\{\operatorname{stop}\}
).
\]

Thus \(\Pi\) should not be treated as novel.

A blackboard-style controller can evaluate candidate generator activations such as:

\[
\operatorname{Invoke}(g_i,\text{input},\text{expected cost/benefit}).
\]

The project's warrant layer can make such control decisions explicit:

\[
\mathfrak W_{\mathrm{ctrl}};
A
\vdash_{\pi}
\operatorname{invokeGenerator}(g_i):
G.
\]

This makes blackboard control compatible with the action-targeted warrant architecture.

---

# 5. Multistrategy learning: unusually close conceptual precedent

Michalski's Inferential Theory of Learning was motivated by the proliferation of learning/inference paradigms and the need for a general framework describing their relationships and integration.

It explicitly considers task-adaptive integration of:

- empirical induction;
- constructive induction;
- deductive generalization;
- abduction;
- abstraction;
- analogy/similization;
- other inference modes.

This is extremely relevant to the project's original motivation.

The mapping is:

\[
\boxed{
\text{multistrategy learning}
\approx
\text{multiple typed generators + task-adaptive control}.
}
\]

The main difference is scope.

The present project distinguishes more downstream layers:

\[
\text{generation}
\neq
\text{support}
\neq
\text{warrant}
\neq
\text{license}.
\]

But the high-level idea of dynamically selecting and combining inference/generation strategies is well established.

Therefore future comparison work should treat Michalski's framework as a **primary comparator**, not a peripheral citation.

---

# 6. Algorithm selection and portfolios

Rice's Algorithm Selection Problem formalizes choosing an algorithm based on:

- problem-instance features;
- available algorithms;
- performance measures.

This directly corresponds to generator selection.

Let:

\[
\phi(R)
\]

be task/context features and:

\[
\mathcal G_{\mathrm{portfolio}}
=
\{g_1,\ldots,g_n\}.
\]

Then selection is:

\[
S:
\phi(R)
\to
g_i.
\]

Modern algorithm portfolios and AutoML elaborate this idea using learned performance models.

This provides an established basis for:

\[
\boxed{
\text{select generator}
\neq
\text{generate candidate}.
}
\]

The selection mechanism itself may be learned and warranted independently.

---

# 7. Hyper-heuristics: operator selection and operator invention

Hyper-heuristics explicitly raise search to a higher level.

Rather than searching directly over object-level solutions, they search over:

- heuristics;
- heuristic components;
- sequences of heuristics.

Two major categories are:

1. **heuristic selection**;
2. **heuristic generation**.

This is almost exactly the project's distinction between:

\[
\text{using an operator}
\]

and:

\[
\text{generating/changing an operator}.
\]

Therefore the project's “operator invention” problem is strongly covered by hyper-heuristic research.

Map:

\[
\mathcal O
=
\text{low-level heuristic/operator library}
\]

and meta-generation:

\[
\mathcal O
\xrightarrow{\text{hyper-generator}}
\mathcal O'.
\]

A generated operator may then become part of a new generative regime:

\[
\mu:
\mathcal G
\to
\mathcal G'.
\]

---

# 8. Automated algorithm configuration

Algorithm configuration optimizes parameters of algorithms on task distributions.

SMAC and related methods treat an executable process as a black box with tunable parameters.

For the project:

\[
\theta_{\mathcal G}
=
\text{generator/control parameters}.
\]

Configuration becomes:

\[
\theta^*
=
\arg\max_\theta
\operatorname{Perf}
(
\mathcal G_\theta,
\mathcal T
).
\]

This covers a substantial portion of what could otherwise be called “bias optimization” or “strategy tuning.”

It should be imported rather than rebuilt.

---

# 9. Bias invention and metarule learning

Bias transformation is broader than parameter tuning.

Examples include changing:

- grammar;
- metarules;
- predicate vocabulary;
- prior;
- abstraction;
- admissible operators.

Meta-Interpretive Learning provides a particularly clean precedent.

Later MIL work shows that metarules themselves can be learned via specialization from more general higher-order metarules.

Thus:

\[
B
\xrightarrow{\text{meta-learning}}
B'
\]

is not speculative.

It has concrete symbolic implementations.

The project's \(\mu\)-transition can therefore treat learned bias as a first-class transformation output.

---

# 10. PRODIGY: integrated planning and multiple learning mechanisms

PRODIGY is a strong historical example of an integrated architecture combining:

- planning;
- explanation-based learning;
- derivational analogy;
- abstraction;
- experimentation;
- control learning.

A key design feature is that multiple learning mechanisms operate at common planner decision points and share mutually interpretable knowledge structures.

This is directly relevant to cross-framework interoperability.

The lesson is:

\[
\boxed{
\text{shared typed decision/problem state}
+
\text{multiple specialized learners}
}
\]

is a mature architecture pattern.

Our typed formal substrate and inquiry state can play the role of PRODIGY's common structures, while retaining more explicit epistemic warrant semantics.

---

# 11. Soar: impasse-driven meta-generation and procedural learning

Soar provides another useful precedent.

Operators are proposed and selected.

When the system cannot select or apply an operator, it reaches an **impasse** and creates a substate/subgoal to resolve the missing knowledge.

After resolving the impasse, chunking can create a new production summarizing the successful reasoning.

This resembles:

\[
\text{generation/control failure}
\to
\text{meta-level inquiry}
\to
\text{new reusable operator/control knowledge}.
\]

That is highly relevant to operator/bias invention.

In the project's terms:

\[
\mathcal G
\to
\text{impasse}
\to
E'_G
\to
o_{\mathrm{new}}
\to
\mathcal G'.
\]

Soar demonstrates an operational mechanism for the reflective loop without requiring a wholly new meta-theory.

---

# 12. Reflection and meta-programming

Reflective programming architectures distinguish:

- object-level computation;
- representations of that computation;
- meta-level procedures that inspect/modify object-level behavior.

This provides mature precedent for:

\[
\mu:
\mathcal G
\rightharpoonup
\mathcal G'.
\]

Reflection is especially relevant when the target is not merely a generated candidate but the machinery that generates candidates.

Thus the project's relational:

\[
\operatorname{about}(x,y)
\]

and transformation architecture can be grounded in existing reflection/meta-programming traditions.

---

# 13. Generator-level warrant and the utility problem

Choosing or learning more rules/operators can make a system slower even if each new rule is locally useful.

The classical **utility problem** in speed-up learning addresses this issue.

COMPOSER is one example that uses probabilistic evidence to decide whether learned control knowledge is actually beneficial.

This is strongly aligned with:

\[
\boxed{
\text{generator/control warrant}
\neq
\text{candidate-content warrant}.
}
\]

A generator-level guarantee may concern:

- runtime;
- expected utility;
- coverage;
- success probability;
- transfer;
- memory cost;
- regret.

The warrant layer therefore already has a mature target literature.

---

# 14. Comparison table: what should we import?

| Project requirement | Best mature starting point | Import/adapt |
|---|---|---|
| heterogeneous generators cooperate | Blackboard systems | **adopt architecture pattern** |
| explicit next-generator control | Hayes-Roth blackboard control | **adopt control pattern** |
| combine different inference strategies | Michalski multistrategy learning | **primary conceptual comparator** |
| choose generator by task features | Rice algorithm selection / portfolios | **adopt selection formalism** |
| select operators dynamically | selection hyper-heuristics | **adopt** |
| invent operators/heuristics | generation hyper-heuristics / GP | **adopt** |
| tune generator parameters | SMAC / algorithm configuration | **adopt** |
| invent bias/metarules | MIL/metarule learning | **adopt symbolic precedent** |
| integrated planner + learners | PRODIGY | **architectural precedent** |
| impasse-driven new procedural knowledge | Soar | **architectural precedent** |
| modify own reasoning machinery | reflection/meta-programming | **adopt conceptual semantics** |
| assess whether new procedures help | COMPOSER / metareasoning | **adopt utility/warrant precedent** |
| typed formal interoperation | MMT/institutions/theory morphisms | **retain project substrate** |

There is no evidence that a new universal glue calculus is currently needed.

---

# 15. Recommended cross-framework architecture

The best synthesis of existing work for this project is:

\[
\boxed{
\mathcal C
=
(
\mathbb B,
\mathcal K,
\mathcal P,
\Pi,
\mathcal M,
\mathfrak W
)
}
\]

where:

- \(\mathbb B\): typed blackboard/shared epistemic state;
- \(\mathcal K\): portfolio of knowledge sources/generators/evaluators;
- \(\mathcal P\): adapters/projections between shared and native representations;
- \(\Pi\): controller / algorithm-selection / hyper-heuristic policy;
- \(\mathcal M\): reflective transformations of generators, biases and control;
- \(\mathfrak W\): warrant regimes for content and control actions.

## 15.1 Blackboard

\[
\mathbb B
=
(
\mathcal F,
K_{\mathcal F},
\Gamma,
Q,
D,
F
).
\]

## 15.2 Knowledge-source portfolio

\[
\mathcal K
=
\{
g_i,
V_j,
c_k
\}.
\]

Examples:

- generator;
- evaluator;
- theorem prover;
- measurement interpreter;
- countermodel finder;
- retrieval system.

## 15.3 Adapters

For each component:

\[
p_i:
\mathbb B
\rightleftarrows
L_i.
\]

This is where MMT/institution-style morphisms may provide formal semantics when available.

## 15.4 Controller

\[
\Pi:
\operatorname{Hist}(\mathbb B)
\to
\mathcal P(
\operatorname{Invoke}(\mathcal K)
\cup
\operatorname{Transform}(\mathcal M)
\cup
\{\operatorname{stop}\}
).
\]

## 15.5 Reflective transformation

\[
\mu:
(
\mathcal K,
\mathcal P,
\Pi,
B,
\mathcal L
)
\to
(
\mathcal K',
\mathcal P',
\Pi',
B',
\mathcal L'
).
\]

## 15.6 Warrant

Controller and transformation moves remain explicit epistemic actions:

\[
\mathfrak W;
A
\vdash_\pi
\operatorname{invoke}(g_i):G
\]

or:

\[
\mathfrak W;
A
\vdash_\pi
\operatorname{install}(o_{\mathrm{new}}):G.
\]

---

# 16. Is this itself already an existing framework?

Not exactly as one single standard package.

But nearly every component is well established.

The architecture above is best seen as an **assembly of mature patterns**:

\[
\boxed{
\text{blackboard architecture}
+
\text{multistrategy control}
+
\text{algorithm selection/hyper-heuristics}
+
\text{reflection}
+
\text{typed formal substrate}
+
\text{explicit warrant}.
}
\]

The project-specific part is mostly the alignment with the broader Formal Epistemic Reasoning Meta-Model.

Therefore no novelty assumption is required and no new orchestration mechanism should be implemented unless this assembly fails on a concrete use case.

---

# 17. Remaining integration gaps after importing the literature

The landscape reduces the remaining gap significantly.

## 17.1 Adapter semantics

Classical blackboard systems often assume shared domain representations.

Our generators may have incompatible formal languages.

The hard problem is:

\[
\boxed{
\text{typed semantic adapters between generator-native representations}.
}
\]

MMT/institutions/theory morphisms are the preferred existing machinery when formal semantics exist.

LLM/natural-language components will require weaker provenance-bearing adapters.

## 17.2 Warrant propagation across adapters

Suppose generator \(g_i\) guarantees \(G_i\) in native language \(L_i\).

After translating output into the shared representation:

\[
p_i:
L_i\to\mathbb B,
\]

what guarantee survives?

This is not just orchestration.

It is a **warrant transport** problem.

Likely relevant mature machinery:

- institution satisfaction condition;
- proof translation;
- abstract interpretation soundness;
- refinement/assume-guarantee contracts.

This is probably the most important unresolved cross-framework glue question.

## 17.3 Provenance across generator composition

If:

\[
g_2(g_1(x))
\]

produces \(y\), the system must preserve:

- source input;
- generator versions;
- adapters;
- feedback;
- assumptions;
- transformations.

The inquiry graph/provenance machinery is well suited to this.

## 17.4 Incommensurable control objectives

Generator selection may trade:

- correctness;
- coverage;
- novelty;
- latency;
- computational cost;
- explainability.

There is no universal scalar objective.

This returns to the existing typed-warrant / explicit-policy stance.

## 17.5 Dynamic portfolio growth

Hyper-heuristics and Soar-like learning cover creation of new operators.

But maintaining a growing heterogeneous generator portfolio raises practical questions:

- redundancy;
- dominance;
- deprecation;
- versioning;
- trust calibration.

These are system-management questions rather than missing epistemic primitives.

---

# 18. Adoption decision

The candidate-generation integration problem should now be treated as:

\[
\boxed{
\textbf{typed blackboard orchestration of existing generators under explicit meta-control and warrant.}
}
\]

Do not invent a new generic candidate-generation runtime until this architecture is tested.

The first implementation, if pursued, should be deliberately small:

1. typed shared state;
2. two or three heterogeneous generator adapters;
3. one controller;
4. preserved provenance;
5. explicit generator-level warrant/result metadata.

A useful first trio would be:

- anti-unification;
- CEGIS/synthesis;
- a theory/analogy or LLM-backed proposal generator.

If these cooperate through the shared substrate without distortion, the architecture is sufficient.

---

# 19. Research conclusion

The initial intuition that “the remaining integration gap must also be well trodden” is correct.

The work exists under several historical names rather than one:

- blackboard systems;
- multistrategy learning;
- algorithm selection;
- hyper-heuristics;
- algorithm configuration;
- integrated planning and learning;
- cognitive architectures;
- computational reflection.

The remaining research value lies primarily in **choosing and composing the right established mechanisms**, while preserving the epistemic distinctions of the meta-model.

The most technically substantive unresolved glue problem is not orchestration itself.

It is:

\[
\boxed{
\textbf{transporting typed guarantees/warrants across representation adapters and generator composition.}
}
\]

That should be treated as the next candidate only if we continue foundational work.
