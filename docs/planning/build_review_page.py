"""Build the planning-package review page's data file from the package itself.

Reads the manifest, the open-questions ledger, the domain graph, the open-questions map, the Mermaid
diagrams in docs/model/ARCHITECTURE.md (context and containers), the "Where the sources disagree" list in
docs/planning/DOMAIN.md, the next plan and the cold review, and writes
proposals/planning-package/review-page/data.js. The page (index.html next to it) only renders that
data, so it cannot say anything the package files do not. Adapted from claim-extraction
docs/planning/build_review_page.py.

  python3 docs/planning/build_review_page.py
"""
import json
import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parents[2]
PAGE = REPO / "proposals" / "planning-package" / "review-page"
# The plan-page site copies only the page folder, so repository links must be absolute. The repository
# is public; nothing under private/ is linked.
BLOB = "https://github.com/BrianMills2718/inquiry-graph/blob/main/"
LINK = re.compile(r"\]\((?!https?:|#|mailto:)([^)\s]+)\)")


def _absolute_links(markdown: str, base: str) -> str:
    """Strip YAML front matter and point relative Markdown link targets at GitHub."""
    if markdown.startswith("---\n"):
        markdown = markdown.split("\n---\n", 1)[1]

    def repl(m: re.Match[str]) -> str:
        target, _, anchor = m.group(1).partition("#")
        path = (pathlib.PurePosixPath(base) / target).as_posix()
        parts: list[str] = []
        for piece in path.split("/"):
            if piece == "..":
                parts.pop()
            elif piece not in ("", "."):
                parts.append(piece)
        return "](" + BLOB + "/".join(parts) + ("#" + anchor if anchor else "") + ")"

    return LINK.sub(repl, markdown)


def _read(rel: str) -> str:
    return (REPO / rel).read_text(encoding="utf-8")


def _section(markdown: str, heading: str) -> str:
    start = markdown.index(heading)
    rest = markdown[start + len(heading):]
    nxt = re.search(r"^## ", rest, flags=re.MULTILINE)
    return rest[: nxt.start()] if nxt else rest


def main() -> None:
    manifest = json.loads(_read("docs/planning/planning-package.json"))
    parts = manifest["parts"]
    ledger = json.loads(_read(parts["open_questions"]["path"]))
    domain = json.loads(_read(parts["domain_model"]["path"]))
    qmap = json.loads(_read("docs/planning/open-questions.graph.json"))
    model = _read("docs/model/ARCHITECTURE.md")
    diagrams = re.findall(r"```mermaid\n(.*?)```", model, flags=re.DOTALL)
    section = _section(_read(parts["domain_model"]["glossary"]), "## Where the sources disagree")
    disagreements = [re.sub(r"\s+", " ", item).strip()
                     for item in re.split(r"^- ", section, flags=re.MULTILINE)[1:]]
    revision = manifest["subject_revision"][:7]
    checks = _read(parts["checks"]["path"])
    data = {
        "manifest": manifest,
        "questions": ledger["questions"],
        "fixed_here": ledger.get("fixed_here", []),
        "domain": domain,
        "question_map": qmap,
        "context_diagrams": diagrams,
        "disagreements": disagreements,
        "next_plan": _absolute_links(_read(parts["plan"]["path"]),
                                     str(pathlib.PurePosixPath(parts["plan"]["path"]).parent)),
        "cold_review": _absolute_links(_read(parts["cold_review"]["path"]), "docs/planning"),
        "evidence_links": {
            "checks.txt (full output of every check)": BLOB + parts["checks"]["path"],
            "cold-review.md (independent review)": BLOB + parts["cold_review"]["path"],
            "planning-package.json (the manifest)": BLOB + "docs/planning/planning-package.json",
            "open-questions.json (the ledger)": BLOB + parts["open_questions"]["path"],
            "system-model.md (system model: record types, writers, nightly pipeline)": BLOB + parts["system_model"]["path"],
            "ARCHITECTURE.md (context, blocks, runtime)": BLOB + "docs/model/ARCHITECTURE.md",
            "DOMAIN.md (domain glossary)": BLOB + parts["domain_model"]["glossary"],
            "next-plan.md (the next plan)": BLOB + parts["plan"]["path"],
        },
        "built_from": revision,
        "checks_commit": (re.search(r"at commit ([0-9a-f]{7,40})", checks) or [None, "unknown"])[1],
    }
    PAGE.mkdir(parents=True, exist_ok=True)
    (PAGE / "data.js").write_text("window.PAGE_DATA = " + json.dumps(data, ensure_ascii=False, indent=1)
                                  + ";\n", encoding="utf-8")
    print(f"questions={len(ledger['questions'])} concepts={len(domain['nodes'])} "
          f"context_diagrams={len(diagrams)} disagreements={len(disagreements)} built_from={revision}")


if __name__ == "__main__":
    main()
