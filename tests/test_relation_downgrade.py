from collections import Counter

from inquiry_graph.live_extract import LChunk, LNode, LRelation, convert
from inquiry_graph.model import Conversation, Message, Participant


def _conv():
    return Conversation(
        id="chatgpt:t", title="T", source_kind="normalized", coverage_note="test fixture",
        participants=[Participant(id="participant:brian", label="Brian", role="user"),
                      Participant(id="participant:assistant", label="Assistant", role="assistant")],
        messages=[Message(id="chatgpt:t:msg0001", ordinal=1, text="Graphs are useful because they show structure and reuse.",
                          actor_id="participant:brian", timestamp="2026-01-01T00:00:00Z")])


def _chunk(kind_a, kind_b, rel_kind):
    return LChunk(nodes=[LNode(key="a", kind=kind_a, text="A", message=1, quote="Graphs are useful"),
                         LNode(key="b", kind=kind_b, text="B", message=1, quote="show structure and reuse")],
                  relations=[LRelation(kind=rel_kind, source="a", target="b", message=1, quote="because they show structure")])


def test_type_violating_relation_is_kept_as_related_to():
    drops = Counter()
    c = convert(_conv(), 0, _chunk("concept", "concept", "supports"), drops)   # supports needs claim/hypothesis/example premises
    assert [r.kind for r in c.relations] == ["related_to"] and drops["downgraded_to_related_to"] == 1


def test_valid_relation_keeps_its_kind():
    drops = Counter()
    c = convert(_conv(), 0, _chunk("claim", "claim", "supports"), drops)
    assert [r.kind for r in c.relations] == ["supports"] and drops["downgraded_to_related_to"] == 0
