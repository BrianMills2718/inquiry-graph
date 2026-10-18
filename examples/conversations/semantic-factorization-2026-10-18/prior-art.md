# Prior-art scan: canonical factorization of semantic representations

**Status:** first-pass comparison, 2026-10-18. This is a targeted search, not a systematic literature review.

## Question being tested

Can one established framework derive a nonredundant, compositional account of representations spanning:

- what exists and how entities are classified or related;
- properties, types, cardinality, and logical constraints;
- formal interpretations/models and truth or satisfaction;
- mappings between different representations or formalisms;
- laws, initial conditions, and state transitions;
- calculations, proofs, simulations, and executable behavior;
- correspondence between a model and its intended real-world referents?

The conversation's desired outcome is stronger than a single ontology language or an expressivity ladder. It asks whether a common formal substrate and principled factorization can explain these different capabilities without treating them as an arbitrary peer list.

## Findings

### 1. MMT — closest single umbrella for heterogeneous formal knowledge

**Primary source:** Florian Rabe, [MMT: A Foundation-Independent Approach to Formal Knowledge](https://uniformal.github.io/doc/philosophy/articles/mmt.pdf) (2016); [MMT overview](https://uniformal.github.io/doc/).

MMT is explicitly a framework for representing formal languages such as logics, type theories, set theories, and ontologies without committing to one representational paradigm, syntax, or semantics. It assembles language features as reusable modules and supports generic knowledge-management and logical algorithms. Modules can be declarative or provide programmatic rules.

**Why it is close:** It treats languages and their features as formal objects, supports modular composition, and makes formal knowledge computationally manageable. This is a stronger match to the user's broad representation/meta-framework intuition than a simple taxonomy or ontology spectrum.

**What it does not establish:** The sources reviewed do not establish MMT as a universal MECE factorization of every representational form, including empirical grounding of physical models and arbitrary simulation systems. It is a serious candidate to study, not a verified complete answer.

### 2. Institutions — clearest abstract factorization of logical systems

**Primary source:** Joseph Goguen and Rod Burstall, [Institutions: Abstract Model Theory for Specification and Programming](https://doi.org/10.1145/147508.147524), *Journal of the ACM* 39(1), 95–146 (1992). See also [Goguen's institution-theory page](https://cseweb.ucsd.edu/~goguen/projs/inst.html).

Institution theory abstracts a logical system into four coordinated pieces:

- a category of **signatures** (vocabularies);
- **sentences** associated with each signature;
- **models** associated with each signature;
- a **satisfaction relation** saying which models satisfy which sentences.

It also formalizes translations between signatures and requires satisfaction to remain invariant under translation. The paper treats specification and programming, database theory, and combinations of different logics; it discusses adding data and hierarchy constraints.

**Why it is close:** This is an unusually principled answer to “what are the basic components of a formal representational system?” It distinguishes language, statements, models, and interpretation, and it gives a formal criterion for structure-preserving translation.

**What it does not establish:** Institutions are a general framework for logical systems, not a complete ontology of every possible representation or a general account of empirical reference. Executable behavior may be formalized within suitable logics/specification systems, but is not automatically covered as a universal primitive.

### 3. Ologs — closest direct bridge between ontology, databases, and computation

**Primary source:** David I. Spivak and Robert E. Kent, [Ologs: A Categorical Framework for Knowledge Representation](https://doi.org/10.1371/journal.pone.0024274), *PLOS ONE* 7(1) (2012). [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3269434/).

Ologs use types as objects, functional relationships as arrows, and equations/commutative diagrams to express facts. They connect to database schemas and instance data, and the paper demonstrates that primitive recursive functions can be described by ologs. Functors connect and translate between ologs; the paper also connects its approach to information flow and institutions.

**Why it is close:** It is a concrete category-theoretic representation system that bridges conceptual models, databases, mappings, and a meaningful fragment of computation. It also makes the intended meaning of types and relations explicit.

**What it does not establish:** An olog is a particular knowledge-representation formalism, not a proven canonical factorization for all semantic representations. Its use of functional arrows is also a modeling commitment, not a universal account of all relations or dynamics.

### 4. Operational and denotational semantics — bridge between descriptions and execution

**Primary source:** Daniele Turi and Gordon Plotkin, [Towards a Mathematical Operational Semantics](https://doi.org/10.1109/LICS.1997.614955), LICS 1997. See also the [University of Edinburgh record](https://era.ed.ac.uk/items/acfe983e-b36e-4124-a14f-3f26d4a2cf8f).

This work develops a categorical account of operational rules for programming languages and relates them to a denotational model. It aims to unify descriptions of execution steps with mathematical meanings of programs under suitable conditions.

**Why it is close:** It directly addresses the user's intuition that a representation can describe rules that execute and also have a mathematical interpretation. It gives a formal way to study consistency between these views.

**What it does not establish:** Its target is programming-language semantics. It does not, by itself, unify scientific theories, ontologies, databases, proofs, and physical grounding into one general ontology framework.

### 5. The ontology/semantic spectrum — relevant, but a different kind of answer

**Primary source:** Deborah L. McGuinness, [Ontologies Come of Age](https://www.researchgate.net/publication/221024668_Ontologies_Come_of_Age) (2003); see also the [NCI Semantics Primer](https://www.cancer.gov/about-nci/organization/cbiit/news-events/blog/2022/semantics-primer).

The spectrum organizes knowledge-organization artifacts by semantic strength or expressiveness, from simpler structures toward formal ontologies. It helps explain why vocabularies, taxonomies, and logical ontologies are not equivalent.

**Why it is close:** It is the explicit precedent for the semantic-spectrum framing.

**What it does not establish:** A spectrum is primarily an ordering by expressiveness. It does not provide the requested general factorization into independent dimensions covering model interpretation, grounding, mappings, and executable behavior.

## Working conclusion

No source found in this first-pass search establishes the full requested universal, MECE factorization. However, there is substantial prior art, so it would be premature to treat the problem as unexplored.

**Recommended reading order:**

1. **Institutions** for the cleanest abstract decomposition: signatures, sentences, models, satisfaction, and translation.
2. **MMT** for a modular, foundation-independent framework that represents and computes over formal languages and knowledge.
3. **Ologs** for a concrete ontology/database bridge with categorical mappings and a computation example.
4. **Turi–Plotkin operational semantics** for the relation between executable rules and denotational models.

A productive next step is not to invent dimensions yet. First test whether an institution-like core (language, statements, models, satisfaction, translation) can be extended or composed with MMT-style modules and operational semantics to account for the user's examples. Treat empirical grounding as a separate correspondence problem unless a candidate framework supplies a more precise unification.

## Scope and confidence

- This is a targeted first-pass search, not an exhaustive survey.
- The claim is **not** that no universal factorization exists; it is that these inspected sources do not establish one covering the entire target described above.
- The distinction between a framework's expressiveness and a proof that its dimensions are independent or MECE remains open.
