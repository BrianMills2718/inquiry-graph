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
    "INTEREST": "An intellectual, professional or technical topic: research, ideas, theory, history, politics, "
                "technology, software, AI, data, writing, learning about how things work.",
    "EVERYDAY_LIFE": "An everyday-life errand or curiosity: food, recipes, restaurants, shopping, travel, places, "
                     "local logistics, entertainment trivia, hobbies, pets.",
    "SENSITIVE": "Alcohol, drugs, health, medical, body, mental health, money problems, relationships or "
                 "anything personal.",
    "UNCLEAR": "The title does not say enough to tell.",
}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("titles_json", type=Path, help="list of {id, title}")
    ap.add_argument("out", type=Path)
    ap.add_argument("--batch", type=int, default=10)
    ap.add_argument("--threshold", type=float, default=0.5)
    a = ap.parse_args()
    items = json.loads(a.titles_json.read_text(encoding="utf-8"))
    out = []
    for b in range(0, len(items), a.batch):
        chunk = items[b:b + a.batch]
        questions = {f"t{i}": ChoiceQuestion(f"What kind of chat has the title {it['title'][:120]!r}?", CRITERIA) for i, it in enumerate(chunk)}
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
