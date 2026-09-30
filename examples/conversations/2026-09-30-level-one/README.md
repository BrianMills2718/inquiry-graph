# Level-1 inquiry continuation — 2026-09-30

Separate source-grounded capture from the pasted strategic handoff through Brian's request to record this session and audit the substrate. The founding seed and research schema are unchanged.

## Build and inspect the graph

`source.json` contains 126 excerpts from 67 visible prose/research-update turns. `curation.json` contains the proposed annotation instructions. `build.py` creates and validates the existing native V1 Graph; it is fixture authoring, not a new graph ontology or incremental updater. Source + curation + builder are the durable representation; native JSON and agenda files are deterministic outputs.

```bash
# From an installed repository checkout:
python examples/conversations/2026-09-30-level-one/build.py --out /tmp/level-one-session
python -m pytest -q tests/test_level_one_session.py
```

The generated graph contains **166 content nodes, 142 relations, 68 inquiry moves, 35 stance events, 66 question-status events and 33 distinct questions**. All **477 annotations are proposed**; none are confirmed or rejected.

```python
import runpy
from inquiry_graph.views import trace, open_questions
capture = runpy.run_path('examples/conversations/2026-09-30-level-one/build.py')
graph = capture['build_graph']()
print(trace(graph, 's30:q-canonical'))
print(trace(graph, 's30:m27'))
print(open_questions(graph))
```

Do not add these counts to the founding-seed counts without explicitly merging separate conversations. Similar topics do not establish cross-conversation identity.

## Source and review limits

This is **curated visible dialogue, not a reconciled ChatGPT export**. Every captured visible prose/research-update turn has at least one excerpt. Substantive user turns are retained in full except the long opening quoted handoff; assistant turns have selected exact excerpts. Turn coverage does not establish full token coverage or capture of every subsidiary claim.

IDs such as `s30:t22` are local surrogates. Suffixes group excerpts of one prose turn; their ordinals do not establish separate within-turn events. Native message IDs and timestamps remain absent. Hidden reasoning, system/developer instructions and location metadata are excluded. Full tool transcripts are not reproduced; reports of research and repository actions are retained as attributed content.

The opening handoff is quoted prior-agent material, not automatic Brian endorsement of every assertion. Literature statements record what the assistant reported, not independent verification. Exact quote validation does not establish interpretive correctness. All annotations await review.

## Changes and open threads

All abbreviated IDs below have the `s30:` prefix.

| Arc | What must survive resumption | Entry points |
|---|---|---|
| Audit and test counts | Assistant's 60/82 versus 138 framing caused concern about lost work. Its later reported 138 → 142 → 60+82 explanation is retained alongside the earlier framing. No historical suite was rerun here. | `q-counts`, `r06`, `s04` |
| Pilot interpretation | Omission, extraction, representation and projection were not isolated by the reported pilot. A graph failure or missing repository work was not established. | `q-pilot`, `c-pilot-qualified` |
| Preserve useful work | Brian corrected the assistant's proposal to reduce the project to the original triad and clarified the earlier move from MECE to canonical factorization. | `g-preserve`, `c-mece-to-factor`, `m07`, `r15` |
| Product versus self-application | Brian put broad product optimization after Level 1 while reporting useful recursive inquiry tracking. | `g-level-one`, `c-recursive-use`, `e13` |
| Adoption-first literature route | NARS, Carneades, Soar, Tweety, OpenCog/PLN, SACM/Assurance 2.0 and OPA/XACML are investigated/proposed candidates. “Proceed” is not adoption. | `q-prior-art`, `q-nars`, `m12`, `m14` |
| Conceptual mapping versus proof | The assistant's four-case assurance mapping does not establish executed semantic preservation or a replacement implementation. | `c-assurance-fit`, `c-typed-guarantees` |
| CommonKADS correction | Assistant first presented it as a stronger answer, admitted no canonicity theorem, and later narrowed it to a process-composition comparator after Brian's objection and wider context. | `c-commonkads-strong`, `c-commonkads-narrow`, `m22`, `r49`, `s17` |
| Typed objects and operations | Brian challenged the fuel/hypothesis example; assistant corrected it toward typed inputs and outputs. | `q-object-roles`, `c-typed-roles`, `m20` |
| Related projects | Scientific Hypergraph and O2A are relevant; their relation does not settle a merged architecture or ownership arrangement. | `r-science`, `r-o2a`, `q-science-repo`, `c-access` |
| Repository organization | Brian values independent subproblem research but raised integration/sprawl. Federation and a program map remain assistant proposals. | `q-repos`, `g-local-research`, `c-federation-proposal` |
| Latest priority | Brian wants the inference space first, strategy optimization later and situation-relative, including scientific/adversarial settings and stance/persuadability. | `g-inference-first`, `g-strategy-later`, `c-game-relative`, `m27`, `e32` |
| Proposed next local question | Assistant proposed fixed-representation operations first, then representation/model-class change. Bayesian updating versus hypothesis/model construction is still a live question. | `q-fixed-space`, `q-bayes`, `q-representation-change`, `m30` |
| Recursive capture | This session is itself an example of using the inquiry representation to inspect the inquiry. | `g-checkpoint`, `q-graph-gaps`, `x-session` |

**Canonical factorization remains open.** The eight-factor diagram, CommonKADS replacement, SACM adoption, federation and fixed-representation staging are not recorded as user-adopted solutions. Assistant answers do not close Brian's question. Derivation/subargument and full ABA+/hyperargumentation possibilities remain preserved in `c-escalations`.

## Repository work referenced

Historical reports point to [theory PR #11](https://github.com/BrianMills2718/epistemic-warrant/pull/11), [product PR #63](https://github.com/BrianMills2718/inquiry-graph/pull/63), and [theory comparison issue #5](https://github.com/BrianMills2718/epistemic-warrant/issues/5). Their current status is not inferred from those reports.

[Theory PR #13](https://github.com/BrianMills2718/epistemic-warrant/pull/13) was independently read during capture: **open/unmerged**, head `fad132651a2f36d743a5e29b70eb6a23fe2e0feb`, four documents. The comparison/sketches are not an accepted semantic replacement. This capture starts directly from Inquiry Graph `main` at `1f75cf1fe02000d2a630f591ec0d6fb412940318`, not another unmerged PR.

## Substrate findings

### Direct event-targeted rationale: confirmed limitation, existing workaround

V1 semantic relations can target nodes, relations and moves, but not stance/question-status events. The diagnostic tries `motivates(reason=c-game-relative, result=e32)`, where `e32` is Brian's strategy deferral. Validation returns `dangling_reference`, even though the event exists.

This capture instead links rationale to the corresponding scope/revision move, retains the actor-relative event and records its basis. Rationale is representable; direct targeting of the event is not. Consider event addressability only if that extra join becomes materially ambiguous. No schema change was made.

### Default report: confirmed projection loss

The default report exposes a move's first anchor and raw input/output IDs, not all linked content, stance history or secondary anchors. The phrase **“stances and the persuadability axis”** is present in a secondary anchor of `m27` and in native `trace(m27)`, but absent from the default report.

That is a reproducible graph-to-report loss, not evidence that the ontology cannot represent the point. A rationale-aware trace/context projection is the smaller remedy. The probe records current behavior without forcing future versions to retain the gap.

### Incremental capture: workflow gap

Research findings were entering theory documents/issues, but this conversation was not being incrementally captured as an inquiry graph. The capture process needs checkpoints, not necessarily more concepts.

For subsequent continuation, checkpoint after material scope corrections, decisions or comparison milestones: preserve source excerpts, append proposed annotations, retain earlier claims and expose open/deferred state. Do not regenerate reviewed history. Export reconciliation and completeness accounting remain separate. No background automation was configured.

### External-work provenance: convention rather than native structure

A V1 reference node is text, not a typed repository URI/version/status/verification record. References, explicit claims and this ledger preserve the difference between reported work, conceptual fit, executed checks and unmerged proposals. Repeated automated cross-repo updates may warrant a stable provenance adapter, not a second canonicalization store.

### What did not require an extension

Actor-relative disagreement, conditional scope, deferral, supersession and self-application fit the existing model when carefully annotated. The tests explicitly prevent “proceed” from becoming adoption in this fixture; the structural validator alone cannot judge that interpretation.

The capture also exposes task drift in the conversation: tool/architecture answers repeatedly displaced the narrower inference-factorization question. Retaining the redirects prevents a later summary from presenting that drift as settled consensus.

## Verification

The **last executed isolated-sandbox checkpoint** had native validation 0 errors / 0 warnings and 15 focused tests passing. The latest representation-change and final-collapse additions have **not yet been rerun** in that sandbox. Execution used an isolated Linux sandbox with byte-for-byte copies of the four native modules whose Git blob hashes are in `verification.json`. The committed source, curation and builder hashes were read back and matched the tested files.

Tests cover source anchors, 32 local turn groups, proposed review states, absent native IDs/timestamps, no adoption inferred from continuation, retained retractions/reopenings, deferred branches, rationale links, deterministic native JSON roundtrip, and invalid quote/actor mutations.

This is not the full repository suite, a native-Windows run, a repeated product pilot or independent semantic review. Both Remote MCP devices were offline; no user-machine worktree was touched. The founding-seed verification loose end remains unchanged.

The first fixed-space falsification checkpoint is now also in `q-fixed-space`, `m34`–`m36`, and remains reopened for Brian review. Resume the broader Level-1 work from `q-canonical` and the narrower operation question from `q-fixed-space`. Preserve the other open/deferred threads without turning this checkpoint into a new product-engineering program.


### Incremental fixed-space checkpoint

After Brian said `Proceed`, the graph was extended rather than rebuilt. It records the assistant's provisional collapse of Bayesian/AGM/defeasible change into standing-revision semantics, the Bayesian new-theory counterexample against collapsing candidate introduction into conditioning, the initial three-function proposal, and its immediate refinement into **source relation × state effect**. Brian's authorization to investigate is explicit; no endorsement of the resulting factorization is recorded. The broad `configuration + action + warrant` compression from merged epistemic-warrant PR #14 is recorded as context, not as a replacement for the local question.

The first attempted counterexample—temporary supposition without belief—refined the effect axis rather than adding a new family: role/standing includes temporary contextual assumption, and explicit availability can increase or decrease. This refinement is in `c-role-standing-refinement` / `m37`.


### Representation-change checkpoint

The fixed-space result now distinguishes the **epistemic role of inferential output**—`consequence/readout` versus `candidate/proposal`, with `none` for pure state-role changes—from its **state effect**. This is explicitly not deterministic-versus-stochastic computation. Acquisition/observation is provisionally outside inference proper while remaining an epistemic event in the larger system. The next-layer bridge reuses the existing transition calculus but generalizes its total function `Φ: U → U'` to a typed alignment/correspondence with explicit preservation/loss properties. The stronger question `q-rep-falsifier` remains open.


### Final Level-1 collapse checkpoint

The latest assistant result is deliberately thinner than the earlier two-axis proposal. The graph now preserves that:

- a generic alignment/correspondence is only an interoperability envelope; without a concrete mapping regime and preservation semantics it is too general to be a substantive theory;
- an alignment itself may be uncertain or contested and therefore belongs inside the epistemic state as a candidate object with provenance/standing/warrant;
- consequence/readout versus candidate/proposal remains a useful explanatory distinction, but the final primitive-status check demotes it to method/output-role/guarantee metadata rather than a foundational action coordinate;
- the current Level-1 normal form therefore returns to **reasoning configuration + typed action/output/state effect + typed warrant/guarantee**, with acquisition, representation change and strategy treated as adjacent roles/layers rather than new inference species.

This is recorded as assistant hypothesis, not Brian endorsement. The open representation-change falsifier and the broader canonical-factorization question remain available for review.


### Strategy-distance scope correction

After the final Level-1 collapse, the assistant proposed strategy/control as the next intellectual layer. Brian explicitly corrected that sequencing: **“I still feel like we're a long way from strategies for optimization.”**

The graph therefore keeps strategy optimization deferred and opens `q-before-strategy`: what conceptual or integration work remains between the current inference factorization and any later optimization program? This capture does **not** invent that intervening agenda. The correction reinforces the earlier `g-strategy-later` stance and supersedes any reading of the assistant's previous “next layer” language as the active roadmap.


### Post-Level-1 representation/interoperability track

Brian explicitly queued, **after Level 1**, an adoption-first investigation of heterogeneous representation systems and their composition/translation. The durable starting references are Representation Router, OntoCanon, DODAF and Knowledge Work, together with mature megamodeling/model-management and database-theory prior art.

The deferred questions are:
- is there an existing registry/catalog/profile system for representation formalisms and their interfaces/mappings?
- what role, if any, should OntoCanon's intermediate representation play in translating among them?
- what do existing database, ontology, schema-mapping, model-management and prior internal experiments already establish about unavoidable transfer loss?

This is explicitly **before** strategy optimization in the current sequencing and carries Brian's reuse/no-novelty goal. The branch is recorded but not opened as an active research task yet.


### Representation/interoperability adoption audit activated

Brian explicitly activated the previously deferred track with “go research that.” The supporting note is `representation-interoperability-adoption-audit.md`.

Initial result: no single universal maintained stack was found, but the architecture is heavily covered by mature layers. ISO/IEC 11179-3 + 11179-35 and ISO/IEC 19763 are the strongest registry-model prior art; DOL/Hets cover heterogeneous formal OMS mappings; MDE/QVT/ATL/Epsilon and generic model management cover model transformations; CQL/schema-mapping theory covers database-shaped migration; FAIRsharing and Aristotle provide live registry precedents.

The current assistant hypothesis is **native authority + governed registry + first-class typed mappings + optional declared IR projections**, not universal translation through OntoCanon. Two concrete next questions remain open: crosswalk the current OntoCanon pack/profile contract against ISO registry standards, and test a small heterogeneous registry/mapping graph using existing project profiles without inventing a universal IR.


The initial OntoCanon↔ISO crosswalk now answers `q-registry-crosswalk` provisionally: existing metadata already covers much identity/version/provenance/dependency/validation; remaining work looks like standards alignment for classification/definition, model↔metamodel links, mapping records and lifecycle rather than a new registry core.


### Mini-megamodel experiment

The first concrete registry fixture now exists with 8 native representation/profile nodes and 5 mapping records. It distinguishes implemented mappings from design seams, records loss/preservation claims, and treats disconnectedness as valid. The bounded sandbox path checks passed: no design mapping is promoted to executable, no Scientific Hypergraph→Representation Router path is invented, and no current path automatically transports a guarantee. `q-mini-megamodel` is answered for this bounded case; `q-compositional-chain` is the next falsifier.


### Certified multi-hop mapping result

The first mature-formalism multi-hop falsifier uses CQL functorial pullback. For F:S→T and G:T→U, the fixture checks Δ_F(Δ_G(I)) = Δ_(G∘F)(I) on a concrete instance and separately checks that U-only `department` data is not preserved. This answers `q-compositional-chain` for one preservation family and opens `q-preservation-types`: the registry now needs typed preservation families rather than a single generic preservation flag.
