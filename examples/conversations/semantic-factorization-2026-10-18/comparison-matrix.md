# Comparative matrix: frameworks for semantic representation

Status: **working hypothesis, not final scoring**. This matrix is designed to be revised as primary sources and worked examples are examined. “Not core” means the framework is not primarily designed to solve that problem; it does not mean the problem is impossible to address with extensions or integrations.

## 1. Framework comparison

| Framework | Main problem it addresses | What it provides | Strengths / advantages | Limitations / questions to test |
|---|---|---|---|---|
| **Distributed Ontology, Model, and Specification Language (DOL)** | Expressing and relating heterogeneous ontologies, models, and specifications | A metalanguage for OMS written in different formal languages; structuring constructs, translations, and mappings; formal semantics and criteria such as consistency, conservativity, and consequence | Closest direct match for integrating heterogeneous formal representations; explicitly treats networks of OMS rather than requiring one universal object language | Does not define all underlying languages; does not provide algorithms that automatically discover mappings; empirical grounding and executable operational models are not its central promise. Does it cover the user's required representational spectrum through composition? |
| **MMT** | Modular, foundation-independent representation of formal knowledge and formal languages | Theories, declarations, symbols, judgments, axioms, theorems, proofs, structures, and theory morphisms; framework for describing different logical/formal systems | Broad and extensible; can represent both a formal language and content expressed in it; supports translations and reuse without fixing one foundation | Breadth of framework is not the same as a canonical, minimal, or exhaustive factorization. Need to test how empirical observations/referents and simulation execution are represented versus linked through other systems. |
| **Institution theory** | Abstracting the common structure of logical systems and translating between them | Signatures, sentences, models, satisfaction, and signature morphisms; satisfaction-preserving translations | Clean mathematical core for comparing logics while keeping syntax and semantics distinct; useful basis for formal interoperability | Primarily a framework for logical systems, not a complete account of all semantic representations, physical grounding, or executable artifacts. How far do its abstractions stretch before extra machinery is needed? |
| **Model-driven engineering (MDE)** | Relating system models, metamodels, modeling languages, transformations, and software implementations | Model/metamodel relations, transformations, code generation, and in some approaches executable models and operational semantics | Strong bridge from representation to implementation and execution; useful for testing whether a model can be run or transformed into a system | Does not by itself provide a universal account of logical meaning, proof, ontology, or empirical truth. Tool- and domain-specific assumptions may matter. |
| **Ologs / categorical knowledge representation** | Structuring conceptual knowledge and mappings between conceptualizations | Types, functional relationships, constraints/equations, and structure-preserving mappings | Intuitive schema-like representation with a precise mathematical account of composition and mappings; useful for conceptual alignment | The basic form is not a universal host for arbitrary logic, proofs, dynamics, or simulations. Need to test representation of non-functional relations, uncertainty, time, and operational behavior. |
| **BFO / GFO (upper-level ontologies)** | Providing general categories for entities and reality | Categories such as objects/continuants, processes/occurrents, qualities, relations, time, space, roles, and functions (details differ by ontology) | Helps organize *what kinds of things exist* in a domain and makes ontological commitments explicit | These are ontologies, not general meta-frameworks for every representation format. They do not by themselves define proof systems, translations among formal languages, executable semantics, or empirical validation. |
| **Universal logic** | Studying common patterns and properties across logical systems | General tools and perspectives for comparing logics without privileging one particular logic | Useful for asking which properties are logic-independent and how logics relate | Scope is logic, not all representation types. Does not alone solve ontology-to-data grounding, simulation, or general model execution. |

## 2. Capability coverage (initial, provisional)

Legend:
- **Core** — directly part of the framework's stated purpose or formal machinery.
- **Partial** — possible or supported in a narrower form, by extension, or in combination with other machinery.
- **Not core** — not the framework's main target; do not infer impossibility.
- **Verify** — needs a primary-source check or a worked example before scoring.

| Capability / requirement | DOL | MMT | Institutions | MDE | Ologs | BFO/GFO | Universal logic |
|---|---|---|---|---|---|---|---|
| Represent multiple formal languages / theories | Core | Core | Core (logical systems) | Partial | Partial | Not core | Core (logics) |
| Represent syntax / vocabulary / types | Partial | Core | Core (signatures/sentences) | Core (metamodels) | Core (types/relations) | Core (ontology vocabulary) | Partial |
| Give a formal semantics / account of satisfaction or interpretation | Core (OMS semantics) | Core / extensible | Core | Partial; depends on modeling language | Core within categorical account | Ontological commitments, but different purpose | Core for logical comparison |
| Map / translate between representations | Core | Core | Core | Core (model transformations) | Core (functorial mappings) | Partial / ontology alignment needed | Core between logics, depending on approach |
| State and check consistency / logical consequences | Core, where supported by underlying logics/tools | Supported through formal systems/tools; verify exact workflow | Core conceptually; proof tooling varies | Partial; depends on formalization | Limited to chosen formal structure/constraints | Not core as a general proof service | Core as a topic, not one universal checker |
| Represent axioms, theorems, proofs, derivations | Through underlying OMS languages | Core | Core at logical abstraction level | Not core | Partial | Not core | Discusses logics; not itself a proof assistant |
| Represent time, processes, state change, dynamics | Depends on underlying language | Can encode in a suitable formalism; execution is separate | Depends on chosen logic | Core/strong in suitable executable modeling approaches | Partial | Core ontological categories include processes/time, but not execution | Depends on logic |
| Execute / simulate a model | Not core | Not core as a general guarantee | Not core | Strong in executable-model approaches | Not core | Not core | Not core |
| Link model to observations / real-world referents | Not a complete grounding solution | Not a complete grounding solution | Satisfaction is formal/model-theoretic, not automatically empirical grounding | Can connect to systems/data; empirical warrant is separate | Possible mappings, but not a general empirical-grounding theory | Realist ontology helps state commitments; does not validate observations | Not core |
| Define a canonical, minimal, exhaustive factorization of all representation forms | No evidence found | No evidence found | No | No | No | No | No |

**Important:** The last row means “not established by the sources reviewed so far,” not a proof that no such result exists.

## 3. Cross-cutting dimensions to track

For each framework, keep separate scores/notes for:

1. **Expressiveness:** What can be represented without changing the framework?
2. **Semantic precision:** Are meaning and interpretation formally defined?
3. **Heterogeneity:** Can distinct languages or semantic regimes coexist?
4. **Mappings:** Are translations explicit, compositional, and meaning-preserving?
5. **Inference and verification:** What can be derived or checked, and by which tools?
6. **Identity and cardinality:** How are identity, equality, collections, multiplicity, and type constraints handled?
7. **Dynamics and execution:** Can state transitions be described and actually run?
8. **Grounding:** How are symbols/models tied to observations, measurements, interventions, or referents?
9. **Uncertainty and partiality:** Can ambiguity, missing information, probability, or inconsistent data be represented?
10. **Extensibility and interoperability:** Can the framework be extended without losing formal guarantees?
11. **Practical maturity:** Standards, implementations, examples, tooling, and community adoption.
12. **Meta-level claims:** Is the framework descriptive, prescriptive, executable, normative, or a mixture?

## 4. Test cases that every candidate should face

| Test case | Minimum elements to represent | Questions that expose gaps |
|---|---|---|
| **Physical theory + simulation** | Variables/state, units, laws/equations, parameters, initial/boundary conditions, numerical method, observations | Can the framework distinguish the theory from its numerical implementation? Can it run the model? How are predictions compared with measurements and uncertainty? |
| **Mathematical theory** | Vocabulary/types, axioms, definitions, theorems, proof objects, derivations/calculations | Can it distinguish truth in a model from provability in a proof system? Are proofs machine-checkable? How are theories translated while preserving results? |
| **Cellular automaton** | Cell lattice, state set, neighborhood, transition rule, initial configuration, update schedule, execution trace | Can it represent both declarative rules and operational execution? Are equivalence, invariants, and behavior properties checkable? |
| **Empirical classification / taxonomy** | Categories, instances, membership, hierarchy, exceptions, provenance, observations | What makes a classification warranted? How are revisions, borderline cases, and conflicting observations handled? |
| **Cross-domain translation** | Two independently specified representations, mapping, preserved properties, known losses | Is the mapping explicit and compositional? Which properties are preserved, weakened, or lost? Can that be checked? |

## 5. Evidence ledger (to fill as research proceeds)

Add one row per claim, with a stable source and a concrete example where possible.

| Framework | Claim being assessed | Evidence type | Primary source / section | Demonstration or counterexample | Confidence | Open question |
|---|---|---|---|---|---|---|
| DOL | Integrates heterogeneous OMS and mappings | Standard/specification | OMG DOL 1.0, scope and semantics | To add | Medium — based on overview/spec scope; detailed clauses still need checking | Which guarantees apply to which underlying logics? |
| MMT | Foundation-independent modular representation of formal knowledge | Research paper / framework docs | Rabe, *MMT: A Foundation-Independent Approach to Formal Knowledge* (2016) | To add | Medium — broad framework described; coverage of our test cases untested | What is native versus encoded or delegated? |
| Institution theory | Abstracts logical systems via signatures, sentences, models, satisfaction | Foundational research paper | Goguen & Burstall, *Institutions: Abstract Model Theory for Specification and Programming* (1992) | To add | Medium — core formulation identified | What extra structure is needed for dynamics and empirical grounding? |
| MDE | Connects models/metamodels, transformations, and implementations | Survey / technical literature | da Silva, *Model-driven engineering: A survey supported by the unified conceptual model* (2015) | To add | Medium — broad survey identified | Which guarantees are semantic rather than tool-specific? |
| Ologs | Uses categorical structure for types, relations, constraints, and mappings | Research paper | Spivak & Kent, *Ologs: A Categorical Framework for Knowledge Representation* (2012) | To add | Medium — basic formalism identified | How does it handle dynamic, non-functional, or uncertain relations? |
| BFO/GFO | Supplies general ontological categories | Ontology specification / paper | Official BFO and GFO materials | To add | Medium — high-level scope identified | Which distinctions are useful to the target problem rather than domain-specific? |
| Universal logic | Studies general properties and comparisons of logics | Research book / papers | *Logica Universalis: Towards a General Theory of Logic* | To add | Medium — scope identified | Which results transfer to representations that are not logics? |

## 6. Decision rule

Do not rank a framework as “best overall” yet. For each test case:

1. Specify the representation and desired operations.
2. Build a small example in the candidate framework, or document precisely why it cannot be done natively.
3. Record what must be encoded, delegated to another formalism, or left informal.
4. Check which guarantees are formal, tool-supported, empirical, or merely asserted.
5. Update the matrix with a source citation and confidence level.

A possible eventual result is **a stack of complementary layers**, not a single winner: e.g. ontology for domain categories, a formal meta-framework for theories and mappings, a proof system for derivations, an executable model for dynamics, and a separate account of empirical grounding. Whether these layers can be unified more deeply remains the research question.

## Starting references

- OMG, [Distributed Ontology, Model, and Specification Language (DOL)](https://www.omg.org/dol/) and [DOL 1.0 specification](https://www.omg.org/spec/DOL/1.0/PDF)
- Florian Rabe, [MMT: A Foundation-Independent Approach to Formal Knowledge (2016)](https://uniformal.github.io/doc/philosophy/articles/mmt.pdf) and [MMT documentation](https://uniformal.github.io/doc/)
- Joseph A. Goguen and Rod M. Burstall, [Institutions: Abstract Model Theory for Specification and Programming (1992)](https://doi.org/10.1145/147508.147524)
- Alberto Rodrigues da Silva, [Model-driven engineering: A survey supported by the unified conceptual model (2015)](https://doi.org/10.1016/j.cl.2015.06.001)
- David I. Spivak and Robert E. Kent, [Ologs: A Categorical Framework for Knowledge Representation (2012)](https://doi.org/10.1371/journal.pone.0024274)
- [Basic Formal Ontology](https://basic-formal-ontology.org/) and [General Formal Ontology](https://www.onto-med.de/ontologies/gfo/)
- [Logica Universalis: Towards a General Theory of Logic](https://link.springer.com/book/10.1007/978-3-7643-8354-1)


## 7. Problem / use-case matrix (separate from capabilities)

This section asks **why someone would use the framework**. A use case names the problem, the user goal, and the useful outcome—not just a feature the framework happens to support. Initial entries are hypotheses to validate against primary sources, case studies, and examples.

| Framework | Problems it is intended to solve | Typical use cases / motivating situations | Useful outcome | When it is a poor fit or needs a companion |
|---|---|---|---|---|
| **DOL** | Formal knowledge is split across multiple ontology, modeling, or specification languages; people need to relate those artifacts without forcing them into one language | Combine domain ontologies with system specifications; express that one specification refines or translates another; organize a network of heterogeneous formal theories; state and assess relationships between specifications | An explicit, structured account of how independently expressed formal artifacts relate, including formal conditions that may be checked | When the primary need is to invent a domain ontology, automatically discover correspondences, directly simulate a system, or ground a theory in empirical measurements |
| **MMT** | Formal knowledge and its foundations are fragmented across different logics, type theories, and formal libraries; formal content is hard to reuse or connect | Represent a formal language and theories expressed in it; connect libraries; formalize translations between theories; build a foundation-independent knowledge infrastructure | Reusable formal content with explicit structure and theory-level relationships, without requiring every subject to share one foundational logic | When the main goal is a domain expert's lightweight taxonomy, an empirical validation workflow, or a runtime simulation rather than formal knowledge management |
| **Institution theory** | Researchers need a common mathematical way to define and compare different logical systems while preserving their semantic relationships | Define a new logic abstractly; compare logics; prove that a translation preserves satisfaction; formalize specifications in different logical systems | General results that can apply across logical systems instead of being reproved separately for each logic | When users need an out-of-the-box application, user-facing ontology, code-generation pipeline, or full account of physical measurement and simulation |
| **Model-driven engineering (MDE)** | Software/system complexity makes direct implementation hard to reason about; teams need higher-level models, transformations, and traceability to implementations | Generate code from models; transform models between abstraction levels; validate system designs; execute or simulate models in suitable environments; keep design artifacts aligned with implementations | A path from models to implementations, with repeatable transformations and potentially executable behavior | When the goal is a general theory of meaning, mathematical proof foundations, or ontology of reality independent of a particular engineering domain |
| **Ologs / categorical knowledge representation** | Domain knowledge is scattered across schemas and vocabularies; teams need a clear conceptual schema and principled mappings between viewpoints | Explain a domain's concepts and functional relationships; align conceptual schemas; connect databases or conceptual models through structure-preserving mappings | A compact, compositional conceptual model that makes categories, relations, and mapping assumptions visible | When the domain requires rich temporal processes, arbitrary logical proof, uncertainty, or executable dynamics beyond the chosen categorical formalism |
| **BFO / GFO** | Domain ontologies use incompatible or underspecified assumptions about what kinds of entities exist and how categories relate | Design or evaluate domain ontologies; distinguish enduring entities from processes; align domain terms to a shared upper ontology; make ontological commitments explicit | A shared top-level vocabulary and constraints for ontology design and interoperability | When the main problem is representing formal languages themselves, proving theorems, translating arbitrary logics, or executing a model |
| **Universal logic** | Logic research is fragmented into many systems, making it difficult to state what is general and what depends on a particular logic | Compare logical systems; investigate properties shared across logics; formulate general results without treating one logic as the default | A vocabulary and research program for identifying logic-independent structures and principles | When the target includes non-logical representations, empirical grounding, ontological classification, or runtime execution as first-class problems |

### Use-case prompts for ongoing research

For each framework, answer these questions from its own documentation and published examples:

1. **Who is the user?** (e.g. logician, ontology engineer, software architect, domain scientist, mathematician)
2. **What pain exists before the framework?** What is difficult, unsafe, expensive, ambiguous, or impossible without it?
3. **What artifact goes in and what comes out?** Be concrete: theories, mappings, model, generated code, proof, ontology, simulation trace, etc.
4. **What success criterion does it optimize?** E.g. semantic preservation, reuse, consistency, traceability, executability, conceptual clarity.
5. **What assumptions does it require?** A fixed logic, formalized input, domain vocabulary, executable semantics, tooling, or human-supplied mappings?
6. **What does it explicitly not try to solve?** Prefer scope statements and documented limitations over guesses.
7. **What does it contribute to our broader question?** Does it offer a candidate primitive, a composition rule, a translation mechanism, a grounding relation, or only a useful domain-specific solution?

### Keep problem, mechanism, and capability distinct

Example for DOL:

- **Problem:** Specifications are written in different formal languages and cannot be treated as one homogeneous artifact.
- **Use case:** A team wants to relate two specifications and state how one refines or translates the other.
- **Mechanism:** A metalanguage expresses OMS and relationships among them.
- **Capability:** It can express certain mappings and formal relationships, subject to the underlying languages and supported semantics.
- **Outcome to evaluate:** Whether the relationship is clear and whether relevant properties can be checked.
- **Open gap for our research:** This does not, by itself, establish how a model is empirically grounded or executed.

This pattern should be filled in for each candidate. It prevents the table from treating “supports mappings” as if that were itself the motivating problem or the practical benefit.
