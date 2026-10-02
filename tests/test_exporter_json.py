import pytest

from inquiry_graph.exporter_json import parse_exporter_json


def _thread(**kw):
    d = {"thread_id": "t1", "title": "T", "capture_source": "api", "messages": [
        {"message_id": "m1", "role": "user", "text": "I think X.", "created_at": "2026-01-01T00:00:00Z"},
        {"message_id": "m2", "role": "tool", "text": "web page", "created_at": None},
        {"message_id": "m3", "role": "assistant", "text": "Maybe Y.", "created_at": None},
    ]}
    d.update(kw)
    return d


def test_keeps_user_and_assistant_only_and_original_ids():
    conv, skipped = parse_exporter_json(_thread())
    assert [m.original_id for m in conv.messages] == ["m1", "m3"]
    assert [m.actor_id for m in conv.messages] == ["participant:brian", "participant:assistant"]
    assert skipped["tool"] == 1 and conv.id == "chatgpt:t1"


def test_completeness_warning_reaches_coverage_note():
    conv, _ = parse_exporter_json(_thread(completeness_warning="DOM only"))
    assert "COMPLETENESS WARNING: DOM only" in conv.coverage_note


def test_no_visible_text_fails_loudly():
    with pytest.raises(ValueError):
        parse_exporter_json(_thread(messages=[{"message_id": "m", "role": "tool", "text": "x"}]))


def test_missing_field_fails_loudly():
    with pytest.raises(ValueError):
        parse_exporter_json({"thread_id": "t"})


def test_provider_for_names_the_route_actually_used():
    from inquiry_graph.live_extract import provider_for
    assert provider_for("codex/gpt-5.6-luna") == "codex"
    assert provider_for("openrouter/google/gemini-2.5-flash") == "openrouter"
