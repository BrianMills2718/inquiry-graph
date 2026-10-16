# extraction Specification

## Purpose

Turn a Conversation into a validated graph from a model's candidates, without letting the model invent quotes, confirm its own output, or overwrite sources.

## Requirements

### Requirement: Extraction cannot claim confirmation

The system SHALL ensure: Ingestion sets every candidate's review_status to proposed; an extraction cannot claim confirmation (REQ-08).

Source: inferred by agent (carried over from docs/requirements.md REQ-08 and docs/model/trace.yaml RULE-REVIEW-RESET; not traced to Brian's words)

#### Scenario: Model-confirmed status is reset

- **WHEN** candidates whose review_status says confirmed
- **THEN** every ingested record is proposed

### Requirement: Live output is grounded in the source

The system SHALL ensure: Live model output returns quotes, not offsets; each quote is located in the source and anchored to the exact text, wrong-speaker and ungroundable items are dropped and counted, and the graph is pruned until valid (REQ-08).

Source: inferred by agent (carried over from docs/requirements.md REQ-08 and docs/model/trace.yaml RULE-LIVE-GROUNDING; not traced to Brian's words)

#### Scenario: Quotes are located and speakers enforced

- **WHEN** live model output giving quotes, one attributed to the wrong speaker
- **THEN** found quotes are anchored to exact offsets and the wrong-speaker item is dropped and counted

#### Scenario: Invalid items are pruned and counted

- **WHEN** a converted graph with items that fail validation
- **THEN** they are removed until the graph validates, and counted

#### Scenario: Supersession cycles are broken

- **WHEN** a converted graph whose supersession links form a cycle
- **THEN** pruning breaks the cycle

### Requirement: Failed extractions are quarantined

The system SHALL ensure: Any extraction failure (parse, grounding, validation or transport) writes a private quarantine file and raises; no partial graph is written to the output path (REQ-07, REQ-09).

Source: inferred by agent (carried over from docs/requirements.md REQ-07, REQ-09 and docs/model/trace.yaml RULE-QUARANTINE; not traced to Brian's words)

#### Scenario: A bad response is quarantined

- **WHEN** an extraction response that fails validation
- **THEN** a private quarantine file is written, the command fails, and no graph is written to the output path

#### Scenario: A transport error is quarantined

- **WHEN** a live call that fails in transport
- **THEN** the failure is quarantined and no partial graph is written

### Requirement: Sources are never overwritten

The system SHALL ensure: An output path may never be an input or source snapshot, even with --force (REQ-09).

Source: inferred by agent (carried over from docs/requirements.md REQ-09 and docs/model/trace.yaml RULE-SOURCE-NOT-OVERWRITTEN; not traced to Brian's words)

#### Scenario: Force cannot overwrite a source

- **WHEN** an output path equal to an input or source snapshot, with --force
- **THEN** the command refuses
