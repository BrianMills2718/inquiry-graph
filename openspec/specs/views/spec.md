# views Specification

## Purpose

Answer what is still open, for whom, from a validated graph.

## Requirements

### Requirement: Open questions are scoped per actor

The system SHALL ensure: The open-question agenda is scoped per actor and context; an assistant answer or another actor's resolution does not close a user's question, and rejected events are not applied (REQ-04, REQ-05).

Source: inferred by agent (carried over from docs/requirements.md REQ-04, REQ-05 and docs/model/trace.yaml RULE-STANCE-SEPARATE; not traced to Brian's words)

#### Scenario: An assistant answer does not close a user's question

- **WHEN** a user question followed by an assistant answer
- **THEN** the question stays open for the user

#### Scenario: Question status is per actor

- **WHEN** two actors with different stances on one question
- **THEN** each actor's agenda shows its own status

#### Scenario: A resolution closes only its scope

- **WHEN** a confirmed resolution in one context
- **THEN** the question closes only for that actor and context

#### Scenario: Rejected events are not applied

- **WHEN** an event whose review status is rejected
- **THEN** it does not change the agenda
