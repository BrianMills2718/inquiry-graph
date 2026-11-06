# storage Specification

## Purpose

Write, merge and describe canonical graph files so no write half-finishes, no merge loses a record, and the published schemas match the model.

## Requirements

### Requirement: Writes are atomic and exclusive

The system SHALL ensure: Canonical JSON is written to a temporary file, fsynced, then linked into place exclusively; an existing file is replaced only with --force (REQ-09).

Source: inferred by agent (carried over from docs/requirements.md REQ-09 and docs/model/trace.yaml RULE-EXCLUSIVE-WRITE; not traced to Brian's words)

#### Scenario: Existing files are not replaced without force

- **WHEN** an output path that already exists
- **THEN** the write refuses unless --force is given, and a write never leaves a partial file

### Requirement: Merge is an exact union by id

The system SHALL ensure: Merge is an idempotent, order-independent union by id; two different records with one id raise an identity conflict instead of being merged (REQ-10).

Source: inferred by agent (carried over from docs/requirements.md REQ-10 and docs/model/trace.yaml RULE-EXACT-MERGE; not traced to Brian's words)

#### Scenario: Merge is idempotent and order-independent

- **WHEN** the same graphs merged twice or in another order
- **THEN** the result is identical

#### Scenario: Conflicting ids raise

- **WHEN** two different records sharing one id
- **THEN** merge raises an identity conflict

### Requirement: Schemas come from the model

The system SHALL ensure: The JSON schemas in schemas/ are generated from the Pydantic model and must round-trip (REQ-14).

Source: inferred by agent (carried over from docs/requirements.md REQ-14 and docs/model/trace.yaml RULE-SCHEMA-REPRODUCIBLE; not traced to Brian's words)

#### Scenario: Schemas round-trip

- **WHEN** the JSON schemas regenerated from the Pydantic model
- **THEN** they match the committed schemas and round-trip
