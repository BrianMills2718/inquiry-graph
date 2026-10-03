# Foot-ground contact v2 — completed negative result

**Date:** 2026-10-03  
**Status:** completed; negative result retained in merged Linguistic Core PR #29

## What was tested

The second external grounding family tested whether plantar pressure-insoles
could support a bounded `foot_ground_contact_evidence` factor against an
independent optoelectronic reference.

Inference channel:

- 16 pressure sensors for the evaluated foot.

Primary reference:

- source-authored C3D Foot Strike / Foot Off events;
- Left / Right event context;
- events derived from optoelectronic marker trajectories and visually
  checked/corrected by the source authors.

The preregistered v2 protocol was not changed after data inspection.

## Acquisition

Yareta public archive:

- DOI: `10.26037/yareta:xkxgaw6ewjdhfntdhtj7upepxy`
- CC BY 4.0
- archive size: 2,760,098,341 bytes
- ZIP entries: 775

The public archive download endpoint supports HTTP byte ranges. This made it
possible to retrieve only the frozen acquisition-manifest selection:

- 126 paired walking trials;
- 252 files;
- 321,936,880 uncompressed bytes;
- 169,830,263 compressed bytes transferred;
- every file verified by ZIP CRC and Yareta SHA-256.

Canonical selection hash:

`0cdcc0ca7774648cfd189a9f00c39c49edd6ba036dd39346766e7447fffbe594`

## Alignment

All 126 synchronized CSV / C3D pairs passed the structural gate:

- CSV rows = C3D point frames;
- 100 Hz sampling;
- expected Foot Strike / Foot Off labels only;
- Left / Right contexts only;
- 16 pressure channels per foot.

Three C3D trials had nonzero `first_frame` values. Event times were mapped to
CSV row zero using the C3D-defined frame origin:

```text
adjusted_event_time = EVENT_time - first_frame / frame_rate
```

This resolved every event inside the synchronized CSV time base without a
fitted or heuristic time shift.

## Preregistered reference-window consequence

The frozen protocol used:

- 200 ms non-overlapping windows;
- 150 ms exclusion margin around each event boundary.

That combination produced a severe reference imbalance.

Calibration:

- contact: 492
- no-contact: 3
- boundary-ambiguous: 2,337

Held out:

- contact: 271
- no-contact: 9
- boundary-ambiguous: 1,186

The imbalance was not corrected after inspection.

## Calibration

Calibration participants:

`P02, P04, P05, P07, P08, P10`

Frozen grid selected center:

`0.45`

Calibration balanced accuracy, refusals counted incorrect:

`0.7530487805`

Calibration coverage:

`0.9515151515`

The selected threshold was therefore supported by only three no-contact
calibration windows.

## Held-out result

Held-out participants:

`P03, P06, P09`

- scored windows: 280
- coverage: 91.79%
- balanced accuracy, refusals incorrect: 50.47%
- overall accuracy, refusals incorrect: 45.71%
- accuracy on covered windows: 49.81%
- false contact: 4
- false no-contact: 125
- refusals: 23

Prediction counts:

- contact: 127
- no-contact: 130
- refusal: 23

Reference counts:

- contact: 271
- no-contact: 9

The dominant failure was incorrectly predicting **no contact** during
optoelectronically referenced contact windows.

## Robustness

Sensor-order permutation:

- prediction changes: 0 / 280
- maximum feature drift: 0.0

The expected permutation invariance passed.

Sixteen single-sensor-dropout runs did not rescue the result:

- balanced accuracy approximately 0.390–0.507
- coverage approximately 0.896–0.932
- false no-contact predictions remained high

## Interpretation

This is a meaningful negative result, not an invalid experiment.

Unlike PhysioNet v1, the v2 reference is genuinely independent of the pressure
inference channel. The protocol therefore tested the intended seam and failed
to provide evidence for robust pressure-to-contact grounding across held-out
participants.

The result does not establish a single cause. Plausible contributors include:

- the preregistered window/margin rule, which left almost no no-contact
  calibration windows;
- the normalized summed-pressure feature;
- participant variation;
- interactions among those factors.

No v2 parameter was changed after seeing the result.

## New methodological lessons

The project now has three externally learned rules:

1. **Transformation audit:** identify transformations a grounding factor should
   survive.
2. **Reference-independence audit:** a separately named channel is not
   necessarily independent evidence.
3. **Reference-support audit:** before calibration, check whether the frozen
   reference construction supplies enough examples of every class to support
   the planned objective.

The third rule does **not** authorize post-hoc repair of v2. It applies to
future preregistrations.

## Next constraint

Any v3 redesign requires:

- a separately versioned protocol;
- fresh confirmatory evaluation data not already used as v2 held-out evidence.

`P03`, `P06`, and `P09` are no longer untouched confirmation subjects for
a redesigned pressure rule.

The v2 negative result should remain durable even if a later protocol succeeds.
