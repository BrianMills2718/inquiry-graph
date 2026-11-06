"""Classify chat titles as an INTEREST (work, research, technology, ideas, learning) or something else, using Jev.

Only titles are sent. Several titles go in one typed-decision call (one question per title); calls are
sequential because parallel decision calls hit a budget-store error (llm_client issue #232).
Output: JSON list of {id, title, category, confidence, include}. include = INTEREST with confidence >= threshold.
"""
import argparse
import json
from pathlib import Path

from llm_client import ChoiceQuestion, call_decisions

CRITERIA = {
    "INTEREST": "Sustained thinking about ideas: research questions, theory, science, history, politics, philosophy, the design or architecture of "
                "software or AI systems, evaluating or critiquing plans and papers, understanding a concept in depth. Not a one-off how-to.",
    "ADMIN_OR_TOOL_CHORE": "A one-off task or how-to with no idea behind it: fix or write this code, a pandas/HTML/shell/Git command, a config or install "
                           "problem, reformat text, which setting or tool feature does X; or managing an account, subscription, billing, calendar, email, logistics.",
    "EVERYDAY_LIFE": "Everyday curiosity, trivia or leisure: food, recipes, shopping, travel, places, entertainment, celebrities or gossip, games and poker, "
                     "fashion, dreams, pets, hobbies, definitions of an acronym or a quick fact.",
    "SENSITIVE": "Alcohol, drugs, health, medical, body, mental health, money problems, relationships, sexual or scandalous content, or anything personal.",
    "UNCLEAR": "The title and opening do not say enough to tell.",
}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("titles_json", type=Path, help="list of {id, title[, first]}; with `first` (opening user message) the judgement reads it too")
    ap.add_argument("out", type=Path)
    ap.add_argument("--batch", type=int, default=10)
    ap.add_argument("--threshold", type=float, default=0.5)
    a = ap.parse_args()
    items = json.loads(a.titles_json.read_text(encoding="utf-8"))
    out = []
    for b in range(0, len(items), a.batch):
        chunk = items[b:b + a.batch]
        def ask(it):   # second-stage items carry the opening message ("first"): judge title and opening together
            if it.get("first"):
                return f"What kind of chat has the title {it['title'][:120]!r} and opens with {it['first'][:350]!r}?"
            return f"What kind of chat has the title {it['title'][:120]!r}?"
        questions = {f"t{i}": ChoiceQuestion(ask(it), CRITERIA) for i, it in enumerate(chunk)}
        r = call_decisions("openrouter/typesafe/jev-1.13", state={"task": "classify chat titles"}, questions=questions,
                           task="interest-map-filter", trace_id=f"interest-filter/b{b // a.batch:03d}", max_budget=0.05)
        for i, it in enumerate(chunk):
            ans = r.answers[f"t{i}"]
            cat, conf = getattr(ans, "choice", None), getattr(ans, "confidence", None)
            out.append({**it, "category": cat, "confidence": conf, "include": cat == "INTEREST" and (conf or 0) >= a.threshold})
    a.out.write_text(json.dumps(out, indent=1), encoding="utf-8")
    import collections
    print(json.dumps({"titles": len(out), "by_category": dict(collections.Counter(o["category"] for o in out)),
                      "included": sum(o["include"] for o in out)}))


if __name__ == "__main__":
    main()
