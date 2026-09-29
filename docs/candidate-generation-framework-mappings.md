# Candidate-Generation Framework Mappings

> **Status:** framework-mapping test following the candidate-generation landscape survey and ADR 015.
>
> **Purpose:** test whether five mature candidate-generation frameworks fit the revised meta-model without distortion. New coordinates should be added only if a mapping actually fails.

## 1. Interface under test

The current candidate-generation regime is:

\[
\boxed{
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
}
\]

where:

- \(\mathcal A_R\): artifact ontology / candidate kinds;
- \(\mathcal L_R\): representation or generative language;
- \(\mathcal D_R\): draft/candidate state space;
- \(B_R\): admissibility bias / search constraints;
- \(\mathcal O_R\): construction/traversal operators;
- \(\to_R\): ordinary candidate transition relation;
- \(V_R\): evaluator family.

Strategy/control remains separate:

\[
\Pi_R:
\operatorname{Hist}(R,\mathcal G_R)
\to
\mathcal P(
\mathcal O_R\cup\{\operatorname{stop}\}
).
\]

A candidate-generation **episode** is more precisely:

\[
\boxed{
E_G=(R,\mathcal G_R,d_0)
}
\]

where the reasoning episode \(R\) already carries the task/question, support state, assumptions and broader context, while \(d_0\in\mathcal D_R\) provides the initial generative state.

This restores the initial-state coordinate from the earlier formulation without making the problem instance part of the reusable generative regime.

Transformational change remains:

\[
\mu:
\mathcal G_R
\rightharpoonup
\mathcal G'_R.
\]

## 2. Important qualification: transformationality is representation-relative

A major result of the mapping exercise is that:

\[
\boxed{
\text{ordinary generation}
\quad\text{vs}\quad
\text{generative-system transformation}
}
\]

is **relative to the chosen meta-language**.

For example, predicate invention may look like a transformation of the first-order object language.

But if the generative language \(\mathcal L_R\) already quantifies over fresh predicate symbols or predicate variables, predicate invention may be an ordinary transition inside a fixed higher-order generative regime.

Likewise, a “new concept” can be:

- transformational relative to an object-language vocabulary;
- ordinary relative to a meta-language designed to generate vocabulary extensions.

Therefore:

\[
\boxed{
\mu \text{ means a change to the represented generative regime itself,}
}
\]

not merely “the candidate contains a new symbol.”

This prevents overusing the transformational category.

---

# 3. Mapping 1 — Program synthesis / CEGIS

## 3.1 Canonical problem

A synthesis problem can be written schematically as:

\[
\exists P\;\forall x\;\sigma(P,x),
\]

where \(P\) ranges over programs and \(\sigma\) is the specification.

CEGIS alternates:

\[
\text{synthesis}
\to
\text{candidate}
\to
\text{verification}
\to
\text{counterexample}
\to
\text{refined synthesis}.
\]

## 3.2 Mapping

### Artifact ontology

\[
\mathcal A_R
=
\{\text{program},\text{program skeleton},\text{candidate solution}\}.
\]

### Generative language

\[
\mathcal L_R
=
\text{DSL / syntax-guided grammar / program representation}.
\]

### Draft space

\[
\mathcal D_R
=
\text{partial programs + candidate programs + accumulated example constraints}.
\]

The accumulated counterexample set may be represented in draft state or in \(R\)'s persistent/context state.

### Bias

\[
B_R
=
\{
\text{grammar restrictions},
\text{type constraints},
\text{specification},
\text{bounded resources}
\}.
\]

### Operators

\[
\mathcal O_R
=
\{
\text{instantiate grammar production},
\text{refine skeleton},
\text{solve constraints},
\text{generalize from examples}
\}.
\]

### Transition

A transition adds or modifies a candidate program or its constraints.

### Evaluation

\[
V_R
=
\{
\text{verifier},
\text{SMT solver},
\text{test/example checker}
\}.
\]

Feedback includes counterexamples.

### Strategy/control

Search ordering, solver heuristics, counterexample selection and synthesis policy live in \(\Pi_R\).

## 3.3 Fit assessment

**Fits without a new coordinate.**

CEGIS is almost an ideal instance of:

\[
\text{generation}
\neq
\text{evaluation}
\neq
\text{feedback}
\neq
\text{control}.
\]

The problem specification itself belongs in \(R\)/\(B_R\), not as a new universal coordinate.

## 3.4 Transformationality

Standard CEGIS is usually fixed-space:

\[
\mu \approx \operatorname{id}.
\]

Changing the DSL/grammar during search would be a genuine \(\mu\)-transition.

---

# 4. Mapping 2 — Meta-Interpretive Learning

## 4.1 Canonical problem

MIL learns a logic program from:

- background knowledge \(\mathcal B\);
- metarules \(\mathcal M\);
- positive examples \(E^+\);
- negative examples \(E^-\).

MIL can support predicate invention and recursive definitions.

## 4.2 Mapping

### Artifact ontology

\[
\mathcal A_R
=
\{
\text{logic program},
\text{clause},
\text{invented predicate},
\text{metarule specialization}
\}.
\]

### Generative language

\[
\mathcal L_R
=
\text{higher-order/meta-logical language containing metarules}.
\]

### Draft space

Partial hypotheses, unresolved predicate variables, invented predicate declarations, and candidate logic programs.

### Bias

\[
B_R
=
\{
\mathcal B,
\mathcal M,
E^+,
E^-,
\text{typing/mode restrictions},
\text{program-size bias}
\}.
\]

### Operators

\[
\mathcal O_R
=
\{
\text{instantiate metarule},
\text{specialize},
\text{invent predicate},
\text{compose clauses},
\text{introduce recursion}
\}.
\]

### Evaluation

\[
V_R
=
\{
\text{entail positive examples},
\text{reject negative examples},
\text{consistency},
\text{compression/complexity}
\}.
\]

### Control

Search order, metarule choice, predicate-invention timing, pruning and compression bias are strategy/control.

## 4.3 Fit assessment

**Fits without a new coordinate.**

MIL is especially useful because it stress-tests vocabulary extension.

## 4.4 Transformationality

Predicate invention exposes the representation-relative boundary.

If:

\[
\mathcal L_R
\]

already contains machinery for fresh predicate variables and generated predicate declarations, invention is an ordinary transition:

\[
d\xrightarrow{o_{\text{invent}}}d'.
\]

If the current generative regime did not permit fresh predicates and is modified to permit them, that modification is:

\[
\mu:
\mathcal G_R\to\mathcal G'_R.
\]

Thus:

\[
\boxed{
\text{predicate invention}
\not\Rightarrow
\text{necessarily transformational at the meta-model level}.
}
\]

This is an important correction to the naive use of \(\mu\).

---

# 5. Mapping 3 — Anti-unification

## 5.1 Canonical problem

Given expressions \(s,t\), anti-unification computes a generalization \(g\) such that suitable substitutions recover \(s\) and \(t\).

In classical settings, one seeks a least general generalization relative to a generality ordering.

Variants exist for:

- first-order terms;
- equational theories;
- higher-order terms;
- description logics;
- graphs and other structures.

## 5.2 Mapping

### Artifact ontology

\[
\mathcal A_R
=
\{\text{generalization expression}\}.
\]

### Generative language

The term/formula/graph/theory language in which the input structures and generalizations are represented.

### Draft space

Partial generalizations plus substitution/alignment constraints.

### Bias

\[
B_R
=
\{
\text{chosen equivalence theory},
\text{generality relation},
\text{syntactic restrictions}
\}.
\]

### Operators

\[
\mathcal O_R
=
\{
\text{replace mismatch with variable},
\text{decompose matching structure},
\text{normalize modulo theory},
\text{merge variables/constraints}
\}.
\]

Exact operator sets vary by anti-unification theory.

### Evaluation

Typical criteria include:

- whether \(g\) generalizes each input;
- minimality / least-generality;
- uniqueness up to equivalence;
- satisfiability of side constraints.

### Control

For deterministic classical algorithms, control may be nearly degenerate.

For richer theories with branching search, \(\Pi_R\) becomes substantive.

## 5.3 Fit assessment

**Fits cleanly.**

Anti-unification demonstrates that a candidate-generation regime need not have a rich iterative strategy. Some regimes are close to canonical algebraic operators.

This supports keeping control optional/degenerate rather than assuming every generator is heuristic search.

## 5.4 Transformationality

Usually fixed-space.

Anti-unification changes a candidate expression, not the generative language itself:

\[
\mu\approx\operatorname{id}.
\]

---

# 6. Mapping 4 — HR automated theory formation

## 6.1 Canonical process

HR forms mathematical theories from background axioms by interleaving:

- concept formation;
- example calculation;
- conjecture generation;
- theorem proving;
- model/counterexample generation;
- interestingness assessment;
- best-first search.

This is the richest stress test among the five mappings.

## 6.2 Mapping

### Artifact ontology

Unlike simpler frameworks, HR is genuinely multi-artifact:

\[
\mathcal A_R
=
\{
\text{concept},
\text{definition},
\text{example table},
\text{conjecture},
\text{proof},
\text{countermodel}
\}.
\]

The interface therefore must allow \(\mathcal A_R\) to be a **typed family**, not one homogeneous candidate class.

### Generative language

Mathematical concept/theory representation plus production-rule vocabulary.

### Draft space

The current evolving theory:

- existing concepts;
- newly generated concepts;
- examples;
- conjectures;
- proof/countermodel results;
- interestingness metadata.

### Bias

\[
B_R
=
\{
\text{domain axioms},
\text{production-rule applicability},
\text{interestingness criteria},
\text{resource/search limits}
\}.
\]

### Operators

Production rules generate new concepts from old concepts.

Other operators generate:

- conjectures;
- relationships;
- proof obligations.

### Evaluation

\[
V_R
=
\{
\text{interestingness measures},
\text{theorem proving},
\text{model finding},
\text{empirical examples}
\}.
\]

OTTER and MACE historically provide proof/countermodel feedback.

### Control

Best-first search over concept/theory development belongs squarely in \(\Pi_R\).

## 6.3 Fit assessment

**Fits, but reveals an important requirement: artifact ontology must support heterogeneous interdependent candidate types.**

No new top-level coordinate is required.

However:

\[
\boxed{
\mathcal A_R
\text{ must be typed and relational, not merely a flat set of candidates.}
}
\]

A generated concept can enable a conjecture; a conjecture creates a proof obligation; a countermodel may generate new example data.

Thus the draft state should permit a **candidate dependency graph**, not just one candidate object.

This is a refinement of the semantics of \(\mathcal D_R\), not a new coordinate.

## 6.4 Transformationality

Concept invention can be represented either way depending on the meta-language.

If production rules already generate new concept definitions, it is ordinary exploration in a higher-level theory-formation space.

A genuine \(\mu\)-transition occurs when HR-like reasoning changes:

- its production-rule vocabulary;
- its representation language;
- its interestingness criteria;
- its admissibility rules.

---

# 7. Mapping 5 — Computational conceptual blending

## 7.1 Canonical process

Computational blending systems typically begin with multiple input conceptual structures.

The process includes some combination of:

- finding shared/generalized structure;
- constructing mappings;
- selecting correspondences;
- amalgamating/blending structures;
- repairing inconsistencies;
- evaluating candidate blends.

Eppe et al. formalize generalization as search and prune candidate blends using metrics related to blending optimality principles.

## 7.2 Mapping

### Artifact ontology

\[
\mathcal A_R
=
\{
\text{generic space},
\text{mapping},
\text{blend},
\text{blended theory/concept}
\}.
\]

### Generative language

Ontologies, theories, graphs or other structured conceptual representations.

### Draft space

Partial:

- alignments;
- generic spaces;
- correspondences;
- candidate amalgams;
- repairs.

### Bias

\[
B_R
=
\{
\text{input spaces},
\text{mapping constraints},
\text{consistency constraints},
\text{blending optimality criteria}
\}.
\]

### Operators

\[
\mathcal O_R
=
\{
\text{generalize},
\text{map},
\text{select},
\text{amalgamate},
\text{complete},
\text{repair}
\}.
\]

### Evaluation

\[
V_R
=
\{
\text{consistency},
\text{optimality metrics},
\text{structural preservation},
\text{domain-specific quality}
\}.
\]

### Control

Search over generic spaces, mappings and blends is strategy/control.

## 7.3 Fit assessment

**Fits without a new coordinate.**

The multi-input nature of blending does not require another universal dimension; the source structures belong in \(R\), \(B_R\), or \(d_0\).

## 7.4 Transformationality

A blend can look radically novel while still being generated inside a fixed meta-language for theories and mappings.

Therefore novelty of the output is not sufficient for \(\mu\).

Use \(\mu\) only if the blending process modifies the generative regime itself.

---

# 8. Cross-framework mapping matrix

| Dimension | CEGIS | MIL | Anti-unification | HR | Conceptual blending |
|---|---|---|---|---|---|
| \(\mathcal A\) artifact kinds | programs | clauses/programs/predicates | generalizations | concepts/conjectures/proofs/models | mappings/generic spaces/blends |
| \(\mathcal L\) language | DSL/program grammar | logic + metarules | term/structural language | mathematical theory language | ontology/theory/graph language |
| \(\mathcal D\) draft state | partial/candidate programs + examples | partial hypotheses | partial generalization | evolving theory graph | partial maps/blends |
| \(B\) bias | grammar/spec | BK/metarules/examples | generality/equational theory | axioms/production rules/interestingness | inputs/mapping/optimality constraints |
| \(\mathcal O\) operators | synthesize/refine | instantiate/invent/compose | generalize/decompose | production rules/conjecture formation | generalize/map/amalgamate/repair |
| \(V\) evaluation | verifier | entailment/consistency | least-generality | proof/model/interestingness | consistency/optimality |
| Feedback | counterexample | examples/failure | constraints | proofs/countermodels | failed constraints/quality |
| \(\Pi\) control | search policy | hypothesis search | often minimal | best-first search | blend search/pruning |
| Typical \(\mu\) | grammar change | metarule/language change | theory/language change | production/evaluation-language change | representation/generation-rule change |

---

# 9. Does the revised interface survive?

Yes.

None of the five mappings requires an additional top-level coordinate.

The interface:

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

plus:

\[
E_G=(R,\mathcal G_R,d_0)
\]

and:

\[
\mu:
\mathcal G_R
\rightharpoonup
\mathcal G'_R
\]

is sufficient for all five at this level of abstraction.

Therefore the correct project decision is:

\[
\boxed{
\textbf{do not add another candidate-generation coordinate yet.}
}
\]

---

# 10. Refinements discovered by mapping

Although no new coordinate is required, the mapping produced four important refinements.

## 10.1 Separate regime from episode

A reusable generative regime should not contain its specific starting problem state.

Use:

\[
\mathcal G_R
=
(
\mathcal A,
\mathcal L,
\mathcal D,
B,
\mathcal O,
\to,
V
)
\]

for the regime and:

\[
E_G=(R,\mathcal G_R,d_0)
\]

for an episode.

This clarifies the status of specifications, examples and input structures.

## 10.2 Artifact ontology may be heterogeneous

HR demonstrates that generation may interleave multiple candidate kinds.

Therefore \(\mathcal A_R\) should be a typed artifact ontology with admissible relations, not merely a flat candidate type.

## 10.3 Draft state may be a graph

In multi-artifact systems:

\[
d\in\mathcal D_R
\]

may itself be a structured graph of:

- concepts;
- hypotheses;
- mappings;
- examples;
- obligations;
- feedback.

There is no need to assume a draft is one object.

## 10.4 Transformationality is representation-relative

This is the most important theoretical refinement.

\[
\boxed{
\text{inventing a new object-language symbol}
\neq
\text{necessarily changing the generative meta-language}.
}
\]

Whether an operation is ordinary or transformational depends on the representation contract defining \(\mathcal G_R\).

---

# 11. Generator warrant

The mapping strengthens the distinction between two warrant targets.

## Candidate-content warrant

Example:

\[
\mathfrak W;
A
\vdash_{\pi_c}
\operatorname{accept}(h):G.
\]

## Generator warrant

Example:

\[
\mathfrak W_{\mathrm{gen}};
A_{\mathrm{gen}}
\vdash_{\pi_g}
\operatorname{useGenerator}(\mathcal G):
G_{\mathrm{coverage/cost/convergence}}.
\]

CEGIS may admit completeness/termination results in restricted spaces.

Anti-unification may have least-general-generalization guarantees.

MIL may have soundness/completeness results relative to a hypothesis/metarule class.

These are properties of the generator/regime, not warrants for the truth of each generated candidate.

Therefore:

\[
\boxed{
\text{generator adequacy}
\neq
\text{candidate adequacy}.
}
\]

---

# 12. What remains open after the mapping

The mapping closes the question of whether another immediate top-level coordinate is required.

The remaining candidate-generation research is narrower.

## 12.1 Generative-system equivalence

Define when:

\[
\mathcal G_1\sim\mathcal G_2.
\]

Candidate notions include:

- same reachable formal artifacts;
- same closure up to formal equivalence;
- same distributions;
- same transformation closure;
- simulation/bisimulation of generation traces.

## 12.2 Transformation composition

How do:

\[
\mu_1,\mu_2
\]

compose?

When are two representation-changing paths equivalent?

## 12.3 Operator invention

How is a new:

\[
o_{\mathrm{new}}
\]

constructed, represented and warranted?

MIL metarule generation is a concrete precedent.

## 12.4 Bias invention

The most important unresolved generative object may be the bias itself:

- new grammar;
- new metarule;
- new prior;
- new abducible set;
- new heuristic;
- new concept language.

## 12.5 Concept-invention semantics

The distinction between definitional extension and substantively new representation remains open.

This is not solved merely by supporting fresh symbols.

## 12.6 Cross-regime composition

Can one generator invoke another as an operator?

Examples:

- conceptual blending calls anti-unification for generic-space construction;
- HR calls theorem provers/model generators as evaluators;
- synthesis uses learned proposal models;
- MIL-generated predicates become vocabulary for later abduction.

This suggests a future algebra of generative-regime composition, but the mapping does not yet force one.

---

# 13. Current conclusion

The framework-mapping test supports the adoption-first policy.

The project's candidate-generation layer should be interpreted as a **typed interoperability interface** across mature generative systems.

The next foundational questions are no longer:

> What are the primitive ways to invent candidates?

They are:

> How do typed generative regimes compose, transform, compare, and receive warrants?

and:

> How does generation of new representational bias differ from generation of ordinary candidate content?

Those are narrower and better-grounded questions.
