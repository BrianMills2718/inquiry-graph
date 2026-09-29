"""Relation-typed links between one person's positions in different conversations.

Same-claim alignment finds almost nothing across chats: views get related,
extended and reworded, rarely restated (see evaluation/cross_conversation).
This module links positions by a typed judgment instead:

1. collect the person's positions and questions from per-chat graphs, with
   stance, question status, chat title, date and verbatim quote;
2. recall candidate pairs by embedding similarity, restricted to different
   chats and to each item's nearest neighbours;
3. label every recalled pair with one typed model judgment. `unrelated` is kept
   as a judged negative, never silently dropped.

Embedding similarity alone never creates a link.
"""
import math
from collections import defaultdict
from typing import Literal

from pydantic import BaseModel, Field

from .model import Graph

LINKER_VERSION = "linker-1.2.0"
RelationType = Literal["same", "agrees", "extends", "pulls_against", "evolves", "unrelated"]


class Position(BaseModel):
    id: str
    chat_id: str
    chat_title: str
    date: str | None
    kind: str
    stance: str
    text: str
    quote: str
    question_status: str | None = None


class Link(BaseModel):
    a: str
    b: str
    relation: RelationType
    rationale: str
    cosine: float


def collect_positions(graph: Graph, actor_id: str) -> list[Position]:
    """The actor's stances (one per target node) plus the latest status of questions they raised."""
    conv = graph.conversations[0]
    msgs = {m.id: m for m in conv.messages}
    nodes = {n.id: n for n in graph.nodes}
    status = {}
    for e in sorted(graph.question_events, key=lambda e: msgs[e.at_message_id].ordinal):
        status[e.question_id] = e.status
    out, seen = [], set()
    for s in sorted(graph.stance_events, key=lambda s: msgs[s.at_message_id].ordinal):
        if s.actor_id != actor_id or s.target_id in seen:
            continue
        seen.add(s.target_id)
        node, msg = nodes[s.target_id], msgs[s.at_message_id]
        out.append(Position(id=s.target_id, chat_id=conv.id, chat_title=conv.title,
                            date=(msg.timestamp or "")[:10] or None, kind=node.kind, stance=s.stance,
                            text=node.text, quote=s.anchors[0].quote, question_status=status.get(node.id)))
    return out


def cosine(u: list[float], v: list[float]) -> float:
    dot = sum(a * b for a, b in zip(u, v))
    nu, nv = math.sqrt(sum(a * a for a in u)), math.sqrt(sum(b * b for b in v))
    if nu == 0 or nv == 0:
        raise ValueError("zero-length embedding")
    return dot / (nu * nv)


def recall_pairs(positions: list[Position], vectors: dict[str, list[float]],
                 k: int = 4, floor: float = 0.45) -> list[tuple[str, str, float]]:
    """Cross-chat pairs where either side is among the other's k nearest cross-chat neighbours."""
    chat = {p.id: p.chat_id for p in positions}
    ids = [p.id for p in positions]
    best = defaultdict(list)
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            if chat[a] == chat[b]:
                continue
            c = cosine(vectors[a], vectors[b])
            if c >= floor:
                best[a].append((c, b))
                best[b].append((c, a))
    pairs = {}
    for a, cands in best.items():
        for c, b in sorted(cands, reverse=True)[:k]:
            pairs[tuple(sorted((a, b)))] = c
    return sorted(((a, b, c) for (a, b), c in pairs.items()), key=lambda t: -t[2])


class _Judgment(BaseModel):
    pair: int
    shared_subject: str | None = Field(
        description="the specific subject BOTH items are about (e.g. 'whether induction and abduction are distinct'), "
                    "or null if they only share a broad theme")
    relation: RelationType
    rationale: str = Field(description="one sentence naming what connects or separates the two")


class _Batch(BaseModel):
    judgments: list[_Judgment]


JUDGE_PROMPT = """Each numbered pair holds two positions or questions that {person} expressed in DIFFERENT
conversations (chat title and date given). Label how they relate, from {person}'s point of view:
- same: the same position or question, restated;
- agrees: both make claims about the SAME specific subject and the claims support each other
  (merely being consistent, or one being a background fact for the other, is 'unrelated');
- extends: the later one explicitly builds on, refines or applies the earlier one's SPECIFIC idea
  (a later item that is merely on a neighbouring topic is 'unrelated');
- pulls_against: they are in tension or conflict (would be hard to hold both without qualification);
- evolves: the view on the same topic changed between the chats (say from what to what);
- unrelated: only superficially similar (shared vocabulary, different subject).
First decide the specific subject both items are about. A broad shared theme ("formal models",
"ontology", "inference", "the project") is NOT a shared subject. If there is no specific shared subject,
set shared_subject to null and relation to 'unrelated'. Only 'pulls_against' when holding both would
need a qualification; only 'evolves' when the later chat takes a different view on that same subject.
Be strict: prefer 'unrelated' over a weak link. Return one judgment per pair.

{pairs}"""


def judge_pairs(pairs, positions: dict[str, Position], model: str, person: str,
                trace_prefix: str, batch_size: int = 15) -> tuple[list[Link], list[str], float]:
    from llm_client import call_llm_structured
    links, traces, cost = [], [], 0.0
    for start in range(0, len(pairs), batch_size):
        batch = pairs[start:start + batch_size]
        lines = []
        for n, (a, b, _) in enumerate(batch, 1):
            pa, pb = positions[a], positions[b]
            lines.append(f"{n}. A [{pa.chat_title}, {pa.date}] ({pa.stance}) {pa.text}\n"
                         f"   B [{pb.chat_title}, {pb.date}] ({pb.stance}) {pb.text}")
        trace = f"{trace_prefix}/judge-{start // batch_size:03d}"
        res, meta = call_llm_structured(
            model, [{"role": "user", "content": JUDGE_PROMPT.format(person=person, pairs="\n".join(lines))}],
            response_model=_Batch, reasoning_effort="medium", model_policy="enforce_allowlist",
            task="judging", trace_id=trace, max_budget=2.00)
        got = {j.pair: j for j in res.judgments}
        if sorted(got) != list(range(1, len(batch) + 1)):
            raise ValueError(f"{trace}: judgments for pairs {sorted(got)}, expected 1..{len(batch)}")
        for n, (a, b, c) in enumerate(batch, 1):
            j = got[n]
            relation = "unrelated" if not j.shared_subject else j.relation
            links.append(Link(a=a, b=b, relation=relation, cosine=round(c, 3),
                              rationale=(f"[{j.shared_subject}] " if j.shared_subject else "") + j.rationale))
        traces.append(trace)
        cost += meta.cost
    return links, traces, cost


def embed_positions(positions: list[Position], model: str, trace_id: str) -> tuple[dict[str, list[float]], float]:
    from llm_client import embed
    vectors, cost = {}, 0.0
    for start in range(0, len(positions), 200):
        chunk = positions[start:start + 200]
        res = embed(model, [p.text for p in chunk], task="embedding",
                    trace_id=f"{trace_id}-{start // 200:02d}", max_budget=1.00)
        if len(res.embeddings) != len(chunk):
            raise ValueError("embedding count mismatch")
        vectors.update({p.id: v for p, v in zip(chunk, res.embeddings)})
        cost += res.cost
    return vectors, cost
