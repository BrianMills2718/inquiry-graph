"""Normalize a speaker-labelled meeting transcript (markdown) into <out_dir>/<id>.conv.json.

Usage: normalize_zoom_transcript.py <transcript.md> <out_dir> --id zoom:<meeting-id> --title "<title>" [--started 2026-10-02T16:25:16Z]
Prints turn and speaker counts. Meeting content may be private: write into a gitignored folder (private/).
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from inquiry_graph.model import Graph  # noqa: E402
from inquiry_graph.validate import require_valid  # noqa: E402
from inquiry_graph.zoom_transcript import parse_zoom_transcript  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("transcript", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--id", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--started")
    a = ap.parse_args()
    conv = parse_zoom_transcript(a.transcript.read_text(encoding="utf-8"), a.id, a.title, a.started)
    require_valid(Graph(id="import-check", conversations=[conv]))
    a.out_dir.mkdir(parents=True, exist_ok=True)
    out = a.out_dir / f"{a.id.replace(':', '-')}.conv.json"
    out.write_text(conv.model_dump_json(indent=1), encoding="utf-8")
    per = Counter(m.actor_id for m in conv.messages)
    labels = {p.id: p.label for p in conv.participants}
    print(json.dumps({"out": str(out), "turns": len(conv.messages), "speakers": len(conv.participants),
                      "turns_per_speaker": {labels[k]: v for k, v in per.items()}}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
