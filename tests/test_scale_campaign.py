"""Campaign routing stays isolated from the existing OpenRouter cache."""

import json
import sys
from argparse import Namespace
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evaluation/cross_conversation_scale"))
import scale  # noqa: E402


def _args(**overrides):
    values = {
        "codex_subscription": True,
        "campaign_dir": None,
        "model": None,
        "judge_model": None,
        "model_justification": None,
        "linker_dir": None,
    }
    values.update(overrides)
    return Namespace(**values)


def _isolate_globals(monkeypatch, tmp_path):
    private = tmp_path / "private" / "xconv"
    monkeypatch.setattr(scale, "PRIV", private)
    monkeypatch.setattr(scale, "DEFAULT_RUN", private / "scale_run")
    for name in (
        "RUN", "MODEL", "JUDGE", "CALL_OPTIONS", "MODEL_JUSTIFICATION",
        "OBSERVABILITY_POLICY", "KEY_TRACE_PREFIX", "TRACE_PREFIX",
    ):
        monkeypatch.setattr(scale, name, getattr(scale, name))
    return private


def test_codex_campaign_uses_isolated_directory_and_read_only_metadata_route(monkeypatch, tmp_path):
    private = _isolate_globals(monkeypatch, tmp_path)
    legacy_key = private / "scale_run" / "key" / "6ab8563b.positions.json"
    legacy_key.parent.mkdir(parents=True)
    legacy_key.write_text('{"route":"openrouter"}', encoding="utf-8")

    linker_dir = scale.configure_campaign(_args())

    assert scale.RUN == private / "scale_run_codex"
    assert linker_dir == private / "scale_run" / "linker"
    assert scale.MODEL == "codex/gpt-5.6-luna"
    assert scale.JUDGE == "codex/gpt-5.6-sol"
    assert scale.CALL_OPTIONS["codex_transport"] == "cli"
    assert scale.CALL_OPTIONS["sandbox_mode"] == "read-only"
    assert scale.CALL_OPTIONS["approval_policy"] == "never"
    assert scale.OBSERVABILITY_POLICY.mode == "metadata_only"
    manifest = json.loads((scale.RUN / "campaign.json").read_text(encoding="utf-8"))
    assert manifest["transport"] == "codex-cli"
    assert json.loads(legacy_key.read_text(encoding="utf-8")) == {"route": "openrouter"}


def test_codex_campaign_refuses_manifest_settings_mismatch(monkeypatch, tmp_path):
    _isolate_globals(monkeypatch, tmp_path)
    scale.configure_campaign(_args())

    with pytest.raises(ValueError, match="campaign settings differ"):
        scale.configure_campaign(_args(judge_model="codex/gpt-5.6-luna"))


def test_codex_campaign_refuses_to_adopt_nonempty_directory_without_manifest(monkeypatch, tmp_path):
    private = _isolate_globals(monkeypatch, tmp_path)
    campaign = private / "preexisting"
    campaign.mkdir(parents=True)
    (campaign / "cross_key.json").write_text("{}", encoding="utf-8")

    with pytest.raises(ValueError, match="without a manifest"):
        scale.configure_campaign(_args(campaign_dir=campaign))


def test_campaign_paths_cannot_escape_private_directory(monkeypatch, tmp_path):
    _isolate_globals(monkeypatch, tmp_path)

    with pytest.raises(ValueError, match="must stay under"):
        scale.configure_campaign(_args(campaign_dir=tmp_path / "outside"))
