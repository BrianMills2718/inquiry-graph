"""Label Brian's own chat messages with reasoning MOVES using Jev (typed decisions), as a pilot.

Per message, one call asks three typed questions: a single-choice MOVE question (ChoiceQuestion; the
Decisions API has no multi-select, so runner-up labels come from its probabilities) plus two NoulQuestions for
the policy markers prior_art_first and over_engineering_critique, which are kept separate from moves.
Stages (outputs under private/moves_pilot/, gitignored):
  evalset  seed messages + N random corpus messages (seed 17), each with the previous assistant text (<=600 chars)
  earlier  eval set of the earlier retrieval+judge run's top same_move calls per method (for comparison)
  label    two-stage Jev: gate (any reasoning move? + policy markers) then single-choice move on gate-yes only; stops at a spend cap
  corpus   same two stages over private/motifs_recur/corpus.json into private/moves_labels/
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
    "ask": "Asks a genuine question about ideas, facts or how something works, to obtain an explanation or answer. Not a request to do work (find, fetch, write, run, fix).",
    "clarify": "Makes a previous statement, term or request more precise, or asks what a term or statement means.",
    "distinguish": "Separates two things that were run together: says X is not the same as Y.",
    "challenge": "Objects to or tests the validity, applicability or sufficiency of a claim, plan or answer, giving or implying a reason. Not a pasted error, traceback or log, and not an order to fix something.",
    "retract": "Withdraws or corrects an earlier position of his own (I was wrong, scratch that, actually I meant).",
    "hypothesize": "Offers a tentative explanation, conjecture or guess about how things are.",
    "generalize": "Moves from specific cases to a general principle or pattern.",
    "deduce": "Draws a consequence that follows from stated premises or rules (so then X must be true).",
    "test": "Proposes or applies a check, experiment or criterion to see whether an idea holds. Not a pasted test output and not an order to run the tests.",
    "reframe": "Recasts the whole problem or topic in a different frame or set of terms (what if we think of it as ...).",
    "decompose": "Breaks a problem or thing into named parts or ordered steps.",
    "connect": "Links one idea, system or conversation to another, noting a relation between them.",
    "scope": "Sets, narrows or widens what is in or out of the discussion or the work.",
    "summarize": "Restates or condenses what has been said or decided. Not a request for someone else to summarize and not a pasted text.",
    "propose": "Puts forward his own design, approach or idea of what could be done, as a candidate for discussion. A plain order, instruction, task assignment or request to produce something (write this, do X, give me the code) is NOT a proposal.",
    "define_by_role": "Says what a thing IS by what it is for, who uses it or what job it does, not by what it is made of (X is whatever plays the role of Y; a tool is defined by its intended use). Example: 'a spec is whatever lets a stranger reproduce the work'. Not distinguish (which separates two named things) and not reframe (which changes the whole frame).",
    "frame_as_hypothesis": "Treats a boundary, frame, category or model as provisional: a guess to be tried and revised by acting on it or running an experiment.",
    "request_example": "Asks for a concrete example, instance or specific case to ground an abstraction or claim.",
    "factor_and_check": "Splits a whole into primitives, then checks whether the split is over- or under-factored (too many or too few pieces, or overlapping pieces).",
    "step_back": "Returns to the overall goal or polices scope: are we drifting, what are we actually trying to do, is this the main thing.",
    "none_of_these": "No reasoning move: a task order or instruction, chore or tool request (find sources, fix this, write the code, give me the full code, continue), pasted error, traceback, log, data or code, a greeting or thanks, or a one-word reply.",
}
GATE = ("Does Brian's message make any reasoning move about ideas (asks about meaning or reasons, objects, defines, distinguishes, "
        "hypothesizes, proposes his own design, tests, steps back)? Answer NO if it is a task order or instruction, a chore, a request "
        "to find, fetch, write, run or fix something, a pasted error, traceback, log, data or code, a greeting, thanks, or a bare reply.")
GATE_CUTOFF = 0.5       # stage 2 runs only when P(gate=yes) >= this
POLICY_CUTOFF = 0.9     # pilot: p>0.5 over-fired on chores; 0.8-0.9 kept the true cases (hand check, PR #170)
POLICY = {
    "prior_art_first": "Expects that something already exists and prefers to reuse or adopt it over building something new. Not a chore such as find sources or search the web.",
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


def _msg(r):
    ctx = f"Previous assistant message (context only): {r['prev']!r}\n" if r["prev"] else ""
    return f"{ctx}Brian's message: {r['text']!r}\n"


def label_questions(chunk, stage):
    """Questions for one Jev call. stage 'gate': any reasoning move? + policy markers. stage 'move': single-choice move."""
    from llm_client import ChoiceQuestion, NoulQuestion
    qs = {}
    for i, r in enumerate(chunk):
        if stage == "gate":
            qs[f"g{i}"] = NoulQuestion(_msg(r) + GATE)
            for k, d in POLICY.items():
                qs[f"{k}{i}"] = NoulQuestion(_msg(r) + f"Does Brian's message show this? {d}")
        else:
            qs[f"m{i}"] = ChoiceQuestion(_msg(r) + "Which reasoning move does Brian's message mainly perform?", MOVES)
    return qs


def label(out, cap, batch, name="", suffix="_v2", evalfile=None, outdir=None):
    """Two-stage labelling. Resumable; labels<suffix>.json holds one record per message."""
    from llm_client import call_decisions
    from llm_client.observability.query import get_cost
    sfx = f"_{name}" if name else ""
    outdir = outdir or out
    rows = json.loads((evalfile or out / f"evalset{sfx}.json").read_text())
    lf = outdir / f"labels{sfx}{suffix}.json"
    done = {r["id"]: r for r in json.loads(lf.read_text())} if lf.exists() else {}
    start = (outdir / f"start{suffix}.txt").read_text() if (outdir / f"start{suffix}.txt").exists() else datetime.now(timezone.utc).isoformat()
    (outdir / f"start{suffix}.txt").write_text(start)
    rows = [{**r, "id": r.get("id", r.get("mid")), "prev": r.get("prev", "")} for r in rows]
    todo = [r for r in rows if r["id"] not in done]
    for b in range(0, len(todo), batch):
        spent = get_cost(project="inquiry-graph", since=start)
        if spent >= cap: print(f"STOP: spend {spent} >= cap {cap}"); break
        chunk = todo[b:b + batch]
        tid = f"inquiry-graph/label-moves-v2/{name or 'main'}/b{b // batch:04d}"
        g = call_decisions(MODEL, state={"task": "decide whether a chat message makes a reasoning move"}, questions=label_questions(chunk, "gate"),
                           task="move-gate", trace_id=tid + "g", max_budget=0.05)
        rec = {}
        for i, r in enumerate(chunk):
            rec[r["id"]] = {**r, "gate": g.answers[f"g{i}"].probability, **{k: g.answers[f"{k}{i}"].probability for k in POLICY},
                            "batch_cost": g.cost / len(chunk), "move": "none_of_these", "move_probs": None}
        yes = [r for r in chunk if rec[r["id"]]["gate"] >= GATE_CUTOFF]
        if yes:
            m = call_decisions(MODEL, state={"task": "label reasoning moves in a user's chat message"}, questions=label_questions(yes, "move"),
                               task="move-labelling", trace_id=tid + "m", max_budget=0.05)
            for i, r in enumerate(yes):
                a = m.answers[f"m{i}"]
                rec[r["id"]].update(move=a.choice, move_confidence=a.confidence, move_probs=a.probabilities, batch_cost=rec[r["id"]]["batch_cost"] + m.cost / len(yes))
        done.update(rec)
        lf.write_text(json.dumps(list(done.values()), indent=1))
        print(f"batch {b // batch}: {len(done)}/{len(rows)} labelled", flush=True)
    print("spent", get_cost(project="inquiry-graph", since=start))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("stage", choices=["evalset", "earlier", "label", "corpus"])
    ap.add_argument("--corpus-out", type=Path, default=Path.home() / "code/inquiry-graph/private/moves_labels")
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
    elif a.stage == "label": label(out, a.cap, a.batch, a.name)
    else:  # whole corpus of short messages (private/motifs_recur/corpus.json), no previous-assistant context
        a.corpus_out.mkdir(parents=True, exist_ok=True)
        label(out, a.cap, max(a.batch, 10), "", "_corpus", evalfile=a.private / "motifs_recur/corpus.json", outdir=a.corpus_out)
