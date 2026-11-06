---
description: Inquiry Graph architecture in arc42 sections, pointing to the spec, diagram and decision that own each fact
---

# Inquiry Graph architecture

Sections follow [arc42](https://arc42.org). A section whose content another document owns points there.

## 1. Introduction and goals

[Goal and thesis](GOAL.md): turn conversation exports into a graph of what each person said, asked and
revised, grounded in exact quotes, so agents can recover Brian's positions across many chats.

## 2. Constraints

Local files and a small Python toolkit, no database server
([ADR-003](../decisions/003-json-and-libraries.md)); every extracted record is proposed until reviewed
([ADR-004](../decisions/004-grounding-and-review.md)).

## 3. Context and scope

Inputs: chat exports (ChatGPT, Claude, chatgpt-bridge, Kept Markdown), meeting transcripts, and Claude
Code or Codex session records. Outputs: canonical graph JSON, Markdown, Mermaid and DOT views, and
answers about Brian's positions. Detail: [architecture prose](../model/ARCHITECTURE.md).

## 4. Solution strategy

Behavior is planned as [OpenSpec specs](../index.md); each requirement names its owning module by an
`Implements:` line and each scenario its test by `@pytest.mark.req`. `code2check trace` checks both.

## 5. Building block view

The modules and which may import which: [model.c4](model.c4). `code2check arch gen` turns it into
`.importlinter`, which `lint-imports` enforces. Scripts under `tools/` are not a package and are not
drawn.

## 6. Runtime view

[Architecture prose](../model/ARCHITECTURE.md), runtime section.

## 7. Deployment view

Not separate: a Python package installed with `uv` into a local environment.

## 8. Crosscutting concepts

[Ontology](../ontology.md): nodes, relations, moves and events.

## 9. Architecture decisions

[Decision records](../decisions/index.md).

## 10. Quality requirements

Owned by the OpenSpec specs, listed in [the documentation index](../index.md).

## 11. Risks and technical debt

- Module docstrings are not checked for argument documentation (pydoclint, interrogate); the existing
  code predates that rule.
- [docs/requirements.md](../requirements.md) and [docs/model/trace.yaml](../model/trace.yaml) overlap
  the specs and `Implements:` lines; they are kept, not maintained.

## 12. Glossary

[Ontology](../ontology.md).
