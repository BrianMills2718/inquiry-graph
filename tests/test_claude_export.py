import pytest

from inquiry_graph.claude_export import parse_claude_conversation

C = {"uuid": "u1", "name": "A chat", "chat_messages": [
    {"uuid": "m1", "sender": "human", "text": "I think X", "created_at": "2026-01-01T00:00:00Z"},
    {"uuid": "m2", "sender": "assistant", "text": "Reply", "created_at": "2026-01-01T00:00:05Z"},
    {"uuid": "m3", "sender": "assistant", "text": "", "created_at": "2026-01-01T00:00:06Z"}]}


def test_keeps_human_and_assistant_text_only():
    conv = parse_claude_conversation(C)
    assert conv.id == "claude:u1" and [m.actor_id for m in conv.messages] == ["participant:brian", "participant:assistant"]
    assert conv.messages[0].original_id == "m1"


def test_conversation_without_text_fails_loudly():
    with pytest.raises(ValueError):
        parse_claude_conversation({"uuid": "u2", "name": "x", "chat_messages": [{"sender": "human", "text": " "}]})
