"""Hop 2: real committed graph.json -> epistemic-warrant judgments (no hand-built judgments)."""
import importlib.util
import json
import os
import sys
from collections import Counter
from pathlib import Path

import pytest

if importlib.util.find_spec("epistemic_warrant") is None:
    if os.environ.get("REQUIRE_EPISTEMIC_WARRANT"):
        raise ImportError("epistemic_warrant is required (REQUIRE_EPISTEMIC_WARRANT is set)")
    pytest.skip("epistemic_warrant not installed (private package; see docs/warrant-adapter.md)",
                allow_module_level=True)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import warrant_adapter  # noqa: E402
from inquiry_graph.io import load  # noqa: E402
from inquiry_graph.model import Graph, StanceEvent  # noqa: E402

EX = ROOT / "examples/operational-games-2026-09-30"
P = "dialogue-2026-09-30-operational-games:"


@pytest.fixture(scope="module")
def result():
    return warrant_adapter.adapt(load(EX / "graph.json", Graph))


def by_id(result):
    return {j["claim_id"]: j for j in result["judgments"]}


def test_real_graph_claims_get_expected_statuses(result):
    j = by_id(result)
    assert len(j) == 62 and result["counts"] == {"accepted": 61, "defeated": 1}
    # The one successful challenge: Brian's "broad on purpose" hypothesis rebuts the
    # assistant's vacuity concern (r:027, excerpt ex033/ex037).
    assert j[P + "n:vacuity-concern"]["status"] == "defeated"
    assert j[P + "n:vacuity-concern"]["defeated_by"] == [P + "n:universal-game-vacuity"]
    assert j[P + "n:vacuity-concern"]["excerpt_ids"] == [P + "ex037"]
    # The challenger is unattacked, so it stays accepted; so do supported claims.
    assert j[P + "n:universal-game-vacuity"]["status"] == "accepted"
    assert j[P + "n:decision-sensitive-activation"]["status"] == "accepted"
    assert j[P + "n:game-as-hypothesis"]["status"] == "accepted"


def test_every_judgment_carries_real_source_excerpt_ids(result):
    excerpt_ids = {m["id"] for m in json.loads((EX / "source-excerpts.json").read_text())["messages"]}
    assert excerpt_ids
    for judgment in result["judgments"]:
        assert judgment["excerpt_ids"], judgment["claim_id"]
        assert set(judgment["excerpt_ids"]) <= excerpt_ids


HELD_PROPOSED = {P + "n:" + h for h in (
    "goal-perspective-nonidentity", "heterogeneous-component-semantics",
    "game-choice-decision-coupling")}

# Reworded to say only what their quote says, then confirmed (review-2026-10-02.md addendum).
REWORDED_CONFIRMED = {P + "n:" + h for h in (
    "metaphysical-underdetermination", "operational-adequacy", "universal-game-vacuity",
    "universal-game-prior-art-result", "candidate-generation-mature-prior-art",
    "simudyne-budget-infeasible", "truck-fixture-merged-result")}


def test_license_split_after_2026_10_02_review(result):
    """59 of 62 judged nodes are confirmed (basis: review note + addendum); 3 stay proposed."""
    j = by_id(result)
    licensed = {k for k, v in j.items() if v["licensed"]}
    assert len(licensed) == 58
    assert Counter((v["status"], v["licensed"]) for v in j.values()) == {
        ("accepted", True): 58, ("accepted", False): 3, ("defeated", False): 1}
    # The 3 held nodes are accepted but unlicensed, solely because still proposed.
    assert {k for k, v in j.items() if v["status"] == "accepted" and not v["licensed"]} == HELD_PROPOSED
    for k in HELD_PROPOSED:
        assert j[k]["unmet_assumptions"] == ["annotation-confirmed:" + k]
    # vacuity-concern is confirmed but defeated, so it is not licensed and has nothing unmet.
    assert j[P + "n:vacuity-concern"]["licensed"] is False
    assert j[P + "n:vacuity-concern"]["unmet_assumptions"] == []
    # Licensed claims have no unmet assumptions; game-goal-model-coupling is confirmed and licensed.
    assert all(j[k]["unmet_assumptions"] == [] for k in licensed)
    assert P + "n:game-goal-model-coupling" in licensed
    assert REWORDED_CONFIRMED <= licensed
    # Confirming universal-game-vacuity changes its license, not the defeat it imposes.
    assert j[P + "n:universal-game-vacuity"]["licensed"] is True
    assert j[P + "n:vacuity-concern"]["defeated_by"] == [P + "n:universal-game-vacuity"]
    # Who said the licensed claims (not endorsement by Brian when speaker is assistant).
    assert Counter(j[k]["speaker_kind"] for k in licensed) == {
        "assistant": 33, "user": 20, "curation-summary": 5}


def test_graph_confirmation_matches_judgments():
    graph = load(EX / "graph.json", Graph)
    judged = {x["claim_id"] for x in json.loads((EX / "warrant-judgments.json").read_text())["judgments"]}
    confirmed = {n.id for n in graph.nodes if n.review_status == "confirmed"}
    assert confirmed == judged - HELD_PROPOSED and len(confirmed) == 59
    assert all(n.review_status == "proposed" for n in graph.nodes if n.id not in confirmed)


def test_proposed_annotation_is_never_licensed():
    graph = load(EX / "graph.json", Graph)
    node = next(n for n in graph.nodes if n.id == P + "n:game-goal-model-coupling")
    assert {x["claim_id"]: x for x in warrant_adapter.adapt(graph)["judgments"]}[node.id]["licensed"] is True
    node.review_status = "proposed"
    j = {x["claim_id"]: x for x in warrant_adapter.adapt(graph)["judgments"]}[node.id]
    assert j["licensed"] is False and j["unmet_assumptions"] == ["annotation-confirmed:" + node.id]


def test_question_targeted_challenge_is_reported_unmapped(result):
    assert result["unmapped"]["challenges:non-propositional-endpoint"] == 1


def test_committed_output_is_reproducible(result):
    assert json.loads((EX / "warrant-judgments.json").read_text()) == json.loads(json.dumps(result))


def test_acceptance_changing_stance_fails_loudly():
    graph = load(EX / "graph.json", Graph)
    target = next(n for n in graph.nodes if n.kind == "claim")
    template = graph.stance_events[0]
    graph.stance_events.append(StanceEvent(**{**template.model_dump(), "id": P + "s:test",
                                              "target_id": target.id, "stance": "retracts"}))
    with pytest.raises(NotImplementedError):
        warrant_adapter.adapt(graph)


def test_speaker_attribution_on_real_graph(result):
    j = by_id(result)
    assert j[P + "n:universal-game-prior-art-result"]["speaker_kind"] == "assistant"
    assert j[P + "n:universal-game-prior-art-result"]["speakers"][0]["participant_id"] == "participant:assistant"
    assert j[P + "n:universal-game-vacuity"]["speaker_kind"] == "user"
    assert j[P + "n:candidate-generation-mature-prior-art"]["speaker_kind"] == "user"
    brian = j[P + "n:universal-game-vacuity"]["speakers"]
    assert [(s["participant_id"], s["label"], s["role"]) for s in brian] == [("participant:brian", "Brian", "user")]
    assert Counter(x["speaker_kind"] for x in result["judgments"]) == {
        "assistant": 36, "user": 21, "curation-summary": 5}
    assert all(x["speakers"] and x["speaker_kind"] for x in result["judgments"])
    for x in result["judgments"]:
        assert sorted(m for s in x["speakers"] for m in s["message_ids"]) == x["excerpt_ids"]
        if x["speaker_kind"] == "curation-summary":
            assert x["speakers"][0]["participant_id"].startswith("participant:curation-request")


def test_speaker_is_metadata_only_and_mixed_is_reported():
    graph = load(EX / "graph.json", Graph)
    base = {x["claim_id"]: (x["status"], x["licensed"]) for x in warrant_adapter.adapt(graph)["judgments"]}
    node = next(n for n in graph.nodes if n.id == P + "n:universal-game-vacuity")
    other = next(a for a in graph.nodes if a.id == P + "n:universal-game-prior-art-result").anchors[0]
    node.anchors = node.anchors + [other]
    changed = warrant_adapter.adapt(graph)
    j = {x["claim_id"]: x for x in changed["judgments"]}
    assert j[node.id]["speaker_kind"] == "mixed"
    assert {s["kind"] for s in j[node.id]["speakers"]} == {"user", "assistant"}
    assert {k: (v["status"], v["licensed"]) for k, v in j.items()} == base
