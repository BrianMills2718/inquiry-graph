"""Thin adapter: Inquiry Graph -> epistemic-warrant grounded-dialectical judgments.

Hop 2 of the source -> trust-judgment pipeline. Consumes a validated Inquiry
Graph and emits one real `WarrantJudgment` assessment per propositional node
(kind `claim` or `hypothesis`) using `epistemic_warrant` unchanged.

Mapping (every choice here is a declared policy, not warrant semantics):

* propositional node          -> `Argument` (id = node id, claim = node id)
* node anchors (excerpt ids)  -> support: one alternative route per anchored
                                 excerpt, assumption `excerpt-faithful:<excerpt id>`
* `supports` relation         -> conclusion also gains the premise's support
                                 joined with assumption `relation:<relation id>`
* `challenges` relation       -> `Defeat(kind="rebut")` challenger -> target.
                                 The graph does not record whether a challenge
                                 *succeeds*; every challenge between two
                                 propositional nodes is treated as successful.
* `review_status != confirmed`-> judgment assumption `annotation-confirmed:<id>`
                                 (so an unreviewed annotation is never licensed)

Fields with no clean mapping are counted in the output under `unmapped`.
Stance events that would change acceptance (`rejects`, `retracts`, `suspends`)
are not representable; the adapter raises instead of silently ignoring them.

Speaker attribution (metadata only; never changes status or licensing): each
judgment lists `speakers` (participant id, label, declared role, derived `kind`,
and the anchored `message_ids` each said) and a single `speaker_kind` in
{user, assistant, curation-summary, mixed}. `curation-summary` is a participant
whose id starts with `participant:curation-request` (a curator's summary, not an
original dialogue turn); `mixed` means the node is anchored to more than one kind.

epistemic-warrant is an external package (private repo; install with
`pip install -e ../epistemic-warrant` or the pinned `warrant` extra).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from epistemic_warrant.defeat import Argument, Defeat, DefeatFramework  # noqa: E402
from epistemic_warrant.support import SupportAntichain  # noqa: E402
from epistemic_warrant.warrant import (  # noqa: E402
    EpistemicAction,
    GroundedDialecticalWarrantRegime,
    Guarantee,
    WarrantJudgment,
)
from inquiry_graph.io import load  # noqa: E402
from inquiry_graph.model import Graph  # noqa: E402
from inquiry_graph.validate import require_valid  # noqa: E402

PROPOSITIONAL = {"claim", "hypothesis"}
ACCEPTANCE_CHANGING_STANCES = {"rejects", "retracts", "suspends"}
# A participant whose id starts with this is a curator's summary of a turn, not an
# original dialogue turn (even though its declared role is "user"); it must never be
# read as the user speaking in the dialogue.
CURATION_PARTICIPANT_PREFIX = "participant:curation-request"


def _speaker_kind(participant) -> str:
    if participant.id.startswith(CURATION_PARTICIPANT_PREFIX):
        return "curation-summary"
    return participant.role


def _speakers(anchors, actors) -> tuple[list[dict], str]:
    """Who said the anchored messages. Metadata only: never feeds warrant evaluation."""
    found: dict[str, dict] = {}
    for a in sorted(anchors, key=lambda x: x.message_id):
        message, participant = actors[a.message_id]
        entry = found.setdefault(participant.id, {
            "participant_id": participant.id,
            "label": participant.label,
            "role": participant.role,
            "kind": _speaker_kind(participant),
            "message_ids": [],
        })
        if message.id not in entry["message_ids"]:
            entry["message_ids"].append(message.id)
    speakers = sorted(found.values(), key=lambda e: e["participant_id"])
    kinds = {e["kind"] for e in speakers}
    return speakers, (kinds.pop() if len(kinds) == 1 else "mixed")


def _support(node_id, nodes, anchors, premises, memo, active):
    if node_id in memo:
        return memo[node_id]
    if node_id in active:
        raise ValueError(f"cyclic `supports` relations through {node_id}")
    active.add(node_id)
    support = SupportAntichain(
        [[f"excerpt-faithful:{a.message_id}"] for a in anchors[node_id]]
    )
    for relation_id, premise_id in premises.get(node_id, []):
        premise = _support(premise_id, nodes, anchors, premises, memo, active)
        support = support.alternative(
            premise.joint(SupportAntichain.atom(f"relation:{relation_id}"))
        )
    active.discard(node_id)
    memo[node_id] = support
    return support


def adapt(graph: Graph) -> dict:
    """Return per-node grounded-dialectical assessments plus an unmapped-field tally."""
    require_valid(graph)
    nodes = {n.id: n for n in graph.nodes if n.kind in PROPOSITIONAL}
    for s in graph.stance_events:
        if s.stance in ACCEPTANCE_CHANGING_STANCES and s.target_id in nodes:
            raise NotImplementedError(
                f"stance {s.stance!r} on {s.target_id} has no epistemic-warrant mapping"
            )

    anchors = {i: n.anchors for i, n in nodes.items()}
    actors = {}
    for conv in graph.conversations:
        people = {p.id: p for p in conv.participants}
        for m in conv.messages:
            actors[m.id] = (m, people[m.actor_id])
    premises: dict[str, list] = {}
    defeats, skipped = [], Counter()
    for r in graph.relations:
        roles = {b.role: b.ref for b in r.bindings}
        if r.kind == "supports":
            c, p = roles.get("conclusion"), roles.get("premise")
            if c in nodes and p in nodes:
                premises.setdefault(c, []).append((r.id, p))
            else:
                skipped["supports:non-propositional-endpoint"] += 1
        elif r.kind == "challenges":
            c, t = roles.get("challenger"), roles.get("target")
            if r.review_status == "rejected":
                raise NotImplementedError(f"rejected relation {r.id} has no mapping")
            if c in nodes and t in nodes:
                defeats.append(Defeat(source=c, target=t, kind="rebut"))
            else:
                skipped["challenges:non-propositional-endpoint"] += 1
        else:
            skipped[f"relation:{r.kind}"] += 1

    memo: dict = {}
    framework = DefeatFramework(
        [Argument(i, _support(i, nodes, anchors, premises, memo, set()), claim=i) for i in nodes],
        defeats,
    )
    regime = GroundedDialecticalWarrantRegime()
    judgments = []
    for i, n in nodes.items():
        assumptions = [] if n.review_status == "confirmed" else [f"annotation-confirmed:{i}"]
        judgment = WarrantJudgment(
            regime=regime.id,
            assumptions=assumptions,
            certificate_id=i,
            action=EpistemicAction("retain_candidate", i),
            guarantee=Guarantee(
                "defeasible-acceptability",
                "annotation remains acceptable under grounded semantics",
            ),
        )
        decision = regime.evaluate(judgment, framework)
        a = decision.assessment
        speakers, speaker_kind = _speakers(n.anchors, actors)
        judgments.append({
            "claim_id": i,
            "kind": n.kind,
            "text": n.text,
            "status": "accepted" if a.warranted else "defeated" if a.certificate_status.value == "out" else "undecided",
            "grounded_status": a.certificate_status.value,
            "licensed": decision.licensed,
            "unmet_assumptions": sorted(decision.unmet_assumptions),
            "excerpt_ids": sorted({x.message_id for x in n.anchors}),
            "speaker_kind": speaker_kind,
            "speakers": speakers,
            "defeated_by": sorted(framework.attackers_of(i)),
            "reason": a.reason,
        })

    for kind, field, items in (
        ("node", "kind", graph.nodes), ("move", "kind", graph.moves),
        ("stance_event", "stance", graph.stance_events),
        ("question_event", "status", graph.question_events),
    ):
        for it in items:
            if kind == "node" and it.kind in PROPOSITIONAL:
                continue
            skipped[f"{kind}:{getattr(it, field)}"] += 1
    return {
        "graph_id": graph.id,
        "regime": regime.id,
        "counts": dict(Counter(j["status"] for j in judgments)),
        "judgments": judgments,
        "unmapped": dict(sorted(skipped.items())),
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("graph")
    ap.add_argument("--out")
    args = ap.parse_args(argv)
    result = adapt(load(args.graph, Graph))
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    print(f"judgments={len(result['judgments'])} counts={result['counts']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
