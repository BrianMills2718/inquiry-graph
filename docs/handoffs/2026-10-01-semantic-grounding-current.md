# Semantic grounding inquiry — current handoff (2026-10-01)

## Purpose

This handoff supersedes the earlier partial semantic-grounding checkpoint in Inquiry Graph PR #86. It records the conversation through the completed executable measurement-to-factor probe.

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

The mappings should carry provenance, uncertainty, preservation/loss, and explicit refusal rather than silently asserting equivalence.

## Key distinctions

- A **lexical primitive** is not necessarily a grounding primitive.
- A **definitional basis** is not necessarily semantically irreducible.
- A **grounding primitive** must have an explicit non-lexical derivation or measurement path.
- Sensor evidence is not world truth.
- A top-level ontology projection is not automatically an equivalence.

## Current artifacts

### Linguistic Core PR #21

Six-concept Grounding IR probe for:

- red
- object
- event
- support
- sit
- chair

Includes DOLCE/BFO/UFO loss-aware projections and NSM/Longman comparison.

### Linguistic Core PR #22

Grounding-floor audit for:

- contact
- relative position
- load response
- body posture
- persistence

Pushes those factors toward measurable tactile, proprioceptive, force/load, gravity-reference, displacement, and spatiotemporal correspondence evidence.

### Linguistic Core PR #23

Executable measurement-to-factor specimen.

Pipeline:

```text
raw observations
  -> inferred low-level factors
  -> confidence / uncertainty
  -> semantic classification
```

Cases:

- positive support;
- visual obstruction;
- transient contact / attachment;
- posture + persistence;
- occlusion / replacement identity ambiguity;
- indistinguishable duplicate ambiguity.

Verification:

- 12/12 focused tests;
- 6/6 fixture outcomes;
- 201 full repository tests passed, 4 skipped.

## Current next gate

Use data not authored specifically for the rules.

Preferred order:

1. find a small public sensor / psychophysics dataset supporting pressure/contact/support, posture, or persistence;
2. map raw rows into the existing observation layer without changing semantic labels to fit the data;
3. keep calibration and evaluation separate if thresholds are fitted;
4. include adversarial / negative cases;
5. report refusals and failures;
6. if no suitable public dataset exists, construct a small physics simulation with explicit ground truth.

## Stop rule

Do not expand to the proposed 20–25 word semantic-basis benchmark until the measurement-to-factor layer survives non-hand-authored data.

## Inquiry Graph provenance

See `examples/semantic-grounding-2026-10-01/source-excerpts.json` for the curated visible conversation excerpts underlying this handoff.
