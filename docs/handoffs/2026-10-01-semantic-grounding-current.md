# Semantic grounding inquiry — current handoff (updated 2026-10-02)

## Purpose

This handoff supersedes the earlier partial semantic-grounding checkpoint in Inquiry Graph PR #86. It records the trajectory through the first external-data measurement-to-factor probe.

## Research objective

Build a rigorous basis for a stable, comprehensive, grounded semantic vocabulary suitable for neuro-symbolic AI and world modeling.

The working architecture is:

```text
phenomenal / psychophysical structure
  -> measurable sensory variables
  -> inferred perceptual / sensorimotor factors
  -> learned semantic factors
  -> structured concepts
  -> lexical senses
  -> formal predicates / ontologies
  -> world / scientific models
```

The mappings should carry provenance, uncertainty, preservation/loss, explicit reference-frame assumptions, and refusal rather than silently asserting equivalence.

## Key distinctions

- A **lexical primitive** is not necessarily a grounding primitive.
- A **definitional basis** is not necessarily semantically irreducible.
- A **grounding primitive** must have an explicit non-lexical derivation or measurement path.
- Sensor evidence is not world truth.
- A top-level ontology projection is not automatically an equivalence.
- A grounding factor should state which transformations should preserve it and which should change or invalidate it.

## Merged Linguistic Core grounding sequence

The first four grounding PRs were independently based on `main` and are now merged. The second-family PRs #25–#26 are recorded in the current-state section below:

### PR #21 — six-concept Grounding IR probe

Concepts:

- red
- object
- event
- support
- sit
- chair

Includes DOLCE/BFO/UFO loss-aware projections and NSM/Longman comparison.

### PR #22 — grounding-floor audit

Factors:

- contact
- relative position
- load response
- body posture
- persistence

Pushes those factors toward measurable tactile, proprioceptive, force/load, gravity-reference, displacement, and spatiotemporal correspondence evidence while retaining the remaining inferential gaps.

### PR #23 — executable measurement-to-factor specimen

Pipeline:

```text
raw observations
  -> inferred low-level factors
  -> confidence / uncertainty
  -> semantic classification / refusal
```

The specimen keeps raw evidence, inferred factors, uncertainty, and semantic conclusions mechanically separate. It uses hand-authored fixtures and is therefore a construction/negative-test probe, not external validation.

### PR #24 — external UCI posture grounding and rotation-invariance probe

Uses UCI dataset 341, *Smartphone-Based Recognition of Human Activities and Postural Transitions*, against the dataset's official train/test subject partition.

The semantic target is intentionally narrow:

- `stable_posture_evidence`
- `motion_or_transition_evidence`
- `REFUSAL:uncertain`

Activity labels are calibration/evaluation references only and are not passed into inference.

Held-out result:

- 365 test windows total
- invariant-factor coverage: 338/365 = 92.6%
- covered accuracy for the deliberately collapsed stable-vs-non-static target: 338/338
- static: 91 stable, 17 uncertain, 0 motion
- dynamic: 149 motion, 0 uncertain, 0 stable
- transitions: 98 motion, 10 uncertain, 0 stable

The earlier `mean Z ~= +1 g` reference-frame assumption failed on the real waist-mounted data: only 2/365 held-out windows satisfied that gate, and only 1/108 static windows was accepted as stable by the axis-dependent baseline.

A minimal transformation test rotated each held-out synchronized accelerometer/gyroscope window 90 degrees around X, Y, and Z without recalibration. The vector-magnitude factors were invariant to floating-point roundoff and their predictions were stable in all 1,095 comparisons.

This supports a narrow methodological conclusion: **grounding factors should declare and test the transformations they are expected to survive.** It does not justify adding a GNN, an equivariant neural architecture, or a new semantic layer.

## Licensing boundary

There is a source-level licensing discrepancy for the UCI dataset:

- the current UCI catalog states CC BY 4.0;
- the README bundled inside the pinned archive states that commercial use is prohibited.

The Linguistic Core probe therefore commits no archive bytes and no extracted raw sensor rows. It retains code, aggregate results, and bounded source provenance only.

## Current strongest result

The project has now crossed the first non-hand-authored-data gate:

```text
real raw inertial measurements
  -> train-only calibrated low-level factors
  -> explicit uncertainty/refusal
  -> held-out narrow semantic evidence classification
  -> transformation robustness check
```

The result does **not** establish a complete grounding theory, universal posture semantics, metaphysical identity, or cognitive realism. It does show that the measurement-to-factor seam can be made explicit, externally exercised, loss-aware, and capable of refusing ambiguous cases.

## Current next gate

Do not expand the vocabulary indiscriminately.

The next research step should generalize the lessons from PR #24 without overfitting to inertial posture data:

1. record reference-frame / transformation expectations explicitly for proposed grounding factors;
2. test a second qualitatively different grounding family, preferably contact/load/support or object persistence/tracking;
3. prefer external data when licensing/provenance permit; otherwise use a controlled simulation with explicit ground truth;
4. preserve train/calibration versus held-out evaluation separation;
5. keep failure cases and refusals visible;
6. only after a second grounding family survives should the project expand toward the broader semantic-basis benchmark.

## Inquiry Graph provenance

See `examples/semantic-grounding-2026-10-01/source-excerpts.json` for the curated visible conversation excerpts underlying the earlier trajectory. The source-excerpt file ends before the external-data completion and is retained as a historical source layer rather than rewritten as if it were a full transcript.

## Selected second grounding family — current state 2026-10-02

The second family remains **contact/load evidence beneath support**, but the
first external design failed its reference-independence audit.

### PhysioNet v1 — invalid external reference

Linguistic Core PR #25 preregistered a PhysioNet force experiment before data
inspection. The 18 selected recordings were subsequently downloaded and
hash-verified.

Across 218,142 rows, the proposed per-foot total-force reference channel was
numerically identical to the sum of the eight individual force-sensor inputs to
floating-point roundoff:

- maximum absolute difference: `2.2737367544323206e-13 N`;
- rows differing by more than `1e-9 N`: 0.

Because the v1 inference force was defined as that same sum, scoring it against
the recorded total-force column would have been tautological. No grounding
accuracy result is claimed.

Linguistic Core PR #26 preserves this failure and the original preregistration
rather than rewriting the protocol after inspection.

### Yareta v2 — preregistered independent reference

PR #26 also preregisters the replacement experiment before any Yareta data are
downloaded.

Source:

- University of Geneva / Yareta dataset *Human gait and other movements -
  markers / inertial sensors / pressure insoles / force plates*;
- DOI `10.26037/yareta:xkxgaw6ewjdhfntdhtj7upepxy`;
- CC BY 4.0;
- associated Scientific Data article `10.1038/s41597-023-02077-3`.

Inference channel:

- the 16 pressure sensors for one insole/foot only.

Primary reference:

- foot-strike and foot-off events derived from optoelectronic marker
  trajectories and visually checked/corrected by the dataset authors.

The authors explicitly report that force plates were not used for gait-event
detection and that insole event detection was not used, giving the v2 design
the independent evidence/reference separation missing from v1.

Because the source reports approximately 0.1 s synchronization precision, v2
uses a preregistered 150 ms exclusion margin around gait events and refuses
windows near boundaries.

Calibration participants:

`P02, P04, P05, P07, P08, P10`

Held-out evaluation participants:

`P03, P06, P09`

Participant P01 is excluded because no insole data were recorded.

The exact normalization, threshold grid, refusal band, tie-breaking,
robustness tests, and stop rules are frozen in Linguistic Core
`evaluation/load_bearing_contact/experiment_plan_v2.json`.

The active Inquiry Graph protocol is:

`docs/handoffs/2026-10-02-foot-ground-contact-v2.md`

## Updated process lesson

The second-family attempt added a methodological requirement beyond
train/test separation and transformation testing:

> **Audit whether the proposed reference is genuinely independent of the
> inference inputs before computing semantic accuracy.**

A dataset can contain a separately named channel without that channel being
independent evidence.

## Current next action

Download only the preregistered Yareta walking data needed for participants
P02-P10, verify provenance/format, confirm event-to-synchronized-time mapping
without heuristic shifting, then implement the frozen v2 calibration and
held-out evaluation.

Do not expand the vocabulary until this independent-reference contact probe has
either succeeded or failed transparently.

## Yareta v2 acquisition checkpoint

Linguistic Core PR #27 is merged. It resolves the preregistered v2 scope against
Yareta's public archive-data API without reading signal rows and freezes:

- 126 paired walking trials;
- 252 files (one synchronized CSV plus one raw C3D per trial);
- 321,936,880 bytes total;
- every Yareta public data-file ID, path, size, and SHA-256;
- canonical selection SHA-256
  `0cdcc0ca7774648cfd189a9f00c39c49edd6ba036dd39346766e7447fffbe594`.

The selection contains only preregistered participants P02-P10 (excluding P01)
and the `SlowGait`, `Gait`, and `FastGait` trial families. Every selected
trial has a same-stem synchronized CSV and raw C3D.

Focused manifest tests: 4 passed. Full Linguistic Core suite: 210 passed,
5 skipped.

Yareta's public metadata API and archive preparation flow are working. However,
anonymous per-file delivery currently returns HTTP 500 even after the
documented per-file download-token cookie flow, and the prepared DIP internals
require authentication. No v2 signal rows have been downloaded or scored.

This is an access-layer blocker only. The preregistered dataset, participant
split, reference construction, threshold grid, and evaluation protocol remain
unchanged.

## Yareta download-route diagnostic correction

Linguistic Core PR #28 corrected the access-layer interpretation before any
signal download. The current DLCM 3.1.9 OpenAPI does not define per-file binary
download under archive metadata. It defines per-file download under prepared
DIP resources, while public anonymous dissemination is documented at the
archive level.

Therefore the earlier HTTP 500 from
`/access/metadata/{archiveId}/data/{fileId}/download` is not evidence that the
supported public download flow is broken; that path is absent from the current
OpenAPI.

The only pending diagnostic is a single 1 KiB Range GET to the documented
archive-level download endpoint after obtaining its archive token. The
authorized machine went offline before that request could be executed. No v2
signal rows have been inspected.
