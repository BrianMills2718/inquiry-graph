"""Escaped, dependency-free projections; Markdown/Mermaid and DOT are interchange views."""
import html
import json
from pathlib import Path

from .views import network, open_questions, stats


def diagram_network(graph, view="all"):
    net = network(graph)
    if view == "inquiry":
        # Temporal overview keeps reified reasoning operations, not a concept-only graph.
        moves = {m.id: m for m in graph.moves if m.review_status != "rejected"}
        nodes = {n.id: n for n in graph.nodes}
        net = net.subgraph(moves).copy()
        for mid, m in moves.items():
            targets = [nodes[n].text for n in m.output_ids if n in nodes]
            label = "; ".join(targets) or m.kind
            net.nodes[mid]["label"] = f"{m.kind}: {label}"
    return net


def mermaid(graph, view="all"):
    net = diagram_network(graph, view)
    ids = {key: f"n{i}" for i, key in enumerate(sorted(net.nodes))}
    lines = ["```mermaid", "flowchart TD"]
    for key, data in sorted(net.nodes(data=True)):
        raw = f"{data.get('kind', 'object')}: {data.get('label', key)}"
        # Escape each codepoint, not just quotes: labels cannot inject Mermaid syntax.
        label = "".join(f"#{ord(c)};" if c in '\"<>&[]{}|`\\\n\r' else c for c in raw)
        lines.append(f'  {ids[key]}["{label}"]')
    for a, b, data in sorted(net.edges(data=True)):
        lines.append(f'  {ids[a]} -->|{data["role"]}| {ids[b]}')
    return "\n".join(lines + ["```", ""])


def dot(graph, view="all"):
    net = diagram_network(graph, view)
    q = lambda x: json.dumps(x, ensure_ascii=False)
    lines = ["digraph inquiry {", "rankdir=LR;"]
    for key, data in sorted(net.nodes(data=True)):
        shape = "diamond" if data.get("kind") in ("move", "relation") else "box"
        lines.append(f'{q(key)} [label={q(data.get("label", key))}, shape={shape}];')
    for a, b, data in sorted(net.edges(data=True)):
        lines.append(f'{q(a)} -> {q(b)} [label={q(data["role"])}];')
    return "\n".join(lines + ["}", ""])


# Relation kinds whose sentence carries a reason or a decision, as (head role, connective, tail role).
DECISION_SENTENCES = {
    "motivates": ("result", "because", "reason"),
    "supersedes": ("old", "was replaced by", "new"),
    "reframes": ("original", "was reframed as", "replacement"),
    "challenges": ("target", "was challenged by", "challenger"),
}
DECISION_HEADINGS = {"motivates": "Reasons", "supersedes": "Replaced", "reframes": "Reframed", "challenges": "Challenged"}
LINK_SENTENCES = {
    "depends_on": ("dependent", "depends on", "prerequisite"),
    "supports": ("conclusion", "is supported by", "premise"),
    "answers": ("question", "is answered by", "answer"),
    "distinguishes": ("left", "is distinguished from", "right"),
    "exemplifies": ("general", "is exemplified by", "example"),
    "candidate_for": ("problem", "has candidate", "candidate"),
    "part_of": ("part", "is part of", "whole"),
    "about": ("subject", "is about", "object"),
    "related_to": ("source", "is related to", "target"),
}


def _clip(text, limit=160):
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def _relation_sentences(graph, table, label_of, limit=160):
    lines = []
    for r in graph.relations:
        if r.review_status == "rejected" or r.kind not in table:
            continue
        head, connective, tail = table[r.kind]
        roles = {b.role: b.ref for b in r.bindings}
        if head not in roles or tail not in roles:
            continue
        lines.append(f"- {label_of(roles[head], limit)} — *{connective}:* {label_of(roles[tail], limit)}")
    return lines


def report(graph):
    """Readable linearization: node text is resolved so links read as sentences, not bare IDs."""
    texts = {n.id: n.text for n in graph.nodes}
    label_of = lambda ref, limit=160: html.escape(_clip(texts[ref], limit)) if ref in texts else f"`{ref}`"
    lines = ["# Inquiry graph — first-pass report", "", json.dumps(stats(graph), ensure_ascii=False), "",
             "Structural validity does not establish semantic correctness or truth. Annotations retain their review status.", "",
             "## Source coverage"]
    for c in graph.conversations:
        lines += [f"\n**{html.escape(c.title)}**\n", html.escape(c.coverage_note)]
    lines += ["\n## Open agenda", "", "Rows are actor/context-relative; an assistant answer does not close a user's question."]
    for row in open_questions(graph):
        lines += [f"\n### {html.escape(row['text'])}", f"`{row['id']}` · {row['status']} · {row['review_status']}",
                  f"Actor: `{row['actor_id']}` · context: `{row['conversation_id']}`"]
    lines += ["\n## Decisions and reasons", "",
              "Reasons, replacements, reframings and challenges, in recorded order. Each line reads: subject — *link:* other side."]
    for kind in DECISION_SENTENCES:
        group = _relation_sentences(graph, {kind: DECISION_SENTENCES[kind]}, label_of)
        if group:
            lines += [f"\n### {DECISION_HEADINGS[kind]}", ""] + group
    lines += ["\n## Other links", ""]
    lines += _relation_sentences(graph, LINK_SENTENCES, label_of, limit=100)
    lines += ["\n## Recorded moves"]
    for m in graph.moves:
        if m.review_status == "rejected":
            continue
        ins = "; ".join(label_of(i, 80) for i in m.input_ids) or "(none)"
        outs = "; ".join(label_of(o, 80) for o in m.output_ids) or "(none)"
        lines += [f"\n**{m.kind}** · `{m.id}` · actor `{m.actor_id}` · {m.review_status}",
                  f"Inputs: {ins}", f"Outputs: {outs}",
                  "", "> " + html.escape(m.anchors[0].quote).replace("\n", "\n> ")]
    return "\n".join(lines) + "\n"


def html_view(graph):
    """Offline linked-object inspector. No script, CDN, telemetry, or graph-layout engine."""
    from .views import objects, trace
    items = objects(graph, include_rejected=True)
    ids = {key: f"obj-{i}" for i,key in enumerate(items)}
    esc = html.escape
    sections = []
    for key, obj in items.items():
        links = []
        for entry in trace(graph, key)["linked"]:
            links.append(f'<a href="#{ids[entry["id"]]}">{esc(entry["id"])}</a>')
        label = getattr(obj, "text", getattr(obj, "kind", getattr(obj, "status", getattr(obj,"stance","object"))))
        sections.append(f'<section id="{ids[key]}"><h2>{esc(str(label))}</h2><p>{esc(key)} | {obj.review_status} | {obj.origin}</p>'
                        f'<p>{" · ".join(links)}</p><details><summary>Grounding and record</summary><pre>{esc(obj.model_dump_json(indent=2))}</pre></details></section>')
    agenda = "".join(f'<li><a href="#{ids[r["id"]]}">{esc(r["text"])}</a> — {r["status"]}, {r["review_status"]}</li>'
                     for r in open_questions(graph))
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Inquiry Graph</title><style>body{font:16px system-ui;max-width:1000px;margin:2rem auto;padding:1rem}section{border-top:1px solid;padding:1rem 0}pre{white-space:pre-wrap;overflow-wrap:anywhere}a{overflow-wrap:anywhere}h2{font-size:1.15rem}</style><h1>Inquiry Graph</h1><p>Offline linked-record inspector. Use browser Find to search; select a question or linked record. Proposed annotations are not verified beliefs.</p><h2>Open agenda</h2><ul>' + agenda + '</ul>' + ''.join(sections) + '</html>'
