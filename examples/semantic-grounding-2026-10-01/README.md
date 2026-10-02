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

The curated source excerpts themselves end at that point. They remain a historical
source layer rather than being retroactively extended. The current research state
is maintained in `docs/handoffs/2026-10-01-semantic-grounding-current.md`.

## Durable implementation state

The first external-grounding sequence is merged to Linguistic Core `main`:

- **PR #21** — *Experimental six-concept semantic grounding probe*
- **PR #22** — *Audit the grounding floor beneath support, posture, and persistence*
- **PR #23** — *Executable measurement-to-factor grounding specimen*
- **PR #24** — *External UCI posture grounding and rotation-invariance probe*

The second grounding family is also governed in `main`:

- **PR #25** — preregistered a PhysioNet load-bearing-contact experiment before data inspection;
- **PR #26** — recorded that v1's proposed reference was not independent and preregistered an independent-reference v2.

The progression is now:

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
        ↓
second-family preregistration
        ↓
reference-independence audit catches a circular validation design
        ↓
independent-reference contact v2 preregistered
```

## First external-data result

The UCI posture probe used the dataset's official train/test subject partition.
On 365 held-out windows, the simple rotation-invariant factor path classified
338 (92.6% coverage) and was correct on all covered windows for its deliberately
coarse stable-vs-non-static target; 27 windows remained explicit refusals.

The same data falsified a previous low-level assumption: a `mean Z ~= +1 g`
gate was inappropriate for the waist-mounted recording frame. Only 2/365
held-out windows satisfied it. A minimal coordinate-rotation test showed that
vector-magnitude factors remained invariant to floating-point precision across
1,095 rotated comparisons.

This established a small methodological rule rather than a new architecture:
**grounding factors should state and test the transformations they are expected
to survive.**

## Second-family v1 failure

The PhysioNet v1 experiment was preregistered before the selected force data
were inspected. All 18 selected recordings were subsequently hash-verified.

Across 218,142 rows, the proposed per-foot total-force reference channel was
equal to the sum of the eight individual inference sensors to floating-point
roundoff. The inference rule used that same sum.

Therefore the proposed validation was algebraically circular. No grounding
accuracy metric is claimed for v1.

This added another methodological rule:

> **Audit whether the proposed reference is genuinely independent of the
> inference inputs before semantic scoring.**

A separately named data column is not necessarily an independent measurement.

## Active next gate: independent foot-ground contact v2

Linguistic Core PR #26 preregisters the replacement against the University of
Geneva/Yareta multimodal gait dataset.

Primary design:

- inference: 16 pressure-insole sensors for one foot;
- reference: optoelectronic foot-strike / foot-off events derived from marker
  trajectories and visually checked/corrected by the source authors;
- force plates and insole event detection are not used to construct the primary
  reference;
- 150 ms exclusion margin around gait-event boundaries because the source
  reports approximately 0.1 s synchronization precision;
- calibration: P02, P04, P05, P07, P08, P10;
- held out: P03, P06, P09;
- P01 excluded because no insole data were recorded;
- no vocabulary expansion until this independent-reference contact probe has
  either succeeded or failed transparently.

The active protocol is:
`docs/handoffs/2026-10-02-foot-ground-contact-v2.md`.

The superseded PhysioNet preregistration remains at:
`docs/handoffs/2026-10-02-load-bearing-contact-next-gate.md`.

## Licensing note

The UCI dataset used in Linguistic Core PR #24 has conflicting source-level
license statements: the current UCI catalog says CC BY 4.0, while the README
inside the pinned archive says commercial use is prohibited. The Linguistic
Core artifact therefore redistributes no raw archive bytes or extracted sensor
rows.

The Yareta v2 dataset is published as CC BY 4.0.

## Provenance limitations

`source-excerpts.json` contains curated verbatim excerpts from the visible
conversation available when this source layer was created. It is not a complete
ChatGPT export, does not preserve original message IDs or timestamps, and is
not independently adjudicated gold data. Later implementation state belongs in
the current handoffs rather than being retroactively inserted into the excerpt
corpus.
