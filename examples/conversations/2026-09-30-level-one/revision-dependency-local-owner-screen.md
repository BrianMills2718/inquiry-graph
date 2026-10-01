# Revision dependency local-owner screen

## Question

After the prior-art audit reduced the residual capability to typed dependency metadata plus impact-policy dispatch, do any existing repositories already own the mechanics?

## Result

Yes, substantially.

The remaining capability should **not** become a new repository or general engine.

### DIGIMON — strongest operational owner

Current DIGIMON code already has:

- resolved lineage closure;
- exact dependency IDs;
- dependency hashes;
- reverse bindings;
- projection manifests;
- explicit `invalidation_dependencies`;
- examples of invalidating derived indexes when compiled projection identity changes;
- preserved loss/provenance/reverse-handoff semantics across representation chains.

The Foundation 1.3 consumer literally emits:

```text
"invalidation_dependencies": list(closure.dependency_ids)
```

This is the closest existing operational substrate for:

> changed native artifact/projection -> identify invalidated derived artifacts/indexes.

### OntoCanon — custody/history owner, not recomputation owner

OntoCanon already preserves:

- source/version identity;
- assertion retraction/supersession with history;
- exact evidence reopening;
- derivation lineage.

Its roadmap explicitly says that any future persistent-derived-knowledge consumer would require:
- rule/version identity;
- exact premise/support custody;
- derivation lineage;
- invalidation semantics.

That is a boundary statement, not an implemented general derived-knowledge invalidation engine.

Disposition:
- OntoCanon should remain source/assertion/governance custody;
- do not move downstream recomputation/change propagation into it.

### Inquiry Graph — research dependency representation, not product runtime

Inquiry Graph already has:
- reified `depends_on` relations;
- provenance on relations;
- relation-targeting/undercutting;
- dependency-cycle detection/warnings.

This is sufficient to **represent and study** dependency/impact hypotheses.

It should not become the operational policy-analysis invalidation runtime merely because it can encode the graph.

### Data Contracts — transport/lineage contract, not reverse-impact engine

Data Contracts already has lineage references, pack dependencies, versioned derivation/loss semantics and guarded transitions.

It is suitable for carrying dependency references across a boundary.

No evidence found that it should own cross-artifact reverse impact propagation.

### Project Meta — portfolio/planning dependencies at wrong granularity

Project Meta already has repository `depends_on` metadata and an active dependency-propagation/freshness program.

That machinery is about:
- repository/runtime/build dependencies;
- planning DAGs;
- freshness/staleness of checkouts and dependencies.

It proves the ecosystem already knows how to treat dependency propagation as a separate operational concern, but its nodes are projects/plans rather than evidence/claims/results.

Do not generalize Project Meta into an epistemic artifact graph.

### Mixed Methods Workbench — consumer/integration surface

Workbench already owns:
- investigation continuity;
- artifact references and derivation;
- review state;
- policy-appraisal integration;
- NYC case-specific integration.

It is the natural consumer/view for:
- "this input changed";
- "these artifacts/claims are now stale/need review";
- "these criteria should be reopened".

It should dispatch to method owners rather than compute method validity itself.

## Recommended ownership split

```text
OntoCanon
  source/assertion custody, immutable versions, review/retraction history
          |
          v
DIGIMON / native analytical owners
  derivation lineage, projection dependencies, invalidation dependencies,
  derived-artifact/index refresh
          |
          v
Assurance/TMS-style profile
  claim/evidence/assumption impact semantics
          |
          v
Workbench / decision surface
  reopen affected appraisal/criteria/advice; preserve authority boundary
```

Inquiry Graph records the research history of why those boundaries exist.

## Residual local work

If a future authentic consumer needs this operationally, the smallest addition is likely:

1. extend/reuse DIGIMON's existing dependency/invalidation references;
2. add a tiny profile mapping dependency kind to impact disposition:
   - stale/recompute;
   - revalidate;
   - needsSupport/re-warrant;
   - reopen appraisal;
   - informational only;
3. let Workbench query the reverse closure and dispatch each affected object to its native owner;
4. preserve version/history in OntoCanon/PROV-native records.

No new graph database, no new inference engine, and no universal feedback ontology are justified.

## NYC interpretation

For the sealed air-quality update:

- new evidence artifact is admitted/versioned;
- its explicit criterion/claim dependencies are added;
- reverse impact reaches environmental-health and an air-quality subpart of equity;
- no dependency path reaches the historical traffic arithmetic or medical-access source claim;
- Workbench reopens only the affected appraisal nodes;
- native method/assurance owners evaluate the new evidence.

This can be implemented as a narrow profile over capabilities already present in the cluster.

## Stop decision

**Foundational research on revision-aware dependency propagation is closed.**

Reopen only if a concrete end-to-end consumer demonstrates one of these failures:

1. DIGIMON cannot express the required artifact dependency/invalidation edge;
2. assurance/SACM/TMS prior art cannot express the relevant claim-impact semantics;
3. Workbench cannot consume the resulting affected-set without semantic flattening;
4. a second materially different case demonstrates a recurring gap not specific to NYC.

Until then, do not build a revision engine.
