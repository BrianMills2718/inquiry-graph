import importlib.util
import json
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("normalize_chatgpt_export", Path(__file__).parent.parent / "tools" / "normalize_chatgpt_export.py")
nc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nc)


def node(i, parent, role, text):
    return {"id": i, "parent": parent, "message": {"id": i, "author": {"role": role}, "content": {"parts": [text]},
                                                    "create_time": 1.0, "metadata": {}, "recipient": "all"}}


RAW = {"id": "c1", "title": "A chat", "current_node": "n2", "mapping": {
    "n0": {"id": "n0", "parent": None, "message": None},
    "n1": node("n1", "n0", "user", "I think X"), "n2": node("n2", "n1", "assistant", "Reply"),
    "side": node("side", "n1", "assistant", "abandoned branch")}}


def test_active_branch_with_brian_and_assistant_actors():
    conv = nc.parse_chatgpt_conversation(RAW)
    assert conv.id == "chatgpt:c1"
    assert [m.actor_id for m in conv.messages] == ["participant:brian", "participant:assistant"]
    assert [m.text for m in conv.messages] == ["I think X", "Reply"]


def test_no_visible_text_fails_loudly():
    raw = {"id": "c2", "title": "x", "current_node": "n0", "mapping": {"n0": {"id": "n0", "parent": None, "message": None}}}
    with pytest.raises(ValueError):
        nc.parse_chatgpt_conversation(raw)


def test_cli_one_disposition_per_requested_id(tmp_path, monkeypatch):
    d = tmp_path / "conv"
    d.mkdir()
    (d / "conversations-000.json").write_text(json.dumps([RAW, {"id": "other", "mapping": {}}]))
    ids = tmp_path / "ids.json"
    ids.write_text(json.dumps(["c1", "gone"]))
    monkeypatch.setattr("sys.argv", ["x", str(d), str(ids), str(tmp_path / "out"), "--min-chars", "5"])
    nc.main()
    rows = [json.loads(line) for line in (tmp_path / "out" / "dispositions.jsonl").read_text().splitlines()]
    assert {r["id"]: r["status"] for r in rows} == {"chatgpt:c1": "normalized", "chatgpt:gone": "missing_from_export"}
    assert len(json.loads((tmp_path / "out" / "queue.json").read_text())) == 1
