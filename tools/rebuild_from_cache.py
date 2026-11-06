"""Rebuild finished graphs from the saved model answers (cost 0): new code, same raw responses.

Usage: rebuild_from_cache.py <workdir> <model> [--workers N]
Reads <workdir>/queue.json, and for every chat that already has a graph runs the extractor in INQUIRY_CACHE_ONLY mode
into <workdir>_v2/out (cache dir shared by symlink). A cache miss fails that chat loudly instead of calling a model.
Writes <workdir>_v2/dispositions.jsonl and prints before/after relation counts.
"""
import argparse
import concurrent.futures as cf
import json
import os
import subprocess
import sys
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("workdir", type=Path)
    ap.add_argument("model")
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    src, dst = a.workdir.resolve(), Path(str(a.workdir.resolve()) + "_v2")
    for d in ("out", "rep", "quarantine"):
        (dst / d).mkdir(parents=True, exist_ok=True)
    if not (dst / "cache").exists():
        (dst / "cache").symlink_to(src / "cache")
    env = {**os.environ, "INQUIRY_CACHE_ONLY": "1"}
    items = [i for i in json.loads((src / "queue.json").read_text()) if (src / "out" / f"{i['id'].split(':', 1)[1]}.graph.json").exists()]

    def one(i):
        cid = i["id"].split(":", 1)[1]
        out = dst / "out" / f"{cid}.graph.json"
        if out.exists():
            return cid, "skipped_done"
        subprocess.run([sys.executable, "-m", "inquiry_graph", "extract", "--llm", "--model", a.model, "--cache-dir", str(dst / "cache"),
                        "--report", str(dst / "rep" / f"{cid}.json"), "--quarantine-dir", str(dst / "quarantine"), i["file"], str(out)],
                       capture_output=True, text=True, env=env)
        return cid, "rebuilt" if out.exists() else "failed"

    res = {}
    with cf.ThreadPoolExecutor(a.workers) as ex, open(dst / "dispositions.jsonl", "a") as log:
        for cid, st in ex.map(one, items):
            res[cid] = st
            log.write(json.dumps({"id": cid, "status": st}) + "\n")
    b = n = 0
    for cid, st in res.items():
        if st == "rebuilt":
            b += len(json.loads((src / "out" / f"{cid}.graph.json").read_text())["relations"])
            n += len(json.loads((dst / "out" / f"{cid}.graph.json").read_text())["relations"])
    print(json.dumps({"workdir": src.name, "chats": len(items), "rebuilt": sum(v == "rebuilt" for v in res.values()),
                      "failed": sum(v == "failed" for v in res.values()), "relations_before": b, "relations_after": n}))


if __name__ == "__main__":
    main()
