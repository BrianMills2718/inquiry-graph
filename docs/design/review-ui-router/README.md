# Review UI: representation-router evidence (2026-10-05)

Router inputs and outputs for the confirm / correct / withdraw interface for Brian's positions (two modes: by topic, and a needs-attention stream).
- `uc2-*.json` use cases, `rec2-*.json` recommendations with page plans (master-detail list with a detail card for both modes), `rec3-topic.json` comparison run. `uc-*.json`/`uc-stream`/`rec-stream` are first runs; the first run returned no representation because the brief asked for undo and 20,000 on-screen items, which the catalog does not offer.
- Known router gaps found: no undo vocabulary, no one-at-a-time queue option, planned a 1440 px page despite the mobile flag.
- Design decisions: shared claim card in both modes, labels worded as questions ("Changed over time?") with dashed grey outline until confirmed, solid blue outline plus the word "Confirmed" after, time strip of quote dates, orange "why you are seeing this" line, no red/green. Stream ranking starts with: one quote or one day only; labelled change or pulls-against-itself; authorship "unclear".
- Open for Brian (defaults): Correct rewrites line and label, quotes untouched; one Withdraw with optional reason; a confirmation does not expire but a disagreeing newer quote returns the claim to the stream; "confirm all" does not confirm the topic summary.
- Save path for decisions is an open architecture question (gated endpoint appending JSONL; browser-only with export; endpoint that commits to git).
