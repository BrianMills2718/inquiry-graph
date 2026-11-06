# import Specification

## Purpose

Turn a ChatGPT export or chat transcript into a normalized Conversation that keeps only the visible text people actually saw.

## Requirements

### Requirement: Import keeps only the visible active branch

The system SHALL ensure: A ChatGPT export imports only the current_node ancestor branch and only visible user/assistant text; hidden, tool and non-text parts are skipped and counted (REQ-01).

Source: inferred by agent (carried over from docs/requirements.md REQ-01 and docs/model/trace.yaml RULE-ACTIVE-BRANCH; not traced to Brian's words)

#### Scenario: Only the current branch is imported

- **WHEN** an export with an edited message, so two branches exist
- **THEN** only messages on the current_node ancestor branch are imported

#### Scenario: Hidden messages are skipped

- **WHEN** an export containing hidden system or tool messages
- **THEN** they are skipped and counted, not imported

#### Scenario: Non-text parts are skipped

- **WHEN** an export containing analysis or non-text content parts
- **THEN** no text is imported from them
