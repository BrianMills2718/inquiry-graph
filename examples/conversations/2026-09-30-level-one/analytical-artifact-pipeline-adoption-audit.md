# Analytical artifact pipeline adoption audit — 2026-09-30

> **Concrete falsifier:** Twitter table → social graph → embedding/vector space → clusters → cluster-level sentiment → downstream model/output.
> **Rule:** build nothing unless this case cannot be expressed with mature workflow/provenance/lineage/catalog tooling plus native analytic libraries.

## Requirement → mature owner → disposition

| Requirement | Mature owner / precedent | Disposition |
|---|---|---|
| Record artifact derivation across heterogeneous steps | W3C PROV (`Entity`, `Activity`, `used`, `wasGeneratedBy`, `wasDerivedFrom`) | **ADOPT** |
| Record executable scientific/data-analysis provenance graph | AiiDA data/process provenance | **ADOPT pattern/tool where suitable** |
| Define explicit pipeline nodes + datasets + catalog entries | Kedro pipelines + Data Catalog | **ADOPT where orchestration is needed** |
| Cross-tool run/job/dataset lineage | OpenLineage | **ADOPT for operational lineage** |
| Dataset/model/run experiment tracking | MLflow | **ADOPT for ML-specific artifacts** |
| Native table semantics | pandas/Polars/SQL/etc. | **NATIVE OWNER** |
| Native graph semantics | NetworkX/igraph/graph-tool/Neo4j/etc. | **NATIVE OWNER** |
| Embeddings/vector arrays | NumPy/PyTorch/vector stores/model library | **NATIVE OWNER** |
| Clustering semantics | scikit-learn/HDBSCAN/etc. | **NATIVE OWNER** |
| Sentiment/classification semantics | model/library used | **NATIVE OWNER** |
| Artifact schemas/profiles | native schema/model metadata + registry/catalog | **REGISTER, DON'T NORMALIZE** |
| Run parameters/code/tool versions | AiiDA/Kedro/OpenLineage/MLflow/native workflow | **ADOPT** |
| Human responsibility/provenance | PROV/OpenLineage/owning workflow | **ADOPT** |
| One universal analytical IR | none needed | **DO NOT BUILD** |
| New workflow engine | Airflow/Kedro/Prefect/Dagster/AiiDA/etc. | **DO NOT BUILD** |
| New lineage system | PROV/OpenLineage/AiiDA/etc. | **DO NOT BUILD** |

## The example is already representable

```text
TwitterTable
  -- build_interaction_graph --> InteractionGraph
  -- embed_nodes -------------> EmbeddingMatrix
  -- cluster -----------------> ClusterAssignment
  -- group_text_by_cluster ---> ClusterCorpus
  -- sentiment ---------------> ClusterSentiment
  -- fit_or_evaluate ---------> DownstreamModelOrResult
```

At the generic provenance layer:

- each artifact is an entity/data node;
- each operation is an activity/process/job;
- edges record input usage and output generation;
- execution/run records carry parameters, versions, status and timing;
- domain-native metadata says whether an artifact is a table, graph, embedding, clustering, model, score set, etc.

PROV already allows application-specific specialization of entities and activities; AiiDA explicitly separates data nodes and process nodes; OpenLineage standardizes datasets/jobs/runs; Kedro provides named datasets and function nodes; MLflow tracks datasets/runs/models.

## What this does *not* give automatically

The mature generic provenance stack does not itself know:

1. why a table→graph projection was chosen;
2. what distinctions the graph construction discarded or introduced;
3. whether an embedding preserves a property relevant to the question;
4. whether cluster membership is stable/uncertain;
5. what inferential claim a sentiment result licenses downstream.

But these are **method/domain semantics**, not evidence of a missing universal pipeline metamodel.

They should come from:

- the native method/library;
- a method-specific profile or certificate;
- existing scientific/statistical methodology;
- the epistemic warrant layer already developed elsewhere;
- a thin loss/assumption annotation only when needed by a real case.

## Residual common envelope, if needed

If OntoCanon/DIGIMON need a cross-tool index, keep it extremely thin:

```text
artifact_id
artifact_kind/profile_ref
native_schema_or_model_ref
produced_by_run
consumed_by_run[]
tool/operator_ref
parameters_ref
source_artifact_refs[]
provenance_ref
assumption_or_loss_claim_refs[]
result/warrant refs[]
```

This is a registry/index over native artifacts and provenance, not a universal representation.

## Architecture consequence

### Workflow/provenance layer owns
- what ran;
- what inputs were used;
- what outputs were produced;
- when/where/by what tool/version;
- execution/run lineage.

### Native analytical system owns
- semantics of graph construction;
- embedding geometry;
- clustering objective and labels;
- sentiment model semantics;
- statistical/model assumptions.

### OntoCanon can own
- governed identity/custody for registered artifacts/profiles/mappings;
- references to provenance and evidence;
- reviewed semantic claims.

### DIGIMON can own
- downstream representation selection;
- typed analytical operators if still useful as a local catalog;
- evidence recovery and derivation navigation.

### O→A should not own
- a new workflow engine;
- a new universal analytical artifact graph;
- duplicate provenance semantics.

## Verdict

**The generalized megamodel idea mostly collapses into existing workflow/provenance/lineage infrastructure plus native artifact typing.**

What remains potentially useful is not a new metamodel but a **catalog/view over the provenance graph that indexes heterogeneous artifact profiles and method-specific loss/assumption claims**.

That should only be built if a real end-to-end policy-analysis case needs cross-tool queries that existing AiiDA/OpenLineage/Kedro/MLflow catalogs cannot answer directly.

## Stop condition

Do not create a new repository or generalized analytical-artifact schema now.

Next evidence should come from implementing or replaying this concrete pipeline with off-the-shelf lineage/provenance capture and asking:

- Can we reconstruct every artifact and run?
- Can we identify its native representation/profile?
- Can we trace the exact operator and parameters?
- Can we attach method-specific assumptions/losses without inventing a new ontology?

If yes, close this as an integration problem.
