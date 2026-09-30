# Representation interoperability adoption matrix — 2026-09-30

> **Status:** adoption/deletion recommendation, not an implementation mandate.
> **Goal:** map each requirement to the mature field/standard/tool that already owns it, then minimize custom theory/code.

| Requirement | Established owner / precedent | Candidate standard/tool | Disposition |
|---|---|---|---|
| Register models, metamodels, versions, concepts and mappings | Metadata registry / model-registration standards | ISO/IEC 11179-3 + ISO/IEC 11179-35 | **ADOPT as semantic baseline** |
| Register heterogeneous model kinds under a common interoperability framework | Metamodel framework for interoperability | ISO/IEC 19763 MFI | **ADOPT/ALIGN** |
| Basic mapping metadata between registered models | Metadata registry / MFI mapping facilities | ISO/IEC 11179 mapping facilities; ISO/IEC 19763-10 | **ADOPT/ALIGN** |
| Heterogeneous formal logics/ontologies/specifications | Formal ontology/specification interoperability | OMG DOL + Hets | **INTEGRATE / DO NOT REBUILD** |
| Formal ontology metamodels and mappings | Ontology/metamodel standards | OMG ODM | **ADOPT WHERE APPLICABLE** |
| Generic model/metamodel transformations | Model-driven engineering / model management | QVT, ATL, Epsilon | **DISPATCH / DO NOT REBUILD** |
| Manage models + mappings + transformations as first-class artifacts | Generic/global model management; megamodeling | Bernstein-style model management, megamodeling/AM3 concepts | **ADOPT CONCEPTUAL MODEL; DON'T REVIVE OLD STACKS** |
| Relational/schema mapping, migration, data exchange | Database theory | CQL / functorial data migration; classical schema-mapping/data-exchange theory | **INTEGRATE / DO NOT REBUILD** |
| Sound abstraction/coarse-graining | Abstract interpretation | Galois connections / abstract domains | **USE NATIVE THEORY** |
| Bidirectional synchronization / round trips | Bidirectional transformations | lenses / bx | **USE NATIVE THEORY** |
| Human-facing view selection from semantic truth | Visualization/viewpoint selection | Representation Router; ISO 42010/Sirius-style viewpoint separation | **KEEP LOCAL THIN LAYER** |
| Govern artifact identity, provenance, review, immutable imports | Governance / metadata registry | OntoCanon existing pack/profile library + ISO registry crosswalk | **KEEP; ALIGN TO STANDARDS** |
| Store one universal semantic normal form | No mature field requires this; DOL explicitly avoids it | none | **DO NOT BUILD** |
| Universal transformation engine | Existing domains already have engines | Hets/QVT/ATL/Epsilon/CQL/etc. | **DO NOT BUILD** |
| Universal mapping algebra | Domain-specific semantics differ materially | none needed above dispatch layer | **DO NOT BUILD** |
| Generic `preserves=true` flag | Too weak; preservation is typed by formalism/property | native certificates + typed guarantee family | **DO NOT BUILD AS BOOLEAN** |
| Mapping discovery/routing | Registry/query layer over mapping metadata | thin OntoCanon query/dispatch surface | **BUILD ONLY THIN GLUE** |
| Mapping-path composition | Native mapping theory | formalism-specific composition rules | **DELEGATE; REGISTRY RECORDS RESULT** |
| Loss accounting | Projection/transformation theory + governance | explicit loss receipts / native proof obligations | **KEEP THIN COMMON ENVELOPE** |

## Main conclusion

The architecture is not a new theory problem.

A thin program-level layer is enough:

```text
native representation/profile
        |
registered identity + metamodel + authority
        |
first-class mapping artifact
        |
native formalism/tool owns transformation semantics
        |
typed preservation/loss certificate
        |
optional target-side re-warrant
```

OntoCanon should primarily own **registry/governance/custody**, not universal semantics or universal transformation.

## What to delete from the research agenda

Unless a concrete case proves otherwise, stop researching/building:

1. a universal IR;
2. a universal mapping algebra;
3. generic mapping-composition semantics;
4. a new model/metamodel registry ontology;
5. a custom schema/data-migration engine;
6. a custom heterogeneous-logic translation framework;
7. a generic preservation boolean or scalar.

## What remains legitimately project-specific

Only thin integration concerns appear project-specific:

1. crosswalk OntoCanon's existing artifact/profile records to ISO 11179/MFI;
2. define a first-class mapping-record envelope that can point to native DOL/Hets, CQL, QVT/ATL/Epsilon, lens, abstraction, or other artifacts;
3. type the **preservation claim family** without interpreting it generically;
4. expose queries such as:
   - what representations exist?
   - which mappings are implemented?
   - what formalism owns each mapping?
   - what is preserved/lost?
   - which path is certified for this requested property?
5. dispatch to the native engine;
6. retain evidence/certificates and require target-side warrant when no preservation theorem applies.

## Recommended implementation posture

**Do not build anything substantial yet.**

First produce a standards crosswalk and an interface contract. The implementation target should be small enough that deleting it later is cheap.

A plausible minimal mapping record is:

```text
mapping_id
source_artifact/version
target_artifact/version
mapping_formalism
mapping_artifact/version
direction
tool/engine
validation/certificate
preservation_claims[]   # typed, formalism-owned
loss_claims[]
composition_rule_ref
authority/provenance
status
```

The registry does not decide what `preservation_claims` mean. Their referenced formalism does.

## Adoption verdict by existing repo

### OntoCanon
Retain as governed local registry/library and evidence/identity authority. Align metadata to ISO 11179/MFI and add only thin first-class mapping records if a real consumer requires them.

### Representation Router
Keep focused on task/human-facing projection and representation choice. It consumes semantic/view availability; it does not own model translation.

### Scientific Hypergraph
Keep native scientific semantics. Its existing "lossless payload + declared lossy projection" is the right pattern.

### DoDAF
Keep native semantic authority + projection registry. It is a strong case of semantic model versus fit-for-purpose views, not a reason to universalize its IR.

### Knowledge Work
Treat as prior internal evidence for the already-known conclusion that universal graph encodability is not universal operational suitability. Prefer established schema/model transformation systems over extending HKSC as a universal compiler.

## Stop condition

If ISO 11179/MFI + DOL/Hets + MDE/model-management + database mapping + lenses/abstract interpretation cover the next concrete cases, **representation interoperability is closed as foundational research**.

Reopen only when a named use case cannot be faithfully expressed or dispatched through those mature owners.
