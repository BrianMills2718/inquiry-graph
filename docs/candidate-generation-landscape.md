# Candidate Generation Landscape and Adoption Decision

> **Status:** literature-driven comparison pass following the Formal Epistemic Reasoning Meta-Model closeout.
>
> **Purpose:** determine whether the project's candidate-generation layer should be invented, imported, or refactored around existing mature frameworks.

## 1. Executive conclusion

The project should **not invent a universal candidate-generation theory from scratch**.

The current interface:

\[
\mathcal G_R=
(\mathcal D_R,d_0,\mathcal O_R,\to_R)
\]

is useful, but its central distinctions already have strong precedents.

The closest general precedent is Geraint Wiggins's formal Creative Systems Framework, which distinguishes a conceptual space, rules determining admissible artifacts, traversal/generation procedures, and evaluation, and explicitly analyzes transformational creativity in which the effective search space itself changes.

Other mature families instantiate different parts of this architecture:

- program synthesis / CEGIS — constrained search in explicit program spaces with verifier feedback;
- ILP / Meta-Interpretive Learning — logical hypothesis search, recursion, and predicate invention;
- anti-unification — least/general generalization operators;
- abductive logic programming — explanatory hypothesis generation under abducible vocabularies and integrity constraints;
- HR automated theory formation — concept invention, conjecture formation, proof/countermodel feedback, and interestingness-guided search;
- conceptual blending / concept invention — representation-changing combination of conceptual structures;
- Bayesian program learning — probabilistic search over compositional generative programs.

The project should therefore treat candidate generation as an **interface over existing generative frameworks**.

The likely reusable factorization is:

\[
\boxed{
\text{artifact ontology}
+
\text{representation/generative language}
+
\text{admissibility bias}
+
\text{construction/traversal}
+
\text{evaluation}
+
\text{feedback}
+
\text{control}
+
\text{representation transformation}
}
\]

rather than a universal list of primitive creativity operators.

## 2. Correction to the earlier project framing

Earlier work correctly separated:

\[
\text{generative space}
\neq
\text{operators}
\neq
\text{strategy}
\neq
\text{evaluation}
\neq
\text{warrant}.
\]

That remains useful.

However, this separation should no longer be treated as a project-specific theoretical invention.

Wiggins's 2006 framework already formalizes a closely related separation between:

- a universe of possible artifacts;
- rules defining a conceptual space;
- traversal rules used to search/generate within that space;
- evaluation rules.

Boden/Wiggins also distinguish exploratory creativity from transformational creativity, where the rules defining or traversing the conceptual space change.

Therefore the project's candidate-generation layer should explicitly align to that literature.

## 3. Comparison dimensions

Candidate-generation systems are best compared along dimensions rather than forced into one operator taxonomy.

### 3.1 Artifact ontology

What kinds of objects may be generated?

Examples:

- term;
- formula;
- hypothesis;
- rule;
- predicate;
- theory;
- program;
- proof sketch;
- model;
- analogy/mapping;
- concept;
- conjecture;
- experiment;
- strategy.

### 3.2 Representation / generative language

What formal language determines representable candidates?

Examples:

- program grammar;
- logic-program signature;
- metarules;
- ontology;
- term algebra;
- probabilistic program language;
- theory graph.

### 3.3 Admissibility bias

What restricts candidate space?

Examples:

- type constraints;
- grammar;
- background theory;
- integrity constraints;
- mode declarations;
- metarules;
- priors;
- resource bounds;
- specification constraints.

### 3.4 Construction / traversal

How are candidates produced?

Examples:

- enumeration;
- specialization;
- generalization;
- anti-unification;
- mutation;
- composition;
- analogy;
- blending;
- constraint solving;
- stochastic sampling;
- learned proposal models.

### 3.5 Evaluation

How are candidates scored or rejected?

Examples:

- formal correctness;
- consistency;
- coverage;
- compression;
- proof;
- countermodel;
- predictive accuracy;
- interestingness;
- novelty;
- explanatory fit;
- cost.

### 3.6 Feedback

What information from evaluation returns to generation?

Examples:

- counterexample;
- failed proof obligation;
- uncovered positive example;
- covered negative example;
- empirical residual;
- countermodel;
- type error;
- human critique.

### 3.7 Control

How is the next move chosen?

Examples:

- best-first search;
- stochastic policy;
- heuristic search;
- branch-and-bound;
- active learning;
- metareasoning policy.

### 3.8 Representation transformation

Can the language/space itself change?

Examples:

- predicate invention;
- invention of new definitions;
- conceptual blending;
- theory extension;
- generation of new metarules;
- introduction of latent variables;
- representation change.

This final dimension is especially important.

## 4. Landscape matrix

| Framework family | Generated artifact | Bias / space | Traversal | Evaluation / feedback | Space-changing? |
|---|---|---|---|---|---|
| Program synthesis | programs | DSL/grammar/specification | enumeration, constraints, stochastic/deductive search | verifier, examples, counterexamples | usually limited |
| CEGIS | programs | synthesis language + specification | iterative synthesis | counterexample from verifier | usually fixed |
| ILP | clauses/programs | background knowledge + language bias | generalization/specialization/search | positive/negative examples | sometimes |
| Meta-Interpretive Learning | logic programs + invented predicates | metarules + background knowledge | meta-level logical search | entailment/examples | yes |
| Anti-unification | generalized expressions | term/theory language | least-general generalization | generality/order criteria | usually fixed |
| Abductive Logic Programming | explanations/abducibles | abducible vocabulary + integrity constraints | constrained abduction | consistency + entailment | usually fixed |
| HR theory formation | concepts + conjectures | production rules + domain axioms | interestingness-guided best-first search | theorem proving, countermodels, interestingness | yes |
| Wiggins creative systems | artifacts | conceptual-space rules | traversal rules | evaluation rules | explicitly yes |
| Conceptual blending | blended concepts/theories | input conceptual spaces/ontologies | generalize/map/blend/refine | consistency, optimality metrics | yes |
| Bayesian program learning | latent concept programs | compositional probabilistic language + prior | probabilistic inference/search | posterior/predictive fit | usually fixed meta-language |
| Theory morphism approaches | mappings/translations | formal theories/signatures | morphism construction/search | structure/satisfaction preservation | can alter representation context |

## 5. Wiggins / Boden

Wiggins's Creative Systems Framework is the closest general comparison.

The key lesson is that creativity can be described in terms of:

1. a universe of possible artifacts;
2. rules defining a conceptual space;
3. procedures for traversing that space;
4. evaluation criteria.

Boden's distinction between exploratory and transformational creativity is especially useful.

### Exploratory generation

Search inside an existing space:

\[
\mathcal G
=
(
\mathcal D,
\mathcal O,
\to
).
\]

### Transformational generation

Modify what counts as reachable:

\[
\mathcal G_t
\xrightarrow{\mu}
\mathcal G_{t+1}.
\]

This is the right precedent for the project's earlier observation that generation can alter:

- draft space;
- operator vocabulary;
- representation language;
- evaluation criteria.

Recommendation:

**adopt the exploratory/transformational distinction explicitly rather than reinvent it.**

## 6. Program synthesis and CEGIS

Program synthesis supplies one of the cleanest mature instances of fixed-space candidate generation.

A synthesizer searches a program language for an artifact satisfying a specification.

The mature synthesis literature separates:

- syntactic bias / program language;
- specification;
- search procedure;
- verification;
- optimization.

CEGIS makes feedback explicit:

\[
\text{synthesize candidate}
\to
\text{verify}
\to
\text{counterexample}
\to
\text{repair/search}.
\]

This maps directly onto the project's:

\[
d
\to
\operatorname{Elab}(d)
\to
V(c)
\to
f
\to
\text{control}.
\]

Recommendation:

treat CEGIS as the canonical precedent for **evaluation-driven refinement loops**.

## 7. ILP and Meta-Interpretive Learning

ILP searches logical hypotheses under background knowledge and examples.

Meta-Interpretive Learning is particularly important because it supports:

- recursion;
- higher-order templates/metarules;
- predicate invention.

Predicate invention demonstrates that representation vocabulary can change without requiring unconstrained creativity.

It can be modeled as a controlled extension of the current logical language.

This is a strong precedent for distinguishing:

\[
\boxed{
\text{expression construction}
\neq
\text{predicate invention}.
}
\]

Recommendation:

use MIL as a primary model for **typed vocabulary-extending generation**.

## 8. Anti-unification

Anti-unification computes generalizations of structured expressions.

It is a mature family rather than one algorithm.

It gives a canonical example of a local generative operator:

\[
\operatorname{lgg}(x,y)
\]

or related least/general generalizations.

This is important methodologically because many apparent “creative” operations reduce to well-defined algebraic transformations once the representation language is fixed.

Recommendation:

treat anti-unification as an imported operator family, not a foundational primitive of all generation.

## 9. Abductive Logic Programming

Abductive Logic Programming generates explanations from a declared set of abducibles under integrity constraints.

This supports a key conclusion:

\[
\boxed{
\text{abduction under a fixed hypothesis vocabulary}
=
\text{constrained candidate search}.
}
\]

The mystery is pushed into:

- the abducible vocabulary;
- representation choice;
- search/control;
- evaluation criteria.

Recommendation:

do not treat “abduction” as a primitive generative operator.

Treat it as one domain-specific generative regime.

## 10. HR automated theory formation

HR is a major precedent that the project previously underweighted.

HR performs an integrated loop involving:

- concept invention;
- example calculation;
- conjecture formation;
- theorem proving;
- countermodel/model generation;
- interestingness assessment;
- best-first search.

In other words, HR already implements much of:

\[
\text{generate}
\to
\text{evaluate}
\to
\text{formal check}
\to
\text{feedback}
\to
\text{generate}.
\]

Its production rules are particularly relevant to concept construction.

Recommendation:

study HR's production-rule ontology before inventing any project-specific “concept invention operator” taxonomy.

## 11. Computational concept invention / blending

Conceptual blending frameworks explicitly target generation of new conceptual structures.

Modern computational treatments decompose concept invention into:

- finding shared/generalized structure;
- mapping input structures;
- constructing blends;
- consistency repair;
- evaluation against optimality/quality constraints.

This literature is directly relevant to representation-changing generation.

Recommendation:

treat blending/amalgamation as a mature family for **cross-representation concept construction**, especially when theory/ontology structures are being combined.

## 12. Bayesian program learning

Bayesian program learning represents concepts as compositional generative programs.

Candidate generation becomes probabilistic inference over structured latent programs.

This contributes a distinct perspective:

\[
\boxed{
\text{candidate generation}
=
\text{inference over a generative meta-language}
}
\]

rather than explicit symbolic traversal.

Recommendation:

keep the interface general enough that \(\pi\) may be probabilistic inference/proposal rather than a symbolic search algorithm.

## 13. Revised project abstraction

The earlier interface should be extended slightly.

Instead of only:

\[
\mathcal G_R
=
(
\mathcal D_R,
d_0,
\mathcal O_R,
\to_R
),
\]

use:

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

- \(\mathcal A_R\): artifact ontology / candidate kinds;
- \(\mathcal L_R\): representation or generative language;
- \(\mathcal D_R\): draft/candidate states;
- \(B_R\): generative bias/admissibility constraints;
- \(\mathcal O_R\): construction/traversal operators;
- \(\to_R\): transition relation;
- \(V_R\): candidate evaluators.

Strategy/control remains separate:

\[
\Pi_R:
\operatorname{Hist}(R,\mathcal G_R)
\to
\mathcal P(
\mathcal O_R
\cup
\{\operatorname{stop}\}
).
\]

Feedback is produced by \(V_R\) and becomes part of history/state.

## 14. Transformations of the generative system

To cover transformational creativity and representation change, add a separate meta-transition:

\[
\boxed{
\mu:
\mathcal G_R
\rightharpoonup
\mathcal G'_R.
}
\]

Possible effects include changes to:

- artifact ontology \(\mathcal A\);
- representation language \(\mathcal L\);
- admissibility bias \(B\);
- operator set \(\mathcal O\);
- evaluation regime \(V\).

This avoids forcing space-changing moves into the same category as ordinary candidate moves.

Thus:

\[
\boxed{
\text{candidate transition}
\neq
\text{generative-system transformation}.
}
\]

This is probably the most useful refinement produced by the landscape survey.

## 15. Candidate types versus generation mechanisms

Do not classify candidate generation only by verbs such as:

- generalize;
- specialize;
- combine;
- analogize;
- mutate.

The same operator can act on very different artifact types and under very different languages.

Conversely, the same artifact can be generated by different mechanisms.

A better factorization is:

\[
\boxed{
\text{what is generated}
\times
\text{in what language}
\times
\text{under what bias}
\times
\text{by what transition}
\times
\text{under what evaluation/control}.
}
\]

## 16. Candidate-generation provenance

The project should preserve how a candidate was generated.

A generation event should be able to record:

\[
\operatorname{GenEvent}
=
(
d,
o,
d',
\text{inputs},
\text{feedback},
\text{strategy},
\text{representation version}
).
\]

This matters because two extensionally identical candidates may arise through different processes.

Unlike the ABA argument quotient, generation provenance may matter for:

- explanation;
- strategy evaluation;
- reproducibility;
- learning which operators work.

Do not automatically quotient generation histories by final candidate identity.

## 17. Relationship to warrant

Candidate-generation adequacy and epistemic warrant remain separate.

A generative system may have properties such as:

- completeness relative to a finite search language;
- probabilistic coverage;
- convergence;
- bounded regret;
- expected search cost.

These are warrants about the **generation method**, not warrants for the truth/acceptance of generated candidates.

Thus:

\[
\boxed{
\text{generator warrant}
\neq
\text{candidate-content warrant}.
}
\]

This separation is a major reason to keep candidate generation in the meta-model.

## 18. What is still genuinely open

After importing the mature literature, the remaining research questions become narrower.

### 18.1 Cross-framework interface

Can synthesis, ILP/MIL, abduction, theory formation, blending, and probabilistic program induction be represented faithfully through one typed interface?

### 18.2 Representation-changing moves

What is the cleanest semantics for:

\[
\mu:
\mathcal G
\to
\mathcal G'?
\]

Should these be theory morphisms, meta-level actions, versioned languages, or a more general transition?

### 18.3 Operator invention

How should a system generate a new operator:

\[
o_{\text{new}}
\notin
\mathcal O?
\]

This is distinct from using an existing operator to generate a candidate.

### 18.4 Bias generation

How are new:

- grammars;
- metarules;
- priors;
- abducibles;
- search heuristics;
- representation constraints

generated and warranted?

### 18.5 Generative-space comparison

When are two generative systems equivalent?

Possible notions:

- same reachable candidates;
- same candidates up to formal equivalence;
- same distribution over candidates;
- same asymptotic coverage;
- same search cost class;
- same transformation closure.

### 18.6 Concept invention boundary

When is a generated declaration merely:

- shorthand / definitional extension;

versus:

- a substantively new representational distinction?

This remains philosophically and formally important.

## 19. Adoption decision

The project should adopt the following stance:

\[
\boxed{
\textbf{Candidate generation is a family of typed generative systems, not one universal inference operator.}
}
\]

And:

\[
\boxed{
\textbf{Exploration within a generative system must be separated from transformation of the generative system itself.}
}
\]

The latter distinction should be imported explicitly from the creativity/concept-invention literature.

## 20. Immediate next work

Do not implement a generic candidate-generation engine yet.

Next steps should be:

1. revise the candidate-generation meta-model using the expanded tuple above;
2. map at least five mature frameworks into it:
   - CEGIS/program synthesis;
   - MIL/predicate invention;
   - anti-unification;
   - HR theory formation;
   - conceptual blending;
3. test whether any framework cannot be represented without distortion;
4. only then decide whether additional coordinates are required;
5. connect generative-system transformations to the existing formal representation layer;
6. define generator-level warrant separately from candidate-content warrant.

If those mappings succeed, the project should import the mature mechanisms rather than inventing replacements.
