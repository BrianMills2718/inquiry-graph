# validation Specification

## Purpose

Refuse any graph whose quotes do not match their source text exactly or whose relations break their kind's role rules.

## Requirements

### Requirement: Anchors match the source exactly

The system SHALL ensure: Every semantic record's anchor quote equals the source message text at its Unicode offsets, and every event is anchored at its occurrence by its speaker; otherwise validation errors (REQ-02, REQ-06).

Source: inferred by agent (carried over from docs/requirements.md REQ-02, REQ-06 and docs/model/trace.yaml RULE-EXACT-ANCHOR; not traced to Brian's words)

#### Scenario: Unicode offsets anchor exactly

- **WHEN** a quote containing non-ASCII characters anchored by Unicode offsets
- **THEN** the graph validates

#### Scenario: Wrong offsets, quotes or sources fail

- **WHEN** a graph whose anchor offsets, quote or source message are wrong
- **THEN** validation reports an error such as anchor_mismatch

### Requirement: Relations obey their role signature

The system SHALL ensure: Relations are id-bearing records whose role bindings obey the kind's signature (cardinality and target type); a relation may itself be targeted (REQ-03).

Source: inferred by agent (carried over from docs/requirements.md REQ-03 and docs/model/trace.yaml RULE-ROLE-SIGNATURE; not traced to Brian's words)

#### Scenario: A relation can be challenged

- **WHEN** a relation that targets another relation
- **THEN** the graph validates

#### Scenario: Broken role bindings fail

- **WHEN** a relation whose role bindings break its kind's cardinality or target type
- **THEN** validation reports an error
