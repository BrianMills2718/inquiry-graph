# Representation Management Prior Art: Megamodels, Model Management, and Translation

**Date:** 2026-09-30  
**Status:** research synthesis; no new executable ontology primitives  
**Purpose:** decompose the project's broad "representation change" question into established prior-art problem classes before adding new formal machinery.

## 1. Main conclusion

The project should **not** treat "representation change" as one undifferentiated
new problem.

A substantial portion is already covered by several established bodies of work
that solve different layers:

```text
inventory / relations among representations
  -> megamodeling / global model management

generic operations over models and mappings
  -> generic model management

truth-preserving translation across logics
  -> institution theory / heterogeneous specification

formal theory/module translation
  -> MMT / theory morphisms

data migration and query behavior across schemas
  -> schema mappings / data exchange

synchronized views and update propagation
  -> bidirectional transformations / lenses

sound abstraction / refinement
  -> abstract interpretation
```

The Inquiry project should compose these ideas where they fit instead of
inventing one universal local transformation calculus.

The likely Inquiry-specific requirement is narrower:

> represent which representation/mapping/transformation is being proposed or
> used, what query or purpose it serves, what it preserves or loses, and what
> warrants using it in the present inquiry.

That is an inquiry-governance layer over established representation-management
machinery, not a replacement for that machinery.

## 2. Megamodeling / Global Model Management

### Core idea

Megamodeling emerged in Model-Driven Engineering to support **modeling in the
large**: representing the collection of models, metamodels, transformations,
languages, systems, and relations among them as an explicit model.

Favre and Nguyen's 2004/2005 megamodel work models large-scale software
evolution as a graph of systems connected by relations including:

- `RepresentationOf`;
- `ConformsTo`;
- `IsTransformedIn`.

The later AM3 work describes Global Model Management as practical support for
managing global resources in a model-engineering environment.

A megamodel is therefore not merely "a very large model" and not simply another
word for metamodel.

### Metamodel versus megamodel

A **metamodel** normally describes the language/structure to which a class of
models conforms.

A **megamodel** represents modeling artifacts and their relationships at the
global level.

For example:

```text
ScientificPack
  conformsTo -> OntoCanonPackContract

ScientificModel_v2
  conformsTo -> ScientificPack@2

ScientificModel_v2
  representationOf -> physical/process target

Migration_1
  transforms -> ScientificModel_v1 -> ScientificModel_v2
```

This distinction is directly relevant to the current project.

### What to reuse

The useful architectural lesson is to make global relations among
representations first-class and queryable rather than hiding them in file paths
or prose.

Candidate relation families include:

- representation-of;
- conforms-to;
- transformation/application;
- generated-from / projection-of;
- dependency/import;
- version/supersession;
- mapping/alignment;
- provenance.

Do **not** copy AM3's concrete metamodel or assume MDE artifacts are the only
representations we need.

## 3. Generic Model Management

Bernstein, Melnik, Halevy, Rahm and collaborators treat **models and mappings as
bulk objects** and define generic operations over them.

Established operators include variants of:

- Match;
- Merge;
- Diff;
- Compose;
- Apply;
- ModelGen / generation;
- Extract.

Later semantic work defines model-management operators in terms of their effects
on model instances, rather than only their surface syntax.

### Relevance

This is close to several operations we were beginning to discuss informally:

```text
compare representations
compose mappings
merge compatible models
find differences
derive one representation from another
apply a mapping
```

Before adding local Inquiry operators for these actions, check whether the
desired semantics are already a specialization of generic model management.

### Limit

Generic model management is primarily a metadata/model-engineering discipline.
It does not by itself decide whether a representation is epistemically
appropriate for an inquiry query.

## 4. Institution theory and heterogeneous specification

Institution theory abstracts a logical system into:

[
(mathbf{Sign},operatorname{Sen},operatorname{Mod},models).
]

Its key satisfaction condition says, informally, that truth is invariant under
the coordinated translation of notation/sentences and reduct of models.

This gives precise prior art for:

- logic/signature translation;
- theory structuring;
- heterogeneous logical systems;
- preservation of satisfaction under change of notation.

Hets and DOL are important engineering/standardization descendants of this
line.

### Relevance

When the project's "representation change" is really:

```text
signature / logic / formal-language translation
```

institution theory is the right starting point.

Do not reduce all representation changes to institution morphisms: many of our
artifacts are not formal theories in a logic.

## 5. MMT / theory morphisms

MMT provides a foundation-independent theory graph in which theories and theory
morphisms are first-class.

This is useful where we need concrete formal artifacts and modular translations,
not only institution-level abstract semantics.

The project already uses the useful distinction:

```text
institution theory
  -> semantic abstraction over logics and satisfaction

MMT-like theory graph
  -> concrete formal artifacts, declarations, theories, morphisms
```

### Relevance

For formally specified models, definitions, and theories, use theory morphisms
and module machinery rather than inventing a generic Inquiry-specific formal
translation language.

## 6. Schema mappings and data exchange

Database theory gives a particularly concrete body of work on mappings between
representations.

A schema mapping specifies how data structured under a source schema relates to
or is transformed into data under a target schema.

Important established questions include:

- composition of mappings;
- existence and meaning of target solutions;
- universal/canonical solutions;
- query answering after translation;
- what information and queries are preserved;
- inversion/quasi-inversion.

Fagin, Kolaitis, Miller, Popa, Tan and collaborators provide rigorous semantics
for these questions.

### Relevance

This is highly relevant whenever we ask:

> If I translate representation A into representation B, can I still answer
> query q correctly?

That is much closer to database query-preservation/data-exchange theory than to
a new general philosophical notion of "representation preservation."

## 7. Bidirectional transformations and lenses

Bidirectional transformation research studies coupled representations where a
view is derived from a source and updates may need to propagate back.

Lenses provide well-behaved pairs of transformations such as:

```text
source -> view
updated view + retained source information -> updated source
```

The view-update literature also makes **alignment** important: after insertion,
deletion, or reordering, corresponding parts of source and view must still be
matched correctly.

### Relevance

Use this prior art when the question is not merely one-way translation but:

- keeping two views consistent;
- propagating edits;
- round-tripping;
- defining what information must be retained to reconstruct/update;
- specifying synchronization laws.

OntoCanon pack/profile projections and editable derived views may eventually
need this distinction.

## 8. Abstract interpretation

Abstract interpretation supplies formal machinery for sound abstraction between
concrete and abstract semantic domains.

Classical formulations use abstraction/concretization relationships such as
Galois connections.

### Relevance

This is a strong candidate when we mean:

```text
coarse-grain a representation
preserve sound conclusions
refine an abstraction
relate concrete and abstract properties
```

It gives much more precise vocabulary than saying only that one representation
is "more detailed."

Again, it is not a universal model-translation framework; its central concern is
sound approximation.

## 9. These traditions answer different questions

Do not collapse them.

| Question | Strong prior-art starting point |
|---|---|
| What representations/artifacts exist and how are they globally related? | Megamodeling / GMM |
| What generic operations manipulate models/mappings? | Generic model management |
| Does truth survive a translation of logical language? | Institutions |
| How are formal theories/modules translated and reused? | MMT/theory morphisms |
| How does data move between schemas and which queries survive? | Schema mappings/data exchange |
| How do two related views stay synchronized under updates? | Lenses / bidirectional transformations |
| Is an abstraction sound relative to a concrete semantics? | Abstract interpretation |

A single real workflow may use several rows.

## 10. Reframing the project's "representation problem"

The earlier broad question:

> when is a representation change inquiry-preserving, refining, reframing, or
> distorting?

should be decomposed.

### 10.1 Artifact-management question

What representations, schemas, languages, mappings and transformations exist?

Use megamodel/global-model-management ideas.

### 10.2 Formal-semantic question

What formal claims/truth conditions are preserved by translation?

Use institutions/MMT where applicable.

### 10.3 Instance/data question

What concrete information and query answers survive translation?

Use schema-mapping/data-exchange theory.

### 10.4 Abstraction question

What sound approximations are preserved under coarse-graining/refinement?

Use abstract interpretation.

### 10.5 Synchronization question

If either representation changes, how should the other change?

Use bidirectional-transformation/lens theory.

### 10.6 Inquiry question

Why are we using this representation/transformation for this query, and what
claim does that license?

This remains an Inquiry-layer concern:

[
mathsf W(R,T,q,E,Gamma).
]

The Inquiry layer should record and evaluate that warrant without attempting to
replace the domain-specific transformation theory.

## 11. Implication for the primitive-vs-derived audit

Do not add one primitive called `RepresentationChange` merely because many
domains transform representations.

Prefer:

```text
Representation / Model / Theory / Schema / View
  -> domain/formal artifact type

Mapping / Transformation
  -> explicit first-class relation/artifact

Transformation occurrence
  -> process/event applying a mapping

Preservation / soundness / consistency property
  -> typed property backed by the appropriate formal discipline

Inquiry warrant
  -> why that artifact/transformation is licensed for the current query
```

The OntoCanon carrier only needs to be permissive enough to represent these
objects and higher-order relations. Their substantive semantics live in ontology
packs and specialized formal systems.

## 12. Implication for OntoCanon

OntoCanon is well positioned to carry a **megamodel-like graph** because its
target generalized kernel already aims to support:

- typed semantic elements;
- first-class typed n-ary relations;
- relations as participants;
- provenance;
- identity;
- alignment;
- governance.

That does **not** imply `Megamodel` should become a kernel primitive.

A representation-management ontology pack/profile could declare types such as:

- Representation;
- Model;
- Schema;
- Language;
- Mapping;
- TransformationSpecification;
- TransformationOccurrence;
- View;
- Projection;

and relations such as:

- represents;
- conforms_to;
- maps_to;
- transforms;
- generated_from;
- projection_of;
- preserves_property;
- loses_property.

Only introduce such a pack after concrete consumers justify its vocabulary and
after checking exact prior-art semantics.

## 13. Implication for Inquiry Graph

Inquiry Graph should continue to distinguish:

- the **representation-management artifact** itself;
- a participant's **claim/hypothesis** about that artifact;
- the **inquiry move** that proposes/tests/reframes it;
- the **warrant** for using it.

For now, existing Hypothesis/Method/Question/Claim plus explicit relations can
describe the research discussion.

Do not add a megamodel-specific executable ontology merely because megamodeling
is useful prior art.

## 14. Implication for Company Planning

Company Planning's factorization analysis and megamodeling solve different
problems.

```text
factorization analysis
  -> is this decomposition adequate for the active decision?

megamodeling
  -> what representations/artifacts exist and how are they related?
```

A Company Planning review graph may benefit from a megamodel-like view of:

```text
roadmap
requirements
design
schema
work graph
implementation
evidence
dashboard projection
```

and relations such as `derived_from`, `conforms_to`, `projection_of`,
`evidence_for`, and `supersedes`.

But this should reuse Company Planning's existing authority/traceability model
rather than introduce a second planning ontology merely to use the word
"megamodel."

## 15. Research disposition

### Adopt as prior art

- megamodeling/global model management for representation inventory and global
  relation graphs;
- generic model management for reusable operators over models/mappings;
- institutions/MMT for formal-language/theory translation;
- schema mapping/data exchange for instance and query preservation;
- lenses for bidirectional update/synchronization;
- abstract interpretation for sound abstraction/refinement.

### Do not adopt yet

- a single universal local representation-transformation calculus;
- AM3 or another historical megamodel metamodel as the OntoCanon kernel;
- a new Inquiry primitive for every representation relation;
- the assumption that all Inquiry representations are MDE-style models.

### Next formal step

Use this decomposition during the planned primitive-vs-derived audit.

For each candidate primitive, ask not only "can this be derived?" but:

> Which established representation-management discipline already owns the
> semantics of this operation or relation?

Only retain a new foundational concept when no established layer supplies the
required semantics and the distinction is genuinely cross-domain.

## 16. Primary references

- Jean-Marie Favre and Tam Nguyen, **"Towards a Megamodel to Model Software
  Evolution Through Transformations"**, Electronic Notes in Theoretical
  Computer Science 127(3), 2005. DOI: 10.1016/j.entcs.2004.08.034.
- Freddy Allilaire, Jean Bézivin, Hugo Bruneliere, Frédéric Jouault,
  **"Global Model Management in Eclipse GMT/AM3"**, eTX/ECOOP 2006.
- Andrés Vignaga, Frédéric Jouault, María Cecilia Bastarrica, Hugo Brunelière,
  **"Typing Artifacts in Megamodeling"**, Software and Systems Modeling 12(1),
  2013. DOI: 10.1007/s10270-011-0191-2.
- Philip A. Bernstein, **"Applying Model Management to Classical Meta Data
  Problems"**, CIDR 2003.
- Sergey Melnik, Philip A. Bernstein, Alon Halevy, Erhard Rahm,
  **"A Semantics for Model Management Operators"**, MSR-TR-2004-59, 2004.
- Joseph Goguen and Rod Burstall, **"Institutions: Abstract Model Theory for
  Specification and Programming"**, JACM 39(1), 1992.
- Ronald Fagin, Phokion Kolaitis, Renée Miller, Lucian Popa,
  **"Data Exchange: Semantics and Query Answering"**, Theoretical Computer
  Science 336(1), 2005.
- Ronald Fagin, Phokion Kolaitis, Lucian Popa, Wang-Chiew Tan,
  **"Composing Schema Mappings: Second-Order Dependencies to the Rescue"**,
  ACM TODS 30(4), 2005.
- J. Nathan Foster, Michael Greenwald, Jonathan Moore, Benjamin Pierce,
  Alan Schmitt, **"Combinators for Bidirectional Tree Transformations"**,
  ACM TOPLAS 29(3), 2007.
- Patrick Cousot and Radhia Cousot, **"Abstract Interpretation Frameworks"**,
  Journal of Logic and Computation 2(4), 1992.
