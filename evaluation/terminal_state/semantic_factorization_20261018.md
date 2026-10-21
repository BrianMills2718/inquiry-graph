# Terminal-state continuation regression: semantic factorization, 2026-10-18

## Question
Does Inquiry Graph preserve **operational state** (the currently active research work), rather than only epistemic state (the inquiry's claims and general goals), sufficiently for a new AI reader to resume correctly?

## Source and cutoff
Gold reference: user-provided `ChatGPT-Taxonomy And Ontology Explained-20261018-1749.md`, created 2026-10-18 16:20:33, last updated 17:48:04, exported 17:49:13 (displayed local times). Source ChatGPT conversation: https://chatgpt.com/c/6ad52a11-8988-83ea-8f4e-fe7679198c3f . Compare only the conversation **as of this export cutoff**, not subsequent commits.

Graph baseline: `examples/conversations/semantic-factorization-2026-10-18/graph.json` from `main`. The graph is curated, not a verbatim native export, and has later assistant research updates with synthetic IDs and no original timestamps.

## Ground-truth terminal state
- **Parent objective:** identify whether established formal frameworks already account for the user's proposed semantic-representation capabilities; do not rush to invent new representational dimensions.
- **Current methodology:** prior-art-first research synthesis, systematic mapping and a comparative evidence ledger, plus requirements traceability and representative scenario evaluation.
- **Active step at cutoff:** turn initial source-based research into explicit, **scenario-by-scenario candidate-framework capability and limitations judgments**; distinguish native supported capabilities, encoded/delegated capabilities, unsupported obligations, and unverified tool-level assumptions. Check the inquiry-graph relation roles and source anchors as part of the capture/merge work.
- **Five cases:** physics and simulation; mathematical theories and proof; cellular automata; empirical classification/observation; cross-formalism translation.
- **Candidates of interest:** DOL, MMT, institution theory, Modelica/FMI, SysML v2/KerML, OWL/SKOS, SOSA/SSN, PROV-O, and relevant model-driven or category-theoretic frameworks. Candidate status and comparative fit must not be silently converted into claims of universal coverage.
- **Status:** comparative assessment in progress at exported conversation cutoff. Source-based evaluations are not automatically proof of implementation-level conformance. Subsequent Python/Z3/Lean tests are **post-cutoff evidence**, not proof that the comparative assessment had already been completed when the export ended.
- **Next action:** reconcile which comparison-matrix rows and evidence obligations were finished, then complete and source-check the remaining scenario-by-scenario judgments. Only afterwards reassess representational gaps and tool-level implementation tests.
- **Do not infer:** a universal MECE decomposition is established; DOL/MMT/SysML/Modelica native conformance ran; opening a PR implies its merge; later experiments closed the framework comparison.

## Diagnostic protocol
Use three blinded answer conditions with exactly the same question and rubric:
A. Full visible transcript through the export cutoff.
B. Only the baseline graph's readable report (generated from the same cutoff, **excluding post-cutoff records**).
C. B supplemented by an explicitly source-anchored terminal-state extraction, encoded using existing graph constructs if possible.

Question: **"What was being done at the cutoff? What concrete work must happen next, and which claims remain unverified?"**

Score against these six independent key points, one point each:
1. identifies the active comparative-framework study rather than only the general factorization question;
2. names the scenario-by-scenario capability/limitations judgment as the underway deliverable;
3. recognizes the five test cases;
4. distinguishes documentation/source evidence from tool-level validation;
5. prescribes completing/checking comparative judgments before returning to novel representation design;
6. avoids treating post-cutoff tests or PR activity as proof of cutoff completion.

Record each answer verbatim, model and prompt version, source conditions, answer cost, assessor, pointwise rubric decisions, and supported/unsupported citations. Independently inspect any discrepancies against the visible transcript. Do not calculate a comparative win from this **single** case; grow a varied benchmark from additional long-running inquiries.

## Failure localization
1. **Extraction:** Can the terminal activity be stated and anchored from the exported source?
2. **Encoding:** Can existing `goal`, `move`, `question`, event, and relation constructs express active/incomplete tasks and dependencies?
3. **Projection/retrieval:** Does the report or query return that encoded activity prominently, without burying it under the parent goal?
4. **Reader:** With the same evidence, does an independent answerer choose the correct continuation?

Only propose a shared schema change when an accurately anchored and correctly retrieved existing-schema record *cannot* express the necessary distinctions. Passing JSON validation or exact-anchor checks is not sufficient evidence of continuation accuracy.

## Current outcome
**Protocol and human-checked reference authored; no independent A/B/C model comparison has been run.** Existing observed failure: the earlier assistant continuation identified the parent canonical-factorization problem and later proof checks rather than the active comparative-framework task. This observation is a motivating case, not a measured benchmark score.

## Acceptance criteria for the next experimental PR
- Independent evaluator given no gold key before answering.
- Graph uses only information observable at the specified source cutoff.
- Ground truth and each emitted answer carry source excerpts, with attribution.
- Baseline and augmented graph use the same projection and model prompt.
- Report coverage by rubric point, unsupported assertions, and failures separately.
- Do not advertise schema insufficiency without a failed existing-schema encoding-and-retrieval attempt.
