"""Compare per-account ChatGPT chat-id inventories (from inventory_accounts.sh) with the exporter catalog.

Usage: compare_inventory.py INVENTORY_DIR [OUT.json]
For each account JSON: reported total vs listed ids, ids missing from the catalog, ids in the catalog that no account lists.
Ids and counts only, no titles or text. Exit 1 if any listed chat is missing from the catalog.
"""
import json
import sys
from pathlib import Path

CATALOG = Path.home() / "code/chatgpt-conversation-manager-v0.2/data/metadata/catalog.json"


def ids_of(inv):
    out = set()
    for x in inv.get("ordinary_list", []):
        out.add(x["id"] if isinstance(x, dict) else x)
    for p in inv.get("projects", []):
        for c in p.get("chats", []):
            out.add(c["id"] if isinstance(c, dict) else c)
    return out


def main():
    d = Path(sys.argv[1])
    cat = set(json.loads(CATALOG.read_text())["threads"])
    report, union, missing_total = {}, set(), 0
    for f in sorted(d.glob("*.json")):
        inv = json.loads(f.read_text())
        if "error" in inv and "ordinary_list" not in inv:
            report[f.stem] = {"error": inv["error"]}
            continue
        ids = ids_of(inv)
        miss = sorted(ids - cat)
        union |= ids
        missing_total += len(miss)
        report[f.stem] = {"listed": len(ids), "ordinary_listed": len(inv.get("ordinary_list", [])), "ordinary_reported_total": inv.get("ordinary_reported_total"),
                          "matches_reported_total": inv.get("ordinary_matches_reported_total"), "project_chats": inv.get("project_chat_count"),
                          "missing_from_catalog": len(miss), "missing_ids": miss[:50]}
    report["_catalog_threads"] = len(cat)
    report["_catalog_not_listed_by_any_account"] = len(cat - union)
    report["_listed_union"] = len(union)
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text(json.dumps(report, indent=1))
    print(json.dumps({k: ({kk: vv for kk, vv in v.items() if kk != "missing_ids"} if isinstance(v, dict) else v) for k, v in report.items()}, indent=1))
    sys.exit(1 if missing_total else 0)


if __name__ == "__main__":
    main()
