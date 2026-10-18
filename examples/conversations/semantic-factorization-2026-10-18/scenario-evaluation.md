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
