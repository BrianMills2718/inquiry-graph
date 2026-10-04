# Support vertical slice — decisive research gate

**Date:** 2026-10-04  
**Status:** proposed next experiment; decision criteria frozen before implementation

## Why this gate

The grounding program has accumulated enough horizontal structure. The next
question is whether one semantic claim can be carried end-to-end from
non-lexical measurements through grounded factors into a structured concept and
loss-aware ontology projections.

Use **support** as that vertical slice.

Current Linguistic Core factorization:

```text
contact pattern
+ relative-position pattern
+ load-response pattern
        ↓
support relation
        ↓
support disposition
```

Existing work has independently exposed three methodological requirements:

1. transformation expectations must be explicit and tested;
2. validation references must be independent of inference inputs;
3. reference construction must supply enough usable evidence for every class.

The Yareta v2 negative result is retained; no post-hoc repair is part of this
gate.

## Current evidence inventory

### Contact

Status: empirically decomposable but inferential.

Candidate lower-level evidence:

- cutaneous / pressure deformation;
- tracked boundary coincidence;
- independent spatial evidence.

Gap: evidence for contact is not identical to metaphysical contact.

### Relative position

Status: empirically decomposable but reference-frame dependent.

Candidate evidence:

- tracked object poses;
- explicit gravity vector/reference estimate;
- spatiotemporal correspondence.

Gap: egocentric, allocentric, object-centered and gravity-relative frames must
not be silently collapsed.

### Load response

Status: conceptually decomposed and testable, but not externally validated as
a stable factor.

Candidate evidence:

- applied force/load;
- contact/pressure response;
- relative displacement over time.

This is the largest missing empirical piece beneath support.

### Support relation

Status: candidate composition only.

The current claim is that support can be licensed by the conjunction and
temporal organization of contact, gravity-relative geometry and bounded
load-response evidence. This has not yet been demonstrated across controlled
counterfactual cases.

### Support disposition

Status: higher-level learned/counterfactual claim.

A single observed support episode cannot establish a disposition. Repeated
perturbations under varied loads/conditions are required.

## Decisive experiment

Build a minimal controlled rigid-body environment with:

- explicit gravity;
- two or more rigid bodies;
- independently recorded body poses;
- contact points/normals;
- normal/contact forces;
- externally applied load perturbations;
- displacement/acceleration through time;
- attachment/joint state available only as evaluation ground truth, not as an
  inference feature.

The experiment must generate measurements first and derive grounding factors
from those measurements. It must not pass a simulator-provided `support`
label into the inference path.

## Required episode families

At minimum:

1. **ordinary support**
   - upper body rests on lower body under gravity;
   - contact, appropriate gravity-relative geometry, load force and bounded
     displacement.

2. **visual/near-contact non-support**
   - apparent above/below alignment with a gap;
   - no contact force.

3. **lateral contact**
   - bodies touch side-to-side;
   - contact exists but geometry/load response does not license vertical
     support.

4. **attachment / suspension**
   - body remains positioned because of a joint/tether/attachment rather than
     load-bearing contact from the candidate supporter.

5. **insufficient-strength collapse**
   - initial contact and geometry are support-like;
   - increased load causes large displacement/failure.

6. **stable support under increased load**
   - increased load produces increased contact force while relative position
     remains within preregistered tolerance.

7. **transient collision**
   - nonzero contact impulse without sustained load-bearing stability.

8. **gravity transformation**
   - rotate the entire world/body configuration together with gravity;
   - support classification should be invariant when expressed in the
     gravity-relative frame.

9. **coordinate transformation**
   - rotate/translate the coordinate frame while preserving physical state;
   - all physical-factor classifications should remain invariant.

10. **supporter removal counterfactual**
    - remove the candidate supporter while holding other initial conditions as
      fixed as the simulator permits;
    - the supported body should exhibit the predicted downward/unconstrained
      response if the supporter was causally load-bearing.

## Measurement / factor separation

Raw observations:

```text
body poses
velocities / accelerations
gravity vector
contact points / normals
contact-force vectors
externally applied forces
timestamps
```

Derived factors:

```text
estimated_contact
gravity_relative_position
normal_load_transfer
bounded_relative_displacement
sustained_load_response
supporter_removal_dependence
```

Semantic composition:

```text
support_episode_evidence
REFUSAL:insufficient_or_conflicting_evidence
non_support_evidence
```

The simulator's object IDs and physical contact state may be used for evaluation
and provenance. A simulator-provided semantic support flag, if any, must not be
used.

## Cross-environment requirement

The simulation is not sufficient by itself to establish a universal grounding
factor.

Its role is to provide controlled counterfactual ground truth and determine
whether the factor contract is coherent.

The same factor schema must then be compared against at least one non-simulated
measurement path already available or newly collected. Exact sensors need not
match; the **factor interfaces** must.

Examples:

```text
simulation contact-force vector
physical pressure / force sensor
        ↓
normal_load_transfer
```

and:

```text
simulation body poses
motion-capture / depth / position tracker
        ↓
gravity_relative_position
+ bounded_relative_displacement
```

If the factor definitions become environment-specific rather than
measurement-adapter-specific, that is evidence against the stable-interlingua
thesis.

## Ontology projection gate

Only after the episode-level factorization passes should the resulting
`support_episode_evidence` and `support_disposition` records be projected into
DOLCE, BFO and UFO.

For each projection record:

- relation type;
- preserved structure;
- lost structure;
- added ontological commitments;
- provenance;
- confidence/review status.

Do not use `equivalentTo` by default.

## Go criteria

Continue investing substantially in the grounding architecture if:

1. the same factor definitions handle all required simulation episode families
   without using semantic simulator labels;
2. coordinate transformations preserve predictions exactly or within declared
   numerical tolerance;
3. gravity transformations preserve support when the physical relation is
   transformed with gravity;
4. contact-only cases do not collapse into support;
5. load perturbation distinguishes stable support from collapse;
6. supporter-removal counterfactuals add discriminative information beyond
   static contact/geometry;
7. at least one non-simulated measurement adapter can instantiate the same
   factor interfaces without redefining the factors;
8. ontology projections can mechanically state preservation/loss rather than
   relying only on prose judgment.

## Stop / narrow criteria

Reduce or stop investment in a universal grounded interlingua if:

1. factor definitions must be rewritten for each sensor environment;
2. support classification requires the lexical concept `support` or
   simulator-specific semantic labels in its own derivation;
3. invariance/reference-frame requirements cannot be stated independently of
   individual fixtures;
4. counterfactual load-response evidence adds no stable distinction over
   hand-coded episode labels;
5. cross-environment mappings are mostly bespoke semantic judgments with no
   reusable factor interface;
6. ontology preservation/loss cannot be made mechanically inspectable.

A failure is a valid result and must be retained.

## Scope discipline

Do not expand the broad semantic vocabulary during this gate.

Do not add a geometric-deep-learning stack, GNN, learned world model or new
ontology merely to increase architectural sophistication.

The objective is to decide whether the existing grounding thesis survives one
deep vertical test.
