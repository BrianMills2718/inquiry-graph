"""Recompute a privacy-safe C4 summary from the balanced replay artifacts.

Reads private per-question answers, grades, the reference key, route inputs, and
metadata-only call databases. Writes aggregate metrics only; never emits answer,
question, transcript, or quote text.
"""
from __future__ import annotations

import json
import random
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "evaluation/cross_conversation_scale"))
import scale  # noqa: E402
import audit_answer_evidence as evidence  # noqa: E402

SOURCE_RUN = scale.PRIV / "scale_run_codex_rerun_20260930"
LINKER_RUN = scale.DEFAULT_RUN / "linker"
RUN = scale.PRIV / "scale_run_codex_balanced_20260930"
OUTPUT = ROOT / "evaluation/cross_conversation_scale/balanced_replay_summary.json"
TRACE_PREFIX = "inquiry-graph/xconv-scale-codex-balanced-20260930"
ANSWER_TRACE_PREFIX_A = "inquiry-graph/xconv-scale-codex/answer-A"
N = 13


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def trace_metrics(db_path: Path, pattern: str) -> dict:
    if not db_path.is_file():
        raise FileNotFoundError(db_path)
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    rows = con.execute(
        """select trace_id, model, total_tokens, cost, cost_source, billing_mode,
                  latency_s, error_type, finish_reason
           from llm_calls where trace_id like ? order by trace_id""",
        (pattern,),
    ).fetchall()
    con.close()
    return {
        "calls": len(rows),
        "models": sorted({row[1] for row in rows if row[1]}),
        "total_tokens": sum(row[2] or 0 for row in rows),
        "cost_usd": round(sum(row[3] or 0.0 for row in rows), 9),
        "cost_sources": sorted({row[4] for row in rows if row[4]}),
        "billing_modes": sorted({row[5] for row in rows if row[5]}),
        "latency_seconds": round(sum(row[6] or 0.0 for row in rows), 3),
        "errors": sum(row[7] is not None for row in rows),
        "finish_reasons": sorted({row[8] for row in rows if row[8]}),
        "trace_count": len({row[0] for row in rows}),
        "trace_suffixes": [row[0].rsplit("/", 1)[-1] for row in rows],
    }


def load_answers(key: list[dict], corpus: dict[str, dict]) -> dict[str, list[dict]]:
    source_a = read_json(SOURCE_RUN / "answers_A.json")
    answers = {"A": source_a["answers"]}
    if len(answers["A"]) != N or len(source_a["read"]) != N:
        raise ValueError("archive route A does not contain 13 answers and read records")
    for qi, answer in enumerate(answers["A"], 1):
        if answer.get("question_number") != qi:
            raise ValueError(f"route A answer identity mismatch at q{qi:02d}")

    expected_names = {f"q{qi:02d}.json" for qi in range(1, N + 1)}
    for route in ("B", "C"):
        directory = RUN / f"answers_{route}"
        actual_names = {path.name for path in directory.glob("q*.json")}
        if actual_names != expected_names:
            raise ValueError(f"route {route} checkpoint IDs do not match q01-q13")
        rows = []
        for qi in range(1, N + 1):
            saved = read_json(directory / f"q{qi:02d}.json")
            expected_trace = f"{TRACE_PREFIX}/answer-{route}/q{qi:02d}"
            answer = saved.get("answer", {})
            if saved.get("trace_id") != expected_trace or answer.get("question_number") != qi:
                raise ValueError(f"route {route} identity mismatch at q{qi:02d}")
            rows.append(answer)
        answers[route] = rows
    return answers


def source_message_index(corpus_rows: list[dict]) -> dict[str, list[str]]:
    """Read only the source messages needed for exact-string audit; return no text."""
    messages_by_id = {}
    for row in corpus_rows:
        cid = row["id8"]
        candidates = [scale.PRIV / f"{cid}.conv.json", scale.PRIV / "scale" / f"{cid}.conv.json"]
        existing = [path for path in candidates if path.is_file()]
        if len(existing) != 1:
            raise ValueError(f"expected one archived conversation file for {cid}")
        conv = read_json(existing[0])
        messages_by_id[cid] = [
            evidence.normalize(message.get("text", ""))
            for message in conv.get("messages", [])
            if message.get("text")
        ]
    return messages_by_id


def main() -> int:
    key_data = read_json(SOURCE_RUN / "key/cross_key.json")
    key = key_data["kept"]
    if len(key) != N or len(key_data.get("dropped", [])) != 2:
        raise ValueError("reference key membership differs from the preregistered 13 kept / 2 dropped")

    corpus_rows = read_json(SOURCE_RUN / "corpus.json")["chats"]
    corpus = {row["id8"]: row for row in corpus_rows}
    if len(corpus) != 30:
        raise ValueError(f"expected 30 source chats, found {len(corpus)}")
    answers = load_answers(key, corpus)
    source_a = read_json(SOURCE_RUN / "answers_A.json")
    route_reads = source_a["read"]
    for qi, row in enumerate(route_reads, 1):
        if not set(row["chats"]) <= set(corpus):
            raise ValueError(f"route A read record names an unknown source chat at q{qi:02d}")

    exports = {
        "B": read_json(LINKER_RUN / "export_B.json"),
        "C": read_json(LINKER_RUN / "export_C.json"),
    }
    route_source_ids = {
        "A": [set(row["chats"]) for row in route_reads],
        "B": {
            evidence.short_chat_id(position["chat_id"])
            for position in exports["B"]["positions"]
        },
        "C": {
            evidence.short_chat_id(position["chat_id"])
            for position in exports["C"]["positions"]
        },
    }
    for route in ("B", "C"):
        if not route_source_ids[route] <= set(corpus):
            raise ValueError(f"route {route} export references an unknown source chat")

    # Verify that the persisted blinded assignment matches the preregistered seed.
    rng = random.Random(59)
    grade_rows = []
    grade_dir = RUN / "grades"
    expected_names = {f"q{qi:02d}.json" for qi in range(1, N + 1)}
    actual_names = {path.name for path in grade_dir.glob("q*.json")}
    if actual_names != expected_names:
        raise ValueError("blind grade checkpoint IDs do not match q01-q13")

    route_totals = {
        route: {
            "coverage_sum": 0.0,
            "fully_right": 0,
            "contradicts_key": 0,
            "attribution_error": 0,
            "unsupported_claims": 0,
            "cannot_answer": 0,
        }
        for route in ("A", "B", "C")
    }
    category_scores: dict[str, dict[str, list[float]]] = defaultdict(
        lambda: {route: [] for route in ("A", "B", "C")}
    )
    source_recall = {
        route: {"expected_chat_hits": 0, "expected_chat_total": 0, "questions_with_all_expected_chats": 0}
        for route in ("A", "B", "C")
    }

    for qi, item in enumerate(key, 1):
        blinded_routes = ["A", "B", "C"]
        rng.shuffle(blinded_routes)
        expected_labels = dict(zip("XYZ", blinded_routes))
        saved = read_json(grade_dir / f"q{qi:02d}.json")
        if saved.get("trace_id") != f"{TRACE_PREFIX}/judge-q{qi:02d}":
            raise ValueError(f"judge trace identity mismatch at q{qi:02d}")
        if saved.get("labels") != expected_labels or set(saved.get("routes", {})) != {"A", "B", "C"}:
            raise ValueError(f"blinded route assignment mismatch at q{qi:02d}")
        grades = saved["routes"]
        k = len(item["key_points"])
        if k <= 0:
            raise ValueError(f"q{qi:02d} has no key points")

        expected_chats = {evidence.short_chat_id(value) for value in item["chats"]}
        if not expected_chats <= set(corpus):
            raise ValueError(f"q{qi:02d} reference key names unknown source chats")

        for route in ("A", "B", "C"):
            available = route_source_ids[route][qi - 1] if route == "A" else route_source_ids[route]
            hits = len(expected_chats & available)
            source_recall[route]["expected_chat_hits"] += hits
            source_recall[route]["expected_chat_total"] += len(expected_chats)
            source_recall[route]["questions_with_all_expected_chats"] += hits == len(expected_chats)

            grade = grades[route]
            raw_points = grade["points_covered"]
            if raw_points < 0:
                raise ValueError(f"negative grade score at q{qi:02d}, route {route}")
            fraction = min(raw_points, k) / k
            category_scores[item["category"]][route].append(fraction)
            total = route_totals[route]
            total["coverage_sum"] += fraction
            total["fully_right"] += fraction == 1.0 and not grade["contradicts_key"]
            for flag in ("contradicts_key", "attribution_error", "unsupported_claims"):
                total[flag] += bool(grade[flag])
            total["cannot_answer"] += bool(answers[route][qi - 1]["cannot_answer"])

        grade_rows.append({
            "q": qi,
            "category": item["category"],
            "key_points": k,
            **{
                route: round(min(grades[route]["points_covered"], k) / k, 6)
                for route in ("A", "B", "C")
            },
        })

    route_summary = {}
    for route, totals in route_totals.items():
        route_cost = (
            source_a["cost"] if route == "A"
            else sum(read_json(RUN / f"answers_{route}" / f"q{qi:02d}.json").get("recorded_cost_usd", 0.0)
                     for qi in range(1, N + 1))
        )
        route_summary[route] = {
            "mean_key_point_coverage": round(totals["coverage_sum"] / N, 6),
            "fully_right": totals["fully_right"],
            "contradicts_key": totals["contradicts_key"],
            "attribution_error": totals["attribution_error"],
            "unsupported_claims": totals["unsupported_claims"],
            "cannot_answer": totals["cannot_answer"],
            "answer_cost_usd": round(route_cost, 9),
        }

    by_category = {
        category: {
            route: round(sum(scores[route]) / len(scores[route]), 6)
            for route in ("A", "B", "C")
        }
        for category, scores in sorted(category_scores.items())
    }
    source_summary = {
        route: {
            "expected_chat_recall": round(data["expected_chat_hits"] / data["expected_chat_total"], 6),
            "expected_chat_hits": data["expected_chat_hits"],
            "expected_chat_total": data["expected_chat_total"],
            "questions_with_all_expected_chats": data["questions_with_all_expected_chats"],
        }
        for route, data in source_recall.items()
    }

    # Literal quote/title checks are string-presence audits, not semantic citation review.
    corpus_messages = source_message_index(corpus_rows)
    audit = {}
    for route in ("A", "B", "C"):
        title_questions = title_date_questions = 0
        quote_count = exact_quote_count = 0
        for qi, item in enumerate(key):
            text = answers[route][qi]["answer"]
            lowered = text.casefold()
            expected_chats = {evidence.short_chat_id(value) for value in item["chats"]}
            expected_messages = [message for cid in expected_chats for message in corpus_messages[cid]]
            title_matches = date_pair_matches = 0
            for cid in expected_chats:
                title = corpus[cid].get("title", "").strip()
                date = corpus[cid].get("date", "").strip()
                found_title = bool(title and title.casefold() in lowered)
                title_matches += found_title
                date_pair_matches += found_title and bool(date and date in text)
            title_questions += title_matches >= 2
            title_date_questions += date_pair_matches >= 2
            spans = evidence.quote_spans(text)
            quote_count += len(spans)
            exact_quote_count += sum(
                any(evidence.normalize(span) in message for message in expected_messages)
                for span in spans
            )
        audit[route] = {
            "questions_with_at_least_two_expected_titles": title_questions,
            "questions_with_at_least_two_expected_title_date_pairs": title_date_questions,
            "double_quoted_spans": quote_count,
            "spans_found_in_expected_source_messages": exact_quote_count,
        }

    graph_positions = exports["B"]["positions"]
    graph_quote_count = graph_quote_matches = 0
    for position in graph_positions:
        quote = position.get("quote", "")
        if not quote:
            continue
        graph_quote_count += 1
        cid = evidence.short_chat_id(position.get("chat_id", ""))
        normalized_quote = evidence.normalize(quote)
        graph_quote_matches += any(
            normalized_quote in message for message in corpus_messages[cid]
        )

    call_metrics = {
        "A": trace_metrics(
            SOURCE_RUN / "llm-data/llm_observability.db",
            f"{ANSWER_TRACE_PREFIX_A}/q%",
        ),
        "B": trace_metrics(
            RUN / "llm-data/llm_observability.db",
            f"{TRACE_PREFIX}/answer-B/q%",
        ),
        "C": trace_metrics(
            RUN / "llm-data/llm_observability.db",
            f"{TRACE_PREFIX}/answer-C/q%",
        ),
        "judge": trace_metrics(
            RUN / "llm-data/llm_observability.db",
            f"{TRACE_PREFIX}/judge-q%",
        ),
        "control": trace_metrics(
            RUN / "llm-data/llm_observability.db",
            f"{TRACE_PREFIX}/grader-positive-control",
        ),
    }
    for route in ("A", "B", "C"):
        expected_suffixes = [f"q{qi:02d}" for qi in range(1, N + 1)]
        if (
            call_metrics[route]["calls"] != N
            or call_metrics[route]["errors"] != 0
            or call_metrics[route]["trace_suffixes"] != expected_suffixes
        ):
            raise ValueError(f"route {route} has missing calls or call errors")
    expected_judge_suffixes = [f"judge-q{qi:02d}" for qi in range(1, N + 1)]
    if (
        call_metrics["judge"]["calls"] != N
        or call_metrics["judge"]["errors"] != 0
        or call_metrics["judge"]["trace_suffixes"] != expected_judge_suffixes
    ):
        raise ValueError("blind grading calls are incomplete or errored")

    control = read_json(RUN / "grader_control/positive_negative.json")
    control_ok = (
        control.get("trace_id") == f"{TRACE_PREFIX}/grader-positive-control"
        and control.get("known_correct", {}).get("points_covered") == 2
        and control.get("known_correct", {}).get("contradicts_key") is False
        and control.get("known_wrong", {}).get("points_covered") == 0
        and control.get("known_wrong", {}).get("contradicts_key") is True
        and call_metrics["control"]["calls"] == 1
        and call_metrics["control"]["errors"] == 0
        and call_metrics["control"]["trace_suffixes"] == ["grader-positive-control"]
    )
    if not control_ok:
        raise ValueError("fresh grader positive/negative control did not meet the preregistered outcome")

    output = {
        "status": "complete",
        "campaign": "balanced-replay-2026-09-30",
        "plan": "evaluation/cross_conversation_scale/balanced-replay-2026-09-30.md",
        "question_count": N,
        "corpus_chats": len(corpus),
        "answers_per_route": {"A": len(answers["A"]), "B": len(answers["B"]), "C": len(answers["C"])},
        "grades": len(grade_rows),
        "route_means": route_summary,
        "by_category": by_category,
        "per_question": grade_rows,
        "expected_source_chat_availability": source_summary,
        "literal_evidence_audit": {
            "method": "literal title/date and Unicode-normalized quote-substring checks; not semantic citation adjudication",
            "routes": audit,
            "graph_position_quotes": {
                "nonempty": graph_quote_count,
                "exact_contiguous_source_spans": graph_quote_matches,
            },
        },
        "calls": call_metrics,
        "grader_control": {
            "trace_id": control["trace_id"],
            "passed": control_ok,
            "known_correct_points": control["known_correct"]["points_covered"],
            "known_wrong_points": control["known_wrong"]["points_covered"],
            "known_correct_contradiction": control["known_correct"]["contradicts_key"],
            "known_wrong_contradiction": control["known_wrong"]["contradicts_key"],
        },
        "differences": {
            "B_minus_C": round(
                route_summary["B"]["mean_key_point_coverage"] -
                route_summary["C"]["mean_key_point_coverage"], 6
            ),
            "B_minus_A": round(
                route_summary["B"]["mean_key_point_coverage"] -
                route_summary["A"]["mean_key_point_coverage"], 6
            ),
        },
        "limitations": [
            "13 questions from the same 30-chat corpus; key generation saw the full corpus",
            "the seven source-heldout questions are not an independent question-set holdout",
            "coverage scores do not measure semantic citation or quote correctness",
            "the literal evidence audit checks only string presence",
        ],
        "trace_prefixes": {
            "A": ANSWER_TRACE_PREFIX_A,
            "B_C_judges_control": TRACE_PREFIX,
        },
    }
    OUTPUT.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": output["status"],
        "answers_per_route": output["answers_per_route"],
        "grades": output["grades"],
        "route_means": route_summary,
        "by_category": by_category,
        "expected_source_chat_availability": source_summary,
        "literal_evidence_audit": output["literal_evidence_audit"],
        "calls": call_metrics,
        "grader_control_passed": control_ok,
        "differences": output["differences"],
        "output": str(OUTPUT.relative_to(ROOT)),
    }, indent=2, ensure_ascii=False))
    print("CHECK passed=1 failed=0 total=1")
    print("EXIT_STATUS=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
