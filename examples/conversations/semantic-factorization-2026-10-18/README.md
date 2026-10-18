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
- `solver-checks.json` — exact SMT queries/results, solver/package version, verified wheel checksum, native proof-object note, and limitations.
- `lean-proof-checks.lean` — exact four-declaration Lean source submitted through the online playground.
- `lean-proof-checks.json` — Lean version, UI result, declarations checked, printed proof-term notes, and limitations.

## Coverage and status

This is **not** a complete native ChatGPT export. It preserves selected visible excerpts that establish the main questions, hypotheses, distinctions, and requested next action. Intervening wording is omitted. Semantic annotations are proposed, not independently reviewed.

The graph deliberately does not claim that the listed dimensions form a canonical or MECE factorization. That remains an open research question.

## Current frontier

The broader reusable process is: state the goal and success criteria; search across disciplines for prior art; synthesize only where evidence justifies it; evaluate against representative cases; and create new material only for a demonstrated residual gap. The protocol combines established methodological components—systematic mapping, conceptual framework analysis, integrative-review practices, requirements traceability, scenario tests, and provenance—without claiming that a single published standard prescribes this exact combination.

The first-pass map distinguishes the *method of research synthesis* from the *technical frameworks being investigated*. The five-case evaluation covers physics plus simulation, mathematics plus proof, cellular automata, empirical taxonomy, and cross-formalism translation. Source checks point toward a compositional approach: DOL/MMT/institution theory for formal integration and logic; Modelica/FMI or SysML v2/KerML for selected executable system models; SKOS/OWL plus SOSA/SSN and PROV-O for taxonomy, observation artifacts, and provenance; and OAEI for ontology-matching evaluation.

This is **not yet evidence of a universal factorization gap**. The synthetic Rule 30 and oscillator oracle checks now pass in standalone Python; a 1,001-record Person-to-Human age mapping preserved the declared property, and a deliberately incorrect days-to-years identity mapping was rejected. The existing local FOL Operational Metamodel workspace's 21-test importer/evaluator suite also passes. Z3 5.3.1.0 returned UNSAT for the counterexample to n + 0 = n over nonnegative integers and exposed an internal proof object; it also verified the encoded identity-mapping and exact integer day-to-year contracts, while finding the expected wrong-units counterexample. I then ran the corresponding arithmetic and mapping statements in the public Lean 4.30.0 core-library playground; it reported “Compiled without errors” and printed proof terms for all four declarations, with no `sorry` or `admit`. These are checked proofs of the explicitly encoded small statements, not MMT-native formalization or DOL/MMT/SysML/Modelica conformance. Actual DOL mapping and native dynamics tests remain outstanding. Next, run a minimal DOL mapping between two supported OMS with an explicit preservation/coherence check, then execute the oscillator or cellular automaton in Modelica/FMI or a conforming SysML v2 tool. Compare actual tool evidence against requirements R01–R18 before considering a novel contribution.

The fit review distinguishes this research question from Inquiry Graph's own schema. A single conversation can reveal a candidate representational gap but cannot authorize a shared schema change.
