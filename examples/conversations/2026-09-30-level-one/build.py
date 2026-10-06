"""Build this curated session using the existing Inquiry Graph V1 model.

This is fixture authoring, not a new schema, extractor, or incremental updater.
Run from an installed inquiry-graph checkout:
    python examples/conversations/2026-09-30-level-one/build.py --out /tmp/session
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from inquiry_graph.model import (
    Binding, Conversation, Extraction, Graph, Move, Node, QuestionEvent,
    Relation, SIGNATURES, StanceEvent, anchor,
)
from inquiry_graph.validate import require_valid, validate
from inquiry_graph.views import open_questions, stats

HERE = Path(__file__).resolve().parent
PREFIX = "s30:"


def build_graph(directory: Path = HERE) -> Graph:
    """Return the native graph; raise on malformed curation or invalid anchors."""
    conv = Conversation.model_validate_json((directory / "source.json").read_text(encoding="utf-8"))
    source = {m.id.removeprefix(PREFIX): m for m in conv.messages}
    curation = json.loads((directory / "curation.json").read_text(encoding="utf-8"))
    if curation.get("format") != "session-fixture-authoring-1":
        raise ValueError("Unsupported session authoring format")
    nodes, relations, moves, stances, questions = [], [], [], [], []

    def a(key, quote=None):
        return anchor(source[key], source[key].text if quote is None else quote)

    def node(id, kind, text, s, quote=None, origin="inferred"):
        nodes.append(Node(id=PREFIX+id, kind=kind, text=text, anchors=[a(s, quote)], origin=origin))

    def relation(id, kind, left, right, s, quote=None):
        roles = list(SIGNATURES[kind])
        relations.append(Relation(id=PREFIX+id, kind=kind, bindings=[
            Binding(role=roles[0], ref=PREFIX+left), Binding(role=roles[1], ref=PREFIX+right)
        ], anchors=[a(s, quote)], origin="inferred"))

    def move(id, kind, s, ins, outs, quote=None, after=None):
        moves.append(Move(id=PREFIX+id, kind=kind, actor_id=source[s].actor_id,
                          at_message_id=source[s].id, input_ids=[PREFIX+x for x in ins],
                          output_ids=[PREFIX+x for x in outs], anchors=[a(s, quote)],
                          after_move_ids=[PREFIX+x for x in (after or [])], origin="inferred"))

    def stance(id, s, target, stance, quote=None):
        stances.append(StanceEvent(id=PREFIX+id, actor_id=source[s].actor_id,
                                   target_id=PREFIX+target, stance=stance,
                                   at_message_id=source[s].id, anchors=[a(s, quote)], origin="explicit"))

    def question(id, s, q, status, answers=None, quote=None, basis=None):
        questions.append(QuestionEvent(id=PREFIX+id, actor_id=source[s].actor_id,
                                       question_id=PREFIX+q, status=status,
                                       at_message_id=source[s].id,
                                       answer_ids=[PREFIX+x for x in (answers or [])],
                                       anchors=[a(s, quote)], resolution_basis=basis, origin="inferred"))

    constructors = {"N": node, "R": relation, "M": move, "ST": stance, "Q": question}
    for index, (kind, args, kwargs) in enumerate(curation["annotations"], start=1):
        if kind not in constructors:
            raise ValueError(f"Unknown annotation constructor at row {index}: {kind}")
        try:
            constructors[kind](*args, **kwargs)
        except (TypeError, ValueError, KeyError) as exc:
            raise ValueError(f"Invalid annotation row {index} ({kind}): {exc}") from exc

    # Several excerpts belong to one visible prose turn. Preserve the relevant
    # output anchors, rather than treating its first excerpt as the whole turn.
    by_node = {n.id: n for n in nodes}
    for m in moves:
        for out in m.output_ids:
            if out in by_node:
                for bound in by_node[out].anchors:
                    if bound.message_id[4:7] == m.at_message_id[4:7] and bound not in m.anchors:
                        m.anchors.append(bound)

    graph = Graph(
        id=PREFIX+"graph", conversations=[conv], nodes=nodes, relations=relations,
        moves=moves, stance_events=stances, question_events=questions,
        extractions=[Extraction(method="manual visible-dialogue reconstruction",
            prompt_version="session-capture-1", notes=[
                "Every annotation is proposed, including explicit stance annotations.",
                "The opening handoff is quoted material, not automatic Brian endorsement.",
                "Proceed/continue authorizes investigation, not adoption or question closure.",
                "Literature statements record assistant reports, not independently verified results.",
                "No native message IDs or timestamps are invented. Turn grouping is local.",
                "Supersession and reopening preserve earlier claims instead of overwriting them."
            ])],
        notes=[
            "Separate conversation fixture; the founding seed is unchanged.",
            "Brian prioritizes inference-state/move factorization before strategy optimization, while retaining recursive graph use.",
            "Canonical factorization remains open. CommonKADS was narrowed, not adopted as a solution.",
            "SACM/OPA adoption and federated-polyrepo governance are assistant proposals, not user decisions.",
            "Fixed representation is an assistant-proposed first-pass boundary, not a settled theorem.",
            "At capture, theory PR13 was checked open/unmerged at fad132651a2f36d743a5e29b70eb6a23fe2e0feb.",
            "Inquiry source baseline: 1f75cf1fe02000d2a630f591ec0d6fb412940318."
        ],
    )
    return require_valid(graph)


def graph_text(graph: Graph) -> str:
    """Deterministic native JSON. Default-valued fields remain explicit."""
    return graph.model_dump_json(indent=2) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=HERE / "generated")
    args = parser.parse_args()
    graph = build_graph()
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "graph.json").write_text(graph_text(graph), encoding="utf-8")
    results = {"stats": stats(graph), "validation": validate(graph)}
    (args.out / "validation.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    (args.out / "open-agenda.json").write_text(json.dumps(open_questions(graph), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
