# ADR-004: Exact grounding and a review boundary

**Status:** accepted for V1.

**Context.** Well-formed JSON can contain invented citations, wrong source offsets, false endorsements and plausible but unsupported logical relations.

**Decision.** Require nonempty exact source anchors for every semantic record. Validate Unicode offsets, references, actors, roles and allowed chronology. LLM ingestion always resets review metadata to proposed. Store rejected interpretations rather than erasing their audit trail; keep bad extraction output out of canonical storage.

**Alternatives.** Trusting the model's confidence or structured-output success does not check semantic fidelity. Automatically repairing missing quotes by approximate matching can attach a claim to the wrong passage.

**Consequences.** Some useful but weakly grounded candidates are rejected. This is preferable to pretending they are source facts. Review is still necessary: exact quotation alone does not prove a paraphrase or relation correct. Source excerpts remain explicitly incomplete until reconciled with an export.
