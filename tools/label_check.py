"""Ask Jev (typed Choice decision, via llm_client.call_decisions) whether each topic label is informative.

Only the label strings are sent (keywords, no chat text). Calls are sequential: parallel decision calls hit a
budget-store error (llm_client issue #232). Writes {label: {decision, confidence, keep}} to the output file.
"""
import argparse
import json
from pathlib import Path

from llm_client import ChoiceQuestion, call_decisions

CRITERIA = {
    "INFORMATIVE": "The label names a recognizable subject area a reader would understand, such as 'Graph / Knowledge / Graphs'.",
    "NOT_INFORMATIVE": "The label is a fragment, a bare person or company name, a version string, a file or tool artifact, or generic filler.",
}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("members", nargs="+", type=Path, help="layer_*_members.json files written by atlas_map.py --layers")
    ap.add_argument("out", type=Path)
    ap.add_argument("--drop-confidence", type=float, default=0.5, help="drop a label only when Jev says NOT_INFORMATIVE with at least this confidence")
    a = ap.parse_args()
    labels = sorted({lab for p in a.members for lab in json.loads(p.read_text(encoding="utf-8"))})
    res = {}
    for i, lab in enumerate(labels):
        r = call_decisions("openrouter/typesafe/jev-1.13", state={"topic_label": lab},
                           questions={"q": ChoiceQuestion("Is this topic label informative on its own?", CRITERIA)},
                           task="public-map-label-check", trace_id=f"public-filter/label-check-{i:03d}", max_budget=0.05)
        ans = r.answers["q"]
        choice = getattr(ans, "choice", None) or ans.get("choice")
        conf = getattr(ans, "confidence", None) if not isinstance(ans, dict) else ans.get("confidence")
        res[lab] = {"decision": choice, "confidence": conf, "keep": not (choice == "NOT_INFORMATIVE" and (conf or 0) >= a.drop_confidence)}
    a.out.write_text(json.dumps(res, indent=1), encoding="utf-8")
    dropped = [k for k, v in res.items() if not v["keep"]]
    print(json.dumps({"labels": len(res), "kept": len(res) - len(dropped), "dropped": len(dropped)}))
    for k in dropped:
        print("  drop:", k, res[k]["decision"], res[k]["confidence"])


if __name__ == "__main__":
    main()
