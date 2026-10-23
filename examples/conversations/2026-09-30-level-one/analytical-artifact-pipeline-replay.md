# Analytical artifact pipeline replay — Email-Eu-core

> **Purpose:** empirically test whether a heterogeneous analytical chain requires a new generalized metamodel, or whether native analytical tools plus standard provenance are sufficient.

## Source

Existing real-data artifact from `BrianMills2718/observation-to-action-metamodel`:

- case: `cases/email-eu-core-bridge/results.json`
- upstream raw source: Stanford SNAP Email-Eu-core
- existing graph analysis: directed edge list → undirected graph → betweenness/cross-department/removal metrics
- committed source artifact already records projection losses and exact NetworkX method/version.

The raw gzip files were not retrievable into the current execution sandbox, so this replay starts from the repository's committed reproducible `results.json` rather than pretending to recompute the graph.

## Replayed chain

```text
Email-Eu-core graph-analysis result
  → top-20 candidate metric table
  → standardized feature matrix
  → PCA(2) embedding
  → KMeans(k=3) cluster assignment
  → cluster summary table
```

Native tooling:

- pandas / NumPy for tabular/vector representation;
- scikit-learn `StandardScaler`;
- scikit-learn `PCA(n_components=2)`;
- scikit-learn `KMeans(n_clusters=3, random_state=42, n_init=20)`.

Features:

- betweenness;
- degree;
- cross-department neighbor count;
- cross-department neighbor share;
- cross-department reachable-pair loss after node removal.

## Result

PCA component variance ratios:

- PC1: **0.62659685**
- PC2: **0.19389603**
- two-component total: **0.82049288**

Cluster summaries:

| Cluster | n | mean betweenness | mean degree | mean cross-dept share | mean removal-pair loss | departments |
|---|---:|---:|---:|---:|---:|---|
| 0 | 8 | 0.016315 | 123.75 | 0.817882 | 2791.125 | 4, 7, 22, 25, 28, 32, 37 |
| 1 | 11 | 0.024433 | 195.64 | 0.942958 | 1747.455 | 25, 26, 34, 35, 36 |
| 2 | 1 | 0.087415 | 346.00 | 0.965318 | 964.000 | 36 |

Node 160 forms its own cluster under this parameterization because its betweenness/degree profile is an extreme outlier among the top-20 candidates. This is an empirical result of this particular feature choice, scaling, PCA and `k=3`; it is not a semantic class asserted by the source data.

## Provenance sufficiency test

The chain did not require a new universal artifact type system.

At each step we only needed:

1. input artifact identity;
2. native representation/profile (`table`, numeric matrix, PCA embedding, cluster labels, summary table);
3. native operator/tool/version/parameters;
4. generated output artifact identity;
5. derivation links;
6. optional assumptions/loss notes.

Those are directly expressible with standard PROV-style Entity/Activity/used/wasGeneratedBy/wasDerivedFrom records plus native method metadata.

## Important negative result: sentiment stage

The requested motivating pattern included sentiment analysis after clustering. That stage is **not executable on this case** because the SNAP Email-Eu-core artifact contains graph edges and department labels but no message text/content.

This does not expose a missing metamodel concept. Existing provenance/loss information already explains the refusal:

- source artifact lacks message content;
- graph projection cannot manufacture it;
- therefore a text-sentiment operator has no valid input artifact.

The correct workflow result is **no executable sentiment edge**, not a synthetic placeholder.

## Conclusion

**The concrete replay falsifies the need for a new generalized analytical-artifact metamodel for this case.**

The useful common layer is adequately thin:

```text
native artifact
  -- native operator/run + provenance -->
native artifact
```

with optional profile/loss/warrant references.

Before building any new cross-tool artifact schema, require a real case where standard provenance + native representations cannot answer an actually needed query.

## Remaining candidate gap

The only plausible residual is a convenient cross-tool **catalog/query view** over heterogeneous native artifacts and method-specific assumption/loss claims. This is an integration/indexing problem, not a new representation theory.
