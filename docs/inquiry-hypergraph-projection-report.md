# Projection of Both Inquiry Trajectories into the Scientific Hypergraph Carrier

## Result

Both existing Inquiry Graph trajectories were projected into the `scientific-hypergraph-v2` carrier without structural loss.

Generated artifacts:

- `examples/seed/scientific-hypergraph-v2.json`
- `examples/formal-inquiry-2026-09-27/scientific-hypergraph-v2.json`

For both projections:

- every original Inquiry Graph record is represented;
- every source anchor is externalized as a first-class grounding relation;
- n-ary relation bindings map directly to carrier bindings;
- moves, stance events and question events map to relation instances;
- source conversations, participants, messages, content nodes and extraction records map to elements;
- an exact reconstruction check reproduced the original graph JSON semantics and array ordering;
- a structural check against the published `hypergraph-v2.schema.json` shape found no carrier-shape violations.

This is a **carrier projection proof**, not yet a full Scientific Hypergraph profile-conformance proof. The projected `ig:*` relation types and roles are not yet declared in a machine-readable Inquiry profile imported by the Scientific Hypergraph validator.

## Projection counts

| Trajectory | Source records | Carrier elements | Carrier relations | Carrier bindings | Exact reconstruction |
|---|---:|---:|---:|---:|---|
| founding seed | 1 conversation, 214 nodes, 233 relations, 177 moves, 52 stance events, 71 question events, 1 extraction | 426 | 1,697 | 4,116 | yes |
| formal-inquiry trajectory | 1 conversation, 19 nodes, 14 relations, 19 moves, 2 stance events, 4 question events, 1 extraction | 48 | 148 | 360 | yes |

The carrier representation is larger because source grounding and source structure that were nested fields in Inquiry Graph become explicit relation instances.

## Mapping used

### Elements

The following become `ModelElement`-compatible carrier elements:

- Graph
- Conversation
- Participant
- Message
- Inquiry Graph content `Node`
- Extraction record

Original source/domain metadata is retained under `ig:*` attributes.

### Relations

The following become carrier `RelationInstance` records:

- Inquiry Graph semantic relations
- moves
- stance events
- question events
- grounding anchors
- graph/conversation/participant/message structural links

### Bindings

Inquiry Graph:

```text
Relation(id, kind, [(role, ref), ...])
```

projects directly to:

```text
RelationInstance(id, relationType)
RoleBinding(relation=id, role=role, participant=ref)
```

No binary flattening is required.

## Loss

### Semantic/content loss: none observed

The two current trajectories can be reconstructed exactly from the carrier projections.

No Inquiry Graph source field had to be discarded or conflated.

### Carrier-level loss: none observed

No current Inquiry Graph object required a primitive absent from:

```text
ModelElement
RelationInstance
RoleBinding
```

plus attributes and typing/profile semantics.

This is evidence for the current stop rule: **do not create another general semantic carrier.**

## Ambiguities and representation friction

### 1. Inquiry semantics are preserved, but not yet declared as a formal profile

The projection uses relation types such as:

```text
ig:relation:supports
ig:move:challenge
ig:StanceEvent
ig:QuestionEvent
ig:GroundingAnchor
```

and roles such as:

```text
ig:premise
ig:conclusion
ig:actor
ig:target
ig:occurrence
```

The carrier can hold these, but a proper **Inquiry profile** still needs to declare:

- relation types;
- role types;
- role cardinalities;
- permitted participant types;
- symmetry/direction where applicable;
- acyclicity rules;
- status vocabularies and other domain constraints.

This is a profile/schema task, not a carrier extension.

### 2. Binding order is preserved through a qualifier convention

The Scientific Hypergraph v2 binding record has:

```text
relation
role
participant
qualifier?
```

but no dedicated ordinal field.

Inquiry Graph contains arrays where exact order can matter for faithful reconstruction, including move inputs/outputs/after lists and source array ordering.

The proof therefore preserves binding order using:

```text
qualifier = "ordinal:N"
```

This works losslessly, but it is a convention rather than a first-class carrier facility.

This is the strongest carrier-level friction found.

**Possible extension:** add an optional explicit binding ordinal / ordering coordinate, or formally standardize ordered-role semantics in the carrier/profile model. This should be considered alongside the Scientific Hypergraph repository's existing finding that binding order is not always derivable from role contracts.

### 3. Source-grounding semantics are currently profile-local

Inquiry Graph anchors contain:

```text
message_id
start
end
quote
```

The projection represents each as an `ig:GroundingAnchor` relation and retains exact offsets/quote as relation attributes.

Nothing is lost, but the general carrier does not itself define source-span semantics. That belongs in an Inquiry/evidence profile or a shared provenance profile.

No new carrier primitive appears necessary.

### 4. Inquiry state-transition semantics do not come from the carrier

The carrier preserves the records needed to compute:

- current question state;
- stance histories;
- open agenda;
- move chronology;
- supersession;
- review status.

But rules such as:

- `after` must be acyclic within a conversation;
- `supersedes` must be acyclic;
- latest non-rejected QuestionEvent determines recorded current state;
- only confirmed resolved/deferred/superseded removes a question from the open agenda;

remain Inquiry Graph semantics.

These should remain profile/domain validator rules rather than carrier primitives.

### 5. Extraction records have no native identity in Inquiry Graph

`Extraction` objects in the source graph do not have an `id`.

The projection therefore mints deterministic projection-local IDs of the form:

```text
proj:<graph-id>:extraction:<ordinal>
```

No information is lost, but identity is introduced by the projection rather than inherited from the source model.

If extraction records become independently referenced, Inquiry Graph should probably give them stable IDs.

### 6. Naive graph union would create two intentional ID collisions

Across the two trajectories, exactly two source IDs overlap:

- `participant:brian`
- `participant:assistant`

These likely denote the same participants, but the carrier itself should not decide that.

This is precisely the type of identity/reconciliation decision OntoCanon should govern.

The two graphs should therefore remain separate carrier documents until an explicit alignment decision licenses a shared projection.

## Capabilities not exercised by the two trajectories

### Relation-as-participant

Inquiry Graph's ontology permits relations and moves to be semantic targets, and the Scientific Hypergraph carrier supports relation instances as participants.

However, **neither current trajectory actually contains a semantic relation whose target is another relation or move**.

Observed semantic-relation targets in both graphs are currently content nodes only.

So this capability is structurally compatible but not empirically exercised by these two datasets.

A dedicated fixture is still warranted.

### RoleBinding-as-participant

Neither current trajectory contains a record that specifically targets one role assignment within a relation.

Therefore the projections do not exercise:

```text
RoleBinding as participant
```

even though the Scientific Hypergraph kernel supports it.

The previously proposed fixture remains the right next negative/positive control:

```text
R1 = supports(premise=P, conclusion=C)
B1 = addressable binding R1.premise=P
R2 = challenges(challenger=Q, target=B1)
```

This is not required to represent the two current trajectories, but it is important for the claimed general inquiry substrate.

## Required extensions

### Required now: Inquiry profile

Create a machine-readable Inquiry profile over the carrier that declares the current Inquiry Graph ontology.

This is necessary for full Scientific Hypergraph validator conformance rather than merely JSON-carrier conformance.

### Required before governed integration: OntoCanon carrier governance seam

Prove OntoCanon can govern:

- arbitrary typed relation instances, not only proposition-like assertions;
- relation-as-participant references;
- addressable RoleBindings;
- profile-defined alignment relations.

Do not add these abstractions speculatively. Use the projected inquiry graphs plus the focused RoleBinding fixture as the acceptance corpus.

### Candidate carrier improvement: explicit ordered binding semantics

The current `qualifier="ordinal:N"` convention is adequate for this proof but should not silently become the permanent general solution.

Investigate whether ordered/repeated role bindings deserve an explicit carrier-level ordinal or a standardized profile contract.

## No extension indicated

The projection found no need for new primitives for:

- questions;
- claims;
- concepts;
- hypotheses;
- goals;
- methods;
- examples;
- moves;
- stance;
- question state;
- source messages;
- higher-order relation targeting in principle.

All fit as domain/profile semantics over the existing carrier.

## Recommended next proof

1. author `inquiry-profile-v1` using the Hypergraph kernel's own `RelationType`, `RoleType`, `instanceOf`, `specializes` and `declaresRole` machinery;
2. validate both generated projections with the actual Scientific Hypergraph closure validator;
3. add relation-as-participant and RoleBinding-as-participant fixtures;
4. pass the resulting carrier documents through an OntoCanon governance spike;
5. only then design cross-trajectory alignment records.

The two source trajectories should remain independently immutable throughout.
