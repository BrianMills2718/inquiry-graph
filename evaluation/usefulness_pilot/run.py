"""Usefulness pilot for issue #38: does the graph help answer inquiry questions?

Stages (each cached as JSON under private/usefulness/, rerun skips done stages):
  questions  model writes questions + answer keys from the transcript ONLY;
             keys whose supporting quote is not in the cited message are dropped
  answer     same model answers all questions under each condition A/B/C
  judge      blind grading of each answer against the key (condition hidden)
  report     writes evaluation/usefulness_pilot/results.md
"""
import json, random, re, sys
from pathlib import Path
from typing import Literal
from pydantic import BaseModel, Field
from llm_client import call_llm_structured, get_model

ROOT = Path(__file__).resolve().parents[2]
PRIV = ROOT / "private/usefulness"
OUT = Path(__file__).resolve().parent
MODEL = get_model("synthesis")
JUDGE = get_model("judging")
COMMON = dict(model_policy="enforce_allowlist", max_budget=3.00)
norm = lambda s: re.sub(r"\s+", " ", s).strip()

CATEGORIES = ["open_questions", "rejection_reason", "assumptions_dependencies", "attribution",
              "abandoned_or_deferred", "revision_sequence", "resume_point"]

class Evidence(BaseModel):
    message_index: int
    quote: str = Field(description="verbatim span copied exactly from that message, 5-40 words")

class Item(BaseModel):
    category: Literal["open_questions", "rejection_reason", "assumptions_dependencies", "attribution",
                      "abandoned_or_deferred", "revision_sequence", "resume_point"]
    question: str
    answer_key: str
    key_points: list[str] = Field(description="2-4 atomic facts a correct answer must contain")
    evidence: list[Evidence]

class ItemSet(BaseModel):
    items: list[Item]

class Answer(BaseModel):
    question_number: int
    answer: str
    cannot_answer: bool = Field(description="true if the material does not contain the answer")

class AnswerSet(BaseModel):
    answers: list[Answer]

class Grade(BaseModel):
    label: Literal["X", "Y", "Z"] = Field(description="which answer this grade is for")
    points_covered: int = Field(description="how many key points the answer states correctly")
    contradicts_key: bool
    attribution_error: bool = Field(description="attributes a view/decision to the wrong person (Brian vs assistant)")
    false_closure: bool = Field(description="treats an open question as settled")

class GradeSet(BaseModel):
    grades: list[Grade]

def cache(name, build):
    path = PRIV / name
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    data = build()
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    return data

def load(name):
    return (PRIV / name).read_text(encoding="utf-8")

def make_questions():
    transcript = load("A_transcript.txt")
    prompt = f"""You are building a test of whether someone can recover the state and history of a long inquiry.
Below is the full transcript (messages numbered [i], speaker BRIAN or ASSISTANT).

Write 14 questions, two per category: {", ".join(CATEGORIES)}.
- open_questions: what was still unresolved at the END of the transcript.
- rejection_reason: why a specific earlier proposal or framing was dropped or revised.
- assumptions_dependencies: what a specific conclusion depended on.
- attribution: whether a specific position/decision came from Brian or was an assistant proposal Brian did or did not endorse.
- abandoned_or_deferred: a line of inquiry raised and then deferred or dropped.
- revision_sequence: the order of changes that led to a later formulation.
- resume_point: what the next step was, as of the end.
Each question must have one defensible answer found in the transcript, must name its subject concretely (no "the proposal"), and must not be answerable from general knowledge.
Give the answer key, 2-4 atomic key points, and 1-3 evidence items with the message index and an EXACT verbatim quote from that message.

TRANSCRIPT:
{transcript}"""
    items, meta = call_llm_structured(MODEL, [{"role": "user", "content": prompt}], response_model=ItemSet,
                                      reasoning_effort="high", task="synthesis",
                                      trace_id="inquiry-graph/usefulness-pilot/questions", **COMMON)
    msgs = {}
    for block in re.split(r"\n\n(?=\[\d+\] (?:BRIAN|ASSISTANT) \()", transcript):
        m = re.match(r"\[(\d+)\]", block)
        if m:
            msgs[int(m.group(1))] = norm(block)
    kept, dropped = [], []
    for it in items.items:
        ok = all(norm(ev.quote) in msgs.get(ev.message_index, "") for ev in it.evidence) and it.evidence
        (kept if ok else dropped).append(it.model_dump())
    print(f"questions: {len(kept)} kept, {len(dropped)} dropped for unverifiable quotes; cost ${meta.cost:.3f}")
    return {"model": MODEL, "kept": kept, "dropped": dropped}

CONDITIONS = {"A": ("A_transcript.txt", "the full transcript of the conversation"),
              "B": ("B_excerpts.txt", "curated excerpts selected from the conversation"),
              "C": ("C_graph_report.md", "an inquiry-graph report built from the conversation (questions, claims, moves, stances, relations)")}

def answer(cond, items):
    fname, desc = CONDITIONS[cond]
    qs = "\n".join(f"{i + 1}. {it['question']}" for i, it in enumerate(items))
    prompt = f"""You are given {desc} between BRIAN and an ASSISTANT. Answer each question using only this material.
Be specific and concise (1-4 sentences). If the material does not contain the answer, say so and set cannot_answer.

QUESTIONS:
{qs}

MATERIAL:
{load(fname)}"""
    res, meta = call_llm_structured(MODEL, [{"role": "user", "content": prompt}], response_model=AnswerSet,
                                    reasoning_effort="medium", task="synthesis",
                                    trace_id=f"inquiry-graph/usefulness-pilot/answer-{cond}", **COMMON)
    got = {a.question_number: a.model_dump() for a in res.answers}
    if sorted(got) != list(range(1, len(items) + 1)):
        raise ValueError(f"condition {cond}: answers for {sorted(got)}, expected 1..{len(items)}")
    print(f"answers {cond}: cost ${meta.cost:.3f}, tokens {meta.usage.get('total_tokens')}")
    return {"cost": meta.cost, "answers": [got[i + 1] for i in range(len(items))]}

def judge(items, answers):
    rng = random.Random(38)
    out = []
    for qi, it in enumerate(items):
        conds = list(CONDITIONS); rng.shuffle(conds)
        labels = dict(zip("XYZ", conds))
        block = "\n\n".join(f"ANSWER {lab}: {answers[c]['answers'][qi]['answer']}" for lab, c in labels.items())
        prompt = f"""Grade three answers against the answer key. Judge only factual agreement with the key.
QUESTION: {it['question']}
ANSWER KEY: {it['answer_key']}
KEY POINTS ({len(it['key_points'])}): {json.dumps(it['key_points'], ensure_ascii=False)}

{block}

Return one grade per answer, labels X, Y, Z."""
        res, meta = call_llm_structured(JUDGE, [{"role": "user", "content": prompt}], response_model=GradeSet,
                                        reasoning_effort="medium", task="judging",
                                        trace_id=f"inquiry-graph/usefulness-pilot/judge-q{qi + 1}", **COMMON)
        grades = {g.label.strip().upper(): g.model_dump() for g in res.grades}
        if set(grades) != set("XYZ"):
            raise ValueError(f"q{qi + 1}: judge returned labels {sorted(grades)}")
        out.append({lab_c: {**grades[lab], "label": lab} for lab, lab_c in labels.items()})
    return out

def main():
    q = cache("questions.json", make_questions)
    items = q["kept"]
    if len(items) < 8:
        sys.exit(f"only {len(items)} verifiable questions; too few for a readout")
    answers = {c: cache(f"answers_{c}.json", lambda c=c: answer(c, items)) for c in CONDITIONS}
    grades = cache("grades.json", lambda: judge(items, answers))
    print(json.dumps({"n_questions": len(items)}, indent=1))

if __name__ == "__main__":
    main()
