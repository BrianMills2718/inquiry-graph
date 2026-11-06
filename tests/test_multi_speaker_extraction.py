"""Speaker attribution in live extraction: meetings by name, two-party chats by role (unchanged)."""
from collections import Counter

from inquiry_graph.live_extract import LChunk, MChunk, convert, is_meeting
from inquiry_graph.zoom_transcript import parse_zoom_transcript

MEETING = """**[00:01] Ann Lee:** I think we should reuse the existing orchestrator for this.

**[00:05] Bob Ray:** I disagree, the existing orchestrator cannot handle approvals.

**[00:09] Brian Mills:** Can we test it on one real task before deciding anything?

**[00:12] Audio shared by Ann Lee:** I am the demo buyer and I want a discount today.
"""


def node(key, msg, quote):
    return {"key": key, "kind": "claim", "text": key, "message": msg, "quote": quote}


def test_meeting_positions_go_to_the_person_who_said_them():
    conv = parse_zoom_transcript(MEETING, "zoom:t", "t", "2026-10-02T16:00:00Z")
    assert is_meeting(conv)
    out = MChunk.model_validate({
        "nodes": [node("reuse", 1, "we should reuse the existing orchestrator"),
                  node("cant", 2, "the existing orchestrator cannot handle approvals"),
                  node("test", 3, "Can we test it on one real task"),
                  node("discount", 4, "I want a discount today")],
        "stances": [
            {"speaker": "ANN LEE", "target": "reuse", "stance": "posits", "message": 1, "quote": "we should reuse the existing orchestrator"},
            {"speaker": "BOB RAY", "target": "cant", "stance": "posits", "message": 2, "quote": "the existing orchestrator cannot handle approvals"},
            {"speaker": "ANN LEE", "target": "cant", "stance": "posits", "message": 2, "quote": "the existing orchestrator cannot handle approvals"},
            {"speaker": "AUDIO SHARED BY ANN LEE (SHARED AUDIO, NOT A PERSON)", "target": "discount", "stance": "posits", "message": 4, "quote": "I want a discount today"},
            {"speaker": "CAROL", "target": "reuse", "stance": "endorses", "message": 1, "quote": "we should reuse the existing orchestrator"}],
        "question_events": [{"speaker": "Brian Mills", "question": "test", "status": "open", "message": 3, "quote": "Can we test it on one real task"}]})
    out.nodes[2].kind = "question"
    drops = Counter()
    c = convert(conv, 0, out, drops)
    by_actor = {(s.actor_id, s.target_id.rsplit(":", 1)[1]) for s in c.stance_events}
    assert by_actor == {("participant:ann-lee", "reuse"), ("participant:bob-ray", "cant")}
    assert [q.actor_id for q in c.question_events] == ["participant:brian"]
    assert drops["speaker_not_author"] == 1            # Ann credited with Bob's words: dropped
    assert drops["shared_audio_not_a_person"] == 1     # the demo voice holds no positions
    assert drops["unknown_speaker"] == 1               # a name not in the meeting


def test_two_party_chat_attribution_unchanged():
    from inquiry_graph.model import Conversation, Message, Participant
    conv = Conversation(id="c:1", title="t", source_kind="normalized", coverage_note="x",
                        participants=[Participant(id="participant:brian", label="Brian", role="user"),
                                      Participant(id="participant:assistant", label="Assistant", role="assistant")],
                        messages=[Message(id="c:1:m1", actor_id="participant:brian", ordinal=1, text="I think reuse beats building here."),
                                  Message(id="c:1:m2", actor_id="participant:assistant", ordinal=2, text="You could build a custom layer instead.")])
    assert not is_meeting(conv)
    out = LChunk.model_validate({
        "nodes": [node("reuse", 1, "reuse beats building here"), node("custom", 2, "build a custom layer instead")],
        "stances": [{"speaker": "user", "target": "reuse", "stance": "posits", "message": 1, "quote": "reuse beats building here"},
                    {"speaker": "assistant", "target": "custom", "stance": "posits", "message": 2, "quote": "build a custom layer instead"},
                    {"speaker": "user", "target": "custom", "stance": "endorses", "message": 2, "quote": "build a custom layer instead"}]})
    drops = Counter()
    c = convert(conv, 0, out, drops)
    assert {(s.actor_id, s.stance) for s in c.stance_events} == {("participant:brian", "posits"), ("participant:assistant", "posits")}
    assert drops["speaker_not_author"] == 1


def test_meeting_positions_cli_shows_only_that_speaker(tmp_path):
    import subprocess
    import sys
    from pathlib import Path

    from inquiry_graph.model import Graph
    conv = parse_zoom_transcript(MEETING, "zoom:t", "t", "2026-10-02T16:00:00Z")
    out = MChunk.model_validate({
        "nodes": [node("reuse", 1, "we should reuse the existing orchestrator"), node("cant", 2, "the existing orchestrator cannot handle approvals")],
        "stances": [{"speaker": "ANN LEE", "target": "reuse", "stance": "posits", "message": 1, "quote": "we should reuse the existing orchestrator"},
                    {"speaker": "BOB RAY", "target": "cant", "stance": "posits", "message": 2, "quote": "the existing orchestrator cannot handle approvals"}]})
    c = convert(conv, 0, out, Counter())
    f = tmp_path / "m.graph.json"
    f.write_text(Graph(id="g", conversations=[conv], **c.model_dump()).model_dump_json())
    tool = Path(__file__).resolve().parents[1] / "tools" / "meeting_positions.py"
    r = subprocess.run([sys.executable, str(tool), str(f), "--speaker", "Bob", "--json"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    import json
    d = json.loads(r.stdout)
    assert d["speaker"] == "Bob Ray" and [x["quote"] for x in d["shown"]] == ["the existing orchestrator cannot handle approvals"]
    assert d["failed_check"] == []


TALK = """**[00:01] Ann Lee:** So, like, they put agents in Minecraft and… skills over time, you know, and they learn.

**[00:05] Bob Ray:** Sure.

**[00:09] Ann Lee:** I see the whole problem as the waiting time.

**[00:12] Bob Ray:** I think the reps hate the waiting time too.
"""


def test_meeting_quotes_tidied_or_misnumbered_are_grounded_verbatim():
    conv = parse_zoom_transcript(TALK, "zoom:t2", "t", "2026-10-02T16:00:00Z")
    out = MChunk.model_validate({
        "nodes": [node("mc", 1, "they put agents in Minecraft and skills over time"),
                  node("wait", 2, "I see the whole problem as the waiting time."),
                  node("reps", 3, "the reps hate the waiting time too")],
        "stances": [{"speaker": "ANN LEE", "target": "mc", "stance": "posits", "message": 1, "quote": "they put agents in Minecraft and skills over time"},
                    {"speaker": "ANN LEE", "target": "wait", "stance": "posits", "message": 2, "quote": "I see the whole problem as the waiting time."},
                    {"speaker": "ANN LEE", "target": "reps", "stance": "posits", "message": 3, "quote": "the reps hate the waiting time too"}]})
    drops = Counter()
    c = convert(conv, 0, out, drops)
    got = {(s.target_id.rsplit(":", 1)[1], s.actor_id, s.anchors[0].quote) for s in c.stance_events}
    assert ("mc", "participant:ann-lee", "they put agents in Minecraft and… skills over time") in got   # exact source span stored
    assert ("wait", "participant:ann-lee", "I see the whole problem as the waiting time.") in got     # moved from turn 2 to turn 3
    assert not any(t == "reps" for t, _, _ in got)                                                     # Bob's words, claimed for Ann: refused
    assert drops["quote_message_corrected"] >= 1 and drops["quote_realigned_to_source"] >= 1 and drops["speaker_not_author"] >= 1
    for s in c.stance_events:                                                                          # every stored quote is verbatim in its message
        m = {mm.id: mm for mm in conv.messages}[s.anchors[0].message_id]
        assert m.text[s.anchors[0].start:s.anchors[0].end] == s.anchors[0].quote and m.actor_id == s.actor_id
