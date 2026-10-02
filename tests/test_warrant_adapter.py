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


def test_unreviewed_annotations_are_never_licensed(result):
    assert not any(j["licensed"] for j in result["judgments"])
    assert all(j["unmet_assumptions"] for j in result["judgments"])


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
