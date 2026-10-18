# Scenario-based evaluation of representation frameworks

**Status:** source-grounded desk evaluation, v0.1, 2026-10-18.  
**Question:** Which existing frameworks cover the user's five representative cases, and where does composition remain necessary?  
**Limit:** This is not a tool-level conformance run. Official specifications and primary framework papers were inspected, and operational test fixtures were defined. DOL, MMT, SysML tools, Modelica tools, and proof assistants have not been installed or run as part of this evaluation. “Documented match” therefore means that a source describes the capability, not that the specific fixture has passed in a tool.

## 1. Method and judgment labels

Each case has obligations to represent an artifact, state or define semantics, relate/translate it, execute or prove something where required, ground it in observations when empirical claims are made, and track provenance.

- **Core/documented:** central to the framework's documented scope or formal machinery.
- **Conditional/partial:** available with particular formalisms, encoding, or tool assumptions.
- **Composition required:** a distinct framework, tool, or artifact is needed; the connecting contract still needs to be specified.
- **Not core:** outside the main purpose of the framework; not proof of impossibility.
- **Unknown:** the inspected sources do not settle the question.

The small fixtures are synthetic. They expose obligations but do not establish real-world empirical validity.

## 2. Cross-case capability map

In this table, **C** = core/documented, **P** = conditional/partial, **X** = composition/delegation required, and **N** = not core to the framework's purpose.

| Case | DOL | MMT | Institution theory | SysML v2 / KerML | Modelica + FMI | Ologs | SKOS + OWL + SOSA/SSN + PROV-O | OAEI |
|---|---|---|---|---|---|---|---|---|
| Physics theory → simulation → observation comparison | X | P/X | P/X | P/X | **C** for dynamic-model execution/exchange; X for empirical validation | P/X | **C** for observation/provenance records; X for theory/solver | N |
| Mathematical theory → theorem → checked proof | P/X (underlying OMS logic and tools matter) | **C** for modular formal knowledge and proof/model-theory representation | **C** for abstract logic, models, satisfaction and translation; proof objects need a calculus/tool | N | N | P (primitive-recursive functions are shown in the paper; not a general proof assistant) | N for proof; provenance may record artifacts | N |
| Cellular automaton → rule → execution trace | P/X | P/X | P/X | P/X | P/X | P/X | N for runtime; PROV-O can record runs | N |
| Empirical taxonomy/classification with observations | P/X | P/X | P/X | N | N | P | **C** for taxonomy/observation/provenance artifacts as a composed stack; X for scientific warrant | P for matching evaluation |
| Translation between independent formalisms | **C** for heterogeneous OMS and mappings | **C** for theory morphisms and modular representation | **C** for logical translation and satisfaction conditions | P within engineering ecosystems | P for dynamic-model exchange, not arbitrary translation | P for schema mappings | P for concept/ontology mapping, not general semantic preservation | **C** for ontology-matching benchmark evaluation, not translation semantics |

A “C” on one obligation does not mean the entire case is covered. The multiple X entries are not defects in the methods; they identify the boundaries that matter to the research question.

## 3. Test A — Physics, execution, and observations

### Fixture

Use a normalized harmonic oscillator with angular frequency \(\omega=1\):

\[
\dot{x}=v,\quad \dot{v}=-x,\quad x(0)=1,\quad v(0)=0.
\]

Analytic reference values are \(x(t)=\cos t\) and \(v(t)=-\sin t\). At \(t\in\{0,\pi/2,\pi\}\), positions are \(1,0,-1\), and velocities are \(0,-1,0\). A numerical run must record solver, step/tolerances, parameter values, and outputs. A real empirical validation would additionally require measurement identity, units, calibration, uncertainty, and an explicit comparison criterion. These values are analytic test oracles, not empirical observations.

### Evaluation

**Modelica + FMI** is the closest domain-specific choice for executable dynamic models. Modelica describes systems with differential, algebraic, and discrete equations. FMI standardizes interfaces for model exchange, co-simulation, and scheduled execution; the overall co-simulation algorithm itself is not prescribed by FMI. Sources: [Modelica specification](https://specification.modelica.org/) and [FMI specification](https://fmi-standard.org/docs/main/).

**SysML v2/KerML** specifies system structure and behavioral semantics, and the SysML v2 standard describes semantic conformance including model execution. A conforming tool and specific model encoding are still needed; this is not a universal scientific solver or empirical-validation method. Source: [OMG SysML v2.0](https://www.omg.org/spec/SysML/2.0/Language/PDF).

**DOL, MMT, and institution theory** can formalize and relate theories/models when the underlying languages are appropriately formalized. They do not themselves pick a numerical method, run a solver, or establish physical truth. **SOSA/SSN** describes observations, properties/features, procedures/sensors, results, and time; **PROV-O** describes entities and activities underlying model runs and assessments. These records do not automatically demonstrate calibration or model validity. Sources: [W3C SSN/SOSA](https://www.w3.org/TR/vocab-ssn/) and [W3C PROV-O](https://www.w3.org/TR/prov-o/).

**Result:** the best-supported pattern is a composition: Modelica/FMI for execution, SOSA/SSN for observation metadata, PROV-O for provenance, and optional DOL/MMT/institution-theory mappings where the component languages support them. The interfaces and validation criteria are part of the solution, not incidental metadata.

## 4. Test B — Mathematical theory, theorem, and proof

### Fixture

Specify natural numbers and addition, then prove \(\forall n\in\mathbb{N},\; n+0=n\) by induction. The test artifact includes vocabulary, definitions/axioms, theorem statement, proof object, and the proof calculus/checker under which acceptance is meaningful.

### Evaluation

**MMT** is the strongest candidate for organizing the formal artifact. Its literature describes modular representations of languages and theories, axioms, theorems, proofs, models, and theory morphisms. Concrete checking still depends on the chosen logic and tooling. Sources: [MMT overview](https://uniformal.github.io/doc/) and [Rabe, “MMT: A Foundation-Independent Approach to Formal Knowledge”](https://uniformal.github.io/doc/philosophy/articles/mmt.pdf).

**Institution theory** captures a different layer: abstract signatures, sentences, models, satisfaction, and a condition governing compatibility under signature translation. This is a principled basis for comparing logics, not a ready-made proof assistant. Sources: [Goguen's institution-theory overview](https://cseweb.ucsd.edu/~goguen/projs/inst.html) and [Goguen & Burstall (1992)](https://doi.org/10.1145/147508.147524).

**DOL** coordinates formal OMS and mappings; proof/consistency capabilities depend on underlying logics and reasoning tools. **Ologs should not be characterized as merely decorative schemas:** their paper shows representations of primitive-recursive functions and functorial interconnections. That does not demonstrate a general machine-checked theorem-proving workflow. Source: [Spivak & Kent (2012)](https://doi.org/10.1371/journal.pone.0024274).

**Result:** for proof-centered work, use a suitable formal system/proof assistant; consider MMT where cross-foundation modularity, library integration, and translation matter; use institution theory for generic statements about logical semantics; use DOL for heterogeneous formal OMS networks. Model satisfaction and proof derivability must remain distinct obligations.

## 5. Test C — Cellular automaton and execution

### Fixture

Use a 15-cell binary ring with periodic boundaries and synchronous updates under elementary cellular automaton Rule 30:

\[
x_i(t+1)=x_{i-1}(t)\oplus(x_i(t)\lor x_{i+1}(t)),
\]

where indices are modulo 15. Start with a single live cell at the center. Required artifacts are state space, neighborhood, transition function, boundary condition, initial configuration, update schedule, deterministic trace, and a defined implementation-equivalence/invariant check.

The following first six configurations provide a reproducible oracle for times 0–5:

\[
\begin{aligned}
t=0 &: 000000010000000\\
t=1 &: 000000111000000\\
t=2 &: 000001100100000\\
t=3 &: 000011011110000\\
t=4 &: 000110010001000\\
t=5 &: 001101111011100
\end{aligned}
\]

The all-zero configuration is a fixed point. These are reference values for the fixture; they are not outputs from a candidate modeling tool.

### Evaluation

**MMT** can host a formal theory of configurations and transition rules, with suitable logic used to state invariants or behavioral equivalence. A generic simulation run is not guaranteed by declaring a theory. **Institution theory** can abstract the transition semantics and support comparisons of formalizations, but it is not a runtime. **SysML v2/KerML** has behavioral constructs and formal semantics, but the lattice and synchronous update need a specific encoding and conforming tool. **Modelica/FMI** could host a suitable discrete-dynamics encoding, but FMI does not automatically create a cellular-automaton abstraction. **DOL** can relate specifications written in supported formalisms but is not a simulator. **Ologs** can express some computations/structures but the paper's primitive-recursion result is not a ready-made CA runtime. **PROV-O** can track which version of a model/code/configuration produced a run without defining its rule semantics.

**Result:** “executable ontology” actually bundles at least three distinct things: a declarative state/transition specification, formal semantics/proofs about the transition system, and an implementation that produces a trace. The interface must specify initialization, boundary conditions, update schedule, trace format, and expected properties.

## 6. Test D — Empirical taxonomy with observations

### Fixture

A classification record for a specimen keeps distinct: (a) taxon/concept definitions and hierarchy; (b) the individual specimen's identifier; (c) observation records, method, procedure, time and result; (d) the classification decision and its provenance; and (e) uncertainty, competing candidates and later revisions.

### Evaluation

**SKOS** is directly relevant for sharing a taxonomy/knowledge-organization scheme, including concepts, labels, broader/narrower relations, notes and mappings. It is intentionally flexible, so it is not by itself a complete scientific classification logic. Source: [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/).

**OWL** can represent formal class/instance axioms when that is the intended meaning; not all broader/narrower relations in a taxonomy should be treated as subclassing. **SOSA/SSN** covers observations, feature/property of interest, procedures/sensors, results, time and samples. **PROV-O** records the entity/activity/agent chain behind collection, transformations, classification and revision. These vocabularies organize evidence; the application still must justify why observations warrant a classification. Sources: [SSN/SOSA](https://www.w3.org/TR/vocab-ssn/) and [PROV-O](https://www.w3.org/TR/prov-o/).

**OAEI** runs benchmark evaluations of ontology matching against defined tasks/reference alignments. Success on a benchmark is evidence about matching performance under that setup, not proof of biological truth or universal mapping correctness. Source: [OAEI 2026](https://oaei.ontologymatching.org/2026/).

DOL/MMT/institution theory can help formalize or relate the ontology artifacts, but do not replace the observation record or empirical assessment.

**Result:** this case needs distinctions among concept scheme/taxonomy, formal domain axioms, individual observations, classification decisions and provenance. A framework that models only taxonomy does not thereby ground the taxonomy in evidence.

## 7. Test E — Translation between independently specified formalisms

### Fixture

Formalism A defines sort Person, integer attribute age, and invariant age ≥ 0. Formalism B defines class Human, integer attribute ageYears, and the same invariant. Define an explicit mapping from A's sort/attribute/invariant to B's. Test whether every model satisfying A's constraints maps to a B model satisfying the corresponding constraints. Then deliberately change units or cardinality on one side and identify which preservation claim fails.

### Evaluation

**DOL** is the most direct candidate: the standard explicitly targets OMS in different formal languages and their mappings, with formal-semantic coherence checks including consistency, conservativity and intended consequences. It still requires appropriate underlying logic encodings and does not automatically discover a correct mapping. Source: [OMG DOL](https://www.omg.org/dol/).

**MMT** theory morphisms can represent translations, implementations, models and reuse across formal theories; each specific mapping still needs a definition and proof/verification obligation. **Institution theory** provides a general form for one key obligation—the satisfaction condition under signature morphisms—but the particular logic's signatures, sentences and models must be supplied. **Ologs** can give structure-preserving mappings for conceptual schemas. **SysML/MDE** and **FMI** are relevant for engineering/executable model exchange, not arbitrary logics. **OAEI** evaluates ontology matching; a proposed alignment is not a semantic-preservation theorem. SKOS mapping relations are useful conceptual links, not a substitute for provenance or proof of preservation.

**Result:** a mapping is not adequately specified by a “maps-to” edge alone. It needs a contract saying what it is expected to preserve—equivalence, refinement, consequences, operational correspondence, or an explicitly lossy transformation—and a suitable check.

## 8. Cross-case synthesis

The five tests suggest that strong prior art exists for most individual obligations:

- **Taxonomy/concept schemes:** SKOS; OWL/domain ontologies where logical constraints are needed.
- **Observations/grounding metadata:** SOSA/SSN, with calibration, uncertainty and scientific justification supplied by the domain workflow.
- **Provenance:** PROV-O or a domain-specific equivalent.
- **Formal theories, languages and proofs:** a suitable logic/proof system; MMT when modular multi-foundation representation is required.
- **Heterogeneous formal OMS integration:** DOL; institution theory when generic cross-logic/satisfaction-preservation claims matter.
- **Executable physical/system models:** Modelica/FMI for dynamic model exchange/execution; SysML v2/KerML for system structure and behavior.
- **Architecture descriptions/viewpoints:** ISO/IEC/IEEE 42010 where architecture description is in scope; it does not prescribe every modeling method/tool.
- **Alignment algorithm evaluation:** OAEI.

No candidate inspected so far documents native coverage of all five cases including proof, execution, empirical grounding and cross-formalism preservation. This does **not** yet demonstrate a novelty gap: a composition could suffice, and this was a source-based review rather than actual tool-level test. The possible gap may be the explicit interfaces/contracts between kinds of artifacts, not a missing grand ontology.

A provisional faceted view to test is: referent and evidence; conceptual domain model; representation language/metamodel; formal interpretation; inferential/proof/calculation operations; dynamics/operational execution; mappings and provenance. These are not claimed to be MECE layers: they overlap and are better treated as obligations or facets until more evidence supports a stricter decomposition.

## 9. Decision and next tests

**Current decision:** do not invent a universal representation language or assert a canonical MECE taxonomy. Treat the target as a candidate meta-framework/contract system for heterogeneous artifacts, and test whether DOL + MMT + explicit observation/provenance and execution interfaces cover the actual requirements.

Highest-value next steps:

1. Run the fixtures in actual tools: DOL/Ontohub or another conforming environment for mapped OMS; MMT for the arithmetic theorem and a transition-system theory; one SysML v2-capable tool for a behavior case; and Modelica/FMI tooling for the oscillator.
2. Record expected versus actual output, what was formalized, and what remained informal or delegated.
3. Compare all results with requirements R01–R18 in research-protocol.md and only change requirements with a recorded rationale.
4. Reopen the broader prior-art search if a tool test demonstrates a gap; otherwise adopt the smallest composition that satisfies the goal.

A novelty claim should wait until these implementation tests and additional citation chaining are complete.


## 10. Independent fixture-oracle checks (executed 2026-10-18)

I ran a small standalone Python check of the **expected behavior of the synthetic fixtures**, separate from all candidate frameworks:

| Check | Actual result | What it establishes | What it does not establish |
|---|---|---|---|
| Rule 30, 15-cell periodic ring, synchronous updates, first six states | Computed trace exactly matched all six expected bit strings recorded above; all-zero state was also confirmed as a fixed point | The cellular-automaton rule, boundary convention, and listed trace oracle agree | No DOL, MMT, SysML, or other modeling tool was run |
| Harmonic oscillator, RK4 step size at most 0.001, targets \(0,\pi/2,\pi\) | Maximum absolute error over position and velocity at target times: approximately \(2.081\times 10^{-13}\) versus the analytic reference | The selected equations, analytic reference values, and numerical sanity check are internally consistent | It does not validate a candidate simulator or any physical measurements |
| Arithmetic identity \(n+0=n\), for \(n=0,\ldots,1000\) | All bounded checks passed | A simple sanity test catches no fixture error over those inputs | Finite testing is not a proof of the universal theorem; no proof assistant was used |
| Toy translation of integer age values from Person.age to Human.ageYears, for values 0–1000 | Constructed 1,001 source Person records and corresponding Human records; all integer/nonnegative age and source-identity checks passed. A negative control that maps day counts directly to years was detected. | The toy mapping contract and a unit-mismatch counterexample are executable checks. | This is a bounded, hand-coded check, not a verified framework translation or general preservation proof |

These were executed in Python on the connected workstation. They are **fixture-oracle tests**, not candidate-framework conformance tests.

## 11. Adjacent implementation evidence already available in the workspace

A separate existing workspace project, **FOL Operational Metamodel** (not part of this repository), provides related implementation evidence:

- Its generated/pinned-fol-ir.json snapshot is derived from a pinned compiled MMT first-order-logic OMDoc artifact; its regression test fixes the snapshot's source hash and expected 16 nodes / 58 edges.
- Running the command python -m unittest discover -s tests -v in that project completed **21 tests successfully** on 2026-10-18.
- The tested capabilities include preserving MMT theory/constant identities and explicit declaration dependencies while importing compiled OMDoc; a small finite-structure evaluator checks formula satisfaction and rejects predicate arity/sort mistakes.
- A dedicated test asserts that a premise being true and a conclusion false in one finite structure does **not** establish semantic consequence. The README also explicitly says its fallback source extractor does not replace MMT parsing/type-checking.

This matters because it is a concrete existing composition of formal-source import, structural representation, a bounded semantic evaluator, and an inspectable graph projection. It should be reused as an adjacent prototype rather than rebuilt from scratch. Its scope remains limited: the tests do not show the MMT executable checking the five fixtures, a universal theorem prover, DOL mappings, Modelica execution, or empirical grounding.

## 12. Updated status and next action

- **Validated:** the five fixture oracles are internally consistent under the stated bounded checks; the connected workspace's FOL importer/evaluator regression suite passes.
- **Still source-assessed only:** candidate capability ratings for DOL, MMT as a framework, SysML v2/KerML, Modelica/FMI, SKOS/SOSA/SSN/PROV-O, and OAEI.
- **Still outstanding:** native tool runs for a formal theorem/proof, a DOL cross-formalism mapping with an explicit preservation check, and an actual Modelica/FMI or SysML behavior-model execution.

The high-value next move is to extend the existing formal-logic prototype with **one proof-producing/checkable theorem and one explicit translation/preservation test**, then compare that actual capability boundary with MMT/institution theory/DOL. For dynamics, run the oscillator in a dedicated Modelica/FMI environment when one is available. Do not treat a fixture passing in standalone Python as evidence that the candidate frameworks implement it.


## 13. Z3 solver checks: arithmetic and mapping (executed 2026-10-18)

A native solver check was successfully performed after downloading the official PyPI wheel for z3-solver==5.3.1.0 and verifying its SHA-256 against the published wheel checksum. It was installed with pip's --target option in an isolated temporary directory; the global Python environment was not modified. Exact records are in [solver-checks.json](solver-checks.json).

| Query | Z3 result | Interpretation |
|---|---|---|
| Find \(n\in\mathbb{Z}\) with \(n\geq0\) and \(n+0\ne n\) | **UNSAT** | No counterexample exists in the encoded integer theory, so \(n+0=n\) holds for all nonnegative integers under this encoding. Z3 returned an internal proof object (188 characters). |
| Find a violation given source_age >= 0, dest_age == source_age, and (dest_age < 0 OR dest_age != source_age) | **UNSAT** | No counterexample to the explicitly stated identity-mapping postcondition exists in the encoded integer model. |
| Find a violation when years >= 0, days == 365 * years, converted_years == days / 365 | **UNSAT** | Division by 365 preserves the original year count for exact day counts under Z3 integer arithmetic. |
| Find a positive years2 where days2 == 365 * years2 but days2 != years2 | **SAT** | Z3 returned a counterexample: years2 = 1, days2 = 365. Directly copying a day count to a years field is invalid. |

### What this adds

This is stronger than the earlier bounded enumeration: Z3 explored the encoded integer constraints and returned UNSAT for the counterexample queries, rather than merely testing a finite list of values. It also produced a native solver proof object for the arithmetic refutation.

The scope still matters:

- This is a **solver-level SMT proof by refutation**, not a natural-deduction/induction proof authored in Lean, Coq, Isabelle, or MMT, and not a certificate independently checked by a small trusted proof kernel.
- The mapping postconditions were explicitly encoded in SMT. The result establishes the stated integer properties, not general semantic preservation between arbitrary formalisms.
- The unit-conversion check assumes exact integer-day counts equal to 365 times the integer-year value. It says nothing about leap years, duration semantics, calendar systems, or empirical age estimates.
- No DOL, MMT executable, SysML v2/KerML, Modelica, or FMI runtime was exercised by these checks.

### Revised next step

A basic arithmetic theorem and one mapping contract now have solver-level evidence. The most informative unresolved technical tests are to: (1) formalize the theorem in a proof assistant or MMT-native formalization and capture the proof/checking path; (2) exercise a real DOL mapping between two OMS and record actual coherence/preservation checks; and (3) execute the oscillator in Modelica/FMI or a conforming SysML v2 behavior tool. The canonical-factorization question remains open.


## 14. Lean proof-assistant check (executed 2026-10-18)

I submitted the corresponding Lean source through the public [Lean playground](https://academy.lean4.dev/playground) editor and pressed **Run**. The UI reported **“Compiled without errors”** in 1.5 seconds and identified the compiler as **Lean 4.30.0**, using its core library (mathlib is not installed). Exact source is saved in [lean-proof-checks.lean](lean-proof-checks.lean); result/environment metadata is saved in [lean-proof-checks.json](lean-proof-checks.json).

The checked declarations:

| Declaration | Statement / obligation | Lean method | Result |
|---|---|---|---|
| \`nat_add_zero\` | \`∀ n : Nat, n + 0 = n\` | \`simp\` | Checked; the UI printed a proof term \`fun n => of_eq_true (eq_self n)\`. |
| \`identity_age_mapping_preserves_nonneg\` | If \`0 ≤ source\` and \`dest = source\`, then \`0 ≤ dest\` over \`Int\` | \`omega\` | Checked; the UI printed a proof term for the invariant. |
| \`exact_days_to_years\` | \`(365 * years) / 365 = years\` for \`years : Nat\` | \`omega\` | Checked for exact whole-year day counts under natural-number division. |
| \`naive_units_counterexample\` | There exist positive integer \`years\` and \`days = 365 * years\` with \`days ≠ years\` | \`decide\` with witness \`years = 1, days = 365\` | Checked; the UI printed an existential proof term. |

The source uses no \`sorry\` or \`admit\`.

### What this changes

This is now an actual Lean proof-assistant/kernel workflow for these four **small formal statements**, not only an SMT query or bounded enumeration. The unit mismatch is represented both as a concrete counterexample and as a machine-checked existential proposition.

### Boundaries that remain

- This is not an MMT-native formalization, a DOL mapping, or a test of a general framework's ability to preserve semantics across languages.
- The identity-mapping theorem assumes the mapping equation \(dest = source\). It does not establish that a real transformation between two independently specified ontologies is correct.
- The day/year theorem assumes exact counts of the form \(365 \\times years\). It does not cover leap years, calendars, duration semantics, uncertainty, or empirical age inference.
- These examples validate selected obligations; they do not establish any canonical, complete, minimal, or MECE factorization of all representations.

### Updated next action

The math/proof example now has a Lean-checked result. The most valuable remaining implementation tests are: (1) an actual DOL mapping between two supported OMS with a documented coherence/preservation check, and (2) a native execution of the oscillator or cellular-automaton behavior in Modelica/FMI or a conforming SysML v2 tool. Results should be captured as tool outputs and tested against the corresponding requirements R01–R18.


## 15. Actual Hets DOLiator translation smoke test (executed 2026-10-18)

I submitted the public DOLiator's built-in DOL example through its ordinary UI and inspected its JSON output. The source was saved as [dol-translation-smoketest.dol](dol-translation-smoketest.dol); detailed output and limitations are in [dol-tool-checks.json](dol-tool-checks.json).

### Successful result

Hets DOLiator returned a development graph with **3 nodes and 2 edges**:

1. \`Parthood_OWL\` — an OWL ontology containing \`AsymmetricObjectProperty(:isProperPartOf)\` and \`SubObjectPropertyOf(:isProperPartOf :isPartOf)\`.
2. \`Parthood_CL__E1\` — an internal Common Logic bridge node generated by the requested translation.
3. \`Parthood_CL\` — a Common Logic extension containing the extra axiom that \`isProperPartOf\` is transitive.

The generated edge from OWL to the internal node was typed \`HetDefInc\` and used morphism \`OWL22CommonLogic\`; the second edge was a \`GlobalDefInc\` using an identity morphism for Common Logic. The tool expanded the bridge with the Common Logic axioms associated with the translated OWL vocabulary.

This is **real tool evidence** that the public DOLiator accepts the example, constructs a heterogeneous development graph, applies the named OWL-to-Common-Logic comorphism, and represents an extension in the target logic.

### Failed consistency-check attempt (a meaningful limitation)

I invoked the page's **Tools → consistency checker** action in two ways: (a) with all three graph nodes selected; and (b) with only \`Parthood_OWL\` selected and prover \`Pellet\`. Both attempts returned:

\`\`\`
*** Error:
user error (no cons checker found)
\`\`\`

Therefore **no consistency or satisfiability result was obtained**. This is a limitation of the deployed checker environment, not evidence that the ontology is inconsistent, and not evidence that Hets as a whole lacks such a checker. The automatic-proof menu was available, but this example does not set up a suitable goal requiring an independent proof.

### What the test does and does not establish

- **Established:** DOL source parsing and the generation of an explicit OWL → Common Logic translation/inclusion graph for this sample.
- **Not established:** satisfaction preservation for a user-defined mapping; consistency of the source/target ontologies; conservativity of the extension; correctness of a mapping between independently specified Person/Human schemas; or universal/MECE coverage.
- The result URL contains a temporary run identifier. The source and structured observation are committed as durable artifacts, so the result can be discussed even if that temporary page expires.

### Revised next step

The most important uncompleted DOL test is now precise: run a custom pair of OMS plus an explicit mapping and **obtain a working checker result** for a stated semantic obligation. The current hosted service's consistency checker is unavailable for this attempt, so the next route is either another supported Hets/Ontohub environment with checkers configured or a local Hets deployment. After that, run an actual dynamic model in Modelica/FMI or SysML v2. Do not infer successful formal verification from a development graph alone.


## 16. Automatic-proof route in DOLiator (executed 2026-10-18)

I also opened the public DOLiator **Tools → automatic proofs** interface, selected **E Prover** and the \`OWL22CASL:CASL2TPTP_FOF\` translation, set a 10-second timeout per goal, left “include Theorems” enabled, and submitted via the normal **Prove** button.

The service returned:

\`\`\`
nothing to prove
\`\`\`

No goal was generated for this example in that workflow. This is **neither a proof success nor a proof failure** because no proposition was checked. It corroborates the boundary noted above: this built-in sample demonstrates parser/development-graph construction, but it does not provide a checked preservation theorem. The service's consistency action separately returned \`no cons checker found\`.

The exact interaction and temporary output URL are recorded in [dol-tool-checks.json](dol-tool-checks.json). To obtain formal verification evidence, the next test must include a real proof goal/view obligation in a supported DOL case and use a Hets environment with a working checker.
