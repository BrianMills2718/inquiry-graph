#!/usr/bin/env python3
"""Validate and summarize an Inquiry Graph representation-fit sidecar."""
import argparse
import json
from pathlib import Path

from inquiry_graph.fit_review import FitReview, summarize


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    review = FitReview.model_validate(json.loads(args.path.read_text()))
    counts = summarize(review)
    print(f"graph: {review.graph_id}")
    print(f"findings: {counts['findings']}")
    for key in sorted(k for k in counts if k != "findings"):
        print(f"{key}: {counts[key]}")
    if review.next_inquiry_question:
        print(f"next: {review.next_inquiry_question}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
