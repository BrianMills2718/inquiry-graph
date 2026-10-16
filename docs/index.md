---
description: Reading order for Inquiry Graph's plan, structure, requirements and decisions, then every other record
---

# Inquiry Graph documentation

Inquiry Graph turns conversation exports into a source-grounded graph of what each person said, asked
and revised. This page is the reading order; [the wiki front page](../wiki/index.md) routes to status
and plans.

## Read in this order

1. [Architecture](architecture/arc42.md): goals, constraints and approach, in arc42 sections.
2. [Diagram](architecture/model.c4): the modules of `src/inquiry_graph` and which may import which.
3. Requirements, as OpenSpec specs: [import](specs/import/spec.md), [validation](specs/validation/spec.md),
   [extraction](specs/extraction/spec.md), [storage](specs/storage/spec.md), [views](specs/views/spec.md),
   [positions](specs/positions/spec.md), [sessions](specs/sessions/spec.md).
4. [Decisions](decisions/index.md).

## The loop

1. Write the behavior as an OpenSpec change: `openspec/changes/<name>/` with a proposal, the scenarios
   and tasks.
2. Write a failing test for each scenario, marked `@pytest.mark.req("<capability>/<scenario>")`, and
   commit it.
3. Change structure in `docs/architecture/model.c4`, then `uv run code2check arch gen`.
4. Implement; say `Implements: <capability>/<requirement>` in the owning module's docstring.
5. Archive the change (`openspec archive <name> --yes`), run `make check`, commit.

The 31 tests marked `existing=True` covered behavior that worked before its scenario was written
(conversion to this format, 2026-10-15). New behavior never uses that flag.

## Earlier documents

Kept as written; the specs and diagram above replace them where they overlap.

- [Requirements REQ-01 to REQ-16](requirements.md), now carried by the OpenSpec specs.
- [Architecture prose](model/ARCHITECTURE.md) and its [checked trace](model/trace.yaml), now carried by
  `Implements:` lines and test markers.
- [Goal and thesis](architecture/GOAL.md), [ontology](ontology.md), [formalism](formalism.md),
  [changelog](../CHANGELOG.md), [environment isolation note](bootstrap-note.md).

## Design notes

- [Capture contract](design/capture-contract.md)
- [Frame and question-space landscape](design/frame-question-space-landscape.md)
- [Problem recognition landscape](design/problem-recognition-landscape.md) and its
  [three-case synthesis](design/problem-recognition-three-case-synthesis.md)
- [Brian's reasoning methods, v1](design/reasoning-methods-v1.md)
- [Review UI router evidence](design/review-ui-router/README.md)
- [Semantic spectrum and motifs](design/semantic-spectrum-and-motifs.md)

## Evaluations

- [Parallel frame profile pilot](evaluation/parallel-frame-profile-pilot.md)
- Problem recognition pressure tests: [entrepreneurial](evaluation/problem-recognition-entrepreneurial-pressure-test.md),
  [organizational](evaluation/problem-recognition-organizational-pressure-test.md),
  [technical](evaluation/problem-recognition-technical-pressure-test.md)
- Reasoning episodes: [first operational test](evaluation/reasoning-episode-view.md),
  [real reconstruction](evaluation/reasoning-episode-real-reconstruction.md)
- [Cross-conversation positions results](../evaluation/cross_conversation/results.md)

## Goals

- [Convert to the code2 format](goals/code2-format-conversion.md)
- [Cross-chat position memory](goals/cross-chat-position-memory.md) and its
  [cost and limits report](goals/cross-chat-position-memory-REPORT-2026-10-05.md)
- [Cross-conversation linker](goals/cross-conversation-linker.md)
- [Cross-conversation positions](goals/cross-conversation-positions.md)

## Handoffs

- [2026-09-29 linker scale and viewer](handoffs/2026-09-29-linker-scale-and-viewer.md)
- [2026-10-01 semantic grounding inquiry](handoffs/2026-10-01-semantic-grounding-inquiry.md) and
  [its update](handoffs/2026-10-01-semantic-grounding-current.md)
- [2026-10-02 load-bearing contact gate (superseded)](handoffs/2026-10-02-load-bearing-contact-next-gate.md)
- [2026-10-02 foot-ground contact v2](handoffs/2026-10-02-foot-ground-contact-v2.md) and its
  [2026-10-03 result](handoffs/2026-10-03-foot-ground-contact-v2-result.md)
- [2026-10-04 support vertical slice gate](handoffs/2026-10-04-support-vertical-slice-decision-gate.md)

## Interfaces and examples

- [User interfaces](../ui/README.md) and the [topic map disposition](ui/topic-map/README.md)
- [Seed example, full map](../examples/seed/full-map.md)
- [Semantic grounding conversation](../examples/semantic-grounding-2026-10-01/README.md)
- [Semantic modeling query, 2026-10-06](../examples/conversations/2026-10-05-semantic-modeling/query-2026-10-06.md)
