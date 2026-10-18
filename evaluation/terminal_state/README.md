# Terminal-state continuation regression: actual source cutoff

## Experiment executed (deterministic part)

The user-provided 2026-10-18 ChatGPT Exporter Markdown ends during a systematic comparison of existing semantic frameworks. The last assistant response says verbatim: "I’m now turning these findings into explicit scenario-by-scenario judgments, while keeping documented capabilities separate from assumptions that still need implementation testing."

The existing graph's `a13` is a **condensed assistant research summary**. It says the five-case evaluation "now covers" the scenarios, and the graph records a successor goal to run native tool tests. It does not contain the exact unfinished-judgments statement. The canonical graph also includes post-export work (Python fixture oracles, Z3, Lean) in assistant records a14–a17.

A source-cutoff structural audit on 2026-10-18 found:

| Control | Observed result |
|---|---|
| Pre/post cutoff source records | 27 retained, 4 removed |
| Anchored semantic nodes | 49 retained, 20 removed |
| Cutoff moves / relations | 19 moves, 36 relations retained |
| Invalid source-anchor offsets in retained records | 0 |
| Exact terminal-activity sentence represented in baseline source messages | No |
| Existing vocabulary for the missing state | Yes: `task`, `QuestionEvent(status="open")`, and `Move(kind="propose")` |
| Independent blind A/B/C reader answers | **Not run** |

This is evidence of **source-extraction/operational-state loss**, not proof that an independent reader cannot recover the task by inference from the condensed graph. Nor does it prove that the schema needs expanding.

## Reproducible experiment

`fixtures/semantic_factorization_20261018.json` is the human-checked reference, with exact visible end-of-transcript quotations. `experiment.py` creates three materials at the same source cutoff:

- **A** — the original uploaded Markdown transcript.
- **B** — the existing graph projected through message `a13`, excluding all post-export nodes, moves, relations and notes.
- **C** — B plus a single exact terminal-reply excerpt, an explicitly open `task`, and a corresponding `propose` move. This is an augmentation using **existing schema types**, not a new graph ontology.

Both B and C are checked with the repository's graph validator. The augmented task must be retrievable from `open_questions` and visible in the normal Markdown report. The script refuses to export any B/C report that still includes the later Lean result.

Run locally inside the repository checkout:

```bash
python -m pytest tests/test_terminal_state_continuation.py -q
python evaluation/terminal_state/experiment.py \
  --transcript "/path/to/ChatGPT-Taxonomy And Ontology Explained-20261018-1749.md" \
  --out /tmp/inquiry-terminal-state
```

If the optional, authorized `llm_client` synthesis model is configured, append `--run-reader` to generate A/B/C answers without revealing the gold key to the answerer. Answers are saved with model IDs and actual cost metadata. Blind independent **grading against the six reference points is still required**. Do not treat generating materials, passing validator checks, or an ungraded model answer as a reader-evaluation success.

## Attribution, limitations and next decision

This is a one-case regression, not a statistical sample. All new annotations have `review_status="proposed"`, preserve assistant authorship and do not assert that the user endorsed the assistant's judgments. The augmented source slice is labelled as a **single excerpt from the final response**, not a new conversation turn; original source message IDs remain unknown.

The falsifiable process prediction is narrow: explicitly source-anchoring the active unfinished task should improve its availability in the default agenda projection. If independent readers still fail with condition C despite seeing the open task, investigate report presentation and reader behavior. Only if a faithful terminal state cannot be encoded and retrieved using existing elements should a shared-schema modification be considered.

The original broader study's next activity remains comparative-framework evaluation; this regression does not claim the DOL/MMT/Modelica/SysML research itself has been completed.

## 2026-10-18 source reconciliation and corrected-extractor trial

PR #221 subsequently added exact terminal-response excerpt slices to the canonical graph. The historic **B** control intentionally excludes these additions and all post-export work; otherwise it would no longer measure the missed terminal state.

A local source-only parse of the user-provided Markdown found **17 visible user prompts and 17 visible assistant responses** (34 alternating sections), ending at the displayed 2026-10-18 17:12:27 assistant response. The exact terminal comparison, source-based-validation, and repository-integrity quotations are present in that reply. These are transcript parsing facts, **not live extraction or independent reader results**.

The optional `live_trial.py` creates a private normalized representation of all 34 visible messages, prepares A/B/C at the correct cutoff, and—when explicitly launched with a locally authorized model—produces:
- **D**, a newly extracted graph using the corrected `live_extract` policy on the actual exported transcript;
- a structural diagnostic of whether D has a source-grounded open terminal comparison task;
- optional separate model-reader answers to A/B/C/D, without giving the reader the gold rubric, with model/cost metadata.

Run from the repository root with an output directory that remains private:

```bash
python -m evaluation.terminal_state.live_trial \
  --transcript "/path/to/ChatGPT-Taxonomy And Ontology Explained-20261018-1749.md" \
  --out private/terminal_trial

# Requires the authorized optional llm_client adapter and model access:
python -m evaluation.terminal_state.live_trial \
  --transcript "/path/to/ChatGPT-Taxonomy And Ontology Explained-20261018-1749.md" \
  --out private/terminal_trial --extract --model codex/gpt-5.6-luna --reader
```

The four reader answers still require **independent six-point grading** to establish continuation accuracy. Structural presence of a task, a passing unit test, or an answer generated by the same model without grading must not be misrepresented as an A/B/C/D evaluation win.

**Privacy:** The raw transcript is user-provided and is never committed. All normalized messages, model output, answer material, and grading inputs must remain under ignored `private/` or another protected directory. Do not run this on public CI with the transcript attached.
