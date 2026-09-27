# Annotation and review guide

## Decide what is actually present

Treat transcript text as evidence of public utterances. A participant's question is not an endorsement of its presupposition. “Maybe X” is normally a hypothesis/posits event, not an endorses event. An assistant agreeing with the user does not establish truth; a user changing the subject does not establish agreement.

Keep source bytes unchanged. Mark partial quotations as excerpts, and do not invent original turn IDs or timestamps. Source excerpts in this release use local ordinals only. Never annotate hidden model reasoning from an answer; only reconstruct the moves expressed in the visible record.

## Separate the annotation decisions

First identify content objects: what is being asked, proposed, contrasted, or used as an example? Then identify relations: what supports or challenges what? Then identify the move: what action changed the inquiry? Finally record actor stance and question state, where supported.

Every record requires anchors. `origin=explicit` means the relevant relation or stance is directly expressed; `origin=inferred` means the curator reconstructed it. Neither means factually true. All extraction output starts `review_status=proposed`. The seed's node and relation annotations are deliberately conservative; its stance events are marked explicit only as a first-pass claim about expressed acts, still proposed for review.

Use exact quoted spans and compute offsets using `anchor(message, quote, occurrence=...)`. Different excerpts can anchor one content object. Do not take a quotation from an assistant turn and attribute the event to Brian. If an assistant reports someone else's views, represent that report as content; do not manufacture a source occurrence by the absent person.

## Identity and granularity

Create different nodes for different scopes or commitments. “Stable structure is necessary for this inference” and “stable structure is sufficient for this inference” are not paraphrases. “Pattern recognition is cognitively informative” and “pattern recognition is logically ampliative” are not the same proposition.

An identical phrase can also be used with different meanings. Leave near-duplicates separate until reviewed. The `related_to` relation can make a possible connection navigable without asserting identity. Changing a claim's meaning calls for a new node plus a revision/supersession move, not silent text replacement.

## Questions and closure

Use `open` for a question explicitly raised or reasonably reconstructed as unresolved. Use `answered` when a candidate answer has been supplied. Do not mark `resolved` just because an assistant said “yes.” Resolution requires a recorded answer or basis, an actor/context, and review before it disappears from the agenda. Preserve a later `reopened` event.

The V1 agenda can show multiple rows for one question, because an assistant may consider it answered while the user remains unconvinced. That duplication is intentional. Cross-conversation status reconciliation remains manual; chronology is not guessed from similar labels.

## Strategy and reflection annotation

Treat a reusable reasoning strategy as a `method` node and a reconstructed occurrence of that strategy as a grounded `example` node. Use `exemplifies` from the occurrence to the strategy and `about` when an episode explicitly reasons about another reasoning artifact, strategy, episode or meta-model. Do not infer a private control policy merely because several moves look similar; strategy attribution remains proposed unless the source makes it explicit and a reviewer confirms it.

Use `about` only for intentional semantic targeting, not generic topical similarity. `related_to` remains the fallback when the source does not justify a stronger reflective/aboutness claim. Fixed meta-level numbers are not stored; nested meta-level depth can be derived from chains of `about` relations if useful.

## Corrections and review procedure

Review the exact source and neighboring source messages, not just the graph label. Check participant identity, hedge words, scope, relation role, and whether a move is merely temporal or genuinely explanatory. Mark an extraction rejected when it misrepresents the record; keep the source and earlier annotation for audit. Change review metadata in a named Git commit so the reviewer and diff are recorded. V1 has no separate collaborative review application.

Review changes to generated seed records should be made in `examples/seed/curation.json` where applicable and regenerated. The bootstrap seed generator intentionally initializes review states to proposed; production human review operates on the canonical graph snapshot, not by rerunning that generator over a reviewed graph. Treat seed regeneration as fixture construction, not an incremental updater.

## Reconcile with the full export

Import the selected active branch. Match each curated quote to exact export text; duplicate matches require manual choice and shortened or expanded spans. Preserve an explicit mapping from excerpt IDs to original message IDs. Re-anchor without rewriting words. Account for excerpts missing from the selected branch; do not force a match. Only after reconciliation should coverage be upgraded from curated excerpts to verified export coverage. No full-export coverage score is claimed now.
