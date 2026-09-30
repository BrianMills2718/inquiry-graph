# Representation interoperability adoption audit — 2026-09-30

> **Status:** supporting research note for the inquiry capture, not an architecture decision.
> **Question:** what mature infrastructure already exists for cataloging heterogeneous representation systems, storing profiles, selecting representations, translating/composing them, and recording semantic preservation/loss?
> **Rule:** prefer adoption/alignment over novelty. Do not promote a universal OntoCanon IR merely because it can encode many things.

## Executive result

Most of the desired architecture already exists **in layers**, but no single maintained system found spans all of them.

The strongest division of labor is:

1. **registry/catalog metadata** — ISO/IEC 11179 + ISO/IEC 19763 MFI;
2. **formal heterogeneous OMS networks/mappings** — OMG DOL + Hets; Ontohub as an older repository-engine precedent;
3. **model/metamodel transformations** — MOF/QVT, ATL, Epsilon, generic/global model management and megamodeling;
4. **database/schema mappings and migration** — categorical databases/CQL plus classical schema-mapping/data-exchange theory;
5. **formal theory graphs** — MMT/theory morphisms where logic/theory semantics apply;
6. **human-facing view selection** — Representation Router / Sirius-style viewpoint separation;
7. **governed local artifact/profile custody** — OntoCanon's existing pack/profile ownership model.

The likely thing **not** to build is a universal semantic translator.

Keep native representations and first-class mappings/adapters. Use an intermediate representation only as a declared projection/interchange surface with explicit loss and guarantee-preservation semantics.

## 1. The closest standards match: ISO metadata/model registries

### ISO/IEC 11179-3:2023 — Metadata registry common facilities

Current ISO registry metamodel. It defines:

- a generic registry item;
- identification, designation/definition, registration and classification;
- **mapping among registry items**.

Source:
https://www.iso.org/standard/78915.html

This is a direct candidate baseline for OntoCanon's library metadata/governance rather than inventing a fresh registry ontology.

### ISO/IEC 11179-35:2023 — Metamodel for model registration

This is unusually close to the present question. It extends the 11179 registry so it can register:

- models;
- associated metamodels;
- concepts associated with model elements;
- mappings between models;
- mappings between metamodels;
- mappings between models and their metamodels.

Source:
https://www.iso.org/standard/81727.html

### ISO/IEC 19763 — Metamodel Framework for Interoperability (MFI)

The current family remains highly relevant:

- Part 1: framework / architecture for registering many kinds of model;
- Part 3: ontology registration;
- Part 5: process-model registration;
- Part 7: service-model registration;
- Part 9: on-demand model selection;
- Part 10: core model and basic mapping;
- Part 12: information-model registration;
- Part 13: form-design registration;
- Part 16: document-model/schema registration;
- Part 6 is being revised as a **registry summary** for discovery/interoperation among registries.

Sources:
- https://www.iso.org/standard/84749.html
- https://www.iso.org/standard/84750.html
- https://www.iso.org/standard/76581.html
- https://www.iso.org/standard/53761.html
- https://www.iso.org/standard/56080.html
- https://www.iso.org/standard/61559.html
- https://www.iso.org/standard/85323.html
- https://www.iso.org/standard/78912.html

Important limitation: these standards define registry/metamodel semantics; ISO/IEC 19763-1 explicitly does **not** prescribe one physical registry implementation.

## 2. Existing websites / registry software

### FAIRsharing

FAIRsharing is a live curated registry of:

- standards;
- terminology artifacts/ontologies;
- models and formats;
- databases/repositories;
- policies;

with inter-record relationships and APIs.

Sources:
- https://fairsharing.org/
- https://fairsharing.gitbook.io/fairsharing

Fit:
- strong precedent for **discover/select a standard/model/format**;
- useful external source to ingest/link rather than duplicate;
- not a formal mapping/guarantee-composition engine.

### Aristotle Metadata Registry

Aristotle is a current product/API ecosystem implementing ISO/IEC 11179-style metadata registries.

Sources:
- https://docs.aristotlemetadata.com/
- https://aristotlemetadata.com/products/aristotle-metadata-registry/

Fit:
- implementation precedent for governed/federated metadata registries;
- evaluate rather than assume as a dependency;
- not a universal representation-transformation engine.

### Ontohub

Ontohub was explicitly designed as a web repository engine for heterogeneous ontologies, models and specifications, integrated with DOL/Hets and supporting mappings between formal theories.

Sources:
- https://github.com/ontohub/ontohub
- https://wiki.dol-omg.org/index.php/DOL

Fit:
- extremely close architectural precedent for **repository + heterogeneous formal representations + mappings**;
- current GitHub organization shows most core Ontohub application components last updated around 2021, so treat the software as an older architecture/donor unless a current deployment is independently verified;
- DOL/Hets remain the more important semantic precedent.

## 3. Formal heterogeneous representations: DOL + Hets

OMG DOL's explicit design goal is to accept multiple ontology/model/specification languages rather than create one language that subsumes them. It represents:

- heterogeneous OMS;
- modular OMS;
- alignments;
- interpretations;
- refinements;
- translations;
- networks of OMS and mappings.

OMG explicitly describes DOL as a formal language for expressing OMS and mappings across different formalisms.

Sources:
- https://www.omg.org/dol/
- https://www.omg.org/spec/DOL/1.0/

Hets operationalizes this with a graph of logics and logic translations; translations are first-class and heterogeneous proof obligations can be decomposed into local ones.

Source:
https://github.com/spechub/Hets

**Implication:** for formal logical/modeling semantics, OntoCanon should not reproduce DOL/Hets. Store/reference the native theory/model plus DOL/Hets-style mapping artifacts/certificates.

## 4. Model-driven engineering / megamodeling

### Generic model management

Bernstein-style generic model management treats **models and mappings as bulk objects** and proposes reusable operators such as:

- Match;
- Merge;
- Diff;
- Compose;
- Extract;
- ModelGen.

Source:
https://dbs.uni-leipzig.de/research/colloquia/2003-09/generic-model-management

This is almost exactly the conceptual API layer implied by "choose, transfer, compose and mix/match representations."

### Megamodeling / AM3

Megamodeling explicitly models collections of:

- models;
- metamodels;
- transformations;
- semantic correspondences;
- tools/technologies;
- relationships among them.

AM3 called this "modeling in the large" / global model management.

Source:
https://wiki.eclipse.org/AM3/

Important status: Eclipse explicitly says AM3 is **not maintained**. Adopt the conceptual pattern, not the implementation.

### MOF / QVT / ATL / Epsilon

OMG QVT standardizes model transformation over MOF-style models.

Source:
https://www.omg.org/spec/QVT/

Eclipse ATL is a mature model-to-model transformation toolkit.

Source:
https://eclipse.dev/atl/

Eclipse Epsilon is broader: a family of model-management languages with a connectivity layer that can uniformly work across heterogeneous modeling technologies including EMF, UML/Cameo, Simulink and XML.

Source:
https://eclipse.dev/epsilon/

**Implication:** mapping execution should be delegated to transformation engines appropriate to the native representation; OntoCanon should register/coordinate the mappings and their evidence, not become the transformation language.

## 5. Database/schema theory

The Knowledge Work repo had already reached the correct caution: "everything can be encoded as a hypergraph" does not make a hypergraph the best operational representation for everything.

The mature database analogue is schema mapping/data exchange.

### Categorical Query Language (CQL)

CQL is an active implementation of functorial data migration. A schema mapping induces principled migration/query operations, and the tool covers data migration, data exchange and ETL with integrity constraints and provenance.

Sources:
- https://categoricaldata.net/
- https://categoricaldata.net/CQL/

**Implication:** for database-shaped representations, CQL/schema-mapping theory is a serious reuse candidate. Do not round-trip relational/document/graph schemas through a generic IR just to prove universality.

## 6. Views are a separate layer

Representation Router already has the right boundary:

> authoritative semantic truth -> task-specific semantic projection -> representation/view -> working surface.

Eclipse Sirius independently reinforces this: semantic models remain separate from representation files, and multiple task/viewpoint-specific diagrams, tables, matrices and trees can project the same model.

Source:
https://eclipse.dev/sirius/doc/specifier/general/Specifying_Viewpoints.html

**Implication:** Representation Router should remain about **human-facing representations/views**, not become the registry of semantic formalisms or the semantic transformation engine.

## 7. What this suggests for OntoCanon

OntoCanon already has an unusually compatible design:

- domain repos own current authored packs/profiles;
- OntoCanon may retain immutable imported versions;
- imports retain source revision/hash/dependency closure/validation;
- the library is not the external domain's editable authority;
- Foundation IR/projections already have explicit loss handling.

The strong adoption hypothesis is:

### OntoCanon library ~= governed local metadata/model registry

Align its catalog metadata first against:

- ISO/IEC 11179-3 registry/common facilities;
- ISO/IEC 11179-35 model/metamodel registration;
- relevant ISO/IEC 19763 MFI extensions.

Do **not** copy the standards blindly. Crosswalk the current pack/profile contract and retain only fields needed by real cases.

### Native representation remains authoritative

A profile/library entry should be able to point to:

- native language/formalism;
- exact artifact/version/hash;
- metamodel/schema;
- available validators/tools;
- declared mappings/adapters;
- provenance/authority;
- capabilities/queries;
- preservation/loss guarantees.

### Mapping is first-class

A mapping/adapter should record at least:

- source representation/profile;
- target representation/profile;
- mapping formalism;
- direction;
- executable tool, if any;
- assumptions;
- preserved properties/guarantees;
- known losses;
- verification/certificate/evidence;
- status/version.

A mapping graph is useful, but **graph reachability is not guarantee transport**. Composition requires the concrete mapping semantics to compose.

### Intermediate representation is optional, not universal

OntoCanon's IR should be used when it actually serves:

- governance;
- identity;
- evidence custody;
- shared querying;
- a declared consumer interchange contract.

Do not force all native semantics through it.

If a native representation cannot be faithfully encoded:

1. retain the native artifact/payload;
2. expose a declared projection;
3. record a loss receipt;
4. re-warrant target-side claims that are not covered by a preservation theorem.

This is already consistent with OntoCanon's Scientific Hypergraph lossless-payload / lossy-projection decisions.

## 8. A plausible division of labor

| Concern | Likely owner / donor |
|---|---|
| catalog models, metamodels, profiles, versions, mappings | ISO 11179 / ISO 19763 semantics; OntoCanon local governed registry |
| find public standards/models/formats | FAIRsharing and domain registries |
| formal heterogeneous logics/models/mappings | DOL + Hets; MMT where theory graphs fit |
| MOF-style model transformation | QVT / ATL / Epsilon |
| database/schema mapping and migration | schema-mapping/data-exchange theory; CQL |
| human-facing representation choice | Representation Router |
| architecture-framework-specific semantics/views | DoDAF/UAF/SysML/etc. native profiles |
| source/evidence/identity/governance | OntoCanon |
| transformation guarantee transport | native mapping theorem/certificate; target re-warrant otherwise |

## 9. What probably should be deleted / not built

Do not build, absent a concrete failure:

- a universal representation language;
- a universal translator implemented by OntoCanon;
- a new universal mapping algebra;
- a new model registry ontology from scratch;
- another generic model-transformation language;
- another schema migration engine;
- a semantic/view conflation between Representation Router and OntoCanon.

Potentially build only thin glue:

- registry crosswalk/profile over ISO 11179/MFI concepts;
- first-class mapping/adapter records;
- connectors to external registries;
- preservation/loss receipts;
- query/routing over the registry;
- dispatch to native transformation/proof engines.

## 10. Best next validation

Before implementing registry machinery:

1. crosswalk OntoCanon's current pack/profile import metadata against ISO/IEC 11179-3 + 11179-35 + relevant MFI fields;
2. register a deliberately heterogeneous mini-set, e.g.:
   - Scientific Hypergraph profile;
   - Inquiry profile;
   - DoDAF semantic IR/profile;
   - a relational schema;
   - a DOL/Hets theory;
   - a Representation Router view profile;
3. register real mappings among only the pairs that have justified semantics;
4. ask:
   - can we discover the right representation for a task?
   - can we see exactly which translations are possible?
   - can we see what each translation preserves/loses?
   - can we compose paths without falsely transporting guarantees?
5. add local concepts only where the standards/tooling cannot express a demonstrated requirement.

This would test the architecture without committing OntoCanon to a universal IR.
