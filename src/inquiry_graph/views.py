"""Projections over a preserved graph. No global belief truth or guessed chronology."""
import networkx as nx
from .model import COLLECTIONS, SIGNATURES


def objects(graph, include_rejected=False):
    return {x.id: x for f in COLLECTIONS for x in getattr(graph, f)
            if include_rejected or x.review_status != "rejected"}


def stats(graph):
    return {"conversations": len(graph.conversations),
            "source_messages": sum(len(c.messages) for c in graph.conversations),
            **{f: len(getattr(graph, f)) for f in COLLECTIONS},
            "questions": sum(n.kind == "question" for n in graph.nodes),
            "review": {s: sum(x.review_status == s for f in COLLECTIONS for x in getattr(graph, f))
                       for s in ("proposed", "confirmed", "rejected")}}


def open_questions(graph):
    msgs = {m.id: (c.id, m.ordinal) for c in graph.conversations for m in c.messages}
    nodes = {n.id: n for n in graph.nodes if n.review_status != "rejected"}
    latest, touched = {}, set()
    for e in graph.question_events:
        if e.review_status == "rejected" or e.question_id not in nodes:
            continue
        cid, ordinal = msgs[e.at_message_id]
        key = (e.question_id, e.actor_id, cid)
        if key not in latest or msgs[latest[key].at_message_id][1] < ordinal:
            latest[key] = e
        touched.add(e.question_id)
    result = []
    for (qid, actor, cid), e in sorted(latest.items()):
        # Proposed resolutions/deferments do not close the agenda without review.
        if e.status in ("resolved", "deferred", "superseded") and e.review_status == "confirmed":
            continue
        result.append({"id": qid, "text": nodes[qid].text, "actor_id": actor,
                       "conversation_id": cid, "status": e.status, "review_status": e.review_status,
                       "event_id": e.id, "anchors": [a.model_dump() for a in e.anchors]})
    for n in nodes.values():
        if n.kind == "question" and n.id not in touched:
            result.append({"id": n.id, "text": n.text, "actor_id": None, "conversation_id": None,
                           "status": "unclassified", "review_status": n.review_status,
                           "event_id": None, "anchors": [a.model_dump() for a in n.anchors]})
    return result


def network(graph):
    """Bipartite/reified graph: both relations and reasoning moves are visible nodes."""
    obj = objects(graph)
    net = nx.DiGraph()
    for n in graph.nodes:
        if n.id in obj:
            net.add_node(n.id, label=n.text, kind=n.kind, review=n.review_status)
    for r in graph.relations:
        if r.id not in obj:
            continue
        net.add_node(r.id, label=r.kind, kind="relation", review=r.review_status)
        first = next(iter(SIGNATURES[r.kind]))
        for b in r.bindings:
            if b.ref not in obj:
                continue
            source, target = (b.ref, r.id) if b.role == first else (r.id, b.ref)
            net.add_edge(source, target, role=b.role)
    for m in graph.moves:
        if m.id not in obj:
            continue
        net.add_node(m.id, label=m.kind, kind="move", review=m.review_status)
        for ref in m.input_ids:
            if ref in obj:
                net.add_edge(ref, m.id, role="input")
        for ref in m.output_ids:
            if ref in obj:
                net.add_edge(m.id, ref, role="output")
        for prior in m.after_move_ids:
            if prior in obj:
                net.add_edge(prior, m.id, role="then")
    return net


def trace(graph, identifier):
    obj = objects(graph, include_rejected=True)
    if identifier not in obj:
        raise ValueError(f"unknown graph object {identifier}")
    linked = []
    for x in obj.values():
        refs = []
        if hasattr(x, "bindings"):
            refs = [b.ref for b in x.bindings]
        elif hasattr(x, "input_ids"):
            refs = x.input_ids + x.output_ids + x.after_move_ids
        elif hasattr(x, "target_id"):
            refs = [x.target_id]
        elif hasattr(x, "question_id"):
            refs = [x.question_id] + x.answer_ids
        if identifier in refs:
            linked.append(x.model_dump(mode="json"))
    return {"object": obj[identifier].model_dump(mode="json"), "linked": linked,
            "notice": "Includes rejected annotations to preserve audit history."}


def relations_of_kind(graph, kind):
    return [r.model_dump(mode="json") for r in graph.relations
            if r.kind == kind and r.review_status != "rejected"]
