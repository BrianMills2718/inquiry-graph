#!/usr/bin/env python3
"""Write domain.graph.json (typed-graph/v1) and DOMAIN.md from the concept table below.

The domain is a conversation read as an inquiry: who said what (source), what was said (content),
how pieces relate (relations), what each participant did (moves) and how each participant's stance
and each question's status changed (events), plus the coding-session and cross-conversation records
built on top. A concept with ``where`` is implemented in this repository (file:line); a concept
without it lives elsewhere or only in the docs and is drawn dashed.

Run from the repository root: python3 docs/planning/build_domain_model.py
Adapted from claim-extraction docs/planning/build_domain_model.py.
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
M = "src/inquiry_graph/model.py"
CS = "src/inquiry_graph/coding_session.py"
ON = "docs/ontology.md"

KINDS = {
    "Source": ("Source record", "#3b6fa8", "What is actually in the conversation, before any interpretation."),
    "Content": ("Content", "#5a87bf", "What was said: concepts, claims, questions, tasks and other content nodes."),
    "Argument": ("Relations", "#7fa3cf", "Role-typed connections between content, each grounded in a quote."),
    "Process": ("Inquiry process and state", "#d9822b", "Who did what (moves), and actor-relative stance and question-status histories."),
    "Review": ("Extraction and review", "#7a8491", "How records were produced, checked, kept apart from bad output and confirmed."),
    "Session": ("Coding sessions", "#a8642b", "Claude Code and Codex session records read as conversations with tasks."),
    "Cross": ("Across conversations", "#4a525c", "Brian's verbatim positions gathered from many graphs, linked and mapped by topic."),
    "Elsewhere": ("Elsewhere or theory only", "#9aa3ad", "Named in the docs but owned by another repository, or not a record type yet."),
}

# id, label, kind, definition, source (file:line of the definition), where (code here or None)
CONCEPTS = [
    ("conversation", "Conversation", "Source",
     "One visible transcript (chat export, bridge capture, meeting or coding session) with its participants, ordered messages and a coverage note saying what was left out.",
     f"{M}:27", f"{M}:27"),
    ("participant", "Participant", "Source",
     "A speaker in a conversation, with role user, assistant or other.", f"{M}:12", f"{M}:12"),
    ("message", "Message", "Source",
     "One visible turn: speaker, ordinal and exact text; the only thing quotes are checked against.", f"{M}:18", f"{M}:18"),
    ("anchor", "Anchor", "Source",
     "A quote with its message id and Unicode start and end offsets; it must equal the message text at those offsets.",
     f"{M}:36", f"{M}:36"),
    ("content-node", "Content node", "Content",
     "Something said, of kind concept, claim, question, hypothesis, method, example, goal, reference, task or work; not the same as an utterance.",
     f"{ON}:16", f"{M}:54"),
    ("question", "Question", "Content",
     "A content node of kind question; whether it is open is recorded by question events, never by the node itself.",
     f"{ON}:20", f"{M}:51"),
    ("task", "Task", "Content",
     "A unit of work an agent lists as open in a coding session; carries the same status events as a question, plus dropped.",
     f"{ON}:18", f"{M}:50"),
    ("work", "Work", "Content",
     "A delivered product (a pull request, a commit) seen in a tool record of a coding session.", f"{ON}:18", f"{M}:50"),
    ("relation", "Relation", "Argument",
     "A reified, grounded connection of one of 13 kinds (supports, challenges, answers, supersedes...) whose players are bound by role; it can itself be challenged.",
     f"{ON}:22", f"{M}:70"),
    ("binding", "Role binding", "Argument",
     "One (role, ref) pair of a relation, such as premise -> a claim id.", f"{M}:59", f"{M}:59"),
    ("relation-signature", "Relation signature", "Argument",
     "For each relation kind, the roles it must have and the node kinds each role may bind; checked by validate().",
     f"{ON}:26", f"{M}:136"),
    ("move", "Inquiry move", "Process",
     "An act by one participant (ask, clarify, challenge, retract, reframe ... 15 kinds) with inputs, outputs, the message it happened at and previous moves.",
     f"{ON}:44", f"{M}:82"),
    ("inference-family", "Inference family", "Process",
     "Optional label on a move: induction, abduction, deduction or unspecified; the seed leaves it unspecified on purpose.",
     f"{ON}:50", f"{M}:89"),
    ("stance-event", "Stance event", "Process",
     "One participant's stance (posits, endorses, questions, rejects, suspends, retracts) toward a target, at a message; content is never belief without one.",
     f"{M}:92", f"{M}:92"),
    ("question-event", "Question event", "Process",
     "A status change of a question or task (open, answered, resolved, deferred, superseded, reopened, dropped) by one actor, at a message.",
     f"{M}:99", f"{M}:99"),
    ("open-question-agenda", "Open-question agenda", "Process",
     "The view of which questions are still open for which actor, folded from question events; an assistant's answer does not close a user's question.",
     "src/inquiry_graph/views.py:23", "src/inquiry_graph/views.py:23"),
    ("review-status", "Grounded record and review status", "Review",
     "Every semantic record carries anchors, an origin (explicit or inferred) and review status proposed, confirmed or rejected; extraction output is always proposed.",
     f"{M}:43", f"{M}:43"),
    ("extraction", "Extraction record", "Review",
     "How a graph's annotations were produced: method, provider, model, prompt version and notes.", f"{M}:110", f"{M}:110"),
    ("candidates", "Candidates", "Review",
     "The proposed nodes, relations, moves and events from one extraction, before they are ingested into a graph.",
     f"{M}:118", f"{M}:118"),
    ("graph", "Inquiry graph", "Review",
     "The canonical JSON record: conversations, all records, extractions and notes; written exclusively, never silently replaced.",
     f"{M}:126", f"{M}:126"),
    ("quarantine", "Quarantine", "Review",
     "The private folder where a failed extraction's raw response and error go, so bad output never replaces a graph.",
     "src/inquiry_graph/io.py:177", "src/inquiry_graph/io.py:177"),
    ("coding-session", "Coding session", "Session",
     "A Claude Code or Codex .jsonl session normalized into a conversation; prompts from headless runs are given to an automation participant.",
     f"{CS}:104", f"{CS}:104"),
    ("launch-kind", "Launch kind (typed or automated)", "Session",
     "Whether a person or a program typed a session's prompts, read from Claude Code entrypoint and Codex originator values.",
     f"{CS}:31", f"{CS}:34"),
    ("reply-fields", "End-of-reply fields", "Session",
     "The Session goal, Active subgoals, Done and Need anything from human lines an agent ends each reply with, read into tasks and question events.",
     f"{CS}:41", f"{CS}:183"),
    ("closure-word", "Closure word", "Session",
     "The fixed word in 'Closed: <item> (<word>)' that maps to a task status (done -> resolved, put off -> deferred ...).",
     f"{ON}:18", f"{CS}:38"),
    ("resume-digest", "Resume digest", "Session",
     "Per session: goals, open, unknown-status and closed items, delivered work and requests waiting on Brian.",
     f"{CS}:244", f"{CS}:244"),
    ("brian-position", "Brian position", "Cross",
     "A stance or question event whose actor and anchored speaker are Brian and whose quote is verbatim in that message; the evidence unit agents ask for.",
     "tools/ask_positions.py:4", "tools/ask_positions.py:22"),
    ("position-link", "Cross-conversation link", "Cross",
     "A judged pair of positions or questions Brian expressed in different conversations, proposed by embedding recall then a model judgment.",
     "src/inquiry_graph/linker.py:40", "src/inquiry_graph/linker.py:40"),
    ("topic-map", "Positions topic map", "Cross",
     "Brian's statements from chats and session prompts embedded and clustered into nested topics after the fact (topics are not stored on records).",
     "tools/position_topics.py:1", "tools/position_topics.py:91"),
    ("topic-name", "Topic name", "Cross",
     "A short model-written name for one topic of the map, carried over between builds when the topic barely changed.",
     "tools/name_topics.py:23", "tools/name_topics.py:23"),
    ("capture-contract", "Capture contract", "Review",
     "Before an expensive extraction run, a file listing every schema collection as captured or not, with cost and later-need ranges for each one left out; tools/extract_queue.py refuses a run of $2 or more without a passing one (adopted by Brian 2026-10-05).",
     "docs/design/capture-contract.md:1", "tools/capture_contract.py:43"),
    ("fit-review", "Fit review", "Review",
     "A sidecar file beside a conversation recording representation, extraction, workflow and factorization friction plus a promotion gate; evidence about the model, not authority to change it.",
     "README.md:73", "src/inquiry_graph/fit_review.py:54"),
    ("episode-profile", "Reasoning-episode profile", "Review",
     "A derived projection that assigns existing graph objects to cross-case reasoning roles so one query shape can be compared across inquiries; does not extend the core schema.",
     "src/inquiry_graph/episode_view.py:1", "src/inquiry_graph/episode_view.py:36"),
    ("frame-profile", "Frame profile", "Review",
     "A thin derived projection binding graph objects to frame content, inquiry scope and an active query; no core Frame node kind.",
     "src/inquiry_graph/frame_view.py:1", "src/inquiry_graph/frame_view.py:29"),
    ("strategy-episode", "Strategy episode", "Elsewhere",
     "A reusable reasoning strategy and its occurrences; not a record type: stored as method and example nodes joined by part_of and exemplifies.",
     f"{ON}:54", None),
    ("canonical-identity", "Cross-source identity and conflict", "Elsewhere",
     "Deciding that records from different sources are the same thing, aligning them and detecting tension; owned by onto-canon6, which consumes these graphs.",
     "docs/architecture/GOAL.md:48", None),
    ("warrant", "Warrant (support and defeat theory)", "Elsewhere",
     "A formal theory of when support beats challenge; moved to epistemic-warrant on 2026-09-29 and reached only through tools/warrant_adapter.py.",
     "docs/architecture/GOAL.md:87", None),
]

EDGES = [
    ("participant", "conversation", "takes part in"),
    ("message", "conversation", "is part of"),
    ("message", "participant", "is spoken by"),
    ("anchor", "message", "quotes exact offsets of"),
    ("content-node", "anchor", "is grounded by"),
    ("question", "content-node", "is a kind of"),
    ("task", "content-node", "is a kind of"),
    ("work", "content-node", "is a kind of"),
    ("relation", "binding", "binds players through"),
    ("binding", "content-node", "plays"),
    ("relation-signature", "relation", "constrains roles of"),
    ("move", "participant", "is done by"),
    ("move", "content-node", "takes inputs and gives outputs"),
    ("inference-family", "move", "labels"),
    ("stance-event", "participant", "is held by"),
    ("stance-event", "content-node", "targets"),
    ("question-event", "question", "changes status of"),
    ("question-event", "task", "changes status of"),
    ("open-question-agenda", "question-event", "is folded from"),
    ("review-status", "content-node", "is carried by every grounded record, like"),
    ("extraction", "candidates", "produces"),
    ("candidates", "graph", "are ingested into"),
    ("extraction", "quarantine", "on failure goes to"),
    ("graph", "conversation", "holds"),
    ("coding-session", "conversation", "is normalized into"),
    ("launch-kind", "coding-session", "labels prompts of"),
    ("reply-fields", "task", "become"),
    ("closure-word", "question-event", "sets status of"),
    ("resume-digest", "coding-session", "summarizes"),
    ("brian-position", "stance-event", "is a verbatim Brian-attributed"),
    ("brian-position", "question-event", "or a verbatim Brian-attributed"),
    ("position-link", "brian-position", "pairs two"),
    ("topic-map", "brian-position", "clusters"),
    ("topic-name", "topic-map", "labels a topic of"),
    ("strategy-episode", "move", "would group"),
    ("capture-contract", "extraction", "decides what a run captures in"),
    ("fit-review", "conversation", "reviews how the graph represented"),
    ("episode-profile", "graph", "binds reasoning roles to objects of"),
    ("frame-profile", "graph", "binds frame roles to objects of"),
    ("canonical-identity", "graph", "consumes"),
    ("warrant", "relation", "would evaluate"),
]

DISAGREEMENTS = [
    "The seed's proposed-annotation count is 858 in README.md:7, docs/project-status.md:38 and the seed itself"
    " (counted 2026-10-27), but 798 in docs/project-status.md:67 and docs/verification.md:131, which predate the"
    " 2026-09-30 continuation (open question Q7).",
    "docs/model/ARCHITECTURE.md cites line numbers that moved: ingest at src/inquiry_graph/io.py:120 is now :126,"
    " merge :149 is now :155, quarantine :171 is now :177. The package's system model (docs/planning/system-model.md)"
    " uses current lines (Q4).",
    "docs/project-status.md:94 reports 67 tests passed and :75 says issue #2 is still to be closed; on 2026-10-27"
    " make check ran 171 passed, 2 skipped, and issue #2 is closed (Q8).",
    ".agentic/repo.yaml names docs/model/ARCHITECTURE.md as the system model, while docs/index.md lists it among"
    " 'Earlier documents' replaced by docs/architecture/arc42.md and the specs. Both are still read; arc42.md points"
    " back to ARCHITECTURE.md for the runtime view, so neither alone is the model (Q4).",
    "docs/project-status.md:118 says the archive holds 0 moves because live extraction skips them; live_extract.py"
    " now has a moves prompt behind a switch (src/inquiry_graph/live_extract.py:35), but no archive run used it (Q9).",
]


def main() -> None:
    """Write both files and print counts."""
    ids = {c[0] for c in CONCEPTS}
    for s, t, _ in EDGES:
        if s not in ids or t not in ids:
            raise SystemExit(f"edge {s}->{t} names an unknown concept")
    graph = {
        "schema": "typed-graph/v1",
        "kinds": {k: {"label": v[0], "color": v[1], "explain": v[2]} for k, v in KINDS.items()},
        "layout": {"direction": "RIGHT", "algorithm": "layered"},
        "nodes": [],
        "edges": [],
    }
    for cid, label, kind, definition, source, where in CONCEPTS:
        node = {"id": cid, "label": label, "kind": kind, "explain": f"{definition} Source: {source}."}
        if where is None:
            node["dashed"] = True
        graph["nodes"].append(node)
    for i, (s, t, label) in enumerate(EDGES):
        graph["edges"].append({"id": f"e{i}", "source": s, "target": t, "label": label})
    (HERE / "domain.graph.json").write_text(json.dumps(graph, indent=1) + "\n")
    implemented = {cid: where for cid, _, _, _, _, where in CONCEPTS if where}
    manifest_path = HERE / "planning-package.json"
    if manifest_path.exists():   # keep the manifest's implemented map equal to the concept table
        manifest = json.loads(manifest_path.read_text())
        manifest["parts"]["domain_model"]["implemented"] = implemented
        manifest_path.write_text(json.dumps(manifest, indent=1) + "\n")

    lines = [
        "---",
        "description: Glossary of Inquiry Graph's domain (conversations, content, relations, moves, stance and"
        " question events, coding sessions, positions) with each concept's source and code location.",
        "---",
        "",
        "# Domain glossary",
        "",
        "Generated by `docs/planning/build_domain_model.py` together with `domain.graph.json`; edit the script,",
        "not this file. The executable contract is `src/inquiry_graph/model.py`; `docs/ontology.md` explains it.",
        "\"Not here\" marks a concept owned by another repository or present only in the docs; it is drawn dashed.",
        "",
    ]
    for kind, (klabel, _, kexplain) in KINDS.items():
        lines += [f"## {klabel}", "", kexplain, "", "| Concept | Definition | Source | In code here |",
                  "| --- | --- | --- | --- |"]
        for cid, label, ckind, definition, source, where in CONCEPTS:
            if ckind == kind:
                lines.append(f"| {label} (`{cid}`) | {definition} | `{source}` | {f'`{where}`' if where else 'not here'} |")
        lines.append("")
    lines += ["## Where the sources disagree", ""] + [f"- {d}" for d in DISAGREEMENTS] + [""]
    (HERE / "DOMAIN.md").write_text("\n".join(lines))
    print(f"concepts={len(CONCEPTS)} edges={len(EDGES)} implemented={len(implemented)} disagreements={len(DISAGREEMENTS)}")


if __name__ == "__main__":
    main()
