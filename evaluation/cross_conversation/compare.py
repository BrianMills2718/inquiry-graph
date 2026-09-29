"""C5: answer the cross-chat key questions from two routes and grade them blind.

Route A: all 5 full visible transcripts (the best case for "search the archive, then read").
Route B: the onto-canon6 export of Brian's positions (grouped by aligned proposition, with
stances, chats, verbatim quotes and tensions).
Same answering model for both; a separate blind grading call per question against the key.
Outputs go to private/xconv/compare/.
"""
import json
import random
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from llm_client import call_llm_structured, get_model

ROOT = Path(__file__).resolve().parents[2]
PRIV = ROOT / "private/xconv"
OUT = PRIV / "compare"
CHATS = ["6ab8563b", "6ab96260", "69c07755", "6a988a7a", "6a171ac3"]
MODEL, JUDGE = get_model("synthesis"), get_model("judging")
COMMON = dict(model_policy="enforce_allowlist", max_budget=6.00)


class Answer(BaseModel):
    question_number: int
    answer: str
    cited_chats: list[str] = Field(description="titles of the chats the answer relies on")
    cannot_answer: bool


class AnswerSet(BaseModel):
    answers: list[Answer]


class Grade(BaseModel):
    label: Literal["X", "Y"]
    points_covered: int
    contradicts_key: bool
    attribution_error: bool = Field(description="attributes an assistant view to Brian, or the reverse")
    unsupported_claims: bool = Field(description="asserts cross-chat links the key does not support")


class GradeSet(BaseModel):
    grades: list[Grade]


def cache(name, build):
    path = OUT / name
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    data = build()
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    return data


def material(route: str) -> str:
    if route == "B":
        return (PRIV / "oc6/export.json").read_text(encoding="utf-8")
    parts = []
    for cid in CHATS:
        conv = json.loads((PRIV / f"{cid}.conv.json").read_text(encoding="utf-8"))
        label = {p["id"]: ("BRIAN" if p["role"] == "user" else "ASSISTANT") for p in conv["participants"]}
        body = "\n\n".join(f"[{m['ordinal']}] {label[m['actor_id']]}:\n{m['text']}" for m in conv["messages"])
        parts.append(f"===== CHAT: {conv['title']} =====\n{body}")
    return "\n\n".join(parts)


DESC = {"A": "the full transcripts of 5 conversations between Brian and an AI assistant",
        "B": "a structured export of Brian's own positions extracted from 5 conversations "
             "(grouped by proposition, with stance, chat title and verbatim quote; plus detected tensions)"}


def answer(route, items):
    qs = "\n".join(f"{i + 1}. {it['question']}" for i, it in enumerate(items))
    prompt = f"""You are an AI assistant that must understand Brian's views across his conversations.
You are given {DESC[route]}. Answer each question using only this material. Be specific (2-5 sentences),
name which chats support the answer, and distinguish Brian's own views from assistant suggestions.
If the material does not support an answer, say so and set cannot_answer.

QUESTIONS:
{qs}

MATERIAL:
{material(route)}"""
    res, meta = call_llm_structured(MODEL, [{"role": "user", "content": prompt}], response_model=AnswerSet,
                                    reasoning_effort="medium", task="synthesis",
                                    trace_id=f"inquiry-graph/xconv-compare/answer-{route}", **COMMON)
    got = {a.question_number: a.model_dump() for a in res.answers}
    if sorted(got) != list(range(1, len(items) + 1)):
        raise ValueError(f"route {route}: answers for {sorted(got)}")
    print(f"route {route}: ${meta.cost:.3f}, {meta.usage.get('total_tokens')} tokens")
    return {"cost": meta.cost, "trace_id": f"inquiry-graph/xconv-compare/answer-{route}",
            "answers": [got[i + 1] for i in range(len(items))]}


def judge(items, answers):
    rng = random.Random(46)
    out = []
    for qi, it in enumerate(items):
        routes = ["A", "B"]; rng.shuffle(routes)
        labels = dict(zip("XY", routes))
        block = "\n\n".join(f"ANSWER {lab}: {answers[r]['answers'][qi]['answer']}" for lab, r in labels.items())
        prompt = f"""Grade two answers against the answer key. Judge only agreement with the key.
QUESTION: {it['question']}
ANSWER KEY: {it['answer_key']}
KEY POINTS ({len(it['key_points'])}): {json.dumps(it['key_points'], ensure_ascii=False)}

{block}

Return one grade per answer, labels X and Y."""
        res, meta = call_llm_structured(JUDGE, [{"role": "user", "content": prompt}], response_model=GradeSet,
                                        reasoning_effort="medium", task="judging",
                                        trace_id=f"inquiry-graph/xconv-compare/judge-q{qi + 1}", **COMMON)
        grades = {g.label: g.model_dump() for g in res.grades}
        if set(grades) != {"X", "Y"}:
            raise ValueError(f"q{qi + 1}: judge labels {sorted(grades)}")
        out.append({r: grades[lab] for lab, r in labels.items()})
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    items = json.loads((PRIV / "key/cross_key.json").read_text(encoding="utf-8"))["kept"]
    answers = {r: cache(f"answers_{r}.json", lambda r=r: answer(r, items)) for r in ("A", "B")}
    grades = cache("grades.json", lambda: judge(items, answers))
    rows, tot = [], {r: [0.0, 0, 0, 0, 0, 0] for r in "AB"}
    for qi, (it, g) in enumerate(zip(items, grades), 1):
        k = len(it["key_points"])
        row = {"q": qi, "category": it["category"]}
        for r in "AB":
            x = g[r]; s = min(x["points_covered"], k) / k
            row[r] = round(s, 2)
            t = tot[r]; t[0] += s; t[1] += (s == 1 and not x["contradicts_key"]); t[2] += x["contradicts_key"]
            t[3] += x["attribution_error"]; t[4] += x["unsupported_claims"]; t[5] += answers[r]["answers"][qi - 1]["cannot_answer"]
        rows.append(row)
    summary = {r: {"mean_points": round(t[0] / len(items), 2), "fully_right": t[1], "contradicts": t[2],
                   "attribution_errors": t[3], "unsupported": t[4], "cannot_answer": t[5],
                   "answer_cost": round(answers[r]["cost"], 3)} for r, t in tot.items()}
    (OUT / "summary.json").write_text(json.dumps({"rows": rows, "summary": summary}, indent=1), encoding="utf-8")
    for row in rows:
        print(row)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
