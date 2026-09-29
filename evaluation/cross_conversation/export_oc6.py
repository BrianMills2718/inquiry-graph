"""Export Brian's extracted stances into onto-canon6 and read back identity and tension (C3, C4).

Run with the onto-canon6 environment and ONTO_CANON6_HOME pointing at the pinned
tree (see results.md). onto-canon6 is consumed read-only through its public API:
- the alignment extension groups paraphrases of the same proposition across chats
  (embedding recall plus its typed restatement judge);
- each Brian stance becomes `ig:holds_stance(holder, stance, proposition)` where the
  proposition is an entity identified by its alignment cluster;
- candidates are auto-accepted and promoted (labelled inquiry-graph:auto-accept;
  this is not human review), and the epistemic extension's tension report is read.

Writes private/xconv/oc6/: the review DB, export.json (route B's material) and loss.json.
"""
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRIV = ROOT / "private/xconv"
OUT = PRIV / "oc6"
CHATS = ["6ab8563b", "6ab96260", "69c07755", "6a988a7a", "6a171ac3"]
PROFILE = ("general_purpose_open", "0.1.0")
OPPOSED = {("posits", "rejects"), ("endorses", "rejects"), ("posits", "retracts"), ("endorses", "retracts")}

if not os.environ.get("ONTO_CANON6_HOME"):
    sys.exit("ONTO_CANON6_HOME must point at the pinned onto-canon6 tree (config/, profiles/, ontology_packs/)")

from onto_canon6 import AssertionService, GovernanceService  # noqa: E402
from onto_canon6.extensions.alignment.models import ClaimTextV1  # noqa: E402
from onto_canon6.extensions.alignment.scoring import EmbeddingCosineScorer, JudgedRestatementScorer  # noqa: E402
from onto_canon6.extensions.alignment.service import AlignmentService  # noqa: E402
from onto_canon6.extensions.epistemic.service import EpistemicService  # noqa: E402


def load_stances():
    rows = []
    for cid in CHATS:
        g = json.loads((PRIV / f"{cid}.graph.json").read_text(encoding="utf-8"))
        conv = g["conversations"][0]
        nodes = {n["id"]: n for n in g["nodes"]}
        msgs = {m["id"]: m for m in conv["messages"]}
        for s in g["stance_events"]:
            if s["actor_id"] != "participant:brian":
                continue
            a = s["anchors"][0]
            rows.append({"chat": cid, "chat_title": conv["title"], "stance_id": s["id"], "stance": s["stance"],
                         "node_id": s["target_id"], "node_kind": nodes[s["target_id"]]["kind"],
                         "text": nodes[s["target_id"]]["text"], "message": msgs[a["message_id"]],
                         "span": {"start_char": a["start"], "end_char": a["end"], "text": a["quote"]}})
    return rows


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    db = OUT / "review.sqlite3"
    if db.exists():
        db.unlink()
    rows = load_stances()
    props = {}
    for r in rows:
        props.setdefault(r["node_id"], r["text"])
    claims = [ClaimTextV1(claim_id=k, text=v) for k, v in props.items()]
    print(f"{len(rows)} Brian stances over {len(claims)} propositions from {len(CHATS)} chats")

    verdict_file = OUT / "judge_verdicts.json"
    recorded = None
    if verdict_file.exists():
        recorded = {tuple(k.split("||")): v for k, v in json.loads(verdict_file.read_text()).items()}
    scorer = JudgedRestatementScorer(
        question="Do these two statements express the same position or the same question, "
                 "so that a person holding one holds the other?",
        recall=EmbeddingCosineScorer(), recorded_verdicts=recorded)
    clusters, scores = AlignmentService(db_path=db).compute_and_persist(claims, scorer=scorer)
    if recorded is None:
        verdict_file.write_text(json.dumps({"||".join(k): v for k, v in scores.verdicts.items()}, indent=0))
    cluster_of = {m.claim_id: c.cluster_id for c in clusters for m in c.members}
    print(f"alignment: {len(clusters)} multi-member clusters; judged pairs {len(scores.verdicts)} "
          f"(same={sum(scores.verdicts.values())}); traces {scores.trace_ids}")

    gov = GovernanceService(db_path=db)
    assertions = AssertionService(db_path=gov.store.db_path)
    submitted, rejected, reused, promoted_ids = [], Counter(), Counter(), {}
    for r in rows:
        prop = cluster_of.get(r["node_id"], r["node_id"])
        payload = {"predicate": "ig:holds_stance", "roles": {
            "holder": [{"kind": "value", "value_kind": "string", "value": "brian"}],
            "stance": [{"kind": "value", "value_kind": "string", "value": r["stance"]}],
            "proposition": [{"kind": "entity", "entity_id": f"ent:prop:{prop}", "entity_type": "oc:Proposition"}]}}
        try:
            res = gov.submit_candidate_assertion(
                payload=payload, profile_id=PROFILE[0], profile_version=PROFILE[1],
                submitted_by="inquiry-graph:live-2.2.0", source_kind="chat_transcript",
                source_ref=f"{r['message']['id']}", source_label=r["chat_title"],
                source_metadata={"chat": r["chat"], "stance_id": r["stance_id"], "node_kind": r["node_kind"]},
                source_text=r["message"]["text"], claim_text=f"Brian {r['stance']}: {r['text']}",
                evidence_spans=(r["span"],))
        except Exception as exc:  # counted, reported; never silently kept
            rejected[type(exc).__name__] += 1
            continue
        cand = res.candidate
        if cand.review_status == "pending_review":
            gov.review_candidate(candidate_id=cand.candidate_id, decision="accepted",
                                 actor_id="inquiry-graph:auto-accept")
        else:
            reused[cand.review_status] += 1
        if cand.candidate_id not in promoted_ids:
            promoted_ids[cand.candidate_id] = assertions.promote_candidate(
                candidate_id=cand.candidate_id, promoted_by="inquiry-graph:auto-accept").assertion.assertion_id
        submitted.append({**{k: r[k] for k in ("chat", "chat_title", "stance_id", "stance", "node_id", "text")},
                          "quote": r["span"]["text"], "proposition": prop,
                          "assertion_id": promoted_ids[cand.candidate_id]})
    print(f"submitted+promoted {len(submitted)}; rejected {dict(rejected)}; already-reviewed reused {dict(reused)}")

    report = EpistemicService(db_path=db).build_promoted_assertion_collection_report(profile_id=PROFILE[0])
    by_assertion = {s["assertion_id"]: s for s in submitted}
    tensions = []
    for t in report.tensions if hasattr(report, "tensions") else ():
        a, b = by_assertion.get(t.assertion_a_id), by_assertion.get(t.assertion_b_id)
        if a and b:
            tensions.append({"kind": t.tension_kind, "anchor_roles": list(t.anchor_roles),
                             "differing_roles": list(t.differing_roles), "a": a, "b": b})
    stance_tensions = [t for t in tensions if t["differing_roles"] == ["stance"]]
    print(f"onto-canon6 tensions: {len(tensions)} total, {len(stance_tensions)} differ only in stance")

    groups = defaultdict(list)
    for s in submitted:
        groups[s["proposition"]].append(s)
    cross = {p: m for p, m in groups.items() if len({x["chat"] for x in m}) >= 2}
    conflicts = [t for t in stance_tensions
                 if tuple(sorted((t["a"]["stance"], t["b"]["stance"]))) in {tuple(sorted(o)) for o in OPPOSED}]

    export = {
        "source": "onto-canon6 6864aa16c via inquiry-graph export (auto-accepted, not human-reviewed)",
        "positions_by_proposition": [
            {"proposition": p, "chats": sorted({x["chat_title"] for x in m}),
             "members": [{k: x[k] for k in ("chat_title", "stance", "text", "quote")} for x in m]}
            for p, m in sorted(groups.items(), key=lambda kv: (-len({x['chat'] for x in kv[1]}), kv[0]))],
        "cross_chat_propositions": len(cross),
        "stance_tensions": [{"a": {k: t["a"][k] for k in ("chat_title", "stance", "text", "quote")},
                             "b": {k: t["b"][k] for k in ("chat_title", "stance", "text", "quote")},
                             "opposed": t in conflicts} for t in stance_tensions],
    }
    (OUT / "export.json").write_text(json.dumps(export, indent=1, ensure_ascii=False), encoding="utf-8")
    loss = {
        "pinned_onto_canon6": "6864aa16c2f38270b0812302c2154391866a4f11",
        "carried": ["speaker (holder role, value 'brian')", "stance (value role)",
                    "proposition identity (entity, alignment cluster id)", "exact evidence span, verified by onto-canon6",
                    "source message text and id", "chat title and stance id (source_metadata)"],
        "not_carried_by_this_export": ["question-status events (open/deferred/resolved)", "relations between nodes",
                                       "assistant stances", "node kind outside source_metadata",
                                       "within-chat ordering beyond message ids"],
        "tension_semantics": "role-filler conflict: same predicate, shared entity anchor, differing fillers. "
                             "Detects the same proposition held with different stances; cannot detect two different "
                             "propositions that contradict each other.",
        "counts": {"brian_stances": len(rows), "propositions": len(claims), "multi_member_clusters": len(clusters),
                   "promoted": len(submitted), "rejected": dict(rejected), "tensions_total": len(tensions),
                   "stance_only_tensions": len(stance_tensions), "opposed_stance_conflicts": len(conflicts),
                   "cross_chat_propositions": len(cross)},
        "alignment_traces": list(scores.trace_ids),
    }
    (OUT / "loss.json").write_text(json.dumps(loss, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(loss["counts"]))


if __name__ == "__main__":
    main()
