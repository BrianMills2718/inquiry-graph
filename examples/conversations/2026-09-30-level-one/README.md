# Level-1 inquiry continuation — 2026-09-30

This is a separate, source-grounded conversation capture, not a replacement of the founding seed or a new research roadmap. It covers the visible dialogue from the pasted strategic handoff through Brian's request to capture this session and audit the substrate.

## Stored graph and authority

- `source.json`: a native V1 Conversation containing 76 excerpts from 24 visible prose turns.
- `curation.json`: 260 hand-authored annotation instructions with stable IDs and exact source references. These are fixture authoring shorthand, not an extension to the graph ontology.
- `build.py`: deterministically constructs the existing native V1 Graph and checks every source anchor and structural constraint.
- `verification.json`: the bounded execution record and substrate-probe results.
- `../../../tests/test_level_one_session.py` is not the test path; the repository-root path is `tests/test_level_one_session.py`.

The durable graph is reproducible from source + curation + builder. The generated native `graph.json`, validation result and open-agenda projection are outputs, not a separately edited authority. The generated graph has **93 content nodes, 75 relations, 31 inquiry moves, 25 stance events, 36 question-status events and 21 distinct questions**. Every annotation is **proposed**; none is confirmed or rejected.

```bash
# From the repository root, with the existing package installed:
python examples/conversations/2026-09-30-level-one/build.py --out /tmp/level-one-session
python -m pytest -q tests/test_level_one_session.py
```

The output is the same Graph model used by the existing validator, trace and agenda tools. It is not a Markdown summary pretending to be a graph. To inspect directly in Python:

```python
import runpy
from inquiry_graph.views import trace, open_questions
capture = runpy.run_path('examples/conversations/2026-09-30-level-one/build.py')
graph = capture['build_graph']()
print(trace(graph, 's30:q-canonical'))
print(trace(graph, 's30:m27'))
print(open_questions(graph))
```

The founding seed is untouched. Do not sum these counts into its documented counts without explicitly merging separate conversations. No cross-conversation identity equivalence is asserted merely because topics overlap.

## Source limitations

This is curated visible dialogue, **not a reconciled ChatGPT export**. All 24 prose turns have at least one excerpt. Substantive user turns are retained in full except the long opening quoted handoff; assistant turns have selected exact excerpts. This does not establish full token coverage or completeness of every subsidiary claim.

IDs such as `s30:t22` are local capture surrogates. Suffixes group excerpts of the same visible prose turn; excerpt ordinals do not imply independent within-turn events. Native message IDs and timestamps remain absent. The capture excludes hidden reasoning, system/developer instructions and location metadata. It does not reproduce the full tool transcript.

The opening handoff is quoted prior-agent material; its presence in Brian's message does not make every assertion a new endorsement by Brian. Literature statements are preserved as assistant reports/proposals. Exact quotations establish what was said, not whether those statements about the literature were correct.

## What changed in the inquiry

| Arc | Preserved change and rationale | Graph entry points |
|---|---|---|
| Initial audit | Assistant prioritized semantic repair, product usefulness and acceptance/composition. Brian challenged both the implied missing-work story and treating mature problems as new research mandates. | `q-audit`, `q-counts`, `q-pilot`, `m03`, `m05` |
| Verification counts | Assistant clarified its reported chronology: 138, then 142, then split 60+82. The earlier confusing framing remains in history. This capture does not rerun those historical suites. | `c-counts-earlier`, `c-counts-reconciled`, `r06`, `s04` |
| Scope correction | Assistant overcontracted the project toward only answering the traditional triad. Brian insisted that useful wider work remain and clarified that the target had shifted from MECE to canonical factorization. | `g-preserve`, `c-mece-to-factor`, `m07`, `r15` |
| Product versus recursive use | Brian put broad product optimization after Level 1 but reported that self-application already helped preserve inquiry and find gaps. | `g-level-one`, `c-recursive-use`, `m-self-application`, `e13` |
| Adoption-first comparisons | NARS, Carneades, Soar, Tweety, OpenCog/PLN, SACM/Assurance 2.0 and OPA/XACML were investigated or proposed. Permission to proceed is not adoption. | `q-prior-art`, `q-nars`, `m12`, `m14`, `g-proceed-one`, `g-proceed-two` |
| Representation versus semantics | Assistant reported a conceptual assurance-case mapping. That does not establish executable preservation, correctness or a replacement implementation. | `c-assurance-fit`, `c-typed-guarantees` |
| CommonKADS overreach | Assistant initially called CommonKADS/UPML a stronger answer, admitted no unique-minimal theorem, then narrowed the claim after Brian's objection and wider project context. | `c-commonkads-strong`, `c-no-canonicity-proof`, `c-commonkads-narrow`, `m22`, `r49`, `s17` |
| Concrete typing | Brian objected to treating fuel, hypotheses and evidence as one undifferentiated input space. Assistant corrected its example toward typed inputs/outputs. | `q-object-roles`, `c-typed-roles`, `m20`, `m21` |
| Related repositories | Scientific Hypergraph and Observation-to-Action were found relevant; their use does not settle a merged architecture or ownership scheme. | `r-science`, `r-o2a`, `q-science-repo`, `c-access` |
| Program organization | Brian described repo sprawl and benefits of isolated subproblem work. The federated-polyrepo/program-map answer remains an assistant proposal. | `q-repos`, `g-local-research`, `c-federation-proposal` |
| Latest scope correction | Brian wants the inference space first and situational strategy optimization later, including different scientific/adversarial settings and stance/persuadability. | `g-inference-first`, `g-strategy-later`, `c-game-relative`, `m27`, `e32` |
| Proposed local next pass | Assistant proposed distinguishing operations in a fixed representation first, then relaxing that restriction. Bayesian updating versus hypothesis/model construction remains a live question. | `q-fixed-space`, `q-bayes`, `q-representation-change`, `m30` |
| Recursive checkpoint | Brian requested this capture and a gap audit while doing it. | `g-checkpoint`, `q-graph-gaps`, `x-session`, `m31` |

All IDs in this table have the `s30:` prefix in the graph.

**The canonical-factorization question remains open.** Neither the eight-factor picture nor CommonKADS has been established as the unique/minimal answer. The graph records assistant answers as answers, not as Brian's resolution. The same applies to library adoption, the proposed federation and the fixed-representation staging choice.

## Durable work referenced by the dialogue

The graph references [theory PR #11](https://github.com/BrianMills2718/epistemic-warrant/pull/11), [product PR #63](https://github.com/BrianMills2718/inquiry-graph/pull/63), and [theory comparison issue #5](https://github.com/BrianMills2718/epistemic-warrant/issues/5) as historical work reports. Their current status is not inferred from those reports.

[Theory PR #13](https://github.com/BrianMills2718/epistemic-warrant/pull/13) was independently read during this capture: **open and unmerged**, head `fad132651a2f36d743a5e29b70eb6a23fe2e0feb`, four documents. It contains comparison/sketch work, not an accepted semantic replacement. This capture branch starts from Inquiry Graph `main` at `1f75cf1fe02000d2a630f591ec0d6fb412940318`, not from that or another unmerged PR.

## Substrate audit

### 1. Confirmed limitation: directly attaching rationale to a status/stance event

The V1 semantic-reference registry contains nodes, relations and moves, but not stance events or question-status events. The probe tries to express:

`motivates(reason=c-game-relative, result=e32)`

where `e32` is Brian's strategy-deferral event. Native validation rejects the event reference with `dangling_reference`, although the event exists.

**Working representation:** attach the rationale to the corresponding `scope`/revision move, retain the actor-relative event, and keep the deferral basis. This capture does that. The graph can preserve the rationale; it cannot currently target that event directly with a semantic relation. Consider event addressability only if the extra join becomes materially ambiguous. No schema extension was made.

### 2. Confirmed projection gap: stored rationale need not appear in the report

The default report displays each move's first anchor and raw input/output IDs, but not all linked content, stance history or secondary anchors. In this session the phrase **“stances and the persuadability axis”** is present in a nonleading anchor of `m27` and in native `trace(m27)`, but absent from the default report.

This is a reproducible graph-to-report loss, not proof that the underlying ontology cannot represent the point. The smallest remedy is a rationale-aware context/trace projection, not new inference primitives. The diagnostic records current behavior without requiring future implementations to retain the gap.

### 3. Workflow gap: no reliable automatic checkpoint was in use

Research results were being put in theory documents/issues, but the present conversation was not being incrementally captured as an inquiry graph. This is not evidence that the native graph model lacks the necessary concepts. It is a capture/integration problem.

For this session, append checkpoints after material scope corrections, decisions or comparison milestones. Preserve source excerpts first, then add proposed annotations and a compact open/deferred-state view. Do not regenerate reviewed history or silently replace earlier claims. Full-export IDs and completeness accounting remain separate work. No background automation has been configured by this change.

### 4. External-work and evidence-strength metadata remain conventions

A V1 reference node is text, not a typed record of repository URI, version, commit/merge status or verification method. This capture uses reference nodes, explicit claims and this evidence ledger to distinguish reported work, conceptual fit, executed tests and unmerged proposals.

That is sufficient to preserve this session, but repeated automatic cross-repo updates would benefit from a stable external-artifact/provenance adapter rather than parsing prose or introducing a second canonicalization store.

### What was not shown to require a new primitive

Actor-relative disagreement, conditional scope, deferral, supersession, correction rationale and self-application all fit the current types when carefully annotated. The failure to retain them would often be a curation or retrieval failure. Structural validation still cannot decide that “proceed” semantically means adoption; the fixture adds explicit negative attribution checks for that danger.

The inquiry itself also exposed task drift: architecture/tool-composition answers repeatedly displaced the narrower canonical-inference question. This is preserved in the history, not concealed by presenting the last answer as settled consensus.

## Verification and next use

The native validator returned **0 errors / 0 warnings**. **14 focused tests passed** in an isolated Linux sandbox, using byte-for-byte copies of the four native modules whose Git blob hashes are recorded in `verification.json`. The committed source, curation and builder hashes were read back and matched the tested files.

The checks cover native schema/anchors, all 24 local turn groups, proposed review states, no invented timestamps/IDs, no adoption inferred from “proceed,” retained retractions/reopenings, preserved deferrals and rationale, deterministic native JSON roundtrip, and negative quote/actor cases.

This is **not** a run of the full repository suite, a native-Windows run, a repeat of the product pilot, or independent semantic review. Both Remote MCP devices were offline; no user-machine worktree was touched. The unrelated founding-seed verification loose end remains unchanged.

Use `q-canonical`, `m27` and `m30` to resume Level-1 research. Preserve the other open/deferred questions rather than allowing this capture task to become a new general product-engineering program.
