# Prior-art investigation: a general framework for heterogeneous representations

**Status:** targeted literature investigation, 2026-10-18. This is broader than the initial scan, but is not a systematic review.

## Executive finding

The user's intuition maps to several established research areas. The closest direct match discovered is the OMG standard **Distributed Ontology, Model, and Specification Language (DOL)**. DOL explicitly treats ontologies, formal models of systems, and formal specifications of system properties/behavior as different kinds of ontology/model/specification (OMS) artifacts, and provides a formal language for mappings between artifacts expressed in different languages. It deliberately does **not** try to create one language that subsumes everything else.

Two complementary frameworks are especially important:

- **MMT** is a foundation-independent meta-framework for representing formal languages and knowledge, including logics, type theories, set theories, ontologies, declarations, expressions, proofs, and mappings between theories.
- **Institution theory** abstracts logical systems into signatures, sentences, models, satisfaction, and translations that preserve satisfaction.

For the executable-model intuition, **model-driven engineering (MDE)** and programming-language semantics address models, metamodels, transformations, and executable/non-executable semantics.

**Revised assessment:** It is too strong to say the user's intended idea has not been worked out. A large amount has. The better question is which of these existing frameworks best matches the intended *scope*, and whether the remaining desire is specifically for a canonical, independent factorization of representational capabilities. No inspected source establishes that last claim as a universal theorem.

## 1. DOL — strongest direct match for heterogeneous ontologies, models, specifications, and mappings

**Primary sources:**
- Object Management Group, [DOL overview](https://www.omg.org/dol/)
- [DOL specification, version 1.0](https://www.omg.org/spec/DOL/)

DOL is an OMG standard for formal interoperability across heterogeneous ontology, model, and specification artifacts. The OMG describes OMS artifacts as ranging from domain knowledge and activities to models of systems and specifications of hardware/software properties and behavior. Complex systems may use multiple formalisms and multiple viewpoints; DOL supplies a formal way to express the artifacts and mappings between them, and supports checks of coherence such as consistency, conservativity, intended consequences, and compliance.

Most importantly, DOL explicitly declines to propose one new OMS language that subsumes all others. Instead, it formally connects existing formalisms.

**Why this is close:** The user imagines different representations—of what exists, relations and laws, initial conditions, proofs/calculations, and runnable systems—as related forms that should be connected by a principled framework. DOL directly addresses the heterogeneous integration part of this intuition, including ontologies, models, specifications, and mappings.

**Limit:** DOL is primarily a metalanguage and interoperability framework. Its existence does not show that it derives a universal MECE list of all representational capabilities, nor that every artifact is executable or empirically grounded. It provides a standard way to state and relate heterogeneous formal artifacts, not a proof that every form is reducible to one canonical factorization.

## 2. MMT — strongest general meta-framework for formal knowledge and languages

**Primary source:** Florian Rabe, [MMT: A Foundation-Independent Approach to Formal Knowledge](https://uniformal.github.io/doc/philosophy/articles/mmt.pdf) (2016); [MMT documentation](https://uniformal.github.io/doc/).

MMT represents declarative languages without committing to one syntax, semantics, or foundation. Reusable modules define language features; languages are assembled from these modules. The paper describes how MMT uniformly represents logics, type theories, set theories, ontologies, symbols, concepts, relations, individuals, judgments, inference rules, axioms, theorems, formulas, derivations, and proofs. Theory morphisms represent translations, implementations, models, and other relationships between theories. It also combines several established approaches, including institutions, structured theories, and proof/type-theoretic ideas.

**Why this is close:** MMT takes the “meta-framework for many forms of formal representation” goal seriously. Its small, reusable primitives and compositional structure are more relevant to a canonical-factorization question than a fixed domain ontology.

**Limit:** MMT's strongest coverage is formal/declarative knowledge and the infrastructure around it. It does not, merely by being foundation-independent, establish a universal decomposition for empirical reference, physical-model validation, arbitrary dynamical systems, or every form of computation.

## 3. Institution theory — a formal abstraction of logical representation systems

**Primary source:** Joseph A. Goguen and Rod M. Burstall, [Institutions: Abstract Model Theory for Specification and Programming](https://doi.org/10.1145/147508.147524) (1992); [author resource](https://cseweb.ucsd.edu/~goguen/projs/inst.html).

An institution abstracts a logical system into:
- signatures (the vocabulary or formal context);
- sentences over each signature;
- models for each signature;
- a satisfaction relation telling which models satisfy which sentences.

Signature translations induce translations of sentences and models, with a satisfaction condition ensuring that truth is invariant under change of notation. The original work addresses specification and programming, databases, constraints, and combinations of different logical systems.

**Why this is close:** It gives a rigorous candidate for the logical core: syntax/context, statements, models, satisfaction, and semantics-preserving translation. It is a first-principles answer to how different logics can be described uniformly.

**Limit:** It is an abstraction of logical systems, not a complete ontology of all representation kinds. Operational behavior and empirical grounding require additional formal treatment when they are not already supplied by the chosen institution.

## 4. Model-driven engineering (MDE) — model-to-execution pipeline

**Primary source:** Alberto Rodrigues da Silva, [Model-driven engineering: A survey supported by the unified conceptual model](https://doi.org/10.1016/j.cl.2015.06.001) (2015).

The survey explicitly relates systems, models, metamodels, modeling languages, transformations, software platforms, and products. It treats models as artifacts from which software can be generated or automatically executed. It also distinguishes executable from non-executable semantics and discusses operational and translational semantics for executable models.

**Why this is close:** It formalizes the idea that a model can be extended with rules and then transformed into, or interpreted as, an executable system.

**Limit:** MDE focuses on software and systems engineering, not a universal theory spanning all scientific, mathematical, logical, and empirical representations.

## 5. Ologs — conceptual structures, databases, mappings, and computation

**Primary source:** David I. Spivak and Robert E. Kent, [Ologs: A Categorical Framework for Knowledge Representation](https://doi.org/10.1371/journal.pone.0024274) (2012); [open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3269434/).

Ologs represent types as objects, functional relations as arrows, and equations as constraints on compositions. They connect conceptual models with databases and instances, support mappings between models, and demonstrate the representation of primitive recursive functions.

**Why this is close:** A concrete bridge between ontology-like structures, database schemas, structure-preserving mappings, and computation.

**Limit:** Ologs are a particular representation formalism, not a proven universal factorization.

## 6. General Formal Ontology (GFO) and Basic Formal Ontology (BFO) — a different target

**Primary sources:**
- [GFO project](https://www.onto-med.de/ontologies/gfo/)
- Loebe, Burek, and Herre, [GFO: The General Formal Ontology](https://doi.org/10.3233/AO-220264) (2022)
- [BFO overview and literature](https://basic-formal-ontology.org/)

These are top-level ontologies: they formalize general categories of things in reality, such as objects, processes, time, properties, relations, roles, and functions (with different category systems in GFO and BFO).

**Why relevant:** They address the user's question about whether there are general types of things and relations that recur across domain ontologies.

**Why not the main answer:** A top-level ontology is primarily an account of what kinds of entities exist and how they relate. It is not the same thing as a meta-framework for comparing representational languages, models, proofs, and executable systems. This is a crucial distinction between an ontology *of a domain/reality* and an ontology/metamodel *of representation systems*.

## 7. Universal logic — general theory of logical systems

**Primary source:** [Logica Universalis: Towards a General Theory of Logic](https://link.springer.com/book/10.1007/978-3-7643-8354-1), edited volume.

Universal logic studies features common to logical systems and formal ways of comparing logics. It is relevant if the core problem is to characterize logics, consequence relations, and translations independently of any one particular logic.

**Limit:** Its scope is logic, not all representational systems, physical grounding, or simulation.

## What the literature suggests about the original formulation

The initial phrase “canonical factorization of all possible forms of semantic representation” may be combining three distinct research problems:

1. **A theory of representational systems:** What are the formal components of a language/system that can represent things? MMT and institution theory are close here.
2. **A theory of heterogeneous integration:** How can distinct ontologies, models, specifications, and logics be related while preserving the relevant semantics? DOL is a direct match.
3. **A theory of model execution:** How can a model's structure, constraints, laws, and initial conditions determine a computation or behavior? MDE and operational semantics are close here.

A fourth, separate question is empirical grounding: what links the model's symbols and structures to intended real-world referents or observations? Model theory specifies formal interpretation/satisfaction, but this should not be conflated with empirical validation or reference.

The user's original intuition need not be discarded. It may need to be restated as a search for a **compositional meta-framework for heterogeneous representations, with formal mappings and optional operational semantics**, rather than a single linear semantic spectrum. The canonical/MECE factorization is then a more specific question to test against that existing framework.

## Recommended next steps

1. Read the OMG's DOL overview/specification first, because it explicitly names ontologies, models, specifications, heterogeneous formalisms, and mappings.
2. Read the MMT overview/paper to understand the meta-framework and its reusable formal primitives.
3. Use institution theory to understand the abstract logic/model/satisfaction core.
4. Use MDE and operational semantics to test the executable-system requirement.
5. Only after this comparison ask what remains absent: e.g. a formal independence result for dimensions, a completeness theorem over a defined universe of formalisms, or a unified treatment of empirical grounding.

## Confidence and limits

- Strong evidence exists for substantial prior art across all these components.
- DOL is the closest direct match found to the integration of heterogeneous ontologies, models, specifications, and mappings.
- MMT is the strongest candidate in this set for a general, modular framework for formal languages and knowledge.
- No inspected source establishes that a single universally canonical, MECE factorization covers every intended form of representation, including empirical grounding and arbitrary executable systems.
- This is a targeted literature investigation, not proof of nonexistence. The correct conclusion is “the intuition overlaps strongly with established work; the exact universal claim remains unverified,” not “nobody has done it.”
