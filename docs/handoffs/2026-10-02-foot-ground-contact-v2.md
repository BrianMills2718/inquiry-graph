# Semantic grounding next gate v2 — independent foot-ground contact reference

**Date:** 2026-10-02  
**Status:** completed negative result; retained in merged Linguistic Core PR #29

## Why v1 was rejected

The PhysioNet load-bearing-contact experiment preregistered in Linguistic Core
PR #25 was executed only far enough to audit its proposed reference channel.

All 18 selected recordings passed their published SHA-256 checks. Across
218,142 rows, the per-foot recorded total-force channel equalled the sum of the
eight per-foot individual force sensors to floating-point roundoff:

- maximum absolute difference: `2.2737367544323206e-13 N`;
- rows differing by more than `1e-9 N`: **0** for either foot.

The v1 inference rule defined force as that same eight-sensor sum. Therefore
the proposed "withheld" total-force reference was algebraically derived from
the inference input. Reporting classification accuracy against it would have
been tautological rather than external validation.

Linguistic Core PR #26 retains the original v1 preregistration, records this
failure explicitly, and preregisters the replacement design below.

## Replacement dataset

Use the University of Geneva / Yareta dataset:

**Human gait and other movements - markers / inertial sensors / pressure
insoles / force plates**

- Yareta DOI: `10.26037/yareta:xkxgaw6ewjdhfntdhtj7upepxy`
- associated Scientific Data article:
  `10.1038/s41597-023-02077-3`
- license: CC BY 4.0
- 10 asymptomatic participants
- 16 pressure sensors per insole, sampled at 100 Hz
- optoelectronic marker trajectories sampled at 100 Hz
- additional IMU and force-plate channels available but not primary inference
  inputs

The dataset authors report that walking gait events (foot strike and foot off)
were detected from optoelectronic marker trajectories using the validated Zeni
et al. method and then visually checked/corrected. They explicitly state that
the force plates were not used to detect those gait events and that vendor
insole event detection was not used.

That separation is the key reason for v2: **pressure data become the inference
channel; independently derived kinematic gait events become the reference.**

## Trial scope

Use only:

- slow gait;
- comfortable gait;
- fast gait.

Exclude running, Timed Up and Go, 2-minute gait, and non-walking functional
tasks from v2.

Participant 01 is excluded because the source reports no insole data for that
participant.

## Predeclared split

Calibration:

`P02, P04, P05, P07, P08, P10`

Held-out evaluation:

`P03, P06, P09`

The split is fixed before the Yareta recordings are downloaded or inspected.

## Semantic target

Per foot and per 200 ms window:

- `foot_ground_contact_evidence`
- `no_foot_ground_contact_evidence`
- `REFUSAL:near_event_or_uncertain`

This is a lower-level contact factor below `support`. It is not a universal
definition of contact and does not by itself establish support.

## Evidence separation

Inference may use only the 16 pressure-sensor channels for the evaluated foot.

Inference may **not** use:

- marker trajectories;
- foot-strike / foot-off event labels;
- force-plate channels;
- IMU channels;
- participant demographics.

Primary reference:

- stance = foot strike through following foot off;
- swing = foot off through following foot strike.

## Synchronization uncertainty

The source reports that system synchronization precision is approximately
0.1 seconds and recommends caution.

Therefore v2 preregisters a **150 ms exclusion margin** around every gait-event
boundary. A 200 ms scoring window is reference-contact or
reference-no-contact only if the entire window lies at least 150 ms from all
event boundaries.

Windows near an event are reference-refusals rather than forced labels.

If event times cannot be mapped unambiguously into the synchronized CSV time
base, the affected trial is excluded and reported. No heuristic time shifting
is allowed.

## Pressure feature and calibration

For each trial and foot:

1. sum the 16 individual pressure sensors at each sample;
2. compute the unlabeled 5th and 95th percentiles of that trial/foot signal;
3. map those percentiles to 0 and 1 and clip to [0,1];
4. for each non-overlapping 20-sample (200 ms) window, use median normalized
   summed pressure as the inference feature.

Threshold fitting is calibration-only.

Candidate center thresholds:

`0.10, 0.15, 0.20, ..., 0.80`

For candidate center `t`:

- feature >= `t + 0.05` -> contact evidence;
- feature <= `t - 0.05` -> no-contact evidence;
- otherwise -> refusal.

Choose the center on calibration participants only to maximize balanced
accuracy with refusals counted as incorrect. Tie-break by higher coverage,
then lower center threshold. Freeze before evaluation.

## Robustness tests

Held-out robustness checks, without retuning:

- sensor-order permutation: prediction must be invariant;
- left/right processing: exact same code path;
- single-sensor dropout: drop each of 16 pressure channels separately and
  report error/coverage/refusal degradation.

Force-plate data may be audited later as a secondary channel on steps that
cross a plate, but may not define or tune the primary v2 labels.

## Stop rules

- Do not modify the split, normalization, synchronization margin, candidate
  threshold grid, refusal width, or calibration objective after inspecting
  outcomes.
- Retain failed or low-coverage results.
- Do not claim full support grounding from this contact factor.
- Any material protocol change requires `experiment_plan_v3.json`.

## Historical acquisition manifest checkpoint

Linguistic Core PR #27 freezes the public metadata selection before signal
inspection:

- 126 paired walking trials;
- 252 files;
- 321,936,880 bytes;
- exact Yareta file IDs, sizes, paths, and SHA-256s;
- selection SHA-256:
  `0cdcc0ca7774648cfd189a9f00c39c49edd6ba036dd39346766e7447fffbe594`.

The discovery tool verifies the preregistered participant split and trial types
and fails closed on missing CSV/C3D counterparts.

Current blocker: Yareta's public archive can be listed and prepared, but
anonymous selective file delivery returns HTTP 500 after the documented token
flow. No signal rows or gait-event contents have been inspected, and the v2
protocol has not been changed in response.

## Download-route diagnostic correction

Linguistic Core PR #28 records a correction to the earlier access diagnosis.

Current DLCM 3.1.9 Access OpenAPI defines:

- public/archive binary download at
  `GET /access/metadata/{dipName}/download`;
- its token endpoint at
  `GET /access/metadata/{dipName}/download-token`;
- per-file binary download only inside a prepared dissemination package at
  `GET /access/dip/{parentId}/data/{id}/download`;
- the corresponding DIP file token endpoint at
  `GET /access/dip/{parentId}/data/{id}/download-token`.

The path previously used for an anonymous individual file,
`/access/metadata/{archiveId}/data/{fileId}/download`, is **not present in the
current OpenAPI specification**. Its HTTP 500 response therefore does not
establish that supported anonymous Yareta download is broken; it establishes
that an unsupported/legacy route failed.

The remaining least-invasive diagnostic is one archive-level request to the
documented public download endpoint with `Range: bytes=0-1023`, after obtaining
the archive-level download-token cookie. The request must use streaming mode so
that a server response of HTTP 200 (Range ignored) can be disposed immediately
without downloading the archive.

Interpretation is frozen:

- HTTP 206: public archive delivery supports ranges; the earlier file route was
  simply wrong;
- HTTP 200: public archive delivery works but ignores ranges, implying
  whole-archive delivery for anonymous users;
- HTTP 500: the documented archive dissemination path itself is failing
  server-side for this archive;
- HTTP 401/403: a deployment/access-policy mismatch with the documented Public
  archive-download role.

The authorized machine went offline before this one request could be issued.
No signal data have been read and the experiment protocol remains unchanged.


## Completed v2 result

The pending archive-range diagnostic later returned **HTTP 206 Partial
Content** with `Accept-Ranges: bytes`. The archive is a standard ZIP, so only
the 252 preregistered files were range-extracted and verified.

All 126 trial pairs passed alignment after applying the C3D-defined frame
origin where required.

Reference support under the frozen 150 ms margin / 200 ms window rule:

Calibration:
- contact: 492
- no-contact: 3
- ambiguous: 2,337

Held out:
- contact: 271
- no-contact: 9
- ambiguous: 1,186

Calibration selected center `0.45`.

Held-out result:
- coverage: 91.79%
- balanced accuracy, refusals incorrect: 50.47%
- accuracy on covered windows: 49.81%
- false contact: 4
- false no-contact: 125
- refusals: 23

Sensor-order permutation caused 0 prediction changes. Single-sensor dropout
did not rescue the model.

The v2 grounding claim is therefore **not supported**.

No parameter in this document is changed in response to the result.

See:
`docs/handoffs/2026-10-03-foot-ground-contact-v2-result.md`

Any redesign must be v3 or later and must use fresh confirmatory evaluation
data rather than silently reusing P03/P06/P09 as untouched held-out subjects.
