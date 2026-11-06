# inquiry-graph instructions

Index for agents. Read [docs/index.md](docs/index.md) first; it lists the architecture, diagram,
requirements and decisions, then every other record. Workspace rules: `~/code2/AGENTS.md`.

- Behavior changes go through OpenSpec (`openspec/changes/<name>/`), then archive with
  `openspec archive <name> --yes`.
- Every requirement and decision record carries a `Source:` line: `Source: Brian, <date>: "<his words>"`
  or `Source: inferred by agent (<basis>)`. Implementation (code, tests, diagram) is the agent's call; a
  significant requirement or decision an agent inferred waits for Brian's yes before it lands.
  `code2check sources` enforces the line.
- Write the failing test before the code, marked `@pytest.mark.req("<capability>/<scenario>")`.
  `existing=True` is only for tests of behavior that worked before its scenario was written.
- The module that implements a requirement says `Implements: <capability>/<requirement>` in its
  docstring; continuation lines are indented. Code under `tools/` counts too (`[tool.code2check]`).
- Change structure in `docs/architecture/model.c4`, then run `uv run code2check arch gen`.
  Never edit `.importlinter` by hand. LikeC4 keywords (`model`, `views`) cannot be element names.
- `make fast` runs on commit; `make check` runs on push and must exit 0 before merging.
- Set up with `uv sync`; the old `uv pip install -e '.[dev]'` route still works for the package alone.
