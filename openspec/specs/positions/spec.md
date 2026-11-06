# positions Specification

## Purpose

Answer a cross-chat question from Brian's own attributed positions, citing only quotes he actually wrote.

## Requirements

### Requirement: Position records are verbatim and Brian's

The system SHALL ensure: A position record is kept only when its event's actor is Brian, the anchored message's speaker is Brian, and the quote is verbatim in that message (REQ-15).

Source: inferred by agent (carried over from docs/requirements.md REQ-15 and docs/model/trace.yaml RULE-VERBATIM-POSITIONS; not traced to Brian's words)

#### Scenario: A verbatim Brian event is kept

- **WHEN** a stance event by Brian whose quote is in his message
- **THEN** it becomes a position record

#### Scenario: A non-verbatim quote is dropped

- **WHEN** an event whose quote is not in the message
- **THEN** it is dropped

#### Scenario: Another actor's event is dropped

- **WHEN** an event whose actor is not Brian
- **THEN** it is dropped
