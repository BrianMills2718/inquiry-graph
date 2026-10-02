# Semantic-grounding conversation continuation — 2026-10-01

This directory is the durable source layer for the semantic-grounding conversation that followed the operational-games inquiry.

## Coverage

The curated excerpts cover the inquiry arc from:

1. grounding formal terms through phenomenal / experiential structure;
2. psychophysics and phenomenal geometry;
3. the chair example and grounded definitions;
4. recursive dictionary definitions and grounded cyclic semantic graphs;
5. prior-art constraint rather than rebuilding formal semantics from scratch;
6. Linguistic Core as a candidate canonical semantic-factor layer for neuro-symbolic AI and world modeling;
7. a neutral Grounding IR with DOLCE/BFO/UFO projections;
8. NSM semantic primes versus Longman Defining Vocabulary versus grounding primitives;
9. the six-concept probe: `red`, `object`, `event`, `support`, `sit`, `chair`;
10. the grounding-floor audit for contact, relative position, load response, body posture, and persistence;
11. the executable hand-authored measurement-to-factor pipeline;
12. the decision to test the seam against non-hand-authored data.

The curated source excerpts themselves end at that point. The current handoff at
`docs/handoffs/2026-10-01-semantic-grounding-current.md` records the subsequent
external-data result.

## Durable implementation state

The corresponding Linguistic Core grounding sequence has now been merged to
`main`:

- **PR #21** — *Experimental six-concept semantic grounding probe*
- **PR #22** — *Audit the grounding floor beneath support, posture, and persistence*
- **PR #23** — *Executable measurement-to-factor grounding specimen*
- **PR #24** — *External UCI posture grounding and rotation-invariance probe*

The progression is:

```text
phenomenal / psychophysical grounding hypothesis
        ↓
candidate semantic factorization
        ↓
hand-authored executable measurement-to-factor probe
        ↓
real external inertial data + held-out evaluation
        ↓
explicit reference-frame / transformation robustness test
```

## Current substantive state

The strongest current claim remains deliberately bounded:

> A machine-checkable grounding boundary can keep raw observations, inferred
> perceptual factors, calibration, uncertainty/refusal, and semantic evidence
> classification separate, and that boundary can be exercised on held-out
> non-hand-authored sensor data.

The external UCI posture probe used the dataset's official train/test subject
partition. On 365 held-out windows, the simple rotation-invariant factor path
classified 338 (92.6% coverage) and was correct on all covered windows for its
coarse stable-vs-non-static target; 27 windows remained explicit refusals.

The same data falsified a previous low-level assumption: a `mean Z ~= +1 g`
gate was inappropriate for the waist-mounted recording frame. Only 2/365
held-out windows satisfied it. A minimal coordinate-rotation test showed that
vector-magnitude factors remained invariant to floating-point precision across
1,095 rotated comparisons.

This supports a small methodological addition, not a new architecture:
**proposed grounding factors should state and test the transformations they are
expected to survive.**

## Current next question

Does the same governed measurement-to-factor discipline survive a second,
qualitatively different grounding family?

Preferred next candidates:

- contact / load / support; or
- object persistence / tracking.

Use external data where provenance and licensing permit; otherwise use a small
controlled simulation with explicit ground truth. Keep calibration separate
from held-out evaluation, preserve refusals, and report failures without tuning
them away.

Do not expand the broad semantic vocabulary merely because the first posture
probe succeeded.

## Licensing note

The UCI dataset used in Linguistic Core PR #24 has conflicting source-level
license statements: the current UCI catalog says CC BY 4.0, while the README
inside the pinned archive says commercial use is prohibited. The Linguistic
Core artifact therefore redistributes no raw archive bytes or extracted sensor
rows.

## Provenance limitations

`source-excerpts.json` contains curated verbatim excerpts from the visible
conversation available when this source layer was created. It is not a complete
ChatGPT export, does not preserve original message IDs or timestamps, and is
not independently adjudicated gold data. It is retained as a historical source
layer; later implementation state is summarized in the current handoff rather
than retroactively inserted into the excerpt corpus.
