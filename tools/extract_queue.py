"""Resumable parallel extraction over a queue of normalized conversations.

Usage: extract_queue.py <queue.json> <workdir> [--workers N] [--model M]
Each item {id, file, brian_chars}. Writes <workdir>/out/<id>.graph.json, rep/<id>.json, and appends one line per
conversation to <workdir>/dispositions.jsonl (extracted | failed | skipped_done). Items with an existing graph are skipped, fast failures are retried (login-refresh race),
so a stopped run resumes where it left off. Nothing is silently dropped: every queue item gets a disposition line.
"""
import argparse
import concurrent.futures as cf
import json
import random
import subprocess
import sys
import time
from pathlib import Path


def run_one(item, work, model):
    cid = item["id"].split(":", 1)[1]
    out = work / "out" / f"{cid}.graph.json"
    if out.exists():
        return {"id": item["id"], "status": "skipped_done"}
    t0 = time.time()
    for attempt in range(3):
        t1 = time.time()
        p = _run(cid, item, work, model, out)
        # A fast failure (< 30 s) with no output is almost always the shared Codex login being refreshed by several
        # workers at once. Wait a staggered moment and retry instead of recording a false extraction failure; a failure
        # after real work is recorded as failed immediately.
        if out.exists() or time.time() - t1 >= 30:
            break
        time.sleep(45 + 15 * attempt + random.randint(0, 20))
    ok = out.exists()
    return {"id": item["id"], "status": "extracted" if ok else "failed", "seconds": round(time.time() - t0), "exit": p.returncode,
            "attempts": attempt + 1, "detail": "" if ok else (p.stdout + p.stderr)[-300:]}


def _run(cid, item, work, model, out):
    return subprocess.run([sys.executable, "-m", "inquiry_graph", "extract", "--llm", "--model", model, "--cache-dir", str(work / "cache"),
                           "--report", str(work / "rep" / f"{cid}.json"), "--quarantine-dir", str(work / "quarantine"), item["file"], str(out)],
                          capture_output=True, text=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("queue", type=Path)
    ap.add_argument("workdir", type=Path)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--model", default="codex/gpt-5.6-luna")
    a = ap.parse_args()
    queue = json.loads(a.queue.read_text())
    with cf.ThreadPoolExecutor(a.workers) as ex, open(a.workdir / "dispositions.jsonl", "a") as log:
        for r in ex.map(lambda i: run_one(i, a.workdir, a.model), queue):
            log.write(json.dumps(r) + "\n")
            log.flush()
    print("QUEUE_DONE")


if __name__ == "__main__":
    main()
