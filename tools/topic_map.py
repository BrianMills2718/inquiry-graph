"""Build a private, offline topic map from cached Inquiry Graph linker output.

Topic communities use the same nearest-neighbour/Louvain method as the retained
prototype. The resulting HTML contains private source quotes and must stay under
``private/xconv/``. Topic labels use the configured Codex subscription route;
linker pairs are read from cache and are never re-judged here.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import networkx as nx
from pydantic import BaseModel, ConfigDict, Field

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from inquiry_graph.linker import cosine  # noqa: E402
from inquiry_graph.model import Graph  # noqa: E402

DEFAULT_LINKER = ROOT / "private/xconv/scale_run/linker"
DEFAULT_CORPUS = ROOT / "private/xconv/scale_run_codex_rerun_20260930/corpus.json"
DEFAULT_OUTPUT = ROOT / "private/xconv/scale_run/map/index.html"
TEMPLATE = ROOT / "tools/topic_map_template.html"
MODEL = "codex/gpt-5.6-luna"
EXPECTED_CHAT_COUNT = 30


class TopicName(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    topic: int = Field(ge=1)
    name: str = Field(min_length=2, max_length=70)
    summary: str = Field(min_length=12, max_length=240)


class TopicNameSet(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    names: list[TopicName]


def digest_inputs(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        digest.update(path.name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def topic_groups(positions: list[dict], vectors: dict[str, list[float]]) -> list[list[str]]:
    graph = nx.Graph()
    ids = [item["id"] for item in positions]
    graph.add_nodes_from(ids)
    for a in ids:
        nearest = sorted(
            ((cosine(vectors[a], vectors[b]), b) for b in ids if b != a),
            reverse=True,
        )[:6]
        for rank, (similarity, b) in enumerate(nearest):
            # Preserve the prototype's two-nearest-neighbour floor so every
            # position remains assigned, even when its embedding is isolated.
            if similarity >= 0.5 or rank < 2:
                graph.add_edge(a, b, weight=similarity)
    communities = nx.community.louvain_communities(
        graph, weight="weight", resolution=1.0, seed=7
    )
    return sorted((sorted(group) for group in communities), key=len, reverse=True)


def load_or_make_groups(
    positions: list[dict],
    vectors: dict[str, list[float]],
    fingerprint: str,
    cache_path: Path,
) -> list[list[str]]:
    if cache_path.exists():
        cached = json.loads(cache_path.read_text(encoding="utf-8"))
        if cached.get("source_fingerprint") == fingerprint:
            groups = cached["groups"]
            if sorted(item for group in groups for item in group) == sorted(
                item["id"] for item in positions
            ):
                return groups
    groups = topic_groups(positions, vectors)
    cache_path.write_text(
        json.dumps({"source_fingerprint": fingerprint, "groups": groups}, indent=2) + "\n",
        encoding="utf-8",
    )
    return groups


def validate_topic_names(names: list[dict], topic_count: int) -> list[dict]:
    parsed = TopicNameSet.model_validate({"names": names}).names
    ids = [item.topic for item in parsed]
    if sorted(ids) != list(range(1, topic_count + 1)) or len(ids) != topic_count:
        raise ValueError(f"topic names must cover 1..{topic_count} exactly once; got {ids}")
    for item in parsed:
        words = item.name.split()
        if not 2 <= len(words) <= 5:
            raise ValueError(f"topic {item.topic} name must contain 2–5 words")
    return [item.model_dump() for item in sorted(parsed, key=lambda item: item.topic)]


def name_topics(
    groups: list[list[str]], by_id: dict[str, dict], fingerprint: str, cache_path: Path,
) -> list[dict]:
    if cache_path.exists():
        cached = json.loads(cache_path.read_text(encoding="utf-8"))
        if cached.get("source_fingerprint") == fingerprint and cached.get("model") == MODEL:
            return validate_topic_names(cached.get("names", []), len(groups))

    from llm_client import ObservabilityContentPolicy, call_llm_structured

    blocks = []
    for index, members in enumerate(groups, 1):
        examples = []
        for item_id in members[:12]:
            item = by_id[item_id]
            context = f" ({item['chat_title']}, {item['date'] or 'date unknown'})"
            examples.append(f"- [{item['kind']}; stance: {item['stance']}]{context} {item['text']}")
        blocks.append(f"Topic {index}, {len(members)} positions:\n" + "\n".join(examples))
    prompt = (
        "These groups contain position summaries and questions extracted from one person's "
        "conversations. For each group, choose a concrete, plain-English topic name of 2–5 "
        "words and a one-sentence summary. Describe only the shared subject represented by "
        "the examples. Do not invent a position, conflict, or conclusion that the examples "
        "do not establish. These labels are interpretations of the grouping, not quotations. "
        "Return each topic number exactly once.\n\n" + "\n\n".join(blocks)
    )
    attempt = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    trace_id = f"inquiry-graph/topic-map/names/{fingerprint[:12]}/{attempt}"
    model_justification = (
        "Use Brian's active Codex subscription for private topic naming; the OpenRouter "
        "campaign stopped because its account could not afford the reference call."
    )
    result, metadata = call_llm_structured(
        MODEL,
        [{"role": "user", "content": prompt}],
        response_model=TopicNameSet,
        reasoning_effort="low",
        model_policy="enforce_allowlist",
        model_justification=model_justification,
        task="synthesis",
        trace_id=trace_id,
        max_budget=1.00,
        codex_transport="cli",
        sandbox_mode="read-only",
        approval_policy="never",
        working_directory=str(ROOT),
        observability_content_policy=ObservabilityContentPolicy(mode="metadata_only"),
    )
    validated = validate_topic_names(
        [item.model_dump() for item in result.names], len(groups)
    )
    cache_path.write_text(
        json.dumps(
            {"source_fingerprint": fingerprint, "model": MODEL, "names": validated},
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    cost = getattr(metadata, "cost", None)
    print(f"topic naming trace={trace_id} model={MODEL} cost={cost if cost is not None else 'n/a'}")
    return validated


def _evidence(anchor, messages: dict, title: str, chat_id: str) -> dict:
    message = messages[anchor.message_id]
    return {
        "source_id": chat_id,
        "source_label": title,
        "date": (message.timestamp or "")[:10] or None,
        "locator": f"message {message.ordinal}",
        "quote": anchor.quote,
    }


def build_chat_view(source: Graph, position_by_id: dict[str, dict], source_revision: str) -> dict:
    conversation = source.conversations[0]
    messages = {message.id: message for message in conversation.messages}
    brian = next((person.id for person in conversation.participants if person.role == "user"), None)
    positions = {
        item_id: item
        for item_id, item in position_by_id.items()
        if item["chat_id"] == conversation.id
    }
    stance_message_by_node: dict[str, object] = {}
    for event in source.stance_events:
        if event.actor_id == brian:
            stance_message_by_node.setdefault(event.target_id, messages[event.at_message_id])

    nodes = []
    known_source_nodes = {item.id for item in source.nodes}
    for item_id, position in positions.items():
        if item_id not in known_source_nodes:
            raise ValueError(f"position {item_id} is missing from its source graph")
        message = stance_message_by_node.get(item_id)
        item_evidence = [{
            "source_id": conversation.id,
            "source_label": conversation.title,
            "date": position["date"],
            "locator": f"message {message.ordinal}" if message else None,
            "quote": position["quote"],
        }]
        nodes.append({
            "id": item_id,
            "kind": position["kind"],
            "label": position["text"],
            "epistemic_status": "inferred",
            "attributes": {
                "date": position["date"],
                "stance": position["stance"],
                "question_status": position["question_status"],
                "personally_stated": True,
            },
            "evidence": item_evidence,
        })

    relations = []
    position_ids = set(positions)
    for item in source.relations:
        # A relation is displayed only if all of its source graph role bindings
        # are present in this Brian-position projection. That preserves its
        # meaning without silently dropping an assistant or context binding.
        if not item.bindings or any(binding.ref not in position_ids for binding in item.bindings):
            continue
        relation_node_id = f"source-relation:{item.id}"
        roles = [binding.role for binding in item.bindings]
        nodes.append({
            "id": relation_node_id,
            "kind": "source relation",
            "label": item.kind,
            "summary": "Extracted relation represented through its role bindings.",
            "epistemic_status": "inferred",
            "attributes": {"binding_roles": ", ".join(roles), "binding_count": len(roles)},
            "evidence": [_evidence(anchor, messages, conversation.title, conversation.id)
                         for anchor in item.anchors],
        })
        binary = len(item.bindings) == 2
        for index, binding in enumerate(item.bindings):
            if binary and index == 0:
                start, end, directed = binding.ref, relation_node_id, True
            elif binary:
                start, end, directed = relation_node_id, binding.ref, True
            else:
                start, end, directed = relation_node_id, binding.ref, False
            relations.append({
                "id": f"role:{item.id}:{index}",
                "kind": f"role: {binding.role}",
                "source": start,
                "target": end,
                "directed": directed,
                "epistemic_status": "inferred",
                "attributes": {"relation_kind": item.kind},
                "evidence": [],
            })

    return {
        "schema_version": "relation-graph-view/v1",
        "graph_id": f"conversation:{conversation.id}",
        "title": f"{conversation.title} · extracted inquiry graph",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_revision": source_revision,
        "nodes": nodes,
        "relations": relations,
        "initial_state": {},
    }


def build_topic_view(index: int, members: list[str], positions: dict[str, dict],
                     links: list[dict], source_revision: str) -> dict:
    ids = set(members)
    nodes = []
    for item_id in members:
        item = positions[item_id]
        nodes.append({
            "id": item_id,
            "kind": item["kind"],
            "label": item["text"],
            "epistemic_status": "inferred",
            "attributes": {
                "date": item["date"],
                "conversation": item["chat_title"],
                "stance": item["stance"],
                "question_status": item.get("question_status"),
            },
            "evidence": [{
                "source_id": item["chat_id"],
                "source_label": item["chat_title"],
                "date": item["date"],
                "locator": "position evidence",
                "quote": item["quote"],
            }],
        })
    topic_links = []
    for link_index, link in enumerate(links):
        if link["relation"] == "unrelated" or link["a"] not in ids or link["b"] not in ids:
            continue
        topic_links.append({
            "id": f"position-link:{index}:{link_index}",
            "kind": link["relation"],
            "source": link["a"],
            "target": link["b"],
            "directed": False,
            "epistemic_status": "inferred",
            "attributes": {"rationale": link["rationale"], "cosine_similarity": link["cosine"]},
            "evidence": [],
        })
    return {
        "schema_version": "relation-graph-view/v1",
        "graph_id": f"topic-detail:{index}",
        "title": f"Topic detail · {len(nodes)} positions",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_revision": source_revision,
        "nodes": nodes,
        "relations": topic_links,
        "initial_state": {},
    }


def build_overview(groups: list[list[str]], names: list[dict], positions: dict[str, dict],
                   links: list[dict], source_revision: str) -> tuple[dict, list[dict]]:
    topic_of = {item_id: index for index, group in enumerate(groups) for item_id in group}
    topics = []
    for index, (members, name) in enumerate(zip(groups, names, strict=True)):
        topics.append({
            "id": index,
            "name": name["name"],
            "summary": name["summary"],
            "members": members,
            "chats": sorted({positions[item_id]["chat_title"] for item_id in members}),
            "chat_count": len({positions[item_id]["chat_id"] for item_id in members}),
        })

    aggregates: dict[tuple[int, int], Counter] = defaultdict(Counter)
    for link in links:
        if link["relation"] == "unrelated":
            continue
        a, b = topic_of[link["a"]], topic_of[link["b"]]
        if a != b:
            aggregates[tuple(sorted((a, b)))][link["relation"]] += 1
    overview_relations = []
    for index, ((a, b), counts) in enumerate(sorted(aggregates.items())):
        attributes = {f"count_{kind}": count for kind, count in sorted(counts.items())}
        attributes["total_links"] = sum(counts.values())
        overview_relations.append({
            "id": f"topic-link:{index}",
            "kind": " + ".join(sorted(counts)),
            "source": f"topic:{a}",
            "target": f"topic:{b}",
            "directed": False,
            "epistemic_status": "aggregate",
            "attributes": attributes,
            "evidence": [],
        })

    graph = {
        "schema_version": "relation-graph-view/v1",
        "graph_id": "inquiry-map:all-topics",
        "title": "Topics across your conversations",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_revision": source_revision,
        "nodes": [{
            "id": f"topic:{item['id']}",
            "kind": "topic",
            "label": item["name"],
            "summary": item["summary"],
            "epistemic_status": "interpretive",
            "attributes": {"positions": len(item["members"]), "conversations": item["chat_count"]},
            "evidence": [],
        } for item in topics],
        "relations": overview_relations,
        "initial_state": {},
    }
    return graph, topics


def graph_paths(corpus: dict) -> list[tuple[dict, Path]]:
    records = corpus.get("chats")
    if not isinstance(records, list) or len(records) != EXPECTED_CHAT_COUNT:
        raise ValueError(f"expected {EXPECTED_CHAT_COUNT} corpus chats; found {len(records or [])}")
    result = []
    for record in records:
        if record.get("graph_valid") is not True:
            raise ValueError(f"chat {record.get('id8', '<unknown>')} is not marked graph_valid")
        short_id = record["id8"]
        candidates = [ROOT / f"private/xconv/{short_id}.graph.json",
                      ROOT / f"private/xconv/scale/{short_id}.graph.json"]
        existing = [path for path in candidates if path.is_file()]
        if len(existing) != 1:
            raise FileNotFoundError(f"expected exactly one graph for chat {short_id}; found {len(existing)}")
        result.append((record, existing[0]))
    return result


def assert_view(view: dict) -> None:
    nodes = view["nodes"]
    relations = view["relations"]
    node_ids = [node["id"] for node in nodes]
    relation_ids = [relation["id"] for relation in relations]
    if len(node_ids) != len(set(node_ids)):
        raise ValueError(f"duplicate node ids in {view['graph_id']}")
    if len(relation_ids) != len(set(relation_ids)):
        raise ValueError(f"duplicate relation ids in {view['graph_id']}")
    known = set(node_ids)
    if known.intersection(relation_ids):
        raise ValueError(f"node/relation id collision in {view['graph_id']}")
    dangling = [r["id"] for r in relations if r["source"] not in known or r["target"] not in known]
    if dangling:
        raise ValueError(f"dangling relations in {view['graph_id']}: {dangling[:4]}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--linker-dir", type=Path, default=DEFAULT_LINKER)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--component-bundle", type=Path, required=True)
    parser.add_argument("--refresh-topic-names", action="store_true")
    args = parser.parse_args()

    output = args.output.expanduser().resolve()
    private = (ROOT / "private/xconv").resolve()
    if not output.is_relative_to(private):
        raise ValueError(f"quote-bearing output must be under {private}")
    linker_dir = args.linker_dir.expanduser().resolve()
    corpus_path = args.corpus.expanduser().resolve()
    bundle_path = args.component_bundle.expanduser().resolve()
    for required in (linker_dir / "positions.json", linker_dir / "links.json",
                     linker_dir / "vectors.json", corpus_path, bundle_path, TEMPLATE):
        if not required.is_file():
            raise FileNotFoundError(required)

    positions_list = json.loads((linker_dir / "positions.json").read_text(encoding="utf-8"))
    raw_links = json.loads((linker_dir / "links.json").read_text(encoding="utf-8"))["links"]
    vectors = json.loads((linker_dir / "vectors.json").read_text(encoding="utf-8"))
    corpus = json.loads(corpus_path.read_text(encoding="utf-8"))
    sources = [linker_dir / name for name in ("positions.json", "links.json", "vectors.json")]
    sources.extend([corpus_path])
    fingerprint = digest_inputs(sources)
    source_revision = f"sha256:{fingerprint}"
    position_by_id = {item["id"]: item for item in positions_list}
    if len(position_by_id) != len(positions_list) or not positions_list:
        raise ValueError("position IDs must be nonempty and unique")
    if set(position_by_id) != set(vectors):
        raise ValueError("position and vector ID sets differ")
    for link in raw_links:
        if link["a"] not in position_by_id or link["b"] not in position_by_id:
            raise ValueError("cached link references a missing position")
        if position_by_id[link["a"]]["chat_id"] == position_by_id[link["b"]]["chat_id"]:
            raise ValueError("cached cross-chat link joins positions from one chat")

    output.parent.mkdir(parents=True, exist_ok=True)
    groups = load_or_make_groups(
        positions_list, vectors, fingerprint, output.parent / "communities.json"
    )
    if sorted(item for group in groups for item in group) != sorted(position_by_id):
        raise ValueError("topic communities do not partition the source positions")
    topic_of = {item_id: index for index, group in enumerate(groups) for item_id in group}
    overview_pairs = {
        tuple(sorted((topic_of[link["a"]], topic_of[link["b"]])))
        for link in raw_links
        if link["relation"] != "unrelated" and topic_of[link["a"]] != topic_of[link["b"]]
    }
    if len(groups) > 120 or len(overview_pairs) > 400:
        raise ValueError("the overview would exceed the shared relation viewer's limits")
    for index, group in enumerate(groups):
        internal_count = sum(
            link["relation"] != "unrelated" and topic_of[link["a"]] == index and topic_of[link["b"]] == index
            for link in raw_links
        )
        if len(group) > 120 or internal_count > 400:
            raise ValueError(f"topic {index} exceeds the shared relation viewer's limits")

    chat_views = {}
    chat_list = []
    seen_chat_ids = set()
    for corpus_record, path in graph_paths(corpus):
        source = Graph.model_validate_json(path.read_text(encoding="utf-8"))
        if len(source.conversations) != 1:
            raise ValueError(f"expected one conversation in graph {corpus_record['id8']}")
        conversation = source.conversations[0]
        if conversation.id in seen_chat_ids:
            raise ValueError("duplicate conversation IDs in the 30-chat source corpus")
        seen_chat_ids.add(conversation.id)
        view = build_chat_view(source, position_by_id, source_revision)
        assert_view(view)
        if len(view["nodes"]) > 120 or len(view["relations"]) > 400:
            raise ValueError(
                f"conversation {corpus_record['id8']} has {len(view['nodes'])} nodes and "
                f"{len(view['relations'])} relations; filter support is needed before it can be shown"
            )
        chat_views[conversation.id] = view
        chat_list.append({
            "id": conversation.id,
            "title": conversation.title,
            "date": (conversation.messages[0].timestamp or "")[:10],
            "positions": sum(item["chat_id"] == conversation.id for item in positions_list),
            "source_id": corpus_record["id8"],
        })
    chat_list.sort(key=lambda item: (item["date"], item["title"]))
    position_chat_ids = {item["chat_id"] for item in positions_list}
    if position_chat_ids != seen_chat_ids or len(position_chat_ids) != EXPECTED_CHAT_COUNT:
        raise ValueError("position source chats do not exactly match the 30 validated conversation graphs")

    # Complete local structural work before the Codex request so malformed
    # source graphs cannot spend the user's subscription call.
    topic_views = {
        str(index): build_topic_view(index, group, position_by_id, raw_links, source_revision)
        for index, group in enumerate(groups)
    }
    for view in topic_views.values():
        assert_view(view)

    names_path = output.parent / "topic_names.json"
    if args.refresh_topic_names:
        names_path.unlink(missing_ok=True)
    topic_names = name_topics(groups, position_by_id, fingerprint, names_path)
    overview, topics = build_overview(
        groups, topic_names, position_by_id, raw_links, source_revision
    )
    assert_view(overview)
    views = {
        "overview": overview,
        "topics": topic_views,
        "chats": chat_views,
        "chat_list": chat_list,
        "topic_list": [
            {key: topic[key] for key in ("id", "name", "summary", "members", "chats", "chat_count")}
            for topic in topics
        ],
    }
    if len(chat_views) != EXPECTED_CHAT_COUNT:
        raise ValueError(f"built {len(chat_views)} conversation views; expected {EXPECTED_CHAT_COUNT}")
    non_unrelated = sum(link["relation"] != "unrelated" for link in raw_links)
    unrelated = len(raw_links) - non_unrelated
    counts = {
        "chats": len(views["chats"]),
        "positions": len(positions_list),
        "topic_count": len(topics),
        "typed_links": non_unrelated,
        "unrelated_hidden": unrelated,
        "cross_topic_aggregate_links": len(overview["relations"]),
    }
    views["counts"] = counts

    bundle = bundle_path.read_bytes()
    encoded_bundle = base64.b64encode(bundle).decode("ascii")
    data = json.dumps(views, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    template = TEMPLATE.read_text(encoding="utf-8")
    html = template.replace("/*__MAP_DATA__*/null", data)
    html = html.replace("__RELATION_GRAPH_BUNDLE_BASE64__", encoded_bundle)
    output.write_text(html, encoding="utf-8")
    if "/*__MAP_DATA__*/" in html or "__RELATION_GRAPH_BUNDLE_BASE64__" in html:
        raise ValueError("map template placeholders were not fully replaced")
    print(
        f"built {counts['chats']} chats, {counts['positions']} positions, {counts['topic_count']} topics, "
        f"{counts['typed_links']} typed links ({counts['unrelated_hidden']} unrelated hidden); "
        f"topic overview has {counts['cross_topic_aggregate_links']} aggregated cross-topic links -> {output}"
    )


if __name__ == "__main__":
    main()
