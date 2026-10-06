"""Opt-in move extraction (INQUIRY_EXTRACT_MOVES=1): conversion, grounding, pruning, default-off."""
from collections import Counter


from inquiry_graph import live_extract as le
from inquiry_graph.live_extract import LChunk, LChunkM, convert, prune_to_valid
from inquiry_graph.model import Graph, MoveKind
from inquiry_graph.validate import validate


def _pieces(graph):
    conv = graph.conversations[0]
    user = next(m for m in conv.messages if m.actor_id.endswith("brian"))
    asst = next(m for m in conv.messages if m.actor_id.endswith("assistant"))
    return conv, user, asst


def _out(user, asst, moves):
    return LChunkM.model_validate({
        "nodes": [{"key": "a", "kind": "claim", "text": "t", "message": user.ordinal, "quote": user.text[:20]},
                  {"key": "b", "kind": "question", "text": "t", "message": user.ordinal, "quote": user.text[:20]}],
        "moves": moves})


def test_move_is_converted_and_grounded(graph):
    conv, user, asst = _pieces(graph)
    q = user.text[:20]
    out = _out(user, asst, [{"kind": "challenge", "speaker": "user", "inputs": ["a"], "outputs": ["b"],
                             "message": user.ordinal, "quote": q}])
    drops = Counter()
    c = convert(conv, 0, out, drops)
    assert len(c.moves) == 1
    m = c.moves[0]
    assert (m.kind, m.actor_id, m.at_message_id) == ("challenge", user.actor_id, user.id)
    assert m.input_ids == [c.nodes[0].id] and m.output_ids == [c.nodes[1].id]
    assert m.anchors[0].quote == q and not drops
    g = Graph(id="g", conversations=[conv], **c.model_dump())
    assert validate(g)["valid"]


def test_move_with_bad_grounding_is_dropped_and_counted(graph):
    conv, user, asst = _pieces(graph)
    base = {"kind": "ask", "inputs": ["a"], "outputs": [], "speaker": "user"}
    out = _out(user, asst, [
        {**base, "message": user.ordinal, "quote": "this quote is not in the message"},
        {**base, "message": asst.ordinal, "quote": asst.text[:20]},                    # user cannot act in the assistant's message
        {**base, "message": 9999, "quote": "x"},
        {**base, "inputs": [], "message": user.ordinal, "quote": user.text[:20]}])
    drops = Counter()
    c = convert(conv, 0, out, drops)
    assert c.moves == []
    assert (drops["quote_not_found"], drops["speaker_not_author"], drops["unknown_message"], drops["move_empty"]) == (1, 1, 1, 1)


def test_move_referencing_missing_node_is_dropped(graph):
    conv, user, asst = _pieces(graph)
    out = _out(user, asst, [{"kind": "ask", "speaker": "user", "inputs": ["ghost"], "outputs": [],
                             "message": user.ordinal, "quote": user.text[:20]}])
    drops = Counter()
    assert convert(conv, 0, out, drops).moves == []
    assert drops["move_node_missing"] == 1


def test_move_keeps_surviving_nodes_when_one_cited_node_is_missing(graph):
    conv, user, asst = _pieces(graph)
    out = _out(user, asst, [{"kind": "test", "speaker": "user", "inputs": ["ghost"], "outputs": ["a"],
                             "message": user.ordinal, "quote": user.text[:20]}])
    drops = Counter()
    c = convert(conv, 0, out, drops)
    assert len(c.moves) == 1 and c.moves[0].input_ids == [] and len(c.moves[0].output_ids) == 1
    assert drops["move_refs_trimmed"] == 1 and drops["move_node_missing"] == 0


def test_moves_prompt_defines_every_kind_and_excludes_routine_acts():
    from typing import get_args
    for kind in get_args(MoveKind):
        assert f"{kind}:" in le.MOVES_INSTRUCTIONS or f"{kind}: " in le.MOVES_INSTRUCTIONS, kind
    assert "NOT moves" in le.MOVES_INSTRUCTIONS and "instead of skipping the move" in le.MOVES_INSTRUCTIONS


def test_prune_removes_move_whose_node_was_pruned(graph):
    conv, user, asst = _pieces(graph)
    out = _out(user, asst, [{"kind": "ask", "speaker": "user", "inputs": ["a"], "outputs": [],
                             "message": user.ordinal, "quote": user.text[:20]}])
    c = convert(conv, 0, out, Counter())
    g = Graph(id="g", conversations=[conv], **c.model_dump())
    data = g.model_dump()
    data["nodes"] = [n for n in data["nodes"] if not n["id"].endswith(":a")]   # as if the node had been pruned
    drops = Counter()
    pruned = prune_to_valid(Graph.model_validate(data), drops)
    assert pruned.moves == [] and drops["invalid:dangling_reference"] == 1


def test_default_off(monkeypatch):
    monkeypatch.delenv("INQUIRY_EXTRACT_MOVES", raising=False)
    assert not le.moves_enabled() and le.prompt_version() == le.PROMPT_VERSION == "live-2.2.0"
    assert "moves" not in LChunk.model_json_schema()["properties"]
    monkeypatch.setenv("INQUIRY_EXTRACT_MOVES", "1")
    assert le.moves_enabled() and le.prompt_version() == "live-2.3.2-moves"
    assert "moves" in LChunkM.model_json_schema()["properties"]
