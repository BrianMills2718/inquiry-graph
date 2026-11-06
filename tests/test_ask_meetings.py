import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("ask_meetings", Path(__file__).parents[1] / "tools" / "ask_meetings.py")
am = importlib.util.module_from_spec(spec)
spec.loader.exec_module(am)

RECS = [{"id": "E0", "speaker": "Tyler", "date": "2026-09-30"}, {"id": "E1", "speaker": "Tyler", "date": "2026-10-05"},
        {"id": "E2", "speaker": "Brian", "date": "2026-09-30"}, {"id": "E3", "speaker": "Tyler", "date": "2026-09-30"}]


def run(kind, cites):
    ans = am.Answer(summary="", unsupported_or_unknown="", claims=[am.Claim(statement="s", kind=kind, who=[], cites=cites)])
    return am.check(ans, RECS)[0]


def test_change_needs_one_speaker_on_two_dates():
    assert run("change", ["E0", "E1"])["shape_ok"]
    assert not run("change", ["E0", "E3"])["shape_ok"]      # same speaker, same day
    assert not run("change", ["E2", "E1"])["shape_ok"]      # two dates but two different speakers


def test_talked_past_needs_two_speakers():
    assert run("talked_past", ["E0", "E2"])["shape_ok"]
    assert not run("talked_past", ["E0", "E1"])["shape_ok"]


def test_unknown_cite_is_reported():
    r = run("open_question", ["E9", "E0"])
    assert not r["cites_resolved"] and r["unresolved"] == ["E9"]
