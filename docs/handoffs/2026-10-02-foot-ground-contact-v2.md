# Semantic grounding next gate v2 — independent foot-ground contact reference

**Date:** 2026-10-02  
**Status:** preregistered in merged Linguistic Core PR #26; no v2 data downloaded yet

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
