# Inquiry Graph to epistemic-warrant adapter (hop 2)

`tools/warrant_adapter.py` turns a validated Inquiry Graph into real
`epistemic_warrant` `GroundedDialecticalWarrantRegime` assessments: one per
`claim`/`hypothesis` node, each carrying the source excerpt ids of its anchors.
It uses `epistemic-warrant` unchanged as an external package (roadmap: "depend on
`epistemic-warrant` as an external package and make the integration explicit").

```bash
pip install -e '.[warrant]'          # pinned git dependency, or: pip install -e ../epistemic-warrant
python tools/warrant_adapter.py examples/operational-games-2026-09-30/graph.json \
  --out examples/operational-games-2026-09-30/warrant-judgments.json
REQUIRE_EPISTEMIC_WARRANT=1 python -m pytest tests/test_warrant_adapter.py
```

`epistemic-warrant` is a private repository, so the hosted CI (plain `.[dev]`)
cannot install it; without it the test module is skipped (visible in the skip
count). Set `REQUIRE_EPISTEMIC_WARRANT=1` to make a missing package a failure.

## Result on the committed operational-games graph

62 propositional nodes: **61 accepted, 1 defeated**; **0 licensed**.
The single defeat is `n:vacuity-concern` (source excerpt `ex037`), rebutted by
Brian's hypothesis `n:universal-game-vacuity`. Full per-claim output with
excerpt ids: `examples/operational-games-2026-09-30/warrant-judgments.json`.

"Accepted" here means only "not defeated by any recorded challenge under grounded
semantics". The hop is a plumbing proof, not evidence that claims are true: the
graph holds very few challenges (one usable), and every annotation is `proposed`.

## Who said it (speaker attribution)

A judgment about a node says nothing about whether Brian or the assistant wrote the
words, so each judgment also carries metadata derived from the anchored messages'
`actor_id` (never used in warrant evaluation; status and license results are
unchanged):

* `speakers`: one entry per distinct participant anchored by the node, with
  `participant_id`, `label`, declared `role`, derived `kind`, and the `message_ids`
  that participant said.
* `speaker_kind`: `user`, `assistant`, `curation-summary`, or `mixed` (anchored to
  more than one kind; all speakers are listed in `speakers`).
* `curation-summary` is a participant whose id starts with
  `participant:curation-request`. Its declared role is `user`, but it is the owner's
  summary of a continuation, not an original dialogue turn, so it is kept separate.

On the committed graph: 36 assistant, 21 user (Brian), 5 curation-summary, 0 mixed.
Confirming a node never means Brian endorsed it when `speaker_kind` is `assistant`.

## Field mapping

| Inquiry Graph | epistemic-warrant | Note |
|---|---|---|
| `claim`/`hypothesis` node | `Argument(id, claim=id)` and one `WarrantJudgment` | policy choice |
| node `anchors[].message_id` | support: alternative routes `excerpt-faithful:<id>`; copied to output `excerpt_ids` | the support never changes grounded status |
| `supports` (premise, conclusion) | conclusion gains premise support joined with `relation:<id>` | same |
| `challenges` (challenger, target) | `Defeat(kind="rebut")` | graph has no "challenge succeeded" field; all counted as successful |
| `review_status != confirmed` | judgment assumption `annotation-confirmed:<id>` | so `derive_license` refuses to license unreviewed annotations |
| `origin` (explicit/inferred) | none | |

## Fields with no clean mapping (the real finding)

* **Challenge success and attack kind.** warrant consumes only *successful, typed*
  defeats (rebut/undercut/undermine); the graph says only that someone challenged.
  The adapter assumes success and `rebut`.
* **Challenges whose target is not a proposition** (here a `question` node, 1 of 2)
  have no argument to attack; reported under `unmapped`, not judged.
* **Stance events** (`posits`, `endorses`, `questions`): per-actor stance has no place in
  the regime (speaker of the anchored text is carried as metadata, see above); acceptance is global, not per actor. `rejects`/`retracts`/`suspends`
  would change acceptance and make the adapter raise.
* **Moves, question events, `answers`, `motivates`, `related_to`, `depends_on`, other
  node kinds** (question, goal, method, ...): not propositions or defeats; counted in `unmapped`.
* **`origin` and relation-level `review_status`**: no analogue; only node review status is used.
* **Support has no effect.** In the grounded-dialectical regime status depends only
  on defeats, so anchored excerpts and `supports` links do not influence accept/defeat;
  they are carried for provenance and for other regimes.
* **Excerpt faithfulness** (is the quote really the source?) is modelled only as an
  assumption name; nothing evaluates it.

No change to warrant semantics was needed to connect the two models.
