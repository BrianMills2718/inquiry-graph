---
description: What Inquiry Graph is for, the bet behind it, what would disprove it, and where the goal was drawn from
---

# Inquiry Graph: goal and thesis

## Introduction and Goals

Inquiry Graph turns visible conversation text (ChatGPT, Claude and Gemini exports,
chatgpt-bridge transcripts, meeting transcripts) into a typed, source-grounded graph of
content, questions, relations, inquiry moves, and actor-relative stance and
question-status histories. Every semantic record quotes the exact source text it came
from, so an AI reader can recover who said what, which question is still open, and how
a position changed, across more conversations than fit in one model context.

### Requirements Overview

The requirements, each with a success line and a disproof line, are in
[docs/requirements.md](../requirements.md): source preservation and exact Unicode
anchors (REQ-01, REQ-02), reified relations and moves (REQ-03), actor stance kept apart
from content and question status (REQ-04), validation beyond JSON shape (REQ-06),
offline operation and quarantine of bad extraction output (REQ-07 to REQ-09), exact
merge (REQ-10), and verbatim-checked cross-chat positions (REQ-15). The rules that
enforce them, with owner files and tests, are in the system model
([ARCHITECTURE.md](../model/ARCHITECTURE.md), [trace.yaml](../model/trace.yaml)).

### Quality Goals

- Grounded or absent: a record whose quote does not match its source message at the
  stated Unicode offsets is a validation error, never a stored fact
  ([ADR-004](../decisions/004-grounding-and-review.md)).
- Content is not belief: a claim's existence never implies any participant accepted
  it, and an assistant answer never closes a user's question
  ([ADR-002](../decisions/002-state-and-attribution.md)).
- Bad output never replaces good data: canonical writes are exclusive by default and
  failed extractions go to a private quarantine file
  ([ADR-006](../decisions/006-extraction-adapter.md)).
- Off-the-shelf and local: Pydantic, NetworkX, argparse and canonical JSON in Git; no
  graph database or service ([ADR-003](../decisions/003-json-and-libraries.md)).

### Stakeholders

- AI agents are the reader (Brian, 2026-09-29, recorded in
  [project-status.md](../project-status.md)): agents ask what Brian has already said
  about a topic through `tools/ask_positions.py` and the shared `brian-positions` skill
  ([goal: positions as shared memory](../goals/positions-as-shared-memory.md)).
- Brian, whose conversations are the source material and who owns the repository.
- onto-canon6, the downstream consumer that owns cross-source identity, alignment and
  conflict detection; Inquiry Graph is its per-conversation producer
  ([roadmap.md](../roadmap.md), "Downstream integration").

## North star (AES extension)

Any agent can ask what Brian has said, asked and changed his mind about on a topic,
across all his conversations, and get back only quotes that are verbatim in the named
source message, attributed to the speaker who said them, with open questions and
revisions kept visible rather than flattened into a summary.

## Thesis (AES extension)

The distinct value of a conversation graph is attribution and history, not retrieval:
for a single conversation the raw transcript beats the graph, and for general
answer-retrieval archive search then read is the default (the 30-chat result in
[roadmap.md](../roadmap.md)). What a graph adds is checkable structure no model keeps
across hundreds of chats: who holds which position, which questions are open, and what
was challenged or retracted. That only holds if every record stays tied to the text
that owns it: quotes are checked against the source message at write time and again
at read time, never copied into a summary that can drift (AES-CTX-004, truth lives
where it is edited).

## Thesis disproof (AES extension)

An agent answering "what has Brian said about X" from the graph gives wrong
attributions or misses positions more often than an agent searching and reading the
raw archive for the same question; or a quote the answer path reports as verified is
not verbatim in its cited message; or no consumer outside this repository uses the
positions for a decision (the condition the
[positions-as-shared-memory goal](../goals/positions-as-shared-memory.md) exists to
test).

## Non-goals

- No automatic harvesting of all chats, and no access to hidden chain of thought or
  private mental states ([requirements.md](../requirements.md), "Non-goals").
- No cross-source identity store or conflict detector: that belongs to onto-canon6.
- No graph database, vector search service, multi-user system or polished web canvas.
- No formal theory of support, defeat or warrant: that moved to `epistemic-warrant`
  on 2026-09-29.

## Lineage (AES extension)

none -- original. The repository was bootstrapped on 2026-09-27 (root commit
`fac835d`, "bootstrap private inquiry graph"); it replaced no earlier repository. On
2026-09-29 its formal theory and paper draft were split out into
`BrianMills2718/epistemic-warrant` with full history (README). This page was drawn
from [README.md](../../README.md), [project-status.md](../project-status.md),
[requirements.md](../requirements.md), [roadmap.md](../roadmap.md) and
[positions-as-shared-memory.md](../goals/positions-as-shared-memory.md).
