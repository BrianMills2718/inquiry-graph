"""Label Brian's own chat messages with reasoning MOVES using Jev (typed decisions), as a pilot.

Per message, one call asks three typed questions: a single-choice MOVE question (ChoiceQuestion; the
Decisions API has no multi-select, so runner-up labels come from its probabilities) plus two NoulQuestions for
the policy markers prior_art_first and over_engineering_critique, which are kept separate from moves.
Stages (outputs under private/moves_pilot/, gitignored):
  evalset  seed messages + N random corpus messages (seed 17), each with the previous assistant text (<=600 chars)
  earlier  eval set of the earlier retrieval+judge run's top same_move calls per method (for comparison)
  label    call Jev on every eval message; stops before a spend cap is exceeded
Usage: label_moves.py evalset|label [--private DIR] [--n-random 130] [--cap 1.0]
"""
import argparse, glob, json, random
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = Path.home() / "code/chatgpt-conversation-manager-v0.2/data/raw/chats"
A, B = "6ab96260-eb14-83ea-ae11-f964811b3b4f", "6ab8563b-cbfc-83ea-81ed-a0acdea0ea9c"
SEEDS = [(A, n) for n in (13, 15, 1445, 1447, 1453, 1455, 1518, 1678, 1682, 876, 828, 11, 1703, 314, 29)] + \
        [(B, n) for n in (72, 70, 96, 146, 227, 396, 413)]
MODEL = "openrouter/typesafe/jev-1.13"

MOVES = {
    "ask": "Asks a question to obtain information or an answer.",
    "clarify": "Makes a previous statement, term or request more precise, or asks for such precision.",
    "distinguish": "Separates two things that were run together; says X is not the same as Y.",
    "challenge": "Questions, objects to or tests the validity, applicability or sufficiency of a claim or plan.",
    "retract": "Withdraws or corrects an earlier position of his own.",
    "hypothesize": "Offers a tentative explanation, conjecture or guess about how things are.",
    "generalize": "Moves from specific cases to a general principle or pattern.",
    "deduce": "Draws a consequence that follows from stated premises or rules.",
    "test": "Proposes or applies a check, experiment or criterion to see whether something holds.",
    "reframe": "Recasts the problem or topic in a different frame or set of terms.",
    "decompose": "Breaks a problem or thing into parts or steps.",
    "connect": "Links one idea, system or conversation to another, noting a relation between them.",
    "scope": "Sets, narrows or widens what is in or out of the discussion.",
    "summarize": "Restates or condenses what has been said or decided.",
    "propose": "Puts forward a plan, design, action or instruction to do something.",
    "define_by_role": "Defines a thing by its role, intent or function rather than its intrinsic nature.",
    "frame_as_hypothesis": "Treats a boundary, frame or model as a hypothesis to be tested by acting or experiment.",
    "request_example": "Asks for a concrete example or specific case to ground an abstraction.",
    "factor_and_check": "Splits a whole into primitives, then checks whether it is over- or under-factored.",
    "step_back": "Returns to the overall goal or polices scope: are we drifting, what are we actually trying to do.",
    "none_of_these": "None of the above: a plain task order, chore request, data paste, greeting, or content with no reasoning move.",
}
POLICY = {
    "prior_art_first": "Expects that something already exists and prefers to reuse or adopt it over building something new.",
    "over_engineering_critique": "Criticises a design or plan as more complicated than needed.",
}


def _conv_files():
    pats = ["private/kept_normalized_20261003/*.conv.json", "private/claude_export_normalized_20261004/*.conv.json",
            "private/official_exports/gemini_20261005/normalized/*.conv.json"]
    return [f for p in pats for f in sorted(glob.glob(str(ROOT / p)))]


def evalset(out, n_random, root):
    """Seeds from raw ChatGPT files; random rows from the earlier corpus builder's corpus.json (test_method_recurrence corpus)."""
    rows, seen = [], set()
    for chat, n in SEEDS:
        ms = json.loads((RAW / f"{chat}.json").read_text())["messages"]
        if n >= len(ms) or ms[n]["role"] != "user":
            print("skip seed (not a user message):", chat[:8], n); continue
        t = ms[n]["text"].strip()
        if t in seen: continue
        seen.add(t)
        prev = ms[n - 1]["text"] if n and ms[n - 1]["role"] == "assistant" else ""
        rows.append({"id": f"seed:{chat[:8]}:{n}", "kind": "seed", "text": t, "prev": prev[:600]})
    corpus = json.loads((root / "private/motifs_recur/corpus.json").read_text())
    corpus = [r for r in corpus if r["chat"].split(":", 1)[-1] not in {A, B} and r["text"] not in seen]
    pick = random.Random(17).sample(corpus, n_random)
    want = {r["mid"] for r in pick}
    prev = {}
    for f in _conv_files():
        c = json.load(open(f))
        if not any(m["id"] in want for m in c["messages"]): continue
        for i, m in enumerate(c["messages"]):
            if m["id"] in want and i and c["messages"][i - 1].get("actor_id") != "participant:brian":
                prev[m["id"]] = c["messages"][i - 1]["text"][:600]
    for r in pick:
        rows.append({"id": r["mid"], "kind": "random", "corpus_i": r["i"], "text": r["text"], "prev": prev.get(r["mid"], "")})
    out.mkdir(parents=True, exist_ok=True)
    (out / "evalset.json").write_text(json.dumps(rows, indent=1))
    print({"seeds": sum(r["kind"] == "seed" for r in rows), "random": n_random, "with_context": sum(bool(r["prev"]) for r in rows)})


def _prev_lookup(want):
    prev = {}
    for f in _conv_files():
        c = json.load(open(f))
        if not any(m["id"] in want for m in c["messages"]): continue
        for i, m in enumerate(c["messages"]):
            if m["id"] in want and i and c["messages"][i - 1].get("actor_id") != "participant:brian":
                prev[m["id"]] = c["messages"][i - 1]["text"][:600]
    return prev


def earlier(out, root, k=8):
    """Eval set from the earlier embedding+LLM-judge run: its top-k (by similarity) same_move calls per method."""
    judged = json.loads((root / "private/motifs_recur/judged.json").read_text())
    rows = []
    for m, v in judged.items():
        for r in sorted((x for x in v if x["verdict"] == "same_move"), key=lambda x: -x["sim"])[:k]:
            rows.append({"id": r["mid"], "kind": "earlier", "method": m, "sim": r["sim"], "text": r["text"], "quote": r["quote"], "prev": ""})
    prev = _prev_lookup({r["id"] for r in rows})
    for r in rows: r["prev"] = prev.get(r["id"], "")
    (out / "evalset_earlier.json").write_text(json.dumps(rows, indent=1)); print({"earlier": len(rows)})


def label(out, cap, batch, name=""):
    from llm_client import ChoiceQuestion, NoulQuestion, call_decisions
    from llm_client.observability.query import get_cost
    sfx = f"_{name}" if name else ""
    rows = json.loads((out / f"evalset{sfx}.json").read_text())
    done = {r["id"]: r for r in json.loads((out / f"labels{sfx}.json").read_text())} if (out / f"labels{sfx}.json").exists() else {}
    start = (out / "start.txt").read_text() if (out / "start.txt").exists() else datetime.now(timezone.utc).isoformat()
    (out / "start.txt").write_text(start)
    todo = [r for r in rows if r["id"] not in done]
    for b in range(0, len(todo), batch):
        spent = get_cost(project="inquiry-graph", since=start)
        if spent >= cap: print(f"STOP: spend {spent} >= cap {cap}"); break
        chunk = todo[b:b + batch]
        qs = {}
        for i, r in enumerate(chunk):
            ctx = f"Previous assistant message (context only): {r['prev']!r}\n" if r["prev"] else ""
            msg = f"{ctx}Brian's message: {r['text']!r}\n"
            qs[f"m{i}"] = ChoiceQuestion(msg + "Which reasoning move does Brian's message mainly perform?", MOVES)
            for k, d in POLICY.items():
                qs[f"{k}{i}"] = NoulQuestion(msg + f"Does Brian's message show this? {d}")
        res = call_decisions(MODEL, state={"task": "label reasoning moves in a user's chat message"}, questions=qs,
                             task="move-labelling", trace_id=f"inquiry-graph/label-moves/b{b // batch:03d}", max_budget=0.05)
        for i, r in enumerate(chunk):
            a = res.answers[f"m{i}"]
            done[r["id"]] = {**r, "move": a.choice, "confidence": a.confidence, "probs": a.probabilities,
                             **{k: res.answers[f"{k}{i}"].probability for k in POLICY}, "batch_cost": res.cost / len(chunk)}
        (out / f"labels{sfx}.json").write_text(json.dumps(list(done.values()), indent=1))
        print(f"batch {b // batch}: {len(done)}/{len(rows)} labelled, call cost {res.cost:.4f}", flush=True)
    print("spent", get_cost(project="inquiry-graph", since=start))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("stage", choices=["evalset", "earlier", "label"])
    ap.add_argument("--name", default="", help="label stage: label evalset_<name>.json (e.g. earlier)")
    ap.add_argument("--private", type=Path, default=Path.home() / "code/inquiry-graph/private")
    ap.add_argument("--n-random", type=int, default=130)
    ap.add_argument("--cap", type=float, default=1.0)
    ap.add_argument("--batch", type=int, default=5)
    a = ap.parse_args()
    root = a.private.parent
    ROOT = root
    out = a.private / "moves_pilot"
    if a.stage == "evalset": evalset(out, a.n_random, root)
    elif a.stage == "earlier": earlier(out, root)
    else: label(out, a.cap, a.batch, a.name)
