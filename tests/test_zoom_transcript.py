import pytest

from inquiry_graph.zoom_transcript import parse_zoom_transcript

SAMPLE = """# A meeting

**[00:05] Ann Lee:** I think we should reuse it.

**[00:09] Brian Mills:** Agreed, but only
if it fits.

**[00:12] Audio shared by Ann Lee:** Hello, I am the demo voice.
"""


def test_speakers_turns_and_verbatim_text():
    c = parse_zoom_transcript(SAMPLE, "zoom:t1", "A meeting", "2026-10-02T16:00:00Z")
    roles = {p.label: (p.id, p.role) for p in c.participants}
    assert roles["Brian Mills"] == ("participant:brian", "user")
    assert roles["Ann Lee"] == ("participant:ann-lee", "other")
    assert roles["Audio shared by Ann Lee (shared audio, not a person)"][0] == "participant:shared-audio"
    assert [m.actor_id for m in c.messages] == ["participant:ann-lee", "participant:brian", "participant:shared-audio"]
    assert c.messages[1].text == "Agreed, but only\nif it fits."          # continuation lines kept verbatim
    assert c.messages[1].timestamp == "2026-10-02T16:00:09+00:00" and c.messages[1].original_id == "[00:09]"


def test_no_turns_fails_loudly():
    with pytest.raises(ValueError):
        parse_zoom_transcript("no speakers here", "zoom:t2", "x")
