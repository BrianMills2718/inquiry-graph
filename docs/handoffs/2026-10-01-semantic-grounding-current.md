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

All four grounding PRs were independently based on `main` and are now merged:

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


## Selected second grounding family — 2026-10-02

The next gate is now concretely selected rather than left as a choice between contact/support and persistence/tracking.

Use PhysioNet **Gait in Parkinson's Disease v1.0.0** (DOI `10.13026/C24H3N`, Open Data Commons Attribution License v1.0) as a public real-force source. The implementation will use only the 18 `GaCo*_01.txt` healthy-control normal-walk recordings.

Published format:

- 100 Hz sampling;
- eight vertical ground-reaction-force sensors under each foot, in Newtons;
- one total-force channel per foot;
- total-force channels withheld from inference and used only as physical reference channels.

Target factor:

- `load_bearing_contact_evidence`
- `no_load_bearing_contact_evidence`
- `REFUSAL:transition_or_uncertain`

The probe will not equate force, contact, and support. Its claim is limited to a measurable load-bearing-contact factor below `support`.

Predeclared held-out subjects: `GaCo04`, `GaCo08`, `GaCo12`, `GaCo16`; the other 14 selected subjects are calibration-only.

Required robustness checks include naturally occurring swing/no-load windows, stance/load windows, loading/unloading transition refusals, sensor-order permutation invariance, and separate synthetic single-sensor-dropout degradation.

The detailed protocol is recorded in `docs/handoffs/2026-10-02-load-bearing-contact-next-gate.md`.

A fresh Linguistic Core worktree was created from merged `main` on `research/load-bearing-contact-physionet`. PhysioNet's format file and SHA-256 manifest were retrieved, but the guarded WSL transport failed before the 18 data recordings were downloaded; the real download command was not launched. No outcomes have been observed and no thresholds have been tuned.
