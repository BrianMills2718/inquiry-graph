# Reusable prior-art-first synthesis protocol

**Status:** proposed working protocol, synthesized from established methods; not a claim that one published standard prescribes this exact combination.  
**Purpose:** solve goal-directed problems by finding, evaluating, adapting, and validating existing work before creating new methods or concepts.  
**Case study:** the inquiry into a general framework for heterogeneous representations.

## Operating principle

Assume that useful prior art probably exists, but treat that as a search heuristic rather than a truth claim. Prefer adoption or adaptation of an existing solution. Synthesize across sources only when the combination is justified. Propose original work only after documenting a specific unresolved requirement and showing why known alternatives do not satisfy it.

LLMs are discovery, translation, comparison, and synthesis aids—not authoritative evidence. Every material claim about prior art should be traceable to sources, and every proposed synthesis should be tested against concrete cases.

## Methodological lineage

This protocol combines complementary established methods:

1. **Systematic mapping / evidence synthesis** to discover and classify the landscape and reduce omission risk.
2. **Conceptual framework analysis** to extract concepts, attributes, assumptions, and relationships across disciplines.
3. **Requirements traceability and quality evaluation** to preserve the user's full intent and connect each requirement to evidence and tests.
4. **Scenario-based comparative evaluation / design science** to test whether candidate frameworks or a synthesis actually meet the goal.
5. **Knowledge provenance** to preserve the chain from source claims through interpretation to recommendation.

This is a purpose-built combination of methods, not a claim that the exact combined protocol is a named, validated standard.

## Stage 0 — State the goal before naming the solution

Record:
- **Desired outcome:** what should become possible or easier?
- **User and context:** who needs it, and under what constraints?
- **Inputs and outputs:** what artifacts enter and leave the process?
- **Success criteria:** observable conditions for considering the goal met.
- **Constraints:** time, cost, tools, formality, interoperability, runtime, or evidence requirements.
- **Known assumptions:** mark each as confirmed, tentative, or to test.
- **Non-goals:** what does not need to be solved?

Do not prematurely translate the goal into a favored technical vocabulary. Keep the user's original language alongside normalized search terms.

## Stage 1 — Search the landscape systematically

### Search questions
1. Is there an existing solution to the whole goal?
2. Are there established methods for the same problem under different names or in other disciplines?
3. Are there standards, textbooks, surveys, systematic reviews, implementations, or mature tools?
4. What does each candidate explicitly claim to solve—and explicitly exclude?
5. What evidence would demonstrate that it works?

### Search procedure
- Search multiple vocabulary families, disciplines, and artifact types; use synonym and adjacent-term expansion.
- Prioritize primary sources, standards, seminal papers, recent surveys, official documentation, and concrete implementations.
- Record exact queries, databases/sites, dates, and follow-up citation trails.
- Follow references backward to foundational work and forward to later comparisons, extensions, critiques, and implementations.
- Use LLMs to propose terminology, candidate references, comparisons, and counterexamples; independently verify citations and substantive claims.
- Stop only when the documented stopping rule is met, not when the first plausible candidate appears.

### Inclusion/exclusion
Include a candidate when a source-backed connection to at least one requirement is plausible. Exclude only with a recorded reason (e.g. wrong problem, inaccessible evidence, obsolete/replaced approach, or merely lexical similarity). Keep near-misses if they clarify the boundary of the problem.

### Search stopping rule
A provisional stopping point requires: (a) coverage of all major vocabulary families and relevant disciplines; (b) review of the strongest primary/overview sources for the leading candidates; (c) backward/forward citation checks on the closest matches; (d) at least one attempt to falsify the leading hypothesis with alternatives and counterexamples; and (e) no newly found source in the last search round that materially changes the candidate set. Report this as a bounded search, never proof that no other work exists.

## Stage 2 — Extract candidates consistently

For each candidate, capture:
- Citation, stable URL/DOI/version/date, and source type.
- Problem and intended users.
- Core concepts and their definitions.
- Input artifacts, output artifacts, and workflow.
- Formal primitives, mechanisms, and composition rules.
- Assumptions, scope, explicit non-goals, and dependencies.
- Supported capabilities and unsupported capabilities.
- Evidence type: normative standard, theorem/proof, empirical evaluation, case study, implementation, author claim, or secondary interpretation.
- Concrete demonstrations or worked examples.
- Maturity, tooling, adoption evidence, and known critiques where available.
- Requirement IDs addressed; direct evidence versus inference; confidence and open questions.

Keep source statements, our interpretations, and our recommendations distinct. Do not convert missing documentation into proof of missing capability.

## Stage 3 — Maintain a stable requirements catalogue

Requirements are derived from the user's goal, not invented to fit the candidates. Each requirement gets a stable ID, plain-language statement, rationale/source anchor, priority, operational test, and status.

For the current representation-framework case, preserve these dimensions as candidate requirements, not presumed independent axes:

- R01 — Categories, taxonomies, types, and subtype/instance distinctions.
- R02 — Relations, attributes/properties, arity, and relation kinds.
- R03 — Identity, equivalence, individuation, and persistence.
- R04 — Cardinality, multiplicity, constraints, invariants, and well-formedness.
- R05 — Syntax, signatures, vocabularies, schemas, and language definitions.
- R06 — Semantics, interpretation, models, satisfaction, and consequence.
- R07 — Intended reference and empirical grounding; measurements, observations, identifiers, and validation.
- R08 — Uncertainty, partial information, context, time, and provenance.
- R09 — Rules, inference, calculations, theorems, derivations, and proof objects.
- R10 — State, transitions, dynamics, causal/law-like constraints, and initial conditions.
- R11 — Execution, simulation, computation, code generation, and operational semantics.
- R12 — Mappings, translations, refinements, alignments, and semantic-preservation conditions across formalisms.
- R13 — Composition, modularity, extensibility, reuse, and interoperability.
- R14 — Consistency, satisfiability, verification, validation, and quality evaluation.
- R15 — Expressiveness, decidability, tractability, and computational/resource costs.
- R16 — Separation between a represented domain/reality and the language/model that represents it.
- R17 — Ability to express meta-level claims about representational systems themselves.
- R18 — Evidence that the proposed decomposition is complete for a declared universe and that its parts are independent or intentionally overlapping.

Do not treat this list as final or MECE. Add, split, merge, or mark inapplicable requirements only with a reason and traceability to the goal. Explicitly distinguish an absent capability from a capability delegated to another formalism or tool.

## Stage 4 — Compare with requirements traceability

For each candidate × requirement, use one of:
- **Demonstrated:** primary source or working example explicitly supports it.
- **Claimed:** source asserts it, but demonstration/evidence not yet inspected.
- **Composable/delegated:** supported only by combining with another formalism/tool.
- **Partial/conditional:** works only under stated assumptions or for a restricted fragment.
- **Not supported / out of scope:** documented limitation or failed test.
- **Unknown:** insufficient evidence; never silently score as failure.

Record a source citation and short rationale for every non-unknown judgment. Avoid a single aggregate score unless weights are justified by the user's priorities. Keep separate columns for problem fit, capability, mechanism, evidence strength, maturity, and practical cost.

## Stage 5 — Synthesize concepts, not just feature lists

Use conceptual framework analysis:
1. Extract each candidate's concepts and operational definitions.
2. Compare meanings that appear similar but may differ.
3. Record attributes, assumptions, exclusions, and levels of abstraction.
4. Map relations between concepts: equivalent, specializes, composes with, translates to, conflicts with, or addresses a different layer.
5. Construct a provisional framework with explicit links to source concepts.
6. Record contradictions and unresolved choices rather than hiding them.
7. Test whether the synthesis adds real explanatory or practical value over using one candidate directly.

A synthesized framework should be minimal only relative to stated goals. Avoid claiming a universal ontology or canonical basis from a convenient diagram.

## Stage 6 — Evaluate against representative cases

Use cases as falsification tests, not illustrations selected only because the framework handles them well. For this inquiry, include at least:
- Physical theory + parameters/initial conditions + numerical simulation.
- Mathematical theory + theorem + proof/derivation.
- Cellular automaton: state space, neighborhood/rule, initial configuration, transition, execution trace.
- Empirical classification with real-world identifiers/observations and uncertainty.
- Translation between heterogeneous specifications or ontologies.

For each case specify the source artifact, desired output, semantic obligations, expected checks, and failure conditions. Ask whether the candidate supports the case directly, through a documented composition, or not at all.

## Stage 7 — Decide what to adopt, combine, or invent

Apply this order:
1. **Adopt** an existing framework if it satisfies the important requirements at acceptable cost.
2. **Configure/extend** it if its documented extension mechanisms cover the gap.
3. **Compose** multiple frameworks if the interface and semantic obligations between them can be made explicit and validated.
4. **Adapt** a method from another discipline if the transfer assumptions hold.
5. **Invent** only for a residual gap supported by evidence.

For every proposed novel element, write a gap statement: requirement ID; candidates considered; evidence for their limitations; why configuration/composition is insufficient; smallest new contribution needed; and a test that would show the contribution is useful.

## Stage 8 — Preserve provenance and update the Inquiry Graph

Capture:
- Goal and requirements.
- Search actions and search coverage.
- Candidate frameworks and source records.
- Source-grounded claims, interpretations, and uncertainty.
- Comparisons and their evidence.
- Synthesis decisions and conflicting concepts.
- Case-test results and failures.
- Decision, residual gaps, and next action.

Keep inferred relationships marked as inferred/proposed until reviewed. A conversation capture is not a complete transcript unless it actually is one. Do not change shared graph schema based on one case without a separate fit review and explicit authorization.

## Threats to validity and safeguards

- **Search bias:** broaden vocabulary, disciplines, and source types; record queries and dates.
- **Confirmation bias:** search for counterexamples and competing approaches.
- **LLM hallucination:** verify citations and source claims against primary material.
- **False equivalence:** compare definitions and semantics, not names alone.
- **Feature-matrix illusion:** distinguish problem, mechanism, capability, evidence, and outcome.
- **False MECE:** define the universe and decomposition target; test overlap, omitted cases, and independence.
- **Over-synthesis:** prefer a strong existing solution over an elaborate hybrid without demonstrated benefit.
- **Novelty inflation:** label uncertainty; a bounded search cannot prove nonexistence.
- **Method drift:** maintain a versioned protocol and requirements catalogue; changes must be justified by evidence.

## Applying this protocol to the current inquiry

The initial stages have now been carried out provisionally:

1. **Goal and requirements:** preserved as provisional requirements R01–R18; none are presumed independent or MECE.
2. **First-pass mapping:** `systematic-mapping.md` records a cross-disciplinary search and primary-source references. This is explicitly a bounded first pass, not a completed database-wide systematic mapping study.
3. **Scenario-based analysis:** `scenario-evaluation.md` defines five operational test fixtures and evaluates the documented scope of DOL, MMT, institution theory, SysML v2/KerML, Modelica/FMI, ologs, SKOS/OWL/SOSA/SSN/PROV-O, and OAEI.
4. **Comparison matrix:** `comparison-matrix.md` records the added candidate families and the cross-case synthesis, with unknown/partial/composition boundaries kept distinct from proven absence.
5. **Inquiry Graph:** new findings and the unresolved hypothesis are captured in `graph.json`; source anchors and graph references were validated.

### Current conclusion

The reviewed sources show strong existing frameworks for distinct obligations, but no single candidate examined so far documents native coverage of formal proof, executable dynamics, empirical observation/grounding, and semantics-preserving translation across all five cases. This is not yet a demonstrated novelty gap. The assessment is based on source-level capability review; the candidate tools have not been run against the fixtures.

The strongest current candidate composition is conditional, not mandatory: DOL for heterogeneous formal OMS and mappings; MMT where formal languages, theories, proofs and cross-foundation modularity matter; institution theory for abstract logic/semantic-preservation reasoning; Modelica/FMI for dynamic execution; SysML v2/KerML for systems-engineering structure/behavior; SKOS or OWL for conceptual classification; SOSA/SSN for observation artifacts; and PROV-O for provenance. OAEI is relevant for benchmarking ontology matching, not as a general semantics-preserving translation framework.

### Next research action

Fixture sanity checks, Z3 solver checks, a Lean proof-assistant check, adjacent local implementation tests, and a real Hets DOLiator parse/translation smoke test have now been completed. A native consistency result and dynamic-model tool run remain open.

1. **Lean proof-assistant check (done):** Lean 4.30.0 core accepted the saved source in `lean-proof-checks.lean`, reporting “Compiled without errors” and printing proof terms for `n + 0 = n`, a nonnegative identity-age mapping invariant, exact Nat day/year arithmetic, and a wrong-units counterexample. No unfinished proof placeholders occur. This validates specific propositions, not a mapping between frameworks.
2. **Z3 solver tests (done):** Z3 5.3.1.0, installed in an isolated temp target after verifying its official PyPI wheel hash, returned UNSAT for arithmetic/mapping violation queries and SAT for the wrong-units negative control. See `solver-checks.json`.
3. **Adjacent prototype (done):** the existing FOL Operational Metamodel workspace passed 21 tests for importing a pinned compiled MMT FOL OMDoc artifact, finite-structure satisfaction, and sort/arity rejection. This is not proof that the MMT executable checked the present examples.
4. **DOL parsing and translation graph (partially done):** the public Hets DOLiator successfully constructed a 3-node/2-edge development graph for `Parthood_OWL`, its internal Common Logic translation node, and `Parthood_CL`, using the `OWL22CommonLogic` morphism. The reproducible sources are `dol-translation-smoketest.dol` and `dol-view-smoketest.dol`; structured results are in `dol-tool-checks.json`. The first produced a 3-node/2-edge OWL-to-Common-Logic graph. The second produced a 3-node graph with a symbol-mapped `GlobalDef` edge and a `GlobalUnprovenThmInc` edge for view `v`. This is actual parser/development-graph evidence, not a proof of preservation or consistency. The deployed consistency checker returned `no cons checker found` even for the OWL-only node with Pellet; the automatic-proof route returned `nothing to prove` for both the original example and the custom view, despite that view edge being labelled unproven. No logical obligation was verified.
5. **Next DOL verification test:** find a supported Hets/Ontohub environment with a working checker or set up a local Hets toolchain without changing system packages implicitly. Then define two minimal OMS and a mapping, run an actual semantic/coherence obligation, and preserve the output plus the precise guarantee it establishes. Do not report parser success as proof.
6. **Native dynamics test (next):** run the oscillator in Modelica/FMI or a conforming SysML v2-capable tool. Save tool/version, source model, solver/execution settings, output trace, and analytic comparison; the standalone RK4 calculation validates only the fixture oracle.
7. **Compare against requirements R01–R18** after the native tests. Update evidence ratings only when supported by primary sources or execution outputs. Then formulate any requirement-specific residual gap and test whether composition already meets the goal.

The standalone Python checks validated the Rule 30 trace and oscillator oracle; a 1,001-record toy mapping preserved its stated age invariant and its units-mismatch negative control was detected. Those checks, the SMT results, Lean proof terms, FOL prototype tests, and Hets development graph are distinct evidence types and must not be conflated.

Continue citation chaining for DOL/MMT and candidate cross-framework compositions. Do not make a “no one has done this” claim from the bounded search. Do not infer that failure to find a tool installed locally means the tool is generally unavailable.


## Methodological starting points

- Jabareen, Y. (2009), “Building a Conceptual Framework: Philosophy, Definitions, and Procedure.” https://doi.org/10.1177/160940690900800406
- Petersen et al. (2008), “Systematic Mapping Studies in Software Engineering.” https://doi.org/10.14236/ewic/EASE2008.8
- Kitchenham & Charters (2007), “Guidelines for performing Systematic Literature Reviews in Software Engineering.” https://www.cs.auckland.ac.nz/~norsaremah/2007%20Guidelines%20for%20performing%20SLR%20in%20SE.pdf
- OQuaRE, ontology quality evaluation framework: https://oquare.github.io/
- Hevner et al. (2004), “Design Science in Information Systems Research.” https://doi.org/10.2307/25148625

These references motivate components of the protocol; they do not validate this exact combination as a single established standard.
