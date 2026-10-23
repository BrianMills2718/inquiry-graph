# LinkML → PostgreSQL: Factgraph vs mature external tooling

> **Question:** Does Factgraph add useful evidence beyond LinkML/PostgreSQL/Data Contract tooling for one real transformation?
> **Case:** LinkML schema with `age` minimum/maximum → LinkML PostgreSQL DDL.

## External stack already covers

### LinkML

- source metamodel/schema;
- PostgreSQL DDL generation;
- generator compliance dashboard based on executable compliance tests;
- SQL validation-query generation for required fields, min/max values, regex patterns, enums and uniqueness.

Therefore LinkML itself can generate PostgreSQL queries that detect rows violating a source `minimum_value` / `maximum_value` constraint even when the DDL does not encode a `CHECK`.

### PostgreSQL

- native DDL constraint enforcement;
- catalog introspection;
- executable acceptance/rejection behavior for inserted test rows.

### Data Contract CLI

- import PostgreSQL or SQL DDL into a data contract;
- validate schema/type/required/unique/key properties;
- execute arbitrary SQL quality rules against PostgreSQL;
- CI-oriented pass/fail reporting;
- import/export across many contract/schema formats.

## What Factgraph adds

Factgraph's pinned LinkML experiment does something more specific:

1. pins the exact LinkML source and generator version;
2. imports the **source semantic obligation** independently of the generated DDL;
3. binds that source obligation to the exact generated physical artifact;
4. generates a source-invalid discriminating population;
5. generates source-valid boundary probes;
6. executes those populations against the generated PostgreSQL artifact;
7. classifies the transformation artifact as weakened / preserved-on-tested-cases / stronger-or-incompatible / unresolved;
8. retains source→mapping→target provenance.

That is not ordinary data validation. It is **transformation-specific semantic preservation testing**.

## Important correction to the Factgraph framing

A result such as:

> LinkML PostgreSQL DDL does not enforce `minimum_value`

does **not** imply:

> LinkML cannot preserve or enforce the semantic rule in a PostgreSQL workflow.

LinkML has a separate SQL-validation generator that can emit range-validation queries. The proper target boundary therefore matters.

Possible target contracts include:

- **DDL alone**;
- DDL + LinkML-generated validation SQL;
- DDL + application validation;
- a broader deployed data-contract pipeline.

Factgraph is only correct if the audit names which target contract it is testing.

## Head-to-head disposition

| Need | Best owner | Factgraph role |
|---|---|---|
| Author LinkML semantics | LinkML | none |
| Generate PostgreSQL DDL | LinkML | none |
| Validate LinkML min/max against PostgreSQL data | LinkML SQLValidation | none by default |
| Generic schema/data contract checks on PostgreSQL | Data Contract CLI / native SQL | none by default |
| Check whether PostgreSQL DDL contains/enforces a rule | PostgreSQL introspection + tests | thin wrapper at most |
| Compare source semantic obligation to generated target artifact behavior | property-preservation testing / formal transformation verification | Factgraph-style harness can be useful |
| Generate discriminating source-semantic counterexamples automatically | model-based/property-based testing / solver literature | Factgraph may provide local glue for supported semantics |
| Preserve exact source→generator→artifact→observation provenance | OntoCanon + test evidence tooling | Factgraph pattern is useful donor |

## Verdict

**Factgraph is not needed for this pipeline if the question is simply 'is the data valid according to LinkML?'** LinkML's own SQL validation already covers the example range constraint, and Data Contract CLI/native SQL cover broad target validation.

Factgraph is only potentially justified for the narrower question:

> **Did this specific transformation artifact preserve this source semantic obligation, and can we demonstrate the answer with a discriminating source-level witness?**

That is a legitimate layer, but it is an **audit/testing layer**, not a semantic or transformation foundation.

## Keep / replace for this case

### Replace / delegate

- LinkML schema semantics → LinkML
- SQL generation → LinkML
- range-validation SQL → LinkML SQLValidation
- generic PostgreSQL contract testing → Data Contract CLI / PostgreSQL
- mapping/property-preservation theory → established model-transformation/formal-method literature

### Keep only if materially useful

- source-semantic obligation identity;
- automatic source-invalid witness generation;
- paired source-valid acceptance probes;
- exact mapping/provenance binding;
- observed transformation-preservation verdict.

## Stronger next comparison

Factgraph should next be compared not against generic target validation, but against an established **model transformation verification / property-based model testing** tool that can take source invariants plus a transformation and generate/verify counterexamples.

If such a tool can replace Factgraph's witness/provenance workflow cleanly, Factgraph should be reduced further or archived.
