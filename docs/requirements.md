---
description: Inquiry Graph requirements, each with a success check and a disproof condition, plus core journeys and non-goals
---

# Requirements and V1 acceptance

## Goal and scope

Create a local-first, inspectable representation of ongoing inquiry from source conversations. A user can recover why a question appeared, which assumption it depends on, how it was challenged, and whether any participant actually accepted its resolution. Deliver one coherent instantiation of the founding conversation before attempting a universal personal-memory system.

## Requirements

Each requirement keeps its V1 number in brackets (the earlier R1 to R14 table). Tests
named below are in `tests/`; the rules that enforce them are in
[docs/model/trace.yaml](model/trace.yaml).

## REQ-01 Preserve visible source; distinguish curated excerpts from a full export [R1]

Success: `test_active_branch_import`, `test_no_analysis_or_nontext_extraction` and `test_hidden_export_messages_are_skipped` pass; `source-excerpts.json` carries its coverage note.
Disproof: an import keeps a message from an inactive branch, a hidden or tool message, or non-text content.

## REQ-02 Enforce exact Unicode source anchors [R2]

Success: `test_unicode_anchor` and the parameterized offset, quote and source cases of `test_negative_invariants` pass.
Disproof: a graph whose anchor quote differs from the source text at its stated offsets validates without an `anchor_mismatch` error.

## REQ-03 Reify relations and multi-input/output reasoning moves [R3]

Success: role signatures are enforced; `test_relation_can_be_challenged` and `test_trace_exposes_retraction` pass.
Disproof: a relation cannot be the target of another relation, or a retraction is missing from a claim's trace.

## REQ-04 Keep actor stance separate from content and question status [R4]

Success: `test_answer_does_not_close_user_question`, `test_actor_specific_question_status` and `test_confirmed_resolution_closes_only_its_scope` pass.
Disproof: an assistant answer, or one actor's resolution, removes another actor's question from the open agenda.

## REQ-05 Preserve revisions, rejected annotations and unresolved questions [R5]

Success: `test_rejected_event_not_applied` passes and `inquiry-graph query examples/seed/graph.json open` lists the seed's unresolved questions.
Disproof: a rejected event changes a projected status, or a revision overwrites the earlier record instead of adding one.

## REQ-06 Validate identity, references, types and allowed chronology beyond JSON shape [R6]

Success: `test_negative_invariants`, `test_supersession_cycle` and `test_dependency_cycle_is_warning` pass.
Disproof: a graph with a duplicate id, dangling reference, wrong role type or supersession cycle validates as error-free.

## REQ-07 Work offline from structured candidate files [R7]

Success: `test_offline_e2e_and_quarantine` passes with no network and no API key.
Disproof: `prepare`, `extract --response-file`, `validate`, `merge`, `query` or `render` needs a network call or a credential.

## REQ-08 Optional live extractor with no network requirement for tests [R8]

Success: `extract --llm` goes through Brian's shared `llm_client` with one trace id per chunk; `test_live_convert_grounds_quotes_and_enforces_speaker`, `test_live_prune_removes_invalid_and_counts` and `test_transport_error_quarantined` pass offline.
Disproof: the test suite makes a provider call, or an ungrounded or wrong-speaker item from the model survives into the graph.

## REQ-09 Invalid candidate output never replaces canonical data [R9]

Success: `test_atomic_no_overwrite`, `test_source_cannot_be_overwritten_even_with_force` and `test_offline_e2e_and_quarantine` pass.
Disproof: a failed extraction leaves a partial graph at the output path, or overwrites an existing file without `--force`.

## REQ-10 Merge exactly and reproducibly, without fuzzy belief merging [R10]

Success: `test_union_idempotent_and_order_independent` and `test_union_conflict` pass.
Disproof: merging the same graphs in a different order gives a different result, or two different records with one id merge without an `identity conflict` error.

## REQ-11 Export a reasoning diagram, graph interchange and grounded report [R11]

Success: `render` writes Mermaid, DOT, Markdown and offline HTML; `test_render_escapes_untrusted_content` and `test_render_deterministic_across_hash_seeds` pass.
Disproof: source text appears unescaped in rendered HTML or Mermaid, or two renders of one graph differ.

## REQ-12 Instantiate the full arc of the founding discussion, not only its final topic [R12]

Success: `inquiry-graph validate examples/seed/graph.json` reports zero errors and `query ... stats` reports 247 source excerpts, 250 nodes, 250 relations, 204 moves, 68 stance events and 86 question events (the extended seed; V1 accepted it at 72 excerpts and 75 nodes); `python tools/build_artifacts.py --check` reports no drift.
Disproof: the seed graph fails validation, or its generated artifacts drift from `examples/build_seed.py` output.

## REQ-13 Keep code and data in a private GitHub repository [R13]

Success: work lands as commits and pull requests on the private `BrianMills2718/inquiry-graph`, and `.githooks/pre-commit` runs the tests, the artifact drift check and seed validation before each commit.
Disproof: the repository is public, or a secret or unreviewed conversation export is committed.

## REQ-14 Keep documented schemas reproducible [R14]

Success: `test_schema_roundtrip` passes and `python tools/build_artifacts.py --check` exits 0.
Disproof: a schema in `schemas/` differs from the one the Pydantic model generates.

## REQ-15 Cross-chat positions cite only verbatim, speaker-attributed quotes

Success: `tools/ask_positions.py` keeps only stance and question events whose actor is Brian and whose quote is verbatim in that message; `test_keeps_verbatim_brian_event`, `test_drops_non_verbatim_quote` and `test_drops_event_whose_actor_is_not_brian` pass.
Disproof: an answer cites a record whose quote is not in its source message, or attributes an assistant's words to Brian.

## Core user journeys

**Resume inquiry.** Open the agenda, find a foundational question, inspect its source, then follow related reasoning moves and dependencies. V1 does not rank the agenda as an optimum.

**Audit a belief attribution.** Trace a claim and see who posited, questioned or retracted it. An assistant-authored quote cannot serve as an actor occurrence attributed to the user.

**Add an exported conversation.** Normalize the active branch, prepare a schema-constrained extraction, validate candidates, and merge the resulting graph. Ambiguous identities remain separate rather than being guessed.

**Review a candidate annotation.** Compare it with exact source text, edit proposed/confirmed/rejected metadata in a review commit, validate, and preserve the preceding commit. New substantive positions get new IDs and events rather than overwriting old claims.

## Non-goals

No automatic harvesting of all chats; no access to hidden chain of thought or private mental states; no general theory proving how to think; no proof that the trichotomy is exhaustive; no autonomous persuasion or inferred psychological profiling; no trained reasoning policy; no full-text/vector search service; no graph database deployment; no multi-user authorization system; no automatic semantic identity reconciliation; no polished web canvas or mobile app.

## Acceptance definition

V1 is complete when the code installs, offline tests and example commands pass, generated artifacts agree with the executable schema, the graph has zero structural errors, the source and semantic limitations are visible, and all implementation/documentation is committed to GitHub. A live provider call and the eventual full-transcript re-extraction are separate validations, not silently implied by the offline fixture passing.
