import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location("ask_positions", Path(__file__).parent.parent / "tools" / "ask_positions.py")
ap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ap)


def _graph(tmp_path, ev_actor, quote):
    g = {"conversations": [{"id": "chatgpt:x", "title": "T", "messages": [
            {"id": "m1", "actor_id": "participant:brian", "text": "i think reuse beats building", "timestamp": "2026-01-02T00:00:00Z"},
            {"id": "m2", "actor_id": "participant:assistant", "text": "reuse is usually cheaper", "timestamp": "2026-01-02T00:01:00Z"}]}],
         "nodes": [{"id": "n1", "text": "Reuse beats building"}],
         "stance_events": [{"actor_id": ev_actor, "target_id": "n1", "stance": "posits",
                            "anchors": [{"message_id": "m1", "quote": quote}]}],
         "question_events": []}
    (tmp_path / "x.graph.json").write_text(json.dumps(g))
    return [tmp_path]


def test_keeps_verbatim_brian_event(tmp_path):
    recs = ap.records(_graph(tmp_path, "participant:brian", "reuse beats building"))
    assert len(recs) == 1 and recs[0]["date"] == "2026-01-02" and recs[0]["target"] == "Reuse beats building"


def test_drops_non_verbatim_quote(tmp_path):
    assert ap.records(_graph(tmp_path, "participant:brian", "reuse always beats building")) == []


def test_drops_event_whose_actor_is_not_brian(tmp_path):
    assert ap.records(_graph(tmp_path, "participant:assistant", "reuse beats building")) == []
