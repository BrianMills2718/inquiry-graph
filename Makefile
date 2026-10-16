.PHONY: check fast docs-specs
# Git hooks export these (in worktrees especially); they would leak into tests' own throwaway repos.
unexport GIT_DIR GIT_INDEX_FILE GIT_WORK_TREE GIT_PREFIX GIT_COMMON_DIR GIT_OBJECT_DIRECTORY
# Each OpenSpec capability appears under docs/specs through a file link.
docs-specs:
	@for d in openspec/specs/*/; do [ -d "$$d" ] || continue; c=$$(basename $$d); mkdir -p docs/specs/$$c; ln -sfn ../../../openspec/specs/$$c/spec.md docs/specs/$$c/spec.md; done
# Commit-hook checks: each finishes in seconds.
fast:
	uv run code2check trace
	uv run code2check sources
	uv run lint-imports
	openspec validate --all --strict --no-interactive
# Everything, run before merging. pydoclint, interrogate and zensical are not run: the existing code
# and docs predate them (docs/architecture/arc42.md, section 11).
check: docs-specs fast
	uv run python -m pytest -ra
	uv run python tools/build_artifacts.py --check
	uv run python -m inquiry_graph validate examples/seed/graph.json
	uv run code2check arch check
	uv run code2check test-first --base origin/main
