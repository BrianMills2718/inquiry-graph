# Mini-megamodel query results

**Status:** hand-checked expected results from `mini-megamodel.json`; the repository test below encodes these expectations. Current hosted CI is not a trustworthy execution signal because its install step is failing before tests.

## Inventory

- representations: **8**
- mappings: **5**
- implemented/bounded/demo mappings: **3**
  - `sh-v2-to-ontocanon-governed-payload`
  - `sh-v2-to-foundation-ir`
  - `knowledgework-logical-to-postgresql`
- declared but not executable/direct mappings: **2**
  - `inquiry-v1-to-ontocanon-pack-profile`
  - `dodaf-ir-to-fit-for-purpose-projections`
- mappings with declared loss/limitation: **4**
- mappings currently eligible for automatic composed guarantee transport: **0**

## Queries

### Scientific Hypergraph v2 → OntoCanon governed carrier

**Implemented path exists.**

`scientific-hypergraph-v2` → `sh-v2-to-ontocanon-governed-payload` → `ontocanon-governed-carrier`

Interpretation: governed custody/attachment of the native payload, **not semantic normalization** into a universal carrier.

### Scientific Hypergraph v2 → Foundation IR

**Implemented path exists, but declared lossy.** Automatic guarantee transport: **no**.

### Inquiry Graph V1 → OntoCanon governed carrier

Implemented-only query: **no path**.

When declared/design mappings are allowed, `inquiry-v1-to-ontocanon-pack-profile` is visible, but remains `design-mapped-not-executable`.

### DoDAF Semantic IR → Representation Router ViewSpec

Implemented-only query: **no path**.

With all declared seams, the architecture relation is visible, but its status is `architecturally-compatible-not-direct-adapter`.

### Scientific Hypergraph v2 → Representation Router ViewSpec

**No path even when declared seams are included.** The registry knows both representations but does not invent a bridge.

### Knowledge Work logical model → PostgreSQL schema

**Implemented demo path exists.** No universal guarantee-transport theorem is claimed.

## What the experiment establishes

The useful primitive is not a universal IR. It is a registry containing native representation/profile identities, exact version/authority/provenance, first-class mappings with maturity status, explicit preservation/loss claims, and conservative composition policy.

A disconnected mapping graph is valid and desirable.

## Next falsifier

Add one **real multi-hop mapping chain** whose component mappings have formal preservation semantics, then test exactly which guarantee survives composition. DOL/Hets or a small CQL schema-migration chain is the strongest candidate.
