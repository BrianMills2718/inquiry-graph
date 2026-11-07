"""Session-prompt embeddings are cached per prompt, so a new prompt costs one encode, not a full rebuild (#249)."""
import importlib.util
import sys
from pathlib import Path

import numpy as np

TOOLS = Path(__file__).parent.parent / "tools"


def _load():
    sys.path.insert(0, str(TOOLS))
    spec = importlib.util.spec_from_file_location("brian_positions", TOOLS / "brian_positions.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class FakeModel:
    def __init__(self):
        self.encoded = []

    def get_embedding_dimension(self):
        return 4

    def encode(self, docs, **_):
        self.encoded += docs
        return np.array([[len(d), 1, 0, 0] for d in docs], dtype="float32")


def _rec(i, text):
    return {"target": "", "quote": text, "message_id": f"claude-code:s:h{i}"}


def test_new_prompt_encodes_only_itself(tmp_path, monkeypatch):
    bp = _load()
    monkeypatch.setattr(bp, "SESS_EMB", tmp_path / "sessions_emb.npy")
    monkeypatch.setattr(bp, "SESS_IDS", tmp_path / "sessions_emb_ids.json")
    recs = [_rec(i, f"prompt number {i} about the harness") for i in range(5)]
    m = FakeModel()
    first = bp.session_embeddings(m, recs, rebuild=False)
    assert len(m.encoded) == 5 and first.shape == (5, 4)
    m.encoded.clear()
    more = recs + [_rec(9, "a brand new prompt Brian just typed")]
    second = bp.session_embeddings(m, more, rebuild=False)
    assert m.encoded == ["a brand new prompt Brian just typed"]
    assert np.array_equal(second[:5], first)
    m.encoded.clear()
    edited = [dict(more[0], quote="the same id with different text")] + more[1:]
    bp.session_embeddings(m, edited, rebuild=False)
    assert m.encoded == ["the same id with different text"]
