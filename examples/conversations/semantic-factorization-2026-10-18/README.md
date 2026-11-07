# Canonical factorization of semantic representations — 2026-10-18

This curated Inquiry Graph fixture covers the discussion of taxonomy, ontology, the semantic spectrum, grounding, model theory, types/cardinality/constraints, category theory, database theory, and executable or operational representations.

## Files

- `graph.json` — source-anchored curated inquiry map.
- `fit-review.json` — representation-fit diagnoses and promotion gates.
- `prior-art.md` — targeted investigation of DOL, MMT, institution theory, model-driven engineering, ologs, top-level ontologies, and universal logic.
- `comparison-matrix.md` — candidate comparison plus the supplementary framework-boundary and scenario summary.
- `research-protocol.md` — reusable prior-art-first workflow assembled from established methodological components; not one named standard.
- `systematic-mapping.md` — first-pass, source-backed map of methodological and technical prior art; not a completed database-wide systematic review.
- `scenario-evaluation.md` — five operational case fixtures, source-based framework evaluation, independent Python oracle checks, Z3 solver checks, Lean-checked propositions, and related local FOL/MMT implementation evidence.
- `comparative-evidence-round2.md` — expanded primary-source, scenario-by-scenario judgments testing overlooked competitors (Maude, Hets, TLA+/TLC, SHACL, Common Logic), explicit native/encoded/delegated distinctions, requirement traceability, and falsification tests.
- `solver-checks.json` — exact SMT queries/results, solver/package version, verified wheel checksum, native proof-object note, and limitations.
- `lean-proof-checks.lean` — exact four-declaration Lean source submitted through the online playground.
- `lean-proof-checks.json` — Lean version, UI result, declarations checked, printed proof-term notes, and limitations.
- `dol-translation-smoketest.dol` — the reproducible OWL-to-Common-Logic translation example submitted to Hets DOLiator.
- `dol-view-smoketest.dol` — a tiny Common Logic view mapping used to test representation of a custom mapping edge.
- `dol-tool-checks.json` — actual development-graph output and the deployed consistency-checker failure.

## Coverage and status

This is **not** a complete native ChatGPT export. It preserves selected visible excerpts that establish the main questions, hypotheses, distinctions, and requested next action. Intervening wording is omitted. Semantic annotations are proposed, not independently reviewed.

The graph deliberately does not claim that the listed dimensions form a canonical or MECE factorization. That remains an open research question.

## Current frontier

The broader reusable process is: state the goal and success criteria; search across disciplines for prior art; synthesize only where evidence justifies it; evaluate against representative cases; and create new material only for a demonstrated residual gap. The protocol combines established methodological components—systematic mapping, conceptual framework analysis, integrative-review practices, requirements traceability, scenario tests, and provenance—without claiming that a single published standard prescribes this exact combination.

The first-pass map distinguishes the *method of research synthesis* from the *technical frameworks being investigated*. The five-case evaluation covers physics plus simulation, mathematics plus proof, cellular automata, empirical taxonomy, and cross-formalism translation. Source checks point toward a compositional approach: DOL/MMT/institution theory for formal integration and logic; Modelica/FMI or SysML v2/KerML for selected executable system models; SKOS/OWL plus SOSA/SSN and PROV-O for taxonomy, observation artifacts, and provenance; and OAEI for ontology-matching evaluation.

This is **not yet evidence of a universal factorization gap**. The synthetic Rule 30 and oscillator oracle checks now pass in standalone Python; a 1,001-record Person-to-Human age mapping preserved the declared property, and a deliberately incorrect days-to-years identity mapping was rejected. The existing local FOL Operational Metamodel workspace's 21-test importer/evaluator suite also passes. Z3 5.3.1.0 returned UNSAT for the counterexample to n + 0 = n over nonnegative integers and exposed an internal proof object; it also verified the encoded identity-mapping and exact integer day-to-year contracts, while finding the expected wrong-units counterexample. I then ran the corresponding arithmetic and mapping statements in the public Lean 4.30.0 core-library playground; it reported “Compiled without errors” and printed proof terms for all four declarations, with no `sorry` or `admit`. These are checked proofs of the explicitly encoded small statements, not MMT-native formalization or DOL/MMT/SysML/Modelica conformance. The public Hets DOLiator now provides a real parser/translation smoke-test result: it built a three-node, two-edge OWL-to-Common-Logic development graph for the sample in `dol-translation-smoketest.dol`. Its deployed consistency checker returned `no cons checker found`, including for an OWL-only check with Pellet. The separate automatic-proof route (E Prover plus OWL-to-TPTP FOF) returned `nothing to prove`. A second custom Common Logic view produced a `GlobalDef` symbol-mapping edge and a `GlobalUnprovenThmInc` edge, but the E Prover/TPTP route still returned `nothing to prove`. Therefore no consistency result or proof of semantic preservation was obtained; the graph records a mapping obligation, not its verification. Next, use a working Hets/Ontohub checker for a custom mapping and execute the oscillator or cellular automaton in Modelica/FMI or a conforming SysML v2 tool. Compare actual tool evidence against requirements R01–R18 before considering a novel contribution.

The fit review distinguishes this research question from Inquiry Graph's own schema. A single conversation can reveal a candidate representational gap but cannot authorize a shared schema change.

## Expanded primary-source comparison — October 18, 2026

The source-based five-case comparison now includes more than the original DOL/MMT/Modelica/ontology set. See [comparative-evidence-round2.md](comparative-evidence-round2.md). The additional **Maude** and **TLA+/TLC** cases challenge the earlier tendency to separate general formal semantics from executable behavior; **Hets** is a concrete heterogeneous translation/proof-management competitor, **SHACL** separates RDF record validation from OWL entailment, and **Common Logic** clarifies what expressive interchange standards explicitly exclude. For the empirical case, the 2026-10-12 SOSA/SSN "2023 Edition" is a **Working Draft**, not a Recommendation. These are all documented capabilities, not native fixture tests performed during this pass.

**Updated research priorities:** (1) actual Hets/DOL multi-logic mapping and semantic-preservation check with negative control; (2) Maude versus TLA+/TLC on the identical synchronous Rule 30 transition semantics; (3) Modelica/FMI oscillator; (4) OWL/SKOS/SHACL/SOSA/PROV specimen classification; (5) MMT theory/morphism checking. These priorities refine, rather than complete or replace, the pending tool-level testing described above. No universal/MECE factorization or novelty gap has been established.
