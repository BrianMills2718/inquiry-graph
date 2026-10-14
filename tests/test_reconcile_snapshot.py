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
