"""Run the typed cross-chat linker over per-chat graphs and write route B's material.

Usage: run_linker.py OUT_DIR GRAPH.json [GRAPH.json ...]
Writes OUT_DIR/positions.json, links.json and export_B.json (positions with status and
dates, plus typed cross-chat links) and export_C.json (positions only, the ablation).
Quote-bearing: keep OUT_DIR under private/.
"""
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from inquiry_graph.linker import (LINKER_VERSION, collect_positions, embed_positions,  # noqa: E402
                                  judge_pairs, recall_pairs)
from inquiry_graph.model import Graph  # noqa: E402
from llm_client import get_model  # noqa: E402

EMBED_MODEL = "openrouter/openai/text-embedding-3-small"


def main(out: Path, graphs: list[Path]):
    out.mkdir(parents=True, exist_ok=True)
    positions = []
    for g in graphs:
        graph = Graph.model_validate_json(g.read_text(encoding="utf-8"))
        brian = next(p.id for p in graph.conversations[0].participants if p.role == "user")
        positions += collect_positions(graph, brian)
    by_id = {p.id: p for p in positions}
    print(f"{len(positions)} positions from {len(graphs)} chats")
    tag = f"inquiry-graph/xconv-linker/{out.name}"
    vcache = out / "vectors.json"
    if vcache.exists():
        vectors, ecost = json.loads(vcache.read_text()), 0.0
    else:
        vectors, ecost = embed_positions(positions, EMBED_MODEL, f"{tag}/embed")
        vcache.write_text(json.dumps(vectors))
    pairs = recall_pairs(positions, vectors)
    lcache = out / "links.json"
    if lcache.exists():
        data = json.loads(lcache.read_text())
    else:
        links, traces, jcost = judge_pairs(pairs, by_id, get_model("judging"), "Brian", tag)
        data = {"linker_version": LINKER_VERSION, "embed_model": EMBED_MODEL, "recalled_pairs": len(pairs),
                "traces": traces, "cost": {"embed": ecost, "judge": jcost},
                "links": [l.model_dump() for l in links]}
        lcache.write_text(json.dumps(data, indent=1, ensure_ascii=False))
    counts = Counter(l["relation"] for l in data["links"])
    print(f"recalled {data['recalled_pairs']} cross-chat pairs; relations {dict(counts)}; cost {data['cost']}")
    pos = [p.model_dump() for p in positions]
    (out / "positions.json").write_text(json.dumps(pos, indent=1, ensure_ascii=False))
    typed = [l for l in data["links"] if l["relation"] != "unrelated"]
    (out / "export_C.json").write_text(json.dumps({"positions": pos}, ensure_ascii=False))
    (out / "export_B.json").write_text(json.dumps({"positions": pos, "cross_chat_links": typed}, ensure_ascii=False))


if __name__ == "__main__":
    main(Path(sys.argv[1]), [Path(p) for p in sys.argv[2:]])
