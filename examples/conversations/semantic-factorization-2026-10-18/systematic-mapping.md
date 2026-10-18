# First-pass systematic map: methods and frameworks for heterogeneous representation

**Date searched:** 2026-10-18  
**Status:** first-pass, bounded map; not a completed systematic review and not a claim of exhaustive coverage.  
**Question:** What established methods should guide prior-art-first cross-disciplinary synthesis, and what existing technical frameworks already represent, relate, transform, or execute heterogeneous representations?

## Executive finding

Two different problems must not be conflated:

1. **How to investigate and synthesize the landscape.** The closest procedural match found is Jabareen's conceptual framework analysis (CFA): a qualitative method for building a network of linked concepts from multidisciplinary literature. Pair it with systematic mapping for search/classification and an integrative review for appraising and synthesizing heterogeneous theoretical and empirical sources. This combination is a proposed workflow assembled from established methods; it is not one named standard.
2. **What technical framework can represent the artifacts.** The strongest directly relevant candidate remains OMG's Distributed Ontology, Model, and Specification Language (DOL), which deliberately integrates heterogeneous ontologies, models, specifications, and mappings without requiring one universal object language. MMT and institution theory are important formal foundations; model-driven engineering (MDE), SysML v2/KerML, ISO/IEC/IEEE 42010, ologs, and ontology-alignment research cover other adjacent layers.

The sources reviewed so far do **not** establish one canonical, minimal, MECE factorization covering arbitrary representation, formal interpretation, real-world grounding, proof/calculation, dynamics, and execution. This is a bounded-search conclusion, not proof of nonexistence.

## Search protocol actually performed

This pass used web-search discovery on 2026-10-18 and checked available primary or authoritative sources for the lead candidates. Queries included:

- "framework integrating heterogeneous models representations ontology mathematics simulation cross disciplinary interoperability"
- "formal framework heterogeneous logics theories models semantics institutions theory ontology metamodeling"
- "knowledge representation framework mapping between ontologies models languages semantics conceptual framework analysis methodology"
- "Distributed Ontology Model and Specification Language DOL heterogeneous ontologies theories official"
- "MMT framework Rabe foundation-independent formal knowledge theory morphisms ontology official documentation"
- "institution theory abstract model theory specification programming Goguen Burstall satisfaction condition"
- "Ologs A Categorical Framework for Knowledge Representation"
- "model-driven engineering survey da Silva 2015 conceptual model"
- "ISO/IEC/IEEE 42010 architecture description viewpoints model kinds"
- "SysML v2 KerML semantic foundation model interoperability OMG"
- "ontology alignment evaluation initiative ontology matching evaluation"

Search coverage was cross-disciplinary but limited to web-search results and source checks; it did not include a reproducible search of every bibliographic database, deduplication of a complete result set, formal screening by multiple reviewers, or a PRISMA-style flow. Accordingly, this document calls itself a first-pass map, not a completed systematic mapping study.

## A. Methodological prior art

| Method | What it contributes | Role in this inquiry | Limit / caveat |
|---|---|---|---|
| **Conceptual framework analysis (Jabareen, 2009)** | Eight-phase qualitative procedure: map sources; read/categorize; identify/name concepts; deconstruct/categorize; integrate; synthesize/resynthesize; validate; rethink. Treats a conceptual framework as a network of interlinked concepts. | Best-fitting core method for extracting and synthesizing concepts, assumptions, attributes, and relationships across disciplines. | Qualitative and non-deterministic; different researchers may produce different frameworks. It does not guarantee exhaustive retrieval, formal soundness, executable behavior, or a canonical/MECE result. |
| **Systematic mapping (Petersen et al., 2015 update)** | Structures a research landscape through explicit search, study selection, classification, and presentation. | Discovery and coverage layer: locate terminology families, candidate disciplines, source types, and research clusters before synthesis. | Mapping the landscape is not itself a full conceptual synthesis or proof that the search found everything. |
| **Integrative review (Whittemore & Knafl, 2005)** | A review approach designed to combine diverse methodologies and theoretical/empirical sources; discusses problem formulation, search, data evaluation, analysis, and presentation. | Evidence-quality layer, useful where standards, conceptual papers, formal results, empirical studies, and implementations must be compared without pretending they are the same kind of evidence. | The authors note that analysis and synthesis methods can remain under-specified; it needs explicit extraction rules and scenario tests here. |
| **Requirements traceability + scenario-based evaluation** | Links user goals to explicit requirements, evidence, and falsifiable test cases. | Prevents the synthesis from drifting into a convenient but incomplete list of dimensions. | These are supporting engineering/evaluation practices, not by themselves cross-disciplinary literature-synthesis methods. |
| **Provenance** | Records which source supports each claim, which conclusions are interpretation, and which assumptions remain open. | Makes source-to-recommendation reasoning auditable and helps distinguish “not found” from “does not exist.” | Provenance is only as strong as the source checks and search record maintained. |

### Recommended research workflow

**Goal and success criteria → systematic landscape map → evidence extraction/evaluation → CFA concept network → requirement traceability → scenario tests → adopt, compose, adapt, or document a residual gap.**

A comparison matrix is a reporting artifact within this workflow, not the methodology itself. Dimensions are requirements to test—not presumed-independent axes of a final factorization.

Primary methodological sources:

- Jabareen, Y. (2009), [“Building a Conceptual Framework: Philosophy, Definitions, and Procedure”](https://doi.org/10.1177/160940690900800406). The article explicitly proposes a qualitative method for building conceptual frameworks from multidisciplinary bodies of knowledge.
- Petersen, K., Vakkalanka, S., & Kuzniarz, L. (2015), [“Guidelines for conducting systematic mapping studies in software engineering: An update”](https://doi.org/10.1016/j.infsof.2015.03.007). It distinguishes landscape mapping from systematic reviews focused on synthesis.
- Whittemore, R. & Knafl, K. (2005), [“The integrative review: updated methodology”](https://doi.org/10.1111/j.1365-2648.2005.03621.x). It describes how to enhance rigor when combining diverse primary-research methods and theoretical sources.

## B. Technical framework landscape

| Candidate / family | Primary problem and contribution | Fit to the target question | Boundary to retain |
|---|---|---|---|
| **DOL — Distributed Ontology, Model, and Specification Language** | Formal interoperability among heterogeneous ontologies, models, specifications (OMS), and mappings; offers a metalanguage for expressing OMS in different formal languages and links among them. | **Closest direct match found** for a network of heterogeneous formal representations and relations between them. It explicitly does not attempt to subsume every language into one new language. | Formal coverage depends on the underlying OMS languages and semantics. This is not, on the evidence reviewed, a complete theory of empirical grounding, arbitrary proof/execution, or a minimal MECE factorization of every representation. |
| **MMT — foundation-independent framework for formal knowledge** | Modular representation of formal languages and knowledge, with theories, declarations, structures, and theory morphisms; avoids fixing one representation paradigm or semantics. | Strong meta-level candidate for representing multiple formal systems and their content. | Generality is not proof of a unique canonical decomposition; real-world grounding and executable behavior may require other systems. |
| **Institution theory** | Abstracts logical systems using signatures, sentences, models, satisfaction, and translations satisfying a formal compatibility condition. | A mathematically precise candidate for separating language from models and stating when translations preserve semantics. | Its core scope is logical systems; arbitrary nonlogical artifacts, measurement, and runtime execution need further structure. |
| **Model-driven engineering (MDE)** | Connects systems, models, metamodels, modeling languages, transformations, software platforms/products, and—in some approaches—execution. | Strong candidate for the transition from model description to implementation/executable system and for traceable transformations between abstraction levels. | Not by itself a universal account of all logical meaning, proof, empiricism, or representation types; capability depends on the modeling formalism/toolchain. |
| **SysML v2 / KerML** | OMG systems-modeling standards: KerML provides a semantic and syntactic foundation for SysML v2; related APIs/services target model interoperability. | Important practical candidate for system structure, behavior, requirements, relationships, and engineering model exchange. | A systems-engineering modeling language/foundation, not a universal meta-framework for mathematical proof, scientific grounding, or every representation family. |
| **ISO/IEC/IEEE 42010:2022** | Specifies the structure and expression of architecture descriptions, including architecture description frameworks/languages, viewpoints, and model kinds; distinguishes an architecture from the description of it. | Useful vocabulary for separating the thing of interest, its descriptions, viewpoints, and model kinds—highly relevant to representation-vs-referent distinctions. | Explicitly does not prescribe the processes, methods, notations, models, or tools used to create or manage an architecture description; not an all-purpose formal semantics. |
| **Ologs / categorical knowledge representation** | Category-theoretic conceptual schemas with types, functional relationships, equations/constraints, and functorial mappings; can connect schemas/worldviews. | Useful for a compositional view of conceptual schema and structure-preserving mappings; category theory is relevant here for precise composition, not because it automatically solves the entire problem. | Basic ologs are not, alone, a universal host for arbitrary logics, proof systems, dynamics, empirical validity, or simulation. |
| **Ontology matching / alignment (OAEI)** | Research community and benchmark campaigns for comparing ontology-matching systems against reference alignments and test tracks. | Supplies an evaluation discipline for one important subproblem: discovering correspondences between independently authored ontologies. | Aligning ontologies is narrower than defining a universal space of all representation forms; matching scores do not establish semantic equivalence in every context. |
| **BFO / GFO and upper ontologies** | Provide upper-level categories and ontological commitments about entities, processes, relations, time, and related distinctions. | Useful for the *domain/reality side* of a framework—what kinds of things are being represented. | An upper ontology is not itself a meta-framework of representation languages, translations, proofs, and execution. |
| **Universal logic** | Studies general aspects of logic and relations among logical systems without privileging one logic. | Relevant if the formal proof shows that representational languages can be classified through properties of logical systems or institutions. | Its scope is logic; it does not automatically cover nonlogical artifacts, observational grounding, or arbitrary computation. |

Primary and authoritative technical sources:

- OMG, [DOL overview](https://www.omg.org/dol/) and [DOL specification catalog](https://www.omg.org/spec/DOL/). The overview explicitly describes interoperability across heterogeneous OMS and mappings, grounded in formal semantics.
- MMT, [framework documentation](https://uniformal.github.io/doc/).
- Goguen & Burstall, [“Institutions: Abstract Model Theory for Specification and Programming” (1992)](https://doi.org/10.1145/147508.147524); see also [Goguen's institution-theory overview](https://cseweb.ucsd.edu/~goguen/projs/inst.html).
- da Silva, [“Model-driven engineering: A survey supported by the unified conceptual model” (2015)](https://doi.org/10.1016/j.cl.2015.06.001).
- OMG, [SysML v2 / KerML specifications](https://www.omg.org/spec/SysML/2.0) and [July 2025 adoption announcement](https://www.omg.org/news/releases/pr2025/07-21-25.htm).
- ISO, [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html).
- Spivak & Kent, [“Ologs: A Categorical Framework for Knowledge Representation” (2012)](https://doi.org/10.1371/journal.pone.0024274).
- Ontology Alignment Evaluation Initiative, [overview](https://oaei.ontologymatching.org/) and [2026 campaign](https://oaei.ontologymatching.org/2026/).

## C. Tentative layered synthesis to test (not a final ontology)

The landscape suggests that the user’s target may be better treated as a **stack of distinguishable obligations plus explicit mappings**, not a single linear “semantic spectrum”:

1. **Target/referent layer** — intended entities, observations, measurements, interventions, identifiers, and uncertainty.
2. **Conceptual/domain layer** — concepts, categories, instances, relations, attributes, identity, cardinality, time, and domain constraints.
3. **Language/meta-model layer** — syntax, types/signatures, schemas, metamodels, and representation-language definitions.
4. **Formal-semantic layer** — interpretation, models, satisfaction, entailment, equivalence, and preservation conditions.
5. **Inferential/proof/calculation layer** — derivations, theorem/proof objects, rules, algorithms, and computation results.
6. **Dynamics/operational layer** — states, transition rules, laws, initial conditions, execution semantics, simulations, traces, and invariants.
7. **Integration/provenance layer** — mappings, translations, refinements, alignments, losses, source evidence, and traceability across layers.

These layers are intentionally **not claimed to be MECE**. Some overlap is expected; for example, a model can simultaneously encode a theory, define operational behavior, and be connected to measurements. The exact decomposition must be revised through test cases and grounded in the candidate literature. DOL/MMT/institutions appear most relevant to formal integration; MDE/SysML to engineering models and execution; upper ontologies to domain commitments; ologs to compositional schemas; and explicit empirical data/provenance to grounding.

## D. Tests that can falsify the synthesis

Do not accept the layered hypothesis merely because it is tidy. Test it against:

1. **Physics + simulation:** distinguish laws/theory from the numerical method, parameterization, initial/boundary conditions, run, output trace, and comparison with measurements and uncertainty.
2. **Math + proof:** distinguish vocabulary/axioms, semantic models, theorem statements, proof objects/derivations, calculations, and machine checking.
3. **Cellular automaton:** represent the cell lattice, state set, neighborhood, local transition rule, initial configuration, update schedule, execution, and trace; assess invariants and behavioral equivalence.
4. **Empirical taxonomy:** distinguish category definitions from individual identifiers, observed data, provenance, borderline cases, contradictions, and revisions.
5. **Cross-formalism translation:** use two independently specified systems, an explicit mapping, and stated preservation/loss conditions; verify which properties really survive.

For each case, record native support, encoded support, delegated support, unformalized parts, and the actual guarantees/evidence. A failed test should update the conceptual framework or requirements, not be hidden as an “edge case.”

## E. Decision and next actions

1. Treat CFA as the current core synthesis method; use systematic mapping for discovery and integrative-review practices for mixed evidence. Keep the limitations visible.
2. Add SysML v2/KerML, ISO 42010, and ontology-alignment evaluation as candidate families in the comparison matrix; verify primary specifications and one worked example for each before scoring.
3. Fill the requirements matrix with evidence-status labels (demonstrated, claimed, composable/delegated, partial/conditional, explicitly out of scope, unknown), avoiding unsupported numeric rankings.
4. Implement small versions of the five tests in the strongest candidates—especially DOL, MMT, and relevant MDE/SysML tooling. Record source artifacts and missing mechanisms.
5. Update the candidate synthesis only after the tests. Document any new concept as a residual gap only after showing why existing frameworks cannot satisfy the corresponding requirement through configuration or composition.

## Research cautions

- A bounded web-search pass cannot prove that no universal factorization exists.
- A standard's overview is not a complete conformance analysis; normative clauses and actual tooling examples remain to be examined.
- “Not core” must not be reported as “impossible.”
- An empty cell means “unknown” unless there is affirmative evidence of an exclusion.
- Category theory, database theory, ontology engineering, model theory, and operational semantics are not one interchangeable framework; their interfaces and preservation conditions need explicit treatment.
