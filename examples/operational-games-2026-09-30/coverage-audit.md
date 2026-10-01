# Coverage audit — 2026-09-30 operational-games / compositional-world conversation

**Status:** substantive-turn coverage audit, not full-export reconciliation.

This audit checks whether each major inquiry arc visible in the 2026-09-30 conversation is represented in `source-excerpts.json` and semantically reflected in the curated graph.

| Arc | Coverage | Representative source keys |
| --- | --- | --- |
| Factorization / canonical decomposition | covered | `factorization-generalization`, `factorization-trigger-question`, `factorization-trigger-answer` |
| Megamodeling and representation structure | covered | `megamodel-question`, `megamodel-role`, `factorization-role` |
| Game-relative formalism and uncertainty over the game | covered | `game-relative-math`, `game-identification-uncertainty`, `game-as-hypothesis` |
| White-box simulation, embedded agents, computational opacity | covered | `white-box-simulation`, `white-box-limit`, `irreducibility-god`, `known-rules-hard` |
| Prior-art-first / stop inventing | covered | `prior-art-expectation`, `unawareness-prior-art`, `stop-inventing` |
| Compositional game theory / open games | covered | `cgt-question`, `cgt-relevance`, `composition-space` |
| Universal-game / competence-all-the-way-down thread | covered | `universal-game-vacuity-user`, `competence-all-way-down-user`, `ball-game-user` |
| Goal/self-model and participant-relative framing | covered | `goal-self-model-user`, `self-goal-fallible-user`, `game-goal-model-coupling-user` |
| Why continue CVS / does this already exist? | covered | `project-purpose-doubt`, `already-exists-reframe`, `replacement-not-differentiation` |
| Off-the-shelf / replacement-first preference | covered | `off-shelf-preference-full`, `replacement-first-user`, `replacement-first-reframe` |
| World Substrate review and CVS seam | covered | `world-substrate-review-request`, `world-substrate-cvs-seam`, `world-runtime-solvers-backends` |
| Cybernetic Influence V3 review / Concordia foundation | covered | `ci-review-request`, `ci-self-replacement` |
| Simudyne replacement candidate and trial | covered | `simudyne-primary-trial`, `trial-execution-request`, `simudyne-access-cost-boundary` |
| Simudyne open-source value question | covered | `simudyne-value-question`, `simudyne-integration-value` |
| Simudyne cost / hiring / budget constraint | covered | `simudyne-cost-hiring-question`, `simudyne-cost-answer`, `budget-block-user`, `do-not-pay-simudyne` |
| Framework-bakeoff objection / first-principles correction | covered | `anti-bakeoff-full`, `anti-bakeoff-correction`, `first-principles-selection` |
| Reconsidering CGT's surviving role | covered | `cgt-value-reopen`, `cgt-strategic-role`, `cgt-strategic-component` |
| Mechanical long-range dependencies / truck fuel | covered | `mechanical-dependencies-user`, `truck-mechanical-example-full`, `composable-units-full` |
| Reframing to compositional causal/mechanical worlds | covered | `causal-world-reframe`, `world-primary-full`, `game-as-component`, `compositional-executable-world` |
| Inquiry Graph update decision | covered | `graph-update-request-full`, `graph-existing-answer`, `graph-update-compositional-world` |
| Composition-layer question | covered | `composition-layer-question` |
| Epistemic Warrant / UGD review | covered | `ugd-review-request`, `ugd-semantic-contract-role` |
| Minimum executable substrate question | covered | `minimum-runtime-question` |
| UGD runtime synthesis result | covered | `wiring-contract-architecture` |
| Request for complete conversation coverage | covered | `full-conversation-coverage-request` |
| Truck logistics composition acceptance fixture | covered | `proceed-truck-fixture`, `truck-fixture-scope`, `truck-fixture-pass`, `truck-fixture-merged` |

## What "covered" means

`covered` means the substantive inquiry move is represented by at least one verbatim visible excerpt and corresponding graph content/move/status where applicable.

It does **not** mean:

- every sentence in every assistant response has been copied into the fixture;
- every turn has an original ChatGPT message ID or timestamp;
- the fixture has been reconciled against a downloadable ChatGPT export;
- semantic annotations have been independently adjudicated as gold labels.

The current source is still `curated_excerpts`. The strongest justified claim is **substantive semantic coverage of the visible conversation available to the curator**.

## Remaining verification step

For byte-for-byte turn completeness, import the full ChatGPT export / active branch and reconcile each excerpt to original message IDs using the repository's documented reconciliation process. Until then, do not relabel this fixture as verified full-export coverage.
