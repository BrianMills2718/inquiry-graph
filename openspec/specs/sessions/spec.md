# sessions Specification

## Purpose

Turn Claude Code and Codex session records into graphs that let agents remind Brian what was being worked on and pick up unfinished work.

## Requirements

### Requirement: Session graphs keep only grounded session fields

The system SHALL ensure: A coding-session graph keeps only Brian's typed text, per-turn assistant text and work lines from tool records; prompts in a headless launch (Claude Code entrypoint sdk-*, Codex codex_exec/codex_sdk_ts, Codex subagents) are attributed to an automated participant, never to Brian, so search over his session words skips them; a task's status is the fixed closure word an agent wrote, an item absent from the last listing without one is reported as unknown, never open, and a request counts as answered only as a proposed event at Brian's next message (REQ-16).

Source: Brian, 2026-10-13: "i want somethign similar for my coding agent sessions"; "largely theis is a way to help agents remind me of what we ahve been working on, and to pick up unifshed worka, and to have agents more easily find stuff i am lookign for"

#### Scenario: Claude records keep typed text, turns and work

- **WHEN** a Claude Code session record with injected hook text
- **THEN** only Brian's typed text, per-turn assistant text and work lines are kept

#### Scenario: Reply fields give tasks, closures and requests

- **WHEN** assistant replies ending with the closeout fields
- **THEN** tasks, closures and requests become nodes anchored verbatim

#### Scenario: A dropped item is unknown, not open

- **WHEN** an item missing from the last listing with no closure word
- **THEN** it is reported with status unknown

#### Scenario: Codex records are imported

- **WHEN** a Codex session record
- **THEN** it becomes a Conversation and a validated graph

#### Scenario: Headless prompts are not Brian's

- **WHEN** a session launched headless (sdk or exec entrypoint)
- **THEN** its prompts are attributed to an automated participant

#### Scenario: Position search reads only Brian's typed prompts

- **WHEN** sessions with typed and automated prompts
- **THEN** position search returns only what Brian typed
