"""Count literal title/date and quote-span evidence in cached scale answers.

This is a conservative, content-free audit: it writes aggregate counts only and
does not claim semantic citation correctness.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "evaluation/cross_conversation"))
sys.path.insert(0, str(ROOT / "src"))

import scale  # noqa: E402

RUN = ROOT / "private/xconv/scale_run_codex_rerun_20260930"
LINKER = ROOT / "private/xconv/scale_run/linker"
OUTPUT = ROOT / "evaluation/cross_conversation_scale/answer_evidence_audit.json"
QUOTE_PATTERNS = (
    re.compile(r'"([^"\n]{15,})"'),
    re.compile(r"“([^”\n]{15,})”"),
    re.compile(r"‘([^’\n]{15,})’"),
    re.compile(r"„([^“\n]{15,})“"),
)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).casefold().replace("…", "...")
    return " ".join(text.split()).strip(" .,:;")


def quote_spans(text: str) -> list[str]:
    found = []
    for pattern in QUOTE_PATTERNS:
        found.extend(pattern.findall(text))
    return found


def short_chat_id(value: str) -> str:
    return value.split(":")[-1][:8]


def main() -> int:
    key = json.loads((RUN / "key/cross_key.json").read_text(encoding="utf-8"))["kept"]
    corpus = json.loads((RUN / "corpus.json").read_text(encoding="utf-8"))["chats"]
    metadata = {chat["id8"]: chat for chat in corpus}
    conversations = {cid: scale.load_conv(cid, directory) for cid, directory in scale.corpus()}
    source_messages = {
        cid: [normalize(message.text) for message in conv.messages if getattr(message, "text", None)]
        for cid, conv in conversations.items()
    }

    route_audit = {}
    for route in "ABC":
        answers = json.loads((RUN / f"answers_{route}.json").read_text(encoding="utf-8"))["answers"]
        title_questions = date_pair_questions = answers_with_quotes = 0
        quote_total = exact_expected_source_total = 0
        for item, answer in zip(key, answers, strict=True):
            answer_text = answer["answer"]
            lowered = answer_text.casefold()
            expected_ids = {short_chat_id(cid) for cid in item["chats"]}
            title_matches = date_pair_matches = 0
            expected_messages = [
                text
                for cid in expected_ids
                for text in source_messages.get(cid, [])
            ]
            for cid in expected_ids:
                chat = metadata.get(cid)
                if not chat:
                    continue
                title = chat.get("title", "").strip()
                date = chat.get("date", "").strip()
                title_found = bool(title and title.casefold() in lowered)
                date_found = bool(date and date in answer_text)
                title_matches += title_found
                date_pair_matches += title_found and date_found
            title_questions += title_matches >= 2
            date_pair_questions += date_pair_matches >= 2

            spans = quote_spans(answer_text)
            answers_with_quotes += bool(spans)
            quote_total += len(spans)
            exact_expected_source_total += sum(
                any(normalize(span) in message for message in expected_messages)
                for span in spans
            )

        route_audit[route] = {
            "answers": len(answers),
            "questions_with_at_least_two_expected_titles": title_questions,
            "questions_with_at_least_two_expected_title_date_pairs": date_pair_questions,
            "answers_with_double_quoted_spans": answers_with_quotes,
            "double_quoted_spans": quote_total,
            "spans_found_verbatim_in_expected_source_messages": exact_expected_source_total,
        }

    positions = json.loads((LINKER / "export_B.json").read_text(encoding="utf-8"))["positions"]
    graph_quote_total = graph_quote_matches = 0
    for position in positions:
        quote = position.get("quote", "")
        if not quote:
            continue
        graph_quote_total += 1
        cid = short_chat_id(position.get("chat_id", ""))
        normalized_quote = normalize(quote)
        graph_quote_matches += any(
            normalized_quote in message for message in source_messages.get(cid, [])
        )

    result = {
        "method": "literal case-insensitive Unicode-normalized substring checks; not semantic citation adjudication",
        "expected_source_set": "reference-key chats for each question",
        "routes": route_audit,
        "graph_position_quotes": {
            "positions": len(positions),
            "nonempty_quotes": graph_quote_total,
            "exact_contiguous_source_spans": graph_quote_matches,
        },
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    for route, data in route_audit.items():
        print(
            f"{route}: titles>=2={data['questions_with_at_least_two_expected_titles']}/13; "
            f"title/date pairs>=2={data['questions_with_at_least_two_expected_title_date_pairs']}/13; "
            f"exact quote spans={data['spans_found_verbatim_in_expected_source_messages']}/"
            f"{data['double_quoted_spans']}"
        )
    print(
        f"graph_position_quotes exact={graph_quote_matches}/{graph_quote_total}; "
        f"CHECK passed={int(graph_quote_total == 620 and graph_quote_matches == 620)} "
        f"failed={int(not (graph_quote_total == 620 and graph_quote_matches == 620))} total=1"
    )
    ok = (
        all(data["answers"] == 13 for data in route_audit.values())
        and graph_quote_total == graph_quote_matches == 620
    )
    print(f"EXIT_STATUS={0 if ok else 1}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
