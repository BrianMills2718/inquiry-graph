#!/usr/bin/env bash
# Run every check the planning package records and write docs/planning/checks.txt.
# Usage (from the repository root): bash docs/planning/run_checks.sh
# Each section prints its command, its output and exit=<status>. Adapted from
# claim-extraction docs/planning/run_checks.sh.
set -uo pipefail
cd "$(dirname "$0")/../.." || exit 2
CP="$HOME/code2/company-planning/plugins/company-planning/scripts"
PY=/usr/bin/python3
OUT=docs/planning/checks.txt
TMP="${TMPDIR:-/tmp}/inquiry-graph-make-check.$$"
{
echo "# Checks for the inquiry-graph planning package"
echo "Run $(date -u +%Y-%m-%dT%H:%MZ) at commit $(git rev-parse --short HEAD), with $PY."
echo
echo '## wiki rule: python3 $HOME/code/project-meta/scripts/md_file_cap.py --repo .'
$PY "$HOME/code/project-meta/scripts/md_file_cap.py" --repo .; echo "exit=$?"
echo
echo '## durable documents: python3 $CP/durable_docs_check.py --repo . --arc42'
$PY "$CP/durable_docs_check.py" --repo . --arc42; echo "exit=$?"
echo
echo '## project navigation: python3 $CP/validate_project_navigation.py .'
$PY "$CP/validate_project_navigation.py" .; echo "exit=$?"
echo
echo '## plan adoption recheck: python3 $CP/method_conformance/cli.py lint --repo-root . --recheck'
$PY "$CP/method_conformance/cli.py" lint --repo-root . --recheck; echo "exit=$?"
for p in docs/plans/coding-sessions.md docs/plans/report-relations-rescore.md docs/plans/session-launch-kind.md; do
  echo
  echo "## plan lint: python3 \$CP/method_conformance/cli.py lint --repo-root . --plan $p"
  $PY "$CP/method_conformance/cli.py" lint --repo-root . --plan "$p"; echo "exit=$?"
done
echo
echo '## repository check: make check (trace, sources, import contracts, OpenSpec, pytest, artifact drift, seed validation, architecture, test-first)'
make check > "$TMP" 2>&1; rc=$?
grep -E 'passed|failed|error|Contracts|KEPT|BROKEN|valid|ok|FAIL|^make' "$TMP" | tail -30
rm -f "$TMP"
echo "exit=$rc"
echo
echo '## typed-graph/v1 schema over docs/planning/domain.graph.json and docs/planning/open-questions.graph.json (code in docs/planning/run_checks.sh)'
$PY - <<'PYEOF'
import json, pathlib, jsonschema
schema = json.loads((pathlib.Path.home() / "code2/representation-router/schemas/typed-graph.schema.json").read_text())
v = jsonschema.Draft202012Validator(schema)
bad = 0
for f in ("docs/planning/domain.graph.json", "docs/planning/open-questions.graph.json"):
    p = pathlib.Path(f)
    if not p.exists():
        print(f, "missing"); bad += 1; continue
    errs = list(v.iter_errors(json.loads(p.read_text())))
    bad += bool(errs)
    print(f, "errors", len(errs))
print(f"graphs_valid={2 - bad} graphs_invalid={bad}")
raise SystemExit(1 if bad else 0)
PYEOF
echo "exit=$?"
} > "$OUT" 2>&1
echo "wrote $OUT"
