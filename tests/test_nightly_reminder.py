import datetime as dt
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import nightly_sessions  # noqa: E402


def digest(cid, to, open_items):
    return {"conversations": [{"id": cid, "title": cid, "from": to, "to": to}], "goals": ["g"],
            "open": open_items, "unknown_status": [], "requests_open": []}


def test_window_uses_session_time_not_file_time(tmp_path, monkeypatch):
    """A bulk re-import gives every file today's time; an old session must still fall outside the window."""
    now = dt.datetime.now(dt.timezone.utc)
    sessions = tmp_path / "private" / "coding-sessions"
    sessions.mkdir(parents=True)
    for name in ("recent", "old", "undated"):
        (sessions / f"{name}.graph.json").write_text("{}")   # all freshly written, as after a re-import
        os.utime(sessions / f"{name}.graph.json", (time.time(), time.time()))
    digests = [digest("recent", (now - dt.timedelta(days=1)).isoformat().replace("+00:00", "Z"), ["still open"]),
               digest("old", (now - dt.timedelta(days=10)).isoformat().replace("+00:00", "Z"), ["stale item"]),
               digest("undated", None, ["no time"])]
    monkeypatch.setattr(nightly_sessions, "P", tmp_path / "private")
    monkeypatch.setattr(nightly_sessions, "run", lambda step, cmd: json.dumps(digests))
    out = tmp_path / "review.md"
    nightly_sessions.recent_reminder(7, out)
    text = out.read_text()
    assert "## recent" in text and "still open" in text
    assert "## old" not in text and "## undated" not in text
    assert not (sessions / "recent.md").exists()   # --out leaves the nightly reminder alone


def test_headless_sessions_are_left_out(tmp_path, monkeypatch):
    """Nightly topic naming runs hundreds of codex exec calls; each imports as a session with no prompt from Brian."""
    now = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=1)).isoformat().replace("+00:00", "Z")
    sessions = tmp_path / "private" / "coding-sessions"
    sessions.mkdir(parents=True)
    for name, actor in (("mine", "participant:brian"), ("headless", "participant:automation")):
        (sessions / f"{name}.graph.json").write_text("{}")
        (sessions / f"{name}.conversation.json").write_text(json.dumps({"messages": [{"actor_id": actor}, {"actor_id": "participant:assistant"}]}))
    seen = []

    def run(step, cmd):
        seen.extend(Path(c).name for c in cmd[2:])
        return json.dumps([digest(Path(c).name.split(".")[0], now, ["open item"]) for c in cmd[2:]])

    monkeypatch.setattr(nightly_sessions, "P", tmp_path / "private")
    monkeypatch.setattr(nightly_sessions, "run", run)
    out = tmp_path / "review.md"
    nightly_sessions.recent_reminder(3, out)
    assert seen == ["mine.graph.json"]
    assert "## mine" in out.read_text() and "## headless" not in out.read_text()
