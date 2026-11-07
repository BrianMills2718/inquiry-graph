import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("reconcile_snapshot", Path(__file__).parent.parent / "tools" / "reconcile_snapshot.py")
rs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rs)

FLT = {"a": {"include": True, "category": "INTEREST"}, "b": {"include": False, "category": "EVERYDAY_LIFE"}}


def c(cid, **kw):
    base = dict(failed=set(), agent=set(), flt=FLT, short=set(), graphs=set(), failed_extract=set(), events={})
    base.update(kw)
    return rs.classify(cid, **base)


def test_every_branch_has_a_disposition():
    assert c("x", failed={"x"}) == "failed_no_visible_text"
    assert c("a", agent={"a"}) == "excluded_agent_sent"
    assert c("b") == "excluded_interest_filter:EVERYDAY_LIFE"
    assert c("a", short={"a"}) == "skipped_too_short"
    assert c("a", graphs={"a"}, events={"a": 3}) == "extracted_with_events"
    assert c("a", graphs={"a"}) == "extracted_no_brian_events"
    assert c("a", failed_extract={"a"}) == "extraction_failed"
    assert c("a") == "pending"
    assert c("unfiltered") == "pending"


def test_a_later_extraction_wins_over_the_first_filter_verdict():
    # the low-confidence rerun extracted chats the filter had first excluded; they must count as extracted
    assert c("b", graphs={"b"}, events={"b": 1}) == "extracted_with_events"


def test_included_but_never_queued_is_not_called_too_short():
    assert c("a", queued=set()) == "included_not_queued"
    assert c("a", queued={"a"}) == "pending"
    assert c("a", queued=set(), short={"a"}) == "skipped_too_short"


def test_damaged_log_lines_are_skipped_and_counted(tmp_path, capsys):
    # a machine crash mid-append leaves a line of NUL bytes; the count must not crash on it
    p = tmp_path / "dispositions.jsonl"
    p.write_bytes(b'{"id": "a", "status": "ok"}\n' + b"\x00" * 40 + b"\n" + b"\n" + b'{"id": "b", "status": "failed"}\n')
    assert [r["id"] for r in rs.jl(p)] == ["a", "b"]
    assert "2 damaged line(s) skipped" in capsys.readouterr().err


def test_official_export_chats_are_counted_once():
    rows = {"chatgpt:dup": "extracted_with_events"}
    disp = [{"id": "chatgpt:a", "status": "normalized"}, {"id": "chatgpt:dup", "status": "normalized"},
            {"id": "chatgpt:gone", "status": "failed"}]
    rs.add_official_export(rows, disp, flt=FLT, short=set(), queued=None, graphs={"chatgpt:a"}, failed_extract=set(),
                           events={"chatgpt:a": 2})
    assert rows["chatgpt:a"] == "extracted_with_events"
    assert rows["officialexport:chatgpt:dup"] == "duplicate_of_exporter"
    assert rows["officialexport:chatgpt:gone"] == "failed_no_visible_text"
    assert rows["chatgpt:dup"] == "extracted_with_events"


def test_a_short_chat_the_filter_never_saw_is_too_short_not_pending():
    assert c("unfiltered", short={"unfiltered"}) == "skipped_too_short"
