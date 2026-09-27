# Requirements and V1 acceptance

## Goal and scope

Create a local-first, inspectable representation of ongoing inquiry from source conversations. A user can recover why a question appeared, which assumption it depends on, how it was challenged, and whether any participant actually accepted its resolution. Deliver one coherent instantiation of the founding conversation before attempting a universal personal-memory system.

## Requirements-to-evidence matrix

| ID | Requirement | Acceptance evidence |
|---|---|---|
| R1 | Preserve visible source and distinguish curated excerpts from a full export | `source-excerpts.json` coverage note; `test_active_branch_import`; `test_no_analysis_or_nontext_extraction` |
| R2 | Enforce exact Unicode source anchors | `test_unicode_anchor`; parameterized offset/quote/source negative cases |
| R3 | Reify relations and multi-input/output reasoning moves | role signatures; `test_relation_can_be_challenged`; `test_trace_exposes_retraction` |
| R4 | Keep actor stance separate from content and question status | `test_answer_does_not_close_user_question`; `test_actor_specific_question_status` |
| R5 | Preserve revisions, rejected annotations and unresolved questions | trace history; rejected-event test; 25 seed questions |
| R6 | Validate identity, references, types and allowed chronology beyond JSON shape | negative-invariant suite, supersession-cycle test, dependency-cycle warning test |
| R7 | Work offline using structured candidate files | `test_offline_e2e_and_quarantine` |
| R8 | Provide an optional real SDK adapter with no network requirement for tests | provider protocol/refusal/truncation tests; live provider validation explicitly not performed |
| R9 | Prevent invalid candidate output from replacing canonical data | atomic no-overwrite and quarantine tests |
| R10 | Merge exactly and reproducibly without fuzzy belief merging | idempotent/order-independent union and conflict tests |
| R11 | Export a reasoning diagram, graph interchange and grounded report | Mermaid, DOT, Markdown, offline linked HTML; escaping test |
| R12 | Instantiate the full arc of this discussion, not only its final topic | 72 excerpts, 75 nodes, 79 relations, 62 moves, 21 stance events, 30 question events; walkthrough |
| R13 | Preserve code/data in a private GitHub repository | commits, PR and CI; no secrets or unrelated local changes |
| R14 | Keep documented schemas reproducible | schema roundtrip test and generated-artifact drift check |

## Core user journeys

**Resume inquiry.** Open the agenda, find a foundational question, inspect its source, then follow related reasoning moves and dependencies. V1 does not rank the agenda as an optimum.

**Audit a belief attribution.** Trace a claim and see who posited, questioned or retracted it. An assistant-authored quote cannot serve as an actor occurrence attributed to the user.

**Add an exported conversation.** Normalize the active branch, prepare a schema-constrained extraction, validate candidates, and merge the resulting graph. Ambiguous identities remain separate rather than being guessed.

**Review a candidate annotation.** Compare it with exact source text, edit proposed/confirmed/rejected metadata in a review commit, validate, and preserve the preceding commit. New substantive positions get new IDs and events rather than overwriting old claims.

## Non-goals

No automatic harvesting of all chats; no access to hidden chain of thought or private mental states; no general theory proving how to think; no proof that the trichotomy is exhaustive; no autonomous persuasion or inferred psychological profiling; no trained reasoning policy; no full-text/vector search service; no graph database deployment; no multi-user authorization system; no automatic semantic identity reconciliation; no polished web canvas or mobile app.

## Acceptance definition

V1 is complete when the code installs, offline tests and example commands pass, generated artifacts agree with the executable schema, the graph has zero structural errors, the source and semantic limitations are visible, and all implementation/documentation is committed to GitHub. A live provider call and the eventual full-transcript re-extraction are separate validations, not silently implied by the offline fixture passing.
