"""Ask a question across several meeting graphs; every claim cites speaker-attributed quotes that code re-checks.
Usage: ask_meetings.py "<question>" <graph.json> [<graph.json> ...] --out answer.json [--model M]
Every stance and question event whose quote is verbatim in a turn spoken by that event's actor becomes an evidence
record {id, meeting, date, speaker, kind, idea, quote}. Meetings are small, so all records go to the model (no
retrieval cut). The model answers in claims that cite record ids; code then checks each cite exists, that a change
cites one speaker on two dates, and that talking past each other cites at least two speakers. Because the records are
extractions and miss turns (a reply that answers the question may not be a record), each claim is then re-read against
the raw transcript around its cited turns and marked supported, partly or not_supported.
"""
import argparse
import asyncio
import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field


def records(graph_paths):
    out, seen = [], set()
    for f in graph_paths:
        g = json.loads(Path(f).read_text(encoding="utf-8"))
        conv = g["conversations"][0]
        msgs = {m["id"]: m for m in conv["messages"]}
        names = {p["id"]: p["label"] for p in conv["participants"]}
        nodes = {n["id"]: n for n in g["nodes"]}
        for kind in ("stance_events", "question_events"):
            for e in g[kind]:
                for a in e["anchors"]:
                    m = msgs.get(a["message_id"])
                    if not m or m["actor_id"] != e["actor_id"] or m["text"][a["start"]:a["end"]] != a["quote"]:
                        continue   # not this speaker's own words at the recorded place
                    k = (a["message_id"], a["quote"], e.get("target_id") or e.get("question_id"))
                    if k in seen:
                        continue
                    seen.add(k)
                    out.append({"id": f"E{len(out):04d}", "meeting": conv["id"], "date": (m.get("timestamp") or "")[:10],
                                "speaker": names.get(e["actor_id"], e["actor_id"]),
                                "kind": e.get("stance") or ("question:" + e.get("status", "")),
                                "idea": nodes.get(e.get("target_id") or e.get("question_id"), {}).get("text", ""),
                                "quote": a["quote"], "message_id": a["message_id"]})
    return out


class Claim(BaseModel):
    statement: str = Field(description="One plain-language statement a reader can check against the cited quotes.")
    kind: Literal["open_question", "change", "talked_past", "agreement"]
    who: list[str] = Field(description="The speakers the statement is about.")
    cites: list[str] = Field(description="Evidence record ids. A change cites the same speaker on two different dates. talked_past cites at least two speakers.")


class Answer(BaseModel):
    summary: str
    claims: list[Claim]
    unsupported_or_unknown: str = Field(description="What the evidence cannot establish.")


SYSTEM = ("You read evidence records from a series of team meetings. Each record is one speaker's own words (verbatim quote) "
          "and the idea they were reacting to, with the meeting date. Answer ONLY from these records and cite record ids. "
          "open_question: something someone asked or was unsure about that no later record settles; say who asked. "
          "change: the SAME speaker says something on a later date that differs from what they said earlier on the same topic; cite both. "
          "talked_past: two or more speakers use the same words or address the same topic but mean different things or answer a "
          "different question than was asked, so they were not actually disagreeing or agreeing; cite each side. "
          "agreement: only when it settles something that was earlier open or disputed. "
          "Prefer fewer, well-supported claims. Do not treat a speaker restating themselves as a change. Write plainly, no jargon. "
          "Say what the evidence cannot establish (the records are machine extractions and miss things).")


async def ask(question, recs, model):
    from llm_client import acall_llm_structured
    ev = "\n".join(f'{r["id"]} | {r["date"]} | {r["speaker"]} | {r["kind"]} | idea: {r["idea"][:200]} | said: "{r["quote"][:300]}"'
                   for r in sorted(recs, key=lambda r: (r["date"], r["message_id"])))
    return await acall_llm_structured(
        model, [{"role": "system", "content": SYSTEM}, {"role": "user", "content": f"Question: {question}\n\nEvidence:\n{ev}"}],
        response_model=Answer, reasoning_effort="medium", model_policy="enforce_allowlist", task="meeting-answer",
        trace_id="inquiry-graph/ask-meetings", max_budget=2.00)


class Verdict(BaseModel):
    verdict: Literal["supported", "partly", "not_supported"]
    reason: str = Field(description="One or two sentences quoting the turn that decides it.")


def windows(graph_paths, pad=3, cap=40):
    """Message id -> (meeting turns in order, names), for reading the transcript around cited turns."""
    out = {}
    for f in graph_paths:
        g = json.loads(Path(f).read_text(encoding="utf-8"))
        conv = g["conversations"][0]
        names = {p["id"]: p["label"] for p in conv["participants"]}
        for m in conv["messages"]:
            out[m["id"]] = (conv["messages"], names)
    return out


def excerpt(ev, wins, pad=3, cap=40):
    parts = []
    for meeting in sorted({r["meeting"] for r in ev}):
        ids = [r["message_id"] for r in ev if r["meeting"] == meeting]
        msgs, names = wins[ids[0]]
        pos = sorted(i for i, m in enumerate(msgs) if m["id"] in ids)
        lo, hi = max(0, pos[0] - pad), min(len(msgs), min(pos[-1] + pad + 1, pos[0] + cap))
        parts.append(f"--- {meeting} ---\n" + "\n".join(f'[{names.get(m["actor_id"], m["actor_id"])}] {m["text"]}' for m in msgs[lo:hi]))
    return "\n".join(parts)


async def verify(claims, wins, model):
    from llm_client import acall_llm_structured
    async def one(c):
        if not c["evidence"]:
            return {"verdict": "not_supported", "reason": "no resolvable citations"}
        out, _ = await acall_llm_structured(
            model, [{"role": "system", "content": "Check one claim about a meeting against the raw transcript excerpt. Judge only from the excerpt. "
                     "If a turn in the excerpt answers a question the claim says went unanswered, or contradicts the claim, it is not_supported."},
                    {"role": "user", "content": f"Claim ({c['kind']}): {c['statement']}\n\nTranscript:\n{excerpt(c['evidence'], wins)}"}],
            response_model=Verdict, reasoning_effort="medium", model_policy="enforce_allowlist", task="meeting-claim-check",
            trace_id="inquiry-graph/ask-meetings-verify", max_budget=1.00)
        return out.model_dump()
    return await asyncio.gather(*(one(c) for c in claims))


def check(answer, recs):
    by = {r["id"]: r for r in recs}
    report = []
    for c in answer.claims:
        ev = [by[i] for i in c.cites if i in by]
        bad = [i for i in c.cites if i not in by]
        speakers = {r["speaker"] for r in ev}
        if c.kind == "change":
            ok = any(len({r["date"] for r in ev if r["speaker"] == s}) >= 2 for s in speakers)
        elif c.kind == "talked_past":
            ok = len(speakers) >= 2
        else:
            ok = bool(ev)
        report.append({**c.model_dump(), "cites_resolved": not bad, "unresolved": bad, "shape_ok": ok, "evidence": ev})
    return report


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("question")
    ap.add_argument("graphs", nargs="+", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--model", default="openrouter/openai/gpt-5.6-luna")
    a = ap.parse_args()
    recs = records(a.graphs)
    answer, meta = asyncio.run(ask(a.question, recs, a.model))
    report = check(answer, recs)
    for c, v in zip(report, asyncio.run(verify(report, windows(a.graphs), a.model))):
        c["transcript_check"] = v
    a.out.write_text(json.dumps({"question": a.question, "records_total": len(recs), "summary": answer.summary,
                                 "unsupported_or_unknown": answer.unsupported_or_unknown, "claims": report,
                                 "trace": str(meta)[:400]}, indent=1), encoding="utf-8")
    ok = sum(1 for r in report if r["cites_resolved"] and r["shape_ok"])
    print(json.dumps({"records_total": len(recs), "claims": len(report), "claims_passing_code_checks": ok,
                      "transcript_check": {v: sum(1 for r in report if r["transcript_check"]["verdict"] == v) for v in ("supported", "partly", "not_supported")}}))
    return 0 if ok == len(report) else 1


if __name__ == "__main__":
    raise SystemExit(main())
