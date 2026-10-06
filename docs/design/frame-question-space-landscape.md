# Frame and question-space exploration landscape

Status: reuse-first landscape note, 2026-10-06.

## Research question

What mature work already covers the upstream inquiry capability of proactively generating alternative frames and important questions before failure forces a reframe?

The answer is: **substantial prior art exists, but it is distributed across several fields.** No new universal frame-shifting theory is warranted.

## Mature owners

### 1. Schön / reflective practice / reframing

Reflective-practice work treats design as a process in which a practitioner frames a situation, acts/experiments, observes the situation "talk back", and may reframe in response. Later design-team research distinguishes sensemaking of prior frames from future framing and shows that surprise often triggers reframing.

Use for Inquiry Graph:
- framing and reframing are activities over an inquiry, not merely static labels;
- a frame can be evaluated by what it makes possible to notice, test, and do;
- surprise/failure is one trigger for reframing, but not the only possible trigger.

Representative source:
- Stompff, Smulders & Henze, "Surprises are the benefits: reframing in multidisciplinary design teams" (Design Studies, 2016): https://www.sciencedirect.com/science/article/pii/S0142694X15300375

### 2. Dorst / frame creation

Dorst treats **frame creation** as a core design practice for open, complex problems. The emphasis is not simply repairing a failed frame but constructing a productive way of interpreting the situation that makes new solution directions available.

Use for Inquiry Graph:
- candidate frames can be generated deliberately;
- frames are productive insofar as they reorganize relations among situation, values, working principles, and desired outcomes;
- frame creation is a method family, not a reason to make `Frame` a universal ontology primitive.

Representative sources:
- Dorst, "The core of design thinking and its application" (Design Studies, 2011): https://doi.org/10.1016/J.DESTUD.2011.07.006
- Dorst, "Frame Creation and Design in the Expanded Field" (She Ji, 2015): https://doaj.org/article/d907199cfb5b4c65b56fd1ede89f8b71
- Dorst & Kokotovic, "Comparing frame creation and TRIZ: from model to methodology" (2014): https://research.tue.nl/en/publications/comparing-frame-creation-and-triz-from-model-to-methodology/

### 3. Problem Structuring Methods

Soft OR / Problem Structuring Methods address situations where the problem itself is contested, ambiguous, or socially constructed. They explicitly surface stakeholder perspectives, boundaries, values, uncertainties, and alternative formulations.

Use for Inquiry Graph:
- problem formulation is itself an inquiry product;
- multiple frames may coexist rather than one frame immediately replacing another;
- frame scope and stakeholder-relative perspective can matter.

This aligns with the repository's earlier problem-recognition pressure test.

### 4. C-K theory

C-K theory separates a **Concept space** from a **Knowledge space** and models design as co-expansion of both. It explicitly provides generative mechanisms for exploring possibilities that are not yet established knowledge.

Use for Inquiry Graph / Epistemic Warrant:
- proactive inquiry does not have to wait for failure;
- new concepts can activate new knowledge search, and new knowledge can expand the concept space;
- this is a mature precedent for coupling creative generation with knowledge acquisition.

Representative sources:
- C-K Theory overview: https://www.ck-theory.org/c-k-theory/?lang=en
- overview article/reference entry: https://en.wikipedia.org/wiki/C-K_theory

### 5. Literature-based discovery / undiscovered public knowledge

Swanson's literature-based discovery (LBD) is especially relevant to the user's reuse-first stance. LBD treats published knowledge as potentially **public but not locally connected**. A useful discovery may come from linking literatures that do not cite or share vocabulary with one another.

Open discovery starts from one concept and searches for previously unrecognized connected concepts; closed discovery starts with two concepts and searches for bridging mechanisms.

Use for the current methodology:
- "unknown unknowns" often mean **unconnected existing knowledge**, not genuinely new knowledge;
- proactive frame/question exploration can be driven by cross-literature bridging;
- apparent novelty should increase terminology translation and cross-domain search pressure.

Representative sources:
- Swanson/LBD retrospective: https://pmc.ncbi.nlm.nih.gov/articles/PMC5771422/
- LBD overview volume: https://link.springer.com/book/10.1007/978-3-540-68690-3
- open vs closed LBD: https://pmc.ncbi.nlm.nih.gov/articles/PMC7228051/

### 6. Transformational creativity / generative-system change

The Epistemic Warrant repository already adopted the distinction between:
- exploring a fixed generative regime; and
- transforming the regime itself.

Frame shifts are now best understood as one important **species** of generative-system transformation: changing representation, assumptions, boundaries, evaluators, or salient variables changes which candidates/questions become reachable.

Use:
- do not invent universal frame operators;
- represent frame shifts through the existing transformation interface when possible.

### 7. Metareasoning / value of computation

Metareasoning provides the control layer for deciding whether further inquiry effort is worth the cost. This is important because proactive question/frame generation can explode combinatorially.

Use:
- exploit current frame when expected value is high;
- repair/reframe when evidence indicates mismatch;
- proactively explore alternate frames/questions when expected information or option value justifies the cost.

This remains an optional control/evaluation layer; it should not define what a frame is.

## Cross-field synthesis

The mature landscape supports three distinct inquiry modes:

```text
EXPLOIT
reason within the current frame

REPAIR
change frame because evidence/surprise/failure makes the current frame inadequate

EXPLORE
generate alternative frames/questions even without an observed failure
```

The third mode is the missing upstream capability highlighted by the current conversation.

A practical reuse-first loop is:

```text
current situation + current frame
        |
        +--> within-frame reasoning / candidate generation
        |
        +--> proactive frame/question exploration
                |
                +--> frame-creation methods
                +--> concept-space expansion (C-K)
                +--> literature-based discovery
                +--> analogy / problem-structuring methods
        |
        v
candidate frames/questions
        |
        v
evaluate relevance, evidence, cost, option value
        |
        v
adopt / combine / suspend / reject
        |
        v
reason under selected frame(s)
```

## What not to invent

Current evidence argues against introducing:
- a universal `FrameShiftOperator` taxonomy;
- a universal "unknown unknown detector";
- one scalar frame-quality score;
- a new generic creativity engine.

Existing fields already own most of the semantics.

## Inquiry Graph implication

The strongest remaining representational seam is narrow:

> Can Inquiry Graph represent **frame content + frame scope + framing/reframing acts + frame-relative questions/candidates** without expensive reconstruction?

A profile/view should be tested before a core schema change.

The new landscape also suggests a useful derived query family:

- Which frame was active?
- Which questions/candidates became salient under it?
- Which frame-creation method produced an alternative?
- Which evidence or values supported/defeated the frame?
- Which knowledge search was triggered by the new frame?
- Which frame shift changed the candidate space materially?

## Next empirical test

Use one real inquiry and run two concurrent lanes:

1. **reuse/discovery lane** — prior art, alternate terminology, adjacent fields, LBD-style bridge search;
2. **frame/question lane** — generate alternate formulations, assumptions, boundaries, perspectives, and questions.

Then compare against a sequential baseline on:
- mature prior art found;
- residual invention gap;
- distinct useful frames/questions generated;
- time/compute;
- downstream decision quality.

The test should evaluate usefulness, not novelty.
