---
description: Decision to use schema-constrained extraction behind a deterministic offline validation and quarantine boundary
---

# ADR-006: Structured output with a deterministic offline boundary

**Status:** accepted for V1.

Source: inferred by agent (design record written during the V1 build; not traced to Brian's words)

Governs: RULE-LIVE-GROUNDING, RULE-QUARANTINE, RULE-SOURCE-NOT-OVERWRITTEN, RULE-EXCLUSIVE-WRITE

**Context.** The extraction is primarily a schema-constrained LLM task. LangExtract supplies valuable grounded extraction machinery, but global relation-role consistency, actor stance, revisions and question-state projection still need a project-specific contract.

**Decision.** Use a thin optional official SDK adapter producing Pydantic Candidates, plus a provider-independent response-file path. Both feed the same source-injection and semantic-validation boundary. No automatic tool-using agent, unbounded retry loop or mandatory paid call.

**Alternatives.** A LangExtract-first pipeline would be useful for large-document mention extraction and grounding, but adds a second intermediate representation here. A future adapter can accept grounded mentions while preserving—not bypassing—the graph validator. No LangExtract adapter is claimed in V1.

**Consequences.** The seed and tests work without credentials or network. The live adapter is implemented but only protocol-tested. One conversation per call is the current unit; long-conversation chunk reconciliation is deferred. Model selection remains explicit, and provider refusal/truncation is a failed extraction, not a partial graph silently accepted.
