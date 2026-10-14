---
description: Start page for Inquiry Graph; routes to the goal, requirements, system model, decisions and current status
---

# Inquiry Graph wiki

Inquiry Graph turns conversation exports into a source-grounded graph of content,
questions, relations, moves and actor-relative stance, so agents can recover what Brian
has said, asked and revised across many chats ([README](../README.md)).

## What it is for and how it works

- [Goal and thesis](../docs/architecture/GOAL.md): north star, the bet, what would disprove it, lineage.
- [Requirements](../docs/requirements.md): REQ-01 to REQ-15, each with success and disproof lines.
- [Architecture](../docs/model/ARCHITECTURE.md): context, building blocks, runtime with file:line, quality checks.
- [Checked trace](../docs/model/trace.yaml): each rule's owner file, tests and decision.
- [Decisions](../docs/decisions/index.md): ADR-001 to ADR-006.
- [Ontology](../docs/ontology.md): the vocabulary of nodes, relations, moves and events.

## What is in progress

- [Project status](../docs/project-status.md): current state and evidence.
- [Roadmap](../docs/roadmap.md): what comes next and why.
- [Goals](../docs/goals/positions-as-shared-memory.md): positions as shared memory for agents.
- [Plan: report reasons as text](../docs/plans/report-relations-rescore.md) and its [goal](../docs/plans/report-relations-rescore.goal.md): render relations with node text and re-score the usefulness pilot.
- [Plan: coding-agent sessions](../docs/plans/coding-sessions.md) and its [goal](../docs/plans/coding-sessions.goal.md): `import-session` and `sessions` turn Claude Code and Codex session records into resumable graphs (REQ-16).
- [Plan: session launch kind](../docs/plans/session-launch-kind.md) and its [goal](../docs/plans/session-launch-kind.goal.md): prompts from headless runs are labelled automated, and `tools/brian_positions.py --sessions` searches what Brian typed in coding sessions. `tools/position_topics.py --sessions` puts those prompts on the same topic map as his chats (topics are clustered after the fact, not stored on each session). The map nests topics at several levels (EVoC clustering, three in the 2026-10-13 build) with model-written names, places points the clusterer left out under their nearest topic, opens a side panel with the quote and the rest of its conversation when a point is clicked, and filters by source, app, kind of statement and date; it is registered as `private-positions-map` in `ui/registry.yaml` and rebuilt nightly by `tools/nightly_sessions.py`.
- [New agent handoff](../docs/new-agent-handoff.md): how to pick up the work.
