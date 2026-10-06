# Revision-aware dependency prior-art audit

## Question

After the NYC sealed-update test, one capability appeared to earn further attention:

> given a changed artifact/evidence item, identify exactly which claims, warrants, criteria, analyses, or decisions depend on it; reopen those, preserve everything else, and retain historical versions.

This audit asks whether that capability is already mature prior art.

## Conclusion

Yes, almost all of it is.

The capability decomposes into several well-established problems with different mature owners:

1. **support/justification maintenance** — truth-maintenance systems (TMS/JTMS/ATMS);
2. **claim/evidence change impact** — assurance/safety-case maintenance and change-impact analysis;
3. **data/output dependency and provenance** — database provenance and lineage;
4. **incremental recomputation** — incremental view maintenance, self-adjusting computation, build systems, Salsa/Adapton/differential dataflow;
5. **normative belief-set revision under contradiction** — AGM and later belief-revision theory, only when that stronger problem is actually required.

No new general theory of epistemic revision is justified.

## 1. Truth-maintenance systems

Doyle's TMS work explicitly records reasons/justifications for beliefs and uses those support dependencies to update beliefs when assumptions are invalidated or new information arrives.

The central reusable idea is not a specific old implementation. It is:

```text
claim/node
  <- justification(s)
       <- supporting assumptions/nodes
```

When support changes, dependent standing changes.

de Kleer's ATMS generalizes this by maintaining the assumption environments in which a node holds and tracking inconsistent environments ("nogoods").

### Relevance

Very high for:
- claim standing;
- explicit support dependencies;
- retraction/invalidation;
- competing assumption contexts;
- explanation of why a claim still holds or no longer holds.

### Do not copy

Do not implement a general ATMS merely because the architecture resembles one. Our artifacts are heterogeneous, many dependencies are not logical implication, and native method owners must remain authoritative.

Use TMS/ATMS as **theory precedent for support-directed invalidation**, not as a universal runtime.

## 2. Assurance/safety-case change impact

This is the closest direct analogue to the NYC result.

Safety/assurance-case maintenance literature explicitly treats:
- claims;
- evidence;
- assumptions/context;
- dependencies among argument elements;
- system/environment changes;
- identification of directly and indirectly affected claims/evidence;
- selective re-evaluation rather than wholesale rebuilding.

Jaradat/Graydon/Bate and later model-based/continuous-assurance work frame the problem as identifying safety-case elements rendered suspect by a change in system design, operation, evidence, or environmental context.

SACM/GSN/Assurance-style argument structures already provide the claim/evidence/context topology on which such change-impact analysis operates.

### Relevance

Extremely high for:
- "this new evidence reopens these claims but not those";
- preserving historical argument versions;
- marking a claim/evidence relation as suspect/needs review;
- continuous or runtime evidence updates.

### Adoption implication

For epistemic/claim-level revision, **assurance-case change-impact analysis is the primary donor**, not a new O2A feedback model.

## 3. Database provenance and lineage

Database provenance asks which inputs contributed to an output.

Mature notions include:
- **where-provenance** — where output data came from;
- **why-provenance** — which source items influenced the existence of an output;
- semiring provenance — symbolic provenance expressions that compose through relational operations.

The provenance literature explicitly connects provenance to view maintenance/update, debugging and annotation propagation.

### Relevance

High for:
- source/output influence;
- reverse dependency lookup;
- "which derived rows/results depend on this changed input?";
- retaining provenance across transformations.

### Limitation

Database provenance does not decide whether an epistemic claim remains warranted. It tells us influence/dependency at the data/query level.

Therefore:

```text
provenance dependency != warrant dependency
```

but provenance can supply the lower-level edges consumed by claim-level impact analysis.

## 4. Incremental view maintenance and incremental computation

Incremental view maintenance (IVM), DBToaster, Differential Dataflow and related systems maintain derived results as inputs change rather than recomputing everything.

Self-adjusting computation records a dynamic dependence graph and re-executes only affected portions.

Build systems make the same idea operational:
- task dependency graph;
- changed input;
- transitive affected closure;
- partial rebuild;
- reuse unaffected outputs.

Salsa applies this to query-like computations: tracked functions record dependencies, revisions identify changed inputs, and cached results are reused unless a dependency changed.

Adapton similarly records demanded computation graphs and repairs only affected computations.

### Relevance

Extremely high for **mechanics**:

```text
change
  -> reverse dependency closure
  -> mark affected nodes dirty/stale
  -> recompute only affected computations
  -> reuse unaffected results
```

### Limitation

These systems generally assume deterministic/pure or otherwise well-defined computational dependencies.

A policy claim, expert judgment, or human decision is not simply a cached function result.

So use these systems for:
- stale detection;
- dependency indexing;
- incremental recomputation;
- caching/reuse;

not for epistemic semantics.

## 5. AGM / belief revision

AGM studies expansion, contraction and revision of logically closed belief sets while minimizing unnecessary change.

### Relevance

Useful only if we later need to answer:

> Given genuinely conflicting accepted propositions, which beliefs should an epistemic agent rationally give up?

That is stronger than the NYC problem.

NYC only required:
- add new evidence;
- identify affected claims;
- reopen them;
- preserve unaffected claims;
- leave unresolved claims unresolved.

No general belief-set revision operator was needed.

### Disposition

Do not adopt AGM machinery into the architecture unless a real case requires rational contraction/revision among conflicting accepted beliefs.

## Canonical decomposition for our program

The NYC behavior is best understood as four separate layers:

```text
A. provenance / dependency
   What depends on what?

B. invalidation / impact
   Which dependent artifacts or claims become suspect after this change?

C. native recomputation / re-warrant
   What operation must the owning method/framework perform again?

D. decision re-entry
   Does the changed evidence alter a criterion, trade-off, recommendation or decision?
```

Mature owners:

| Layer | Mature owner |
|---|---|
| A. artifact/data lineage | W3C PROV, database provenance, workflow provenance |
| B. claim/evidence impact | TMS/ATMS concepts; assurance/safety-case change-impact analysis |
| C. computational refresh | IVM, self-adjusting computation, build systems, Salsa/Adapton/Differential Dataflow; native method engine |
| D. policy/decision reconsideration | native decision-analysis/EtD/MCDA framework and accountable authority |

## NYC remap

The sealed air-quality update becomes a new versioned evidence artifact.

Dependency processing:

```text
new air-quality evaluation
  -> environmental-health evidence node
  -> environmental-health criterion
  -> equity criterion (air-quality subdimension)
  -> any downstream appraisal using those criteria
```

There is no dependency path to:
- the historical 13.4% agency prediction;
- frozen vehicle-entry arithmetic;
- the medical-access-cost source claim;
- the missing six-hearing qualitative result.

Therefore those nodes are reused unchanged.

This is exactly the same structural behavior as:
- partial rebuild in a build system;
- change propagation in self-adjusting computation;
- affected-view maintenance in a database;
- suspect-claim identification in assurance-case maintenance.

The **meaning of each dependency edge** remains domain/native-framework owned.

## What remains local

Only thin integration/profile work appears to remain:

1. stable IDs/references to native artifacts and claims;
2. a small vocabulary of dependency effects, e.g.:
   - input-to-computation;
   - evidence-supports-claim;
   - assumption/context-required-by-claim;
   - criterion-consumes-finding;
   - decision/advice-consumes-appraisal;
3. mapping each dependency type to a consequence on change:
   - recompute;
   - revalidate;
   - re-warrant/review;
   - reopen decision/appraisal;
   - no automatic action;
4. version/history references;
5. dispatch to the native owner.

Even this should preferentially be encoded as configuration/profile over mature representations, not a new ontology.

## Important semantic rule

Reverse reachability alone is insufficient.

An edge must carry or reference its **change-impact semantics**.

For example:
- a changed source byte invalidates an exact extraction;
- a new independent study does not invalidate a historical source claim;
- a changed causal assumption may reopen a causal conclusion;
- a changed value preference may alter a recommendation without changing empirical findings.

Thus:

```text
graph reachability != epistemic invalidation
```

The mature analogue is a build dependency with a rebuild rule, or an assurance trace with an impact rule.

## Adoption/deletion decision

### Adopt conceptually

- TMS/ATMS: justification/support dependency precedent;
- assurance-case change-impact analysis: claim/evidence invalidation and selective review;
- database provenance: influence/lineage;
- incremental computation/build-system theory: dirty propagation and minimal recomputation.

### Integrate when needed

- PROV/native workflow provenance for artifact history;
- existing query/build/incremental engine if scale makes it necessary;
- SACM/GSN/Assurance representation if claim-level change-impact becomes a recurring product feature.

### Do not build

- a universal truth-maintenance engine;
- a universal belief-revision engine;
- a new incremental computation runtime;
- a custom provenance algebra;
- a generic "feedback relation" ontology;
- a universal automatic policy-update engine.

## Revised hypothesis

The residual capability is no longer:

> build a revision-aware epistemic graph.

It is:

> **maintain enough typed cross-artifact dependency metadata to dispatch a change to the mature owner that knows how to recompute, revalidate, re-warrant, or reconsider the affected object.**

That is integration glue, not a new epistemic theory.

## Next falsifier

Before implementing even this thin layer, test whether an existing graph/query substrate already provides the needed reverse dependency/index mechanics in our repository cluster.

Candidate local owners to inspect:
- OntoCanon registry/provenance;
- Inquiry Graph relation/query machinery;
- DIGIMON lineage;
- Data Contracts / Investigation Spine;
- any existing dependency/impact graph in Project Meta.

If one already supports typed reverse reachability with versioned references, the residual implementation may collapse to a **profile plus a few impact-policy rules**.
