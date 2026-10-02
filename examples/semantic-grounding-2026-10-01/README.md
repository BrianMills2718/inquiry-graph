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
11. the executable measurement-to-factor pipeline;
12. the current next gate: external/public or simulated non-hand-authored data.

## Durable implementation state

The corresponding Linguistic Core work is currently in three independent open PRs, all based on `main` rather than on one another:

- **Linguistic Core PR #21** — *Experimental six-concept semantic grounding probe*
  - branch: `research/semantic-grounding-six-concepts`
  - head: `db74c7d88c4edf964b9eaf159938da884a2a4a7d`
- **Linguistic Core PR #22** — *Audit the grounding floor beneath support, posture, and persistence*
  - branch: `research/grounding-floor-audit`
  - head: `93a6cbfe0bf9871fd03f9a8a42e80dd9d5f2f7a7`
- **Linguistic Core PR #23** — *Executable measurement-to-factor grounding specimen*
  - branch: `research/measurement-to-factor-specimen`
  - head: `e2ea293b7fa7256a8f219fafa7d61ce454a676d7`

PR #23 verified:

- 12 focused tests passed;
- 6/6 specimen episodes classified as expected;
- full Linguistic Core suite: 201 passed, 4 skipped.

## Current substantive state

The inquiry has moved through three increasingly concrete levels:

```text
phenomenal / psychophysical grounding hypothesis
        ↓
candidate semantic factorization
        ↓
measurement-to-factor executable probe
```

The strongest current claim is deliberately limited:

> A machine-checkable boundary can keep raw observations, inferred perceptual factors, uncertainty, and semantic classification separate, and can refuse classifications when the evidence is insufficient.

This does not establish a general grounding theory, metaphysical object identity, or universal definitions.

## Current next question

Do the candidate factorization and refusal rules survive **non-hand-authored data**?

Preferred next experiment:

- adapt the measurement-to-factor probe to a small public sensor / psychophysics dataset if a suitable one exists;
- otherwise use a controlled physics simulation with explicit ground truth for gravity, contact, load, displacement, occlusion, replacement, and duplicate objects.

Do not expand the semantic vocabulary before that gate.

## Provenance limitations

`source-excerpts.json` contains curated verbatim excerpts from the visible conversation available in this chat context. It is not a complete export, does not preserve original ChatGPT message IDs or timestamps, and is not independently adjudicated gold data.

The implementation-state claims above were rechecked against GitHub on 2026-10-01. External literature claims from the conversation are not promoted here as independently reviewed facts.
