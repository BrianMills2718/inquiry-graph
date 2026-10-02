# Semantic grounding next gate — load-bearing contact from public force data

**Date:** 2026-10-02  
**Status:** selected next experiment; implementation pending machine availability

## Decision

Use a second external-data grounding family centered on **load-bearing contact evidence** rather than expanding the lexical vocabulary.

The selected source is PhysioNet's **Gait in Parkinson's Disease v1.0.0** database:

- dataset page: https://physionet.org/content/gaitpdb/1.0.0/
- DOI: `10.13026/C24H3N`
- license: Open Data Commons Attribution License v1.0
- format reference: https://physionet.org/content/gaitpdb/1.0.0/format.txt
- published SHA-256 manifest: https://physionet.org/files/gaitpdb/1.0.0/SHA256SUMS.txt

The experiment will use only the **GaCo healthy-control, normal-walk (`_01`) recordings**. This avoids making disease classification part of the grounding probe.

The published manifest contains 18 such recordings:

```text
GaCo01_01  GaCo02_01  GaCo03_01  GaCo04_01  GaCo05_01  GaCo06_01
GaCo07_01  GaCo08_01  GaCo09_01  GaCo10_01  GaCo11_01  GaCo12_01
GaCo13_01  GaCo14_01  GaCo15_01  GaCo16_01  GaCo17_01  GaCo22_01
```

## Why this dataset

This is qualitatively different from the inertial-posture probe.

Each row contains 19 columns sampled at 100 Hz:

1. time;
2. eight vertical ground-reaction-force sensors under the left foot;
3. eight vertical ground-reaction-force sensors under the right foot;
4. withheld total force under the left foot;
5. withheld total force under the right foot.

Force is recorded in Newtons.

This gives a direct measurement path into one factor below `support`:

```text
distributed vertical force measurements
        ↓
sustained load-bearing contact evidence
        ↓
candidate support-related factor
```

It deliberately does **not** claim:

```text
force = contact = support
```

A vertical force pattern can license a bounded claim about load-bearing contact. Full `support` still needs additional structure such as relative position, persistence, bearer/load roles, and counterfactual/load-response behavior.

## Semantic target

Prediction vocabulary:

- `load_bearing_contact_evidence`
- `no_load_bearing_contact_evidence`
- `REFUSAL:transition_or_uncertain`

The target is per foot and per short time window.

The withheld per-foot total-force channel is a **physical reference channel**, not metaphysical ground truth. Inference must use only the eight individual sensors for that foot.

## Predeclared subject split

The split is fixed before looking at model outcomes.

Held-out evaluation subjects are the available GaCo subject numbers divisible by four:

```text
04, 08, 12, 16
```

Calibration subjects are the remaining 14 GaCo normal-walk subjects:

```text
01, 02, 03, 05, 06, 07, 09, 10, 11, 13, 14, 15, 17, 22
```

All threshold selection must use calibration subjects only.

## Evidence separation

Keep four layers distinct:

```text
raw per-sensor force rows
        ↓
inferred distributed-load factors
        ↓
confidence / transition band / refusal
        ↓
load-bearing-contact evidence classification
```

The withheld total-force channel is consulted only after inference for calibration/evaluation reference construction.

No clinical labels, demographic fields, or Parkinson's-disease status are inputs or targets.

## Required negative / adversarial cases

The probe should include naturally occurring and synthetic robustness cases:

- swing-phase / near-zero force windows;
- loaded stance windows;
- loading/unloading transition windows that should refuse;
- single-sensor dropout;
- sensor-order permutation.

The artificial cases are robustness tests only and must be reported separately from external-data evaluation.

## Transformation expectations

The prior UCI posture probe established that grounding factors should declare relevant transformations explicitly.

For total load-bearing contact evidence:

- **sensor ordering:** should be invariant;
- **left/right renaming:** semantic role changes, but load magnitude logic should be symmetric;
- **single-sensor dropout:** should degrade confidence rather than silently flip whenever possible;
- **time reversal:** may preserve static load magnitude but does not preserve loading-vs-unloading transition direction;
- **arbitrary force scaling:** not invariant unless the scaling is explicitly modeled/calibrated.

No GNN or geometric-learning framework is warranted for these tests.

## Success criteria

A useful result does not require perfect classification.

The probe should report, on held-out subjects:

- coverage;
- false load-bearing positives during reference no-load periods;
- false no-load predictions during reference loaded periods;
- refusals in transition/ambiguous regions;
- per-subject variation;
- sensor-permutation invariance;
- degradation under sensor dropout.

Thresholds must not be changed in response to held-out failures.

## Stop rule

Do not promote `support` itself as externally grounded merely because this factor works.

A successful probe establishes only a real-data path for **load-bearing contact evidence**. The next step would be to combine it with relative-position and persistence/load-response evidence before making a stronger support claim.

## Current execution state

A fresh Linguistic Core worktree/branch was prepared from merged `main` as:

`research/load-bearing-contact-physionet`

The PhysioNet format file and SHA-256 manifest were retrieved successfully. The guarded WSL transport failed immediately before downloading the 18 force recordings, and explicitly reported that the real download command was not launched. No dataset rows have therefore been analyzed yet.
