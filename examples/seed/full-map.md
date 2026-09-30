# Full reified graph

Content, relations and moves; use the smaller inquiry map first.

```mermaid
flowchart TD
  n0["move: ask"]
  n1["move: propose"]
  n2["move: challenge"]
  n3["move: retract"]
  n4["move: reframe"]
  n5["move: scope"]
  n6["move: ask"]
  n7["move: distinguish"]
  n8["move: reframe"]
  n9["move: hypothesize"]
  n10["move: ask"]
  n11["move: clarify"]
  n12["move: ask"]
  n13["move: reframe"]
  n14["move: hypothesize"]
  n15["move: reframe"]
  n16["move: scope"]
  n17["move: propose"]
  n18["move: challenge"]
  n19["move: clarify"]
  n20["move: connect"]
  n21["move: challenge"]
  n22["move: hypothesize"]
  n23["move: propose"]
  n24["move: ask"]
  n25["move: ask"]
  n26["move: distinguish"]
  n27["move: hypothesize"]
  n28["move: challenge"]
  n29["move: clarify"]
  n30["move: connect"]
  n31["move: connect"]
  n32["move: challenge"]
  n33["move: propose"]
  n34["move: propose"]
  n35["move: challenge"]
  n36["move: clarify"]
  n37["move: connect"]
  n38["move: ask"]
  n39["move: propose"]
  n40["move: reframe"]
  n41["move: propose"]
  n42["move: propose"]
  n43["move: reframe"]
  n44["move: connect"]
  n45["move: ask"]
  n46["move: propose"]
  n47["move: connect"]
  n48["move: propose"]
  n49["move: connect"]
  n50["move: challenge"]
  n51["move: connect"]
  n52["move: propose"]
  n53["move: reframe"]
  n54["move: hypothesize"]
  n55["move: retract"]
  n56["move: connect"]
  n57["move: summarize"]
  n58["move: summarize"]
  n59["move: propose"]
  n60["move: clarify"]
  n61["move: scope"]
  n62["move: ask"]
  n63["move: clarify"]
  n64["move: connect"]
  n65["move: challenge"]
  n66["move: challenge"]
  n67["move: challenge"]
  n68["move: clarify"]
  n69["move: ask"]
  n70["move: distinguish"]
  n71["move: connect"]
  n72["move: clarify"]
  n73["move: hypothesize"]
  n74["move: hypothesize"]
  n75["move: reframe"]
  n76["move: summarize"]
  n77["move: hypothesize"]
  n78["move: connect"]
  n79["move: ask"]
  n80["move: challenge"]
  n81["move: reframe"]
  n82["move: distinguish"]
  n83["move: ask"]
  n84["move: clarify"]
  n85["move: scope"]
  n86["move: propose"]
  n87["move: clarify"]
  n88["move: ask"]
  n89["move: propose"]
  n90["move: ask"]
  n91["move: clarify"]
  n92["move: propose"]
  n93["move: reframe"]
  n94["move: clarify"]
  n95["move: challenge"]
  n96["move: propose"]
  n97["move: decompose"]
  n98["move: propose"]
  n99["move: summarize"]
  n100["move: ask"]
  n101["move: summarize"]
  n102["move: propose"]
  n103["move: clarify"]
  n104["move: clarify"]
  n105["move: ask"]
  n106["move: clarify"]
  n107["move: connect"]
  n108["move: ask"]
  n109["move: propose"]
  n110["move: challenge"]
  n111["move: distinguish"]
  n112["move: distinguish"]
  n113["move: clarify"]
  n114["move: decompose"]
  n115["move: propose"]
  n116["move: ask"]
  n117["move: scope"]
  n118["move: challenge"]
  n119["move: propose"]
  n120["move: clarify"]
  n121["move: propose"]
  n122["move: decompose"]
  n123["move: retract"]
  n124["move: clarify"]
  n125["move: challenge"]
  n126["move: clarify"]
  n127["move: distinguish"]
  n128["move: clarify"]
  n129["move: ask"]
  n130["move: connect"]
  n131["move: hypothesize"]
  n132["move: clarify"]
  n133["move: propose"]
  n134["move: clarify"]
  n135["move: deduce"]
  n136["move: connect"]
  n137["move: challenge"]
  n138["move: distinguish"]
  n139["move: connect"]
  n140["move: scope"]
  n141["move: summarize"]
  n142["move: ask"]
  n143["move: ask"]
  n144["move: scope"]
  n145["move: test"]
  n146["move: challenge"]
  n147["move: distinguish"]
  n148["move: hypothesize"]
  n149["move: challenge"]
  n150["move: connect"]
  n151["move: distinguish"]
  n152["move: distinguish"]
  n153["move: ask"]
  n154["move: summarize"]
  n155["move: generalize"]
  n156["move: propose"]
  n157["move: clarify"]
  n158["move: ask"]
  n159["move: reframe"]
  n160["move: clarify"]
  n161["move: ask"]
  n162["move: propose"]
  n163["move: clarify"]
  n164["move: generalize"]
  n165["move: ask"]
  n166["move: propose"]
  n167["move: generalize"]
  n168["move: ask"]
  n169["move: connect"]
  n170["move: decompose"]
  n171["move: distinguish"]
  n172["move: distinguish"]
  n173["move: distinguish"]
  n174["move: clarify"]
  n175["move: generalize"]
  n176["move: propose"]
  n177["move: ask"]
  n178["move: clarify"]
  n179["move: scope"]
  n180["move: clarify"]
  n181["move: distinguish"]
  n182["move: propose"]
  n183["move: decompose"]
  n184["move: connect"]
  n185["move: scope"]
  n186["move: distinguish"]
  n187["move: clarify"]
  n188["move: summarize"]
  n189["move: scope"]
  n190["move: ask"]
  n191["move: clarify"]
  n192["move: reframe"]
  n193["move: ask"]
  n194["move: connect"]
  n195["move: reframe"]
  n196["move: test"]
  n197["move: ask"]
  n198["move: connect"]
  n199["move: ask"]
  n200["move: connect"]
  n201["move: clarify"]
  n202["move: ask"]
  n203["move: scope"]
  n204["concept: A: hypotheses newly live after semantic alignment of the previous state."]
  n205["claim: Novelty is not a project objective; mature off-the-shelf theory is preferable to reinventing machinery."]
  n206["reference: AIF+ and Inference Anchoring Theory as candidate dialogue/argument representations."]
  n207["hypothesis: Candidate generation may be better modeled as an algebra over languages, expressions, theories and queries than as a short folk list of cognitive verbs."]
  n208["hypothesis: Ampliative warrant requires assumptions or constraints beyond bare logical entailment from finite evidence."]
  n209["claim: Nontrivial ampliative guarantees require restrictions on the admissible possible-world or problem class."]
  n210["claim: For an embedded observer, constraints used in derivations should be described as assumed rather than known."]
  n211["claim: Assumption is normally a role played by a sentence or theory rather than a base formal artifact type."]
  n212["concept: An ATMS-style environment is a consistent set of assumptions under which consequences can be evaluated."]
  n213["concept: A label records minimal consistent assumption environments sufficient to support a datum."]
  n214["reference: de Kleer's Assumption-based Truth Maintenance System as a precedent for multiple simultaneous assumption environments and dependency labels."]
  n215["hypothesis: Persistent epistemic organization can be represented as assumptions, explicit justifications and minimal support environments rather than one committed theory."]
  n216["goal: Derive a taxonomy from modest explicit assumptions rather than simply assuming it."]
  n217["claim: Conditionalization presupposes a hypothesis space, likelihoods and priors; it does not ground all of them."]
  n218["method: A Bayesian or causal DAG as a candidate representation of inferential relationships."]
  n219["hypothesis: Belief change depends on existing representations and an agent-specific updating process."]
  n220["claim: The black-box state maintains alternatives; a white-box move temporarily stipulates one context and inspects its consequences."]
  n221["reference: Bronstein and geometric deep learning as a candidate framework for learning primitives."]
  n222["claim: Bronstein/geometric deep learning should not be part of the foundational spine merely because it was suggested earlier."]
  n223["hypothesis: A generated candidate can have a compositional footprint spanning several formal artifact kinds rather than exactly one exclusive type."]
  n224["concept: Candidate generation maps current state and evidence to candidate propositions, models or structures before evaluation and commitment."]
  n225["hypothesis: Candidate generation is best modeled by an interface separating draft/search space, construction operators, strategy, elaboration, evaluation feedback and warrant."]
  n226["claim: The dialogue itself can serve as an adversarial test case for candidate-generation operators."]
  n227["claim: Candidate generation has mature precedents across creative systems, synthesis/CEGIS, ILP/MIL, anti-unification, abduction, automated theory formation, conceptual blending and Bayesian program learning."]
  n228["claim: The earlier seven candidate types were not orthogonal; some mixed artifact kinds with epistemic roles."]
  n229["method: Test whether each observed candidate-generation move has a clear artifact footprint and compositional operator description."]
  n230["goal: Construct a canonical factorization of epistemic transitions relative to an explicit semantic representation contract."]
  n231["method: Canonical/primitive factorization: propose factors, test completeness/redundancy/independence/compositionality/canonicality, diagnose failures, and revise."]
  n232["goal: Classify hypothesis and model moves without requiring certainty or strong knowledge claims."]
  n233["claim: Artifact translation does not imply guarantee translation; guarantees transport only through typed certified preservation relations, otherwise the target artifact must be re-warranted."]
  n234["claim: Explanations are only a subset of claims that go beyond observations."]
  n235["goal: Preserve the long-session theory in a canonical closeout and an arXiv-style paper before continuing candidate-generation research."]
  n236["claim: Reasoning episodes, strategies and the meta-model should be representable targets, giving closure under self-description."]
  n237["claim: Internal coherence alone does not establish correspondence with reality."]
  n238["concept: Construction of a new expression or concept from constructors and vocabulary already available in the current language."]
  n239["concept: Introduction of genuinely new conceptual or predicate vocabulary not already definable in the current language."]
  n240["claim: A constraint is broader than an explanation or mechanism; empirical, causal and explanatory commitments can occupy different levels."]
  n241["claim: Concept construction inside an existing language and substantive concept invention are different problems."]
  n242["goal: Instantiate the abstract reasoning model on real conversations and identify strategy episodes and reflective relations with provenance."]
  n243["method: Test proposed exhaustive or primitive distinctions by constructing concrete counterexamples and edge cases."]
  n244["hypothesis: Current endpoint: factor epistemic state change relative to a representation contract, keep warrant separate, and treat candidate-generation factorization as open."]
  n245["hypothesis: Current architecture combines an institution-style logical substrate, ATMS-inspired persistent support state, temporary assumption environment, and external query."]
  n246["claim: Deduction and inference by an embedded empirical observer have different dependencies."]
  n247["claim: Defeasible warrant requires explicit attack/defeat relations and can lose license when new defeating information arrives."]
  n248["concept: Extend a signature with a fresh name explicitly defined from old-language expressions, ideally conservatively."]
  n249["concept: D: previously live aligned hypotheses no longer live after the update."]
  n250["hypothesis: Treat communication as a designed transformation of a recipient representation."]
  n251["example: Recognizing spatial separation of black and white dots from individual positions and colors."]
  n252["claim: A reachable draft may be incomplete or ill-formed and must be elaborated/checked before becoming a formal artifact."]
  n253["hypothesis: For reasoning episode R, a draft-generation system G_R=(D_R,d0,O_R,→_R) defines draft states, an initial draft, operators and generative transitions."]
  n254["hypothesis: Conditional deductive context is the closure C(Gamma)=Cl_J(Gamma) of a temporary assumption environment under justifications."]
  n255["example: This dialogue repeatedly split, merged and retyped candidate primitives after detecting over-, under- or misfactoring."]
  n256["example: This dialogue explicitly turned the developing meta-model back onto the process used to construct that same meta-model."]
  n257["concept: A typed epistemic action is the normalized target of warrant, e.g. derive, retain, raise support, accept, retract, use a report, or select a strategy."]
  n258["claim: Equivalence under predictive or causal consequence is better treated as a relevance or model-selection criterion than as the ontology of all patterns."]
  n259["goal: Evaluate reasoning-move trajectories and learn which strategies work under which conditions."]
  n260["claim: Verification or evaluation feedback does not automatically constitute epistemic warrant."]
  n261["concept: Evaluator feedback is a representable diagnostic such as a counterexample, violated constraint, failed proof obligation, empirical mismatch or warrant condition."]
  n262["claim: Evidence need not be a privileged top-level coordinate; reports and observations can be typed provenance-bearing nodes with their own dependencies."]
  n263["hypothesis: For a fixed hypothesis universe, hard live-set changes reduce to additions and deletions; preserve, restrict, expand and replace are derived cases."]
  n264["concept: Build an expression using constructors already licensed by the current language."]
  n265["concept: Underfactored, overfactored and misfactored are diagnostics for revising a proposed primitive decomposition."]
  n266["claim: Canonical-factorization analysis is one strategy that searches a factorization-specific draft space using local operators and evaluators."]
  n267["claim: Repeated detection of over- and underfactoring is a core recurring reasoning pattern in this inquiry."]
  n268["claim: The earlier five proposed move types were not a minimal state-update basis."]
  n269["concept: Elaboration/checking maps a draft candidate to a well-formed formal artifact or failure."]
  n270["concept: Formal Epistemic Reasoning Meta-Model: the foundational project representing the structure of epistemic reasoning across heterogeneous regimes."]
  n271["method: Model an inference method as a function from evidence histories to hypotheses."]
  n272["claim: Institution semantics alone does not provide the concrete syntax/module layer needed to construct and transform formal artifacts."]
  n273["goal: Construct a coherent formalism for epistemic moves without preserving historical inference labels when they obscure the structure."]
  n274["claim: CEGIS, MIL, anti-unification, HR and conceptual blending fit the typed candidate-generation interface without another top-level coordinate."]
  n275["goal: Formalize candidate generation using the dialogue as a test case while importing established operators where possible."]
  n276["claim: Generative space, construction operators and search/control strategy are distinct components."]
  n277["concept: A generative-system transformation changes the represented generative regime itself, such as its language, artifact ontology, bias, operators or evaluators."]
  n278["hypothesis: Generative structure could be the umbrella object for the inquiry."]
  n279["method: Symmetry, deformation stability and scale separation/locality as geometric learning priors."]
  n280["method: When inquiry drifts into downstream implementation or optimization, return explicitly to the original unresolved question."]
  n281["concept: mu: optional graded support or plausibility over live hypotheses."]
  n282["claim: Institutions/DOL/Hets, MMT theory morphisms, abstract interpretation and contract/refinement theory cover much of formal guarantee transport."]
  n283["reference: Hoel, causal emergence, coarse-graining and entropy, raised as related work."]
  n284["goal: Develop a formal compositional calculus of hypothesis-space transformations with a separate warrant layer."]
  n285["claim: Observed conversations underdetermine a person's internal beliefs and update mechanism."]
  n286["claim: IIT is considered only for algorithmic partition, irreducibility and cause-effect-structure machinery, not for consciousness claims."]
  n287["hypothesis: Imagination might contribute an additional way to learn beyond observation."]
  n288["claim: Imagination can generate candidates without independently justifying them."]
  n289["hypothesis: Inductive pattern recognition could initialize a loop through abduction and deduction."]
  n290["goal: Update the inquiry graph with the later conversation arc before handing work to a fresh agent."]
  n291["claim: Institution theory handles language/model semantics while ATMS-like machinery handles support across assumption environments; they are complementary, not competing."]
  n292["hypothesis: Use an institution-style logical substrate (Sig, Sen, Mod, satisfaction) rather than one overloaded universe variable."]
  n293["reference: Institution theory as an abstract separation of signatures, sentences, models and satisfaction, with signature morphisms for translation."]
  n294["hypothesis: Distributed measurements may support joint relational representations not encoded by any individual sensor."]
  n295["hypothesis: An intermediate repair separates language, model space, live hypotheses and graded support as K=(L,M,H,mu)."]
  n296["hypothesis: An intermediate state proposal K=(Sigma,T,W,rho,E,Q) separates signature, explicit theory, semantic possibilities, support, evidence and query."]
  n297["hypothesis: A pattern can be represented by what remains invariant across specified transformations."]
  n298["claim: An unobserved explanatory variable need not specify the process by which an effect occurs."]
  n299["concept: Latent structure as an unobserved explanatory representation, not necessarily a causal mechanism."]
  n300["concept: License is the context- and regime-relative status that a specified epistemic action is permitted with a stated guarantee; it is not identical to warrant."]
  n301["method: When the problem appears well trodden, search existing formal literature before inventing new primitives."]
  n302["concept: H: the currently live hypotheses or possibilities within U."]
  n303["claim: Measurement theory can characterize accessible measured variables without by itself characterizing every structure recognized over those measurements."]
  n304["hypothesis: Sensors determine accessible distinctions, while memory enables relations across time."]
  n305["reference: Measurement theory, psychophysics, information theory and computational mechanics as relevant literatures."]
  n306["hypothesis: Relative to a current epistemic state, entailment versus non-entailment is an immediate MECE logical split."]
  n307["goal: Make exhaustiveness and non-overlap provable by construction rather than asserted from a folk taxonomy."]
  n308["claim: MECE is a desired property of the formalism, not the name of the formal object."]
  n309["claim: MECE is a special case of the broader search for a complete nonredundant compositional factorization."]
  n310["method: Force proposed external formalisms through the current meta-model and treat mismatches as evidence of a gap or bad factorization."]
  n311["method: Use established concept-generation formalisms as a stress test of the epistemic meta-model."]
  n312["claim: The Formal Epistemic Reasoning Meta-Model is provisionally architecturally complete but not theoretically closed."]
  n313["claim: Meta-strategy is not a separate infinite type hierarchy; a strategy is meta-level relative to reasoning processes or strategies it monitors or controls."]
  n314["concept: Classes of evidence-to-conclusion mappings with shared properties."]
  n315["reference: MMT as a foundation-independent theory/declaration/object/morphism representation and module system."]
  n316["hypothesis: Use an MMT-like theory graph as the concrete formal representation substrate, with LF as a possible foundation inside it."]
  n317["hypothesis: Model-target effects can be represented as an exact subset of language, structure, parameter and state coordinates rather than one exclusive target."]
  n318["claim: Natural learning need not assume a designer; deliberate communication is an additional case."]
  n319["hypothesis: Optimal explanation or design is a further problem for an observer with an uncertain model of other observers."]
  n320["claim: Most components and much integration have strong precedents; any novelty claim should be conservative and established only by systematic comparison."]
  n321["concept: God-view versus embedded-observer perspective."]
  n322["hypothesis: Combine AIF/IAT argument and dialogue structure with provenance and inquiry-transition records."]
  n323["concept: An open node is an unresolved question or epistemic obligation, not just a mentioned topic."]
  n324["claim: Choosing an optimal hypothesis is downstream of first characterizing the kinds of epistemic moves available."]
  n325["claim: Pattern recognition or relational feature extraction from a fully observed finite configuration need not be inductive."]
  n326["reference: Grenander/Brown Pattern Theory as a candidate formal language for generators, configurations, transformations, variation, observation and inference."]
  n327["claim: Pattern Theory supplies broad representational and inferential machinery but does not by itself derive all observer representations from physics."]
  n328["hypothesis: Induction concerns empirical patterns while abduction concerns mechanisms."]
  n329["claim: Persistent epistemic state and the active assumption context of a reasoning episode should be represented separately."]
  n330["hypothesis: Current persistent state: K_Sigma=(N,A,J,lambda,rho), with represented nodes, assumptions, justifications, minimal support environments and optional graded support."]
  n331["concept: Physically realizable pattern recognition, rather than normatively justified recognition."]
  n332["hypothesis: External reality plus partial observation plus logic yields a set of compatible possibilities, not by itself a unique ampliative conclusion."]
  n333["goal: Keep the inquiry on its main path, document deferred extensions, and avoid losing the forest for the trees."]
  n334["example: From the observed sequence 2, 4, 6, 8 to the expectation 10."]
  n335["claim: Recognizing a sample pattern and licensing its extension beyond the sample are distinct operations."]
  n336["question: What assumptions and criteria support abductive model selection?"]
  n337["question: Can ampliative epistemic moves be represented in a provably MECE or uniquely factorizable way?"]
  n338["question: Does Bayesian updating explain warrant or merely relocate assumptions?"]
  n339["question: Can candidate generation be given a small compositional or uniquely factorizable basis?"]
  n340["question: Which mature frameworks already cover candidate generation and its integration?"]
  n341["question: What is the minimal type system for generated epistemic candidates?"]
  n342["question: What factorization of epistemic state change can be canonical relative to an explicit representation contract?"]
  n343["question: What claims beyond observation can have support without being explanations?"]
  n344["question: What role does generation of candidate constraints play in black-box inference?"]
  n345["question: How can reusable strategies and meta-strategies be instantiated and identified in specific conversations?"]
  n346["question: What existing architecture should coordinate heterogeneous candidate generators and evaluators?"]
  n347["question: What domain-independent structure, if any, constrains draft spaces, construction operators and generative transition relations?"]
  n348["question: Which beyond-observation inferences can an embedded observer make?"]
  n349["question: What is the minimal type system for epistemic actions that can be targets of warrant?"]
  n350["question: Can exhaustiveness of the proposed inference taxonomy be proved?"]
  n351["question: Which existing ontology captures temporal inquiry evolution and reasoning moves?"]
  n352["question: What general dynamics make explanations and visual presentations effective?"]
  n353["question: What is the space of possible explanatory hypotheses?"]
  n354["question: What general concept subsumes MECE-style primitive analysis when the decomposition is compositional rather than a partition?"]
  n355["question: What should be formalized next after separating state update from candidate generation?"]
  n356["question: When a generator's artifact is translated into another representation, which guarantees survive the translation?"]
  n357["question: Is the long founding inquiry sufficiently documented and updated for a fresh-agent handoff?"]
  n358["question: What general heuristics or formal scaffolding improve thinking across problems?"]
  n359["question: Can imagination yield knowledge not reducible to inference or introspection?"]
  n360["question: Can the apparent overlap between induction and abduction be explained by a deeper compositional formalism?"]
  n361["question: What assumptions minimally support inductive generalization?"]
  n362["question: Under what conditions does evidence E contain information relevant to a proposition H?"]
  n363["question: Can symmetry, invariance and stability supply primitives of pattern recognition?"]
  n364["question: Is structure a set of constraints, or does emergence and computational irreducibility change the ontology?"]
  n365["question: How is latent structure different from a mechanism?"]
  n366["question: What is the minimal formalization of learning relevant to this inquiry?"]
  n367["question: Is algorithm classification the right level for a simple inference taxonomy?"]
  n368["question: What possible maps take current representations beyond the information currently explicit?"]
  n369["question: Is measurement theory sufficient to explain the observer-to-pattern problem?"]
  n370["question: Can candidate-generation formalisms fit the existing meta-model, and if not, what gap do they expose?"]
  n371["question: Which established metareasoning and reflection formalisms should constrain the strategy/self-application layer before it is frozen?"]
  n372["question: What minimal entities and relations does this inference sketch require?"]
  n373["question: How does an embedded observer learn from a non-designed world?"]
  n374["question: What should be attacked next after the assumption-context refinement?"]
  n375["question: What does higher order mean, and how does it differ from coarse-graining?"]
  n376["question: What, if anything, is fundamental about pattern formation before criteria for useful or optimal abstraction are imposed?"]
  n377["question: What operation makes a relational feature explicit to an observer?"]
  n378["question: Which dimensions of perceptual space are available to a physically embedded observer?"]
  n379["question: Which pattern-recognition mappings can physical embedded observers implement?"]
  n380["question: What established machinery should be checked before freezing the revised meta-model in documentation?"]
  n381["question: How much of the meta-model and its integration already exists in prior work?"]
  n382["question: How should repeated self-application of the developing reasoning model be represented?"]
  n383["question: Is reframe a primitive operation, or is it masking several different transformations?"]
  n384["question: How does the developing epistemic framework characterize the reasoning occurring in this dialogue itself?"]
  n385["question: Where does canonical factorization live when treated as a reusable cognitive strategy?"]
  n386["question: Can the canonical-factorization strategy trace be represented without introducing another vague primitive?"]
  n387["question: Do deduction, induction and abduction exhaust learning beyond observation?"]
  n388["question: Should the model treat a theory used in a derivation as a durable commitment, or only as a temporary assumption context?"]
  n389["question: What warrants the standards by which an inference is warranted?"]
  n390["question: How should multiple independent, conflicting or defeasible warrants combine?"]
  n391["question: How does the earlier warrant work relate to the revised meta-model, and is warrant the same thing as license?"]
  n392["question: What minimal warrant postulates and representation theorems should govern non-entailing commitment changes?"]
  n393["question: How should warrant of warrant be formalized once certainty is removed from the target?"]
  n394["question: Does Wolfram observer theory characterize physically realizable pattern recognizers?"]
  n395["claim: The current query/task belongs to a reasoning episode rather than persistent epistemic state."]
  n396["concept: Reach(R) is the set of draft candidates reachable from d0 by finite sequences of available construction/refinement operators."]
  n397["claim: A mechanism being physically implementable does not establish that it tracks truth."]
  n398["hypothesis: A reasoning episode can be represented as R=(K_Sigma,Gamma,Q)."]
  n399["goal: Map the moves that changed the inquiry, not only the concepts mentioned."]
  n400["claim: Conversations can serve as source-grounded datasets of instantiated reasoning trajectories and proposed strategy episodes."]
  n401["hypothesis: Recognizing a pattern may itself perform the relevant beyond-token representational step."]
  n402["hypothesis: Induction, abduction and deduction can feed back into one another rather than forming a fixed pipeline."]
  n403["hypothesis: Meta-level status is relational: a reasoning episode is meta with respect to the reasoning artifact, strategy or episode it is about."]
  n404["method: Reflective/self-applicative modeling uses the reasoning model to analyze the reasoning process that is constructing the model."]
  n405["claim: Reframe is a dialogue-level macro that may decompose into query, language, theory/support or context transformations."]
  n406["claim: Extracting relations is not necessarily a many-to-one, information-discarding coarse-graining."]
  n407["claim: Any nontrivial target factorization is canonical only relative to a declared representation contract, because structure, parameters and state can be recoded."]
  n408["hypothesis: The relevant map may run between representations rather than raw observations and concepts."]
  n409["hypothesis: Representational lift may be a primitive operation prior to prediction."]
  n410["goal: Anchor the investigation in existing formal theories rather than reinventing terminology."]
  n411["claim: Warrant scope is normally encoded in applicability assumptions and the quantified/type semantics of the guarantee rather than as a separate primitive coordinate."]
  n412["hypothesis: Assume an external reality with sufficiently stable rules."]
  n413["hypothesis: Epistemic state change can be factored, relative to semantic alignment, into representation-space change, additions, deletions and graded-support change."]
  n414["concept: U: the current semantic universe or model space of expressible hypotheses."]
  n415["hypothesis: Stateful computation over an information stream is a general substrate for memory and integration, but does not by itself settle epistemic warrant."]
  n416["hypothesis: A strategy/control layer selects and sequences lower-level reasoning operators; strategy is distinct from primitive operator and candidate artifact."]
  n417["concept: Introduce new predicate/concept vocabulary whose semantics are not merely a definitional abbreviation of the old language."]
  n418["claim: Minimal supporting environments make conditional dependency provenance explicit without warranting the assumptions themselves."]
  n419["claim: Support, warrant, license and executed epistemic update are distinct stages."]
  n420["hypothesis: Memory can be treated abstractly as integration of measurements distributed across time."]
  n421["hypothesis: A set of premises can be stipulated only for a reasoning branch without becoming a durable belief theory."]
  n422["hypothesis: A white-box reasoning branch selects a temporary assumption environment Gamma subseteq A."]
  n423["claim: The dialogue is performing theoretical model construction under conceptual and literature constraints."]
  n424["claim: Theory graphs remain relevant for modular theory networks but are not required as an additional foundational layer yet."]
  n425["claim: Expression construction, definitional extension and substantive concept invention are distinct operations."]
  n426["claim: Candidate generation, warrant/evaluation and epistemic state update are distinct layers and should not be collapsed into a named inference method."]
  n427["claim: The work is best separated into a Formal Epistemic Reasoning Meta-Model, an Inquiry Representation Model, and a useful Inquiry System."]
  n428["hypothesis: Entailment, projection along stable structure and inversion toward generators may recover three inference forms."]
  n429["hypothesis: Use a typed blackboard, heterogeneous generator/evaluator portfolio, explicit controller, reflective transformations and warrant rather than a new universal orchestration calculus."]
  n430["hypothesis: Generated epistemic candidates require types such as sentence, assumption, justification, model, signature extension, mapping or query."]
  n431["claim: Typed candidate generation remains the main unresolved formal layer after the assumption-context refinement."]
  n432["goal: Make typed candidate generation concrete using the conversation as a test corpus."]
  n433["hypothesis: A candidate-generation regime can be factored into artifact ontology, generative language, draft state, bias, operators, transitions and evaluators, with strategy/control separate."]
  n434["goal: Represent the conversation with typed entities and relation roles."]
  n435["claim: The previous U/hypothesis-universe coordinate conflates language, expressibility, model space and live hypotheses."]
  n436["claim: The reusable cross-domain abstraction is the candidate-generation interface, not one universal operator set."]
  n437["goal: The useful Inquiry System is the downstream project of greatest practical interest, while the formal meta-model and inquiry representation remain distinct supporting projects."]
  n438["goal: Deliver a coherent first-pass ontology, conversation instantiation, code and project documentation in GitHub."]
  n439["hypothesis: A warrant certificate records explicit assumptions, a claimed guarantee and support connecting the assumptions to that guarantee."]
  n440["claim: The earlier assumptions/guarantee/certificate warrant shape survives the later meta-model refinements."]
  n441["hypothesis: Core judgment: under warrant regime W and assumptions A, certificate pi warrants epistemic action a with guarantee G."]
  n442["concept: Warrant evaluates whether a candidate-to-commitment move has a specified justification or guarantee under explicit assumptions."]
  n443["hypothesis: Warrant is the structured basis for a derived license rather than a synonym for license."]
  n444["goal: Refactor the existing warrant proposal against the more precise candidate-generation, strategy and epistemic-state model rather than reinventing it."]
  n445["concept: A warrant regime specifies the rules, semantics and acceptance standard under which support can warrant an epistemic action."]
  n446["claim: The inquiry should return from implementation-level pattern and learning theories to the original warrant question."]
  n447["claim: Candidate, transition and strategy warrant need not be primitive warrant types; they are instances of one action-targeted warrant schema."]
  n448["hypothesis: Candidate, transition and strategy warrants appear as distinct descriptive targets before further factorization."]
  n449["claim: Formal well-formedness, typing or deductive validity does not establish epistemic warrant for generating or accepting a candidate."]
  n450["hypothesis: A stipulated model supports within-model reasoning; an embedded observer must infer the model from observations."]
  n451["reference: Wolfram observer theory and rulial space, raised as a related research direction."]
  n452["example: Worked trace of the founding dialogue from I/D/A partition through composition-space, representation-relative factorization, support-context refinement, candidate-type repair and strategy recognition."]
  n453["goal: Build a persistent cross-conversation map of worldview, questions, dependencies and revisions."]
  n454["relation: challenges"]
  n455["relation: supersedes"]
  n456["relation: answers"]
  n457["relation: motivates"]
  n458["relation: candidate_for"]
  n459["relation: motivates"]
  n460["relation: reframes"]
  n461["relation: motivates"]
  n462["relation: candidate_for"]
  n463["relation: motivates"]
  n464["relation: answers"]
  n465["relation: challenges"]
  n466["relation: candidate_for"]
  n467["relation: reframes"]
  n468["relation: challenges"]
  n469["relation: answers"]
  n470["relation: motivates"]
  n471["relation: reframes"]
  n472["relation: candidate_for"]
  n473["relation: challenges"]
  n474["relation: answers"]
  n475["relation: related_to"]
  n476["relation: challenges"]
  n477["relation: supports"]
  n478["relation: candidate_for"]
  n479["relation: depends_on"]
  n480["relation: motivates"]
  n481["relation: motivates"]
  n482["relation: related_to"]
  n483["relation: related_to"]
  n484["relation: candidate_for"]
  n485["relation: challenges"]
  n486["relation: motivates"]
  n487["relation: reframes"]
  n488["relation: distinguishes"]
  n489["relation: related_to"]
  n490["relation: candidate_for"]
  n491["relation: candidate_for"]
  n492["relation: exemplifies"]
  n493["relation: challenges"]
  n494["relation: exemplifies"]
  n495["relation: motivates"]
  n496["relation: candidate_for"]
  n497["relation: challenges"]
  n498["relation: related_to"]
  n499["relation: answers"]
  n500["relation: candidate_for"]
  n501["relation: motivates"]
  n502["relation: candidate_for"]
  n503["relation: candidate_for"]
  n504["relation: reframes"]
  n505["relation: answers"]
  n506["relation: candidate_for"]
  n507["relation: part_of"]
  n508["relation: candidate_for"]
  n509["relation: candidate_for"]
  n510["relation: part_of"]
  n511["relation: motivates"]
  n512["relation: candidate_for"]
  n513["relation: related_to"]
  n514["relation: related_to"]
  n515["relation: related_to"]
  n516["relation: candidate_for"]
  n517["relation: reframes"]
  n518["relation: challenges"]
  n519["relation: depends_on"]
  n520["relation: supersedes"]
  n521["relation: challenges"]
  n522["relation: related_to"]
  n523["relation: depends_on"]
  n524["relation: depends_on"]
  n525["relation: related_to"]
  n526["relation: challenges"]
  n527["relation: motivates"]
  n528["relation: part_of"]
  n529["relation: part_of"]
  n530["relation: motivates"]
  n531["relation: depends_on"]
  n532["relation: depends_on"]
  n533["relation: related_to"]
  n534["relation: answers"]
  n535["relation: candidate_for"]
  n536["relation: supersedes"]
  n537["relation: challenges"]
  n538["relation: reframes"]
  n539["relation: challenges"]
  n540["relation: related_to"]
  n541["relation: challenges"]
  n542["relation: challenges"]
  n543["relation: related_to"]
  n544["relation: related_to"]
  n545["relation: related_to"]
  n546["relation: related_to"]
  n547["relation: related_to"]
  n548["relation: motivates"]
  n549["relation: candidate_for"]
  n550["relation: related_to"]
  n551["relation: related_to"]
  n552["relation: challenges"]
  n553["relation: reframes"]
  n554["relation: distinguishes"]
  n555["relation: related_to"]
  n556["relation: related_to"]
  n557["relation: motivates"]
  n558["relation: reframes"]
  n559["relation: candidate_for"]
  n560["relation: part_of"]
  n561["relation: candidate_for"]
  n562["relation: depends_on"]
  n563["relation: related_to"]
  n564["relation: motivates"]
  n565["relation: motivates"]
  n566["relation: depends_on"]
  n567["relation: depends_on"]
  n568["relation: challenges"]
  n569["relation: candidate_for"]
  n570["relation: part_of"]
  n571["relation: part_of"]
  n572["relation: part_of"]
  n573["relation: part_of"]
  n574["relation: part_of"]
  n575["relation: answers"]
  n576["relation: related_to"]
  n577["relation: related_to"]
  n578["relation: candidate_for"]
  n579["relation: supports"]
  n580["relation: distinguishes"]
  n581["relation: related_to"]
  n582["relation: reframes"]
  n583["relation: depends_on"]
  n584["relation: related_to"]
  n585["relation: part_of"]
  n586["relation: part_of"]
  n587["relation: depends_on"]
  n588["relation: answers"]
  n589["relation: supports"]
  n590["relation: motivates"]
  n591["relation: candidate_for"]
  n592["relation: motivates"]
  n593["relation: motivates"]
  n594["relation: distinguishes"]
  n595["relation: answers"]
  n596["relation: supports"]
  n597["relation: related_to"]
  n598["relation: motivates"]
  n599["relation: challenges"]
  n600["relation: candidate_for"]
  n601["relation: candidate_for"]
  n602["relation: part_of"]
  n603["relation: candidate_for"]
  n604["relation: part_of"]
  n605["relation: part_of"]
  n606["relation: part_of"]
  n607["relation: supports"]
  n608["relation: depends_on"]
  n609["relation: challenges"]
  n610["relation: answers"]
  n611["relation: supports"]
  n612["relation: supports"]
  n613["relation: motivates"]
  n614["relation: candidate_for"]
  n615["relation: supports"]
  n616["relation: supports"]
  n617["relation: part_of"]
  n618["relation: part_of"]
  n619["relation: supersedes"]
  n620["relation: part_of"]
  n621["relation: part_of"]
  n622["relation: supports"]
  n623["relation: challenges"]
  n624["relation: supports"]
  n625["relation: part_of"]
  n626["relation: part_of"]
  n627["relation: related_to"]
  n628["relation: answers"]
  n629["relation: reframes"]
  n630["relation: candidate_for"]
  n631["relation: related_to"]
  n632["relation: candidate_for"]
  n633["relation: candidate_for"]
  n634["relation: challenges"]
  n635["relation: distinguishes"]
  n636["relation: candidate_for"]
  n637["relation: challenges"]
  n638["relation: candidate_for"]
  n639["relation: candidate_for"]
  n640["relation: part_of"]
  n641["relation: distinguishes"]
  n642["relation: answers"]
  n643["relation: candidate_for"]
  n644["relation: part_of"]
  n645["relation: answers"]
  n646["relation: part_of"]
  n647["relation: supports"]
  n648["relation: answers"]
  n649["relation: related_to"]
  n650["relation: supports"]
  n651["relation: motivates"]
  n652["relation: motivates"]
  n653["relation: exemplifies"]
  n654["relation: exemplifies"]
  n655["relation: about"]
  n656["relation: about"]
  n657["relation: related_to"]
  n658["relation: related_to"]
  n659["relation: related_to"]
  n660["relation: related_to"]
  n661["relation: part_of"]
  n662["relation: part_of"]
  n663["relation: depends_on"]
  n664["relation: depends_on"]
  n665["relation: candidate_for"]
  n666["relation: part_of"]
  n667["relation: part_of"]
  n668["relation: supports"]
  n669["relation: supports"]
  n670["relation: supports"]
  n671["relation: part_of"]
  n672["relation: exemplifies"]
  n673["relation: related_to"]
  n674["relation: supports"]
  n675["relation: about"]
  n676["relation: depends_on"]
  n677["relation: depends_on"]
  n678["relation: part_of"]
  n679["relation: part_of"]
  n680["relation: part_of"]
  n681["relation: part_of"]
  n682["relation: part_of"]
  n683["relation: part_of"]
  n684["relation: part_of"]
  n685["relation: part_of"]
  n686["relation: part_of"]
  n687["relation: answers"]
  n688["relation: motivates"]
  n689["relation: motivates"]
  n690["relation: distinguishes"]
  n691["relation: part_of"]
  n692["relation: part_of"]
  n693["relation: part_of"]
  n694["relation: candidate_for"]
  n695["relation: supports"]
  n696["relation: supports"]
  n697["relation: challenges"]
  n698["relation: supports"]
  n699["relation: depends_on"]
  n700["relation: depends_on"]
  n701["relation: related_to"]
  n702["relation: related_to"]
  n703["relation: related_to"]
  n0 -->|then| n1
  n0 -->|output| n387
  n1 -->|then| n2
  n1 -->|output| n287
  n2 -->|then| n3
  n2 -->|output| n359
  n3 -->|then| n4
  n3 -->|output| n288
  n4 -->|then| n5
  n4 -->|output| n389
  n5 -->|then| n6
  n5 -->|output| n216
  n6 -->|then| n7
  n6 -->|output| n350
  n7 -->|then| n8
  n7 -->|output| n246
  n8 -->|then| n9
  n8 -->|output| n348
  n9 -->|then| n10
  n9 -->|output| n218
  n9 -->|output| n328
  n10 -->|then| n11
  n10 -->|output| n365
  n11 -->|then| n12
  n11 -->|output| n298
  n12 -->|then| n13
  n12 -->|output| n353
  n13 -->|then| n14
  n13 -->|output| n343
  n14 -->|then| n15
  n14 -->|output| n408
  n15 -->|then| n16
  n15 -->|output| n368
  n16 -->|then| n17
  n16 -->|output| n410
  n17 -->|then| n18
  n17 -->|output| n271
  n18 -->|then| n19
  n18 -->|output| n338
  n19 -->|then| n20
  n19 -->|output| n217
  n20 -->|then| n21
  n20 -->|output| n314
  n21 -->|then| n22
  n21 -->|output| n367
  n22 -->|then| n23
  n22 -->|output| n412
  n23 -->|then| n24
  n23 -->|output| n428
  n24 -->|then| n25
  n24 -->|output| n372
  n25 -->|then| n26
  n25 -->|output| n364
  n26 -->|then| n27
  n26 -->|output| n321
  n27 -->|then| n28
  n27 -->|output| n289
  n28 -->|then| n29
  n28 -->|output| n335
  n29 -->|then| n30
  n29 -->|output| n331
  n29 -->|output| n379
  n30 -->|then| n31
  n30 -->|output| n394
  n31 -->|then| n32
  n31 -->|output| n283
  n32 -->|then| n33
  n32 -->|output| n401
  n33 -->|then| n34
  n33 -->|output| n251
  n33 -->|output| n377
  n34 -->|then| n35
  n34 -->|output| n409
  n35 -->|then| n36
  n35 -->|output| n375
  n36 -->|then| n37
  n36 -->|output| n406
  n37 -->|then| n38
  n37 -->|output| n221
  n38 -->|then| n39
  n38 -->|output| n363
  n39 -->|then| n40
  n39 -->|output| n279
  n40 -->|then| n41
  n40 -->|output| n378
  n41 -->|then| n42
  n41 -->|output| n304
  n42 -->|then| n43
  n42 -->|output| n434
  n43 -->|then| n44
  n43 -->|output| n399
  n44 -->|then| n45
  n44 -->|output| n206
  n45 -->|then| n46
  n45 -->|output| n351
  n46 -->|then| n47
  n46 -->|output| n322
  n47 -->|then| n48
  n47 -->|output| n358
  n48 -->|then| n49
  n48 -->|output| n259
  n49 -->|then| n50
  n49 -->|output| n219
  n50 -->|then| n51
  n50 -->|output| n285
  n51 -->|then| n52
  n51 -->|output| n352
  n52 -->|then| n53
  n52 -->|output| n250
  n53 -->|then| n54
  n53 -->|output| n373
  n54 -->|then| n55
  n54 -->|output| n319
  n55 -->|then| n56
  n55 -->|output| n318
  n56 -->|then| n57
  n56 -->|output| n402
  n57 -->|then| n58
  n57 -->|output| n361
  n58 -->|then| n59
  n58 -->|output| n336
  n59 -->|then| n60
  n59 -->|output| n453
  n60 -->|then| n61
  n60 -->|output| n323
  n61 -->|then| n62
  n61 -->|output| n438
  n62 -->|then| n63
  n62 -->|output| n369
  n63 -->|then| n64
  n63 -->|output| n303
  n64 -->|then| n65
  n64 -->|output| n326
  n65 -->|then| n66
  n65 -->|output| n222
  n66 -->|then| n67
  n66 -->|output| n327
  n67 -->|then| n68
  n67 -->|output| n376
  n68 -->|then| n69
  n68 -->|output| n258
  n69 -->|then| n70
  n69 -->|output| n366
  n70 -->|then| n71
  n70 -->|output| n325
  n71 -->|then| n72
  n71 -->|output| n294
  n72 -->|then| n73
  n72 -->|output| n286
  n73 -->|then| n74
  n73 -->|output| n420
  n74 -->|then| n75
  n74 -->|output| n415
  n75 -->|then| n76
  n75 -->|output| n393
  n76 -->|then| n77
  n76 -->|output| n446
  n77 -->|then| n78
  n77 -->|output| n208
  n78 -->|then| n79
  n78 -->|output| n332
  n79 -->|then| n80
  n79 -->|output| n344
  n80 -->|then| n81
  n80 -->|output| n324
  n81 -->|then| n82
  n81 -->|output| n362
  n82 -->|then| n83
  n82 -->|output| n210
  n83 -->|then| n84
  n83 -->|output| n360
  n84 -->|then| n85
  n84 -->|output| n240
  n85 -->|then| n86
  n85 -->|output| n273
  n86 -->|then| n87
  n86 -->|then| n88
  n86 -->|output| n306
  n87 -->|then| n89
  n87 -->|output| n307
  n88 -->|then| n89
  n88 -->|output| n337
  n89 -->|then| n90
  n89 -->|output| n317
  n90 -->|then| n91
  n90 -->|output| n342
  n91 -->|then| n93
  n91 -->|output| n308
  n92 -->|then| n157
  n92 -->|output| n230
  n93 -->|then| n94
  n93 -->|output| n232
  n94 -->|then| n95
  n94 -->|output| n284
  n95 -->|then| n96
  n95 -->|output| n268
  n96 -->|then| n97
  n96 -->|output| n263
  n97 -->|then| n98
  n97 -->|output| n224
  n97 -->|output| n413
  n97 -->|output| n442
  n98 -->|then| n99
  n98 -->|output| n281
  n98 -->|output| n302
  n98 -->|output| n414
  n99 -->|then| n100
  n99 -->|then| n101
  n99 -->|output| n413
  n100 -->|then| n102
  n100 -->|output| n339
  n101 -->|then| n102
  n101 -->|output| n244
  n102 -->|then| n103
  n102 -->|output| n439
  n103 -->|then| n104
  n103 -->|output| n209
  n104 -->|then| n106
  n104 -->|output| n442
  n105 -->|then| n164
  n105 -->|output| n384
  n106 -->|then| n107
  n106 -->|output| n423
  n107 -->|then| n108
  n107 -->|output| n226
  n108 -->|then| n109
  n108 -->|output| n355
  n109 -->|then| n110
  n109 -->|output| n275
  n110 -->|then| n111
  n110 -->|output| n383
  n111 -->|then| n112
  n111 -->|output| n238
  n112 -->|then| n113
  n112 -->|output| n239
  n113 -->|then| n114
  n113 -->|output| n241
  n114 -->|then| n115
  n114 -->|output| n405
  n115 -->|then| n116
  n115 -->|output| n207
  n116 -->|then| n117
  n116 -->|output| n370
  n117 -->|then| n118
  n117 -->|output| n311
  n118 -->|then| n119
  n118 -->|output| n435
  n119 -->|then| n120
  n119 -->|output| n295
  n120 -->|then| n121
  n120 -->|output| n292
  n120 -->|output| n293
  n121 -->|then| n122
  n121 -->|output| n296
  n122 -->|then| n123
  n122 -->|output| n248
  n122 -->|output| n264
  n122 -->|output| n417
  n122 -->|output| n425
  n123 -->|then| n124
  n123 -->|output| n405
  n124 -->|then| n125
  n124 -->|output| n430
  n125 -->|then| n126
  n125 -->|output| n388
  n126 -->|then| n127
  n126 -->|output| n421
  n127 -->|then| n128
  n127 -->|output| n329
  n128 -->|then| n129
  n128 -->|output| n220
  n129 -->|then| n130
  n129 -->|output| n380
  n130 -->|then| n131
  n130 -->|output| n214
  n131 -->|then| n132
  n131 -->|output| n215
  n132 -->|then| n133
  n132 -->|output| n212
  n132 -->|output| n213
  n133 -->|then| n134
  n133 -->|output| n330
  n134 -->|then| n135
  n134 -->|output| n422
  n135 -->|then| n136
  n135 -->|output| n254
  n136 -->|then| n137
  n136 -->|output| n291
  n137 -->|then| n138
  n137 -->|output| n262
  n138 -->|then| n139
  n138 -->|output| n395
  n139 -->|then| n140
  n139 -->|output| n398
  n140 -->|then| n141
  n140 -->|output| n424
  n141 -->|then| n142
  n141 -->|output| n245
  n142 -->|then| n143
  n142 -->|output| n341
  n142 -->|output| n431
  n143 -->|then| n144
  n143 -->|output| n374
  n144 -->|then| n145
  n144 -->|output| n432
  n145 -->|then| n146
  n145 -->|output| n229
  n146 -->|then| n147
  n146 -->|output| n228
  n147 -->|then| n148
  n147 -->|output| n211
  n148 -->|then| n149
  n148 -->|output| n223
  n149 -->|then| n150
  n149 -->|output| n272
  n150 -->|then| n151
  n150 -->|output| n315
  n150 -->|output| n316
  n151 -->|then| n152
  n151 -->|output| n269
  n152 -->|then| n153
  n152 -->|output| n449
  n153 -->|then| n154
  n153 -->|output| n354
  n154 -->|then| n155
  n154 -->|output| n267
  n155 -->|then| n92
  n155 -->|then| n156
  n155 -->|output| n309
  n156 -->|then| n157
  n156 -->|output| n231
  n157 -->|then| n158
  n157 -->|output| n265
  n158 -->|then| n159
  n158 -->|output| n385
  n159 -->|then| n160
  n159 -->|output| n416
  n160 -->|then| n161
  n160 -->|output| n313
  n161 -->|then| n165
  n161 -->|then| n166
  n161 -->|output| n382
  n162 -->|then| n105
  n162 -->|then| n163
  n162 -->|output| n404
  n163 -->|then| n164
  n163 -->|output| n403
  n164 -->|then| n167
  n164 -->|output| n236
  n165 -->|then| n162
  n165 -->|output| n345
  n166 -->|then| n162
  n166 -->|output| n242
  n167 -->|then| n168
  n167 -->|output| n400
  n168 -->|then| n169
  n168 -->|output| n371
  n169 -->|then| n170
  n169 -->|output| n225
  n170 -->|then| n171
  n170 -->|output| n253
  n170 -->|output| n396
  n171 -->|then| n172
  n171 -->|output| n276
  n172 -->|then| n173
  n172 -->|output| n252
  n173 -->|then| n174
  n173 -->|output| n260
  n173 -->|output| n261
  n174 -->|then| n175
  n174 -->|output| n266
  n175 -->|then| n176
  n175 -->|output| n436
  n176 -->|then| n177
  n176 -->|output| n347
  n176 -->|output| n386
  n176 -->|output| n452
  n177 -->|then| n178
  n177 -->|output| n391
  n178 -->|then| n179
  n178 -->|output| n443
  n178 -->|output| n448
  n179 -->|then| n180
  n179 -->|output| n444
  n180 -->|then| n181
  n180 -->|output| n440
  n181 -->|then| n182
  n181 -->|output| n300
  n181 -->|output| n419
  n182 -->|then| n183
  n182 -->|output| n257
  n182 -->|output| n441
  n182 -->|output| n445
  n183 -->|then| n184
  n183 -->|output| n411
  n183 -->|output| n447
  n184 -->|then| n185
  n184 -->|output| n247
  n184 -->|output| n349
  n184 -->|output| n390
  n185 -->|then| n186
  n185 -->|output| n333
  n186 -->|then| n187
  n186 -->|then| n188
  n186 -->|output| n427
  n186 -->|output| n437
  n187 -->|then| n189
  n187 -->|output| n270
  n188 -->|then| n189
  n188 -->|output| n312
  n189 -->|then| n190
  n189 -->|output| n235
  n190 -->|then| n191
  n190 -->|output| n381
  n191 -->|then| n193
  n191 -->|output| n320
  n192 -->|then| n195
  n192 -->|output| n205
  n193 -->|then| n194
  n193 -->|output| n340
  n194 -->|then| n192
  n194 -->|output| n227
  n195 -->|then| n196
  n195 -->|output| n277
  n195 -->|output| n433
  n196 -->|then| n197
  n196 -->|output| n274
  n197 -->|then| n198
  n197 -->|then| n199
  n197 -->|output| n346
  n198 -->|then| n200
  n198 -->|output| n429
  n199 -->|then| n200
  n199 -->|output| n356
  n200 -->|then| n201
  n200 -->|output| n282
  n201 -->|then| n202
  n201 -->|output| n233
  n202 -->|then| n203
  n202 -->|output| n357
  n203 -->|output| n290
  n204 -->|part| n573
  n206 -->|input| n45
  n206 -->|candidate| n508
  n207 -->|source| n597
  n208 -->|candidate| n549
  n209 -->|premise| n579
  n210 -->|left| n554
  n211 -->|left| n635
  n212 -->|part| n617
  n213 -->|part| n618
  n214 -->|input| n131
  n214 -->|candidate| n614
  n215 -->|input| n132
  n215 -->|input| n133
  n215 -->|input| n136
  n215 -->|premise| n615
  n216 -->|input| n6
  n216 -->|reason| n459
  n217 -->|answer| n474
  n218 -->|input| n18
  n218 -->|candidate| n462
  n219 -->|input| n50
  n219 -->|input| n51
  n220 -->|premise| n612
  n221 -->|input| n38
  n221 -->|input| n65
  n221 -->|candidate| n500
  n221 -->|reason| n501
  n222 -->|new| n536
  n223 -->|candidate| n636
  n224 -->|input| n100
  n224 -->|source| n576
  n224 -->|left| n580
  n225 -->|input| n170
  n225 -->|input| n173
  n225 -->|input| n175
  n225 -->|input| n176
  n225 -->|input| n193
  n225 -->|input| n195
  n225 -->|candidate| n665
  n226 -->|input| n108
  n226 -->|premise| n589
  n226 -->|reason| n590
  n228 -->|input| n147
  n228 -->|input| n148
  n228 -->|challenger| n634
  n228 -->|part| n684
  n229 -->|candidate| n633
  n230 -->|dependent| n562
  n231 -->|input| n157
  n231 -->|input| n158
  n231 -->|input| n159
  n231 -->|input| n174
  n231 -->|input| n176
  n231 -->|candidate| n643
  n231 -->|part| n646
  n231 -->|part| n661
  n232 -->|input| n94
  n234 -->|challenger| n468
  n234 -->|answer| n469
  n236 -->|premise| n650
  n237 -->|candidate| n458
  n238 -->|input| n113
  n238 -->|input| n122
  n238 -->|left| n594
  n239 -->|input| n113
  n239 -->|input| n122
  n240 -->|source| n556
  n241 -->|answer| n595
  n242 -->|input| n167
  n243 -->|source| n660
  n244 -->|input| n105
  n244 -->|dependent| n587
  n245 -->|input| n140
  n245 -->|input| n143
  n245 -->|input| n161
  n245 -->|input| n177
  n245 -->|input| n185
  n245 -->|input| n186
  n245 -->|answer| n628
  n246 -->|input| n8
  n246 -->|reason| n461
  n247 -->|premise| n698
  n248 -->|part| n605
  n249 -->|part| n574
  n250 -->|input| n53
  n250 -->|input| n55
  n250 -->|candidate| n516
  n251 -->|input| n34
  n251 -->|input| n71
  n251 -->|example| n494
  n251 -->|reason| n495
  n252 -->|premise| n669
  n253 -->|input| n171
  n253 -->|input| n172
  n253 -->|part| n666
  n254 -->|part| n621
  n255 -->|input| n154
  n255 -->|example| n653
  n255 -->|subject| n655
  n256 -->|example| n654
  n256 -->|subject| n656
  n257 -->|part| n692
  n258 -->|challenger| n539
  n259 -->|input| n49
  n259 -->|candidate| n512
  n259 -->|source| n513
  n259 -->|part| n529
  n260 -->|premise| n670
  n261 -->|part| n671
  n262 -->|challenger| n623
  n263 -->|candidate| n569
  n264 -->|part| n604
  n265 -->|part| n644
  n265 -->|part| n686
  n266 -->|source| n673
  n268 -->|input| n96
  n268 -->|challenger| n568
  n269 -->|input| n152
  n269 -->|part| n640
  n270 -->|input| n188
  n270 -->|input| n190
  n271 -->|input| n20
  n271 -->|candidate| n472
  n272 -->|input| n150
  n272 -->|challenger| n637
  n273 -->|input| n86
  n274 -->|input| n197
  n275 -->|input| n110
  n275 -->|input| n115
  n275 -->|input| n116
  n275 -->|input| n124
  n275 -->|candidate| n591
  n276 -->|premise| n668
  n278 -->|candidate| n466
  n279 -->|candidate| n502
  n280 -->|source| n659
  n281 -->|input| n99
  n281 -->|part| n572
  n282 -->|input| n201
  n283 -->|candidate| n491
  n284 -->|input| n95
  n284 -->|input| n97
  n284 -->|dependent| n566
  n284 -->|dependent| n567
  n285 -->|source| n514
  n286 -->|source| n544
  n287 -->|input| n2
  n287 -->|input| n3
  n288 -->|new| n455
  n288 -->|answer| n456
  n289 -->|input| n28
  n289 -->|input| n56
  n289 -->|candidate| n484
  n291 -->|premise| n622
  n292 -->|input| n121
  n292 -->|input| n136
  n292 -->|input| n141
  n292 -->|input| n149
  n292 -->|part| n602
  n293 -->|candidate| n601
  n294 -->|input| n72
  n294 -->|input| n73
  n294 -->|source| n543
  n295 -->|input| n120
  n295 -->|candidate| n600
  n296 -->|input| n125
  n296 -->|input| n137
  n296 -->|candidate| n603
  n297 -->|candidate| n503
  n298 -->|input| n12
  n298 -->|answer| n464
  n298 -->|challenger| n465
  n299 -->|input| n10
  n300 -->|part| n691
  n301 -->|source| n657
  n302 -->|input| n99
  n302 -->|part| n571
  n303 -->|input| n64
  n303 -->|answer| n534
  n304 -->|answer| n505
  n305 -->|candidate| n506
  n306 -->|input| n87
  n306 -->|candidate| n559
  n307 -->|input| n88
  n307 -->|input| n89
  n307 -->|input| n90
  n307 -->|input| n153
  n307 -->|input| n155
  n307 -->|part| n560
  n307 -->|reason| n564
  n308 -->|input| n92
  n308 -->|source| n563
  n309 -->|answer| n642
  n310 -->|source| n658
  n312 -->|input| n189
  n313 -->|premise| n647
  n314 -->|input| n21
  n314 -->|input| n80
  n314 -->|source| n475
  n315 -->|candidate| n638
  n316 -->|input| n151
  n316 -->|input| n172
  n316 -->|candidate| n639
  n316 -->|part| n685
  n317 -->|candidate| n561
  n317 -->|part| n680
  n318 -->|new| n520
  n319 -->|input| n56
  n319 -->|dependent| n519
  n321 -->|source| n482
  n322 -->|input| n47
  n322 -->|candidate| n509
  n323 -->|part| n528
  n324 -->|challenger| n552
  n325 -->|challenger| n541
  n325 -->|challenger| n542
  n326 -->|input| n66
  n326 -->|candidate| n535
  n327 -->|input| n67
  n327 -->|challenger| n537
  n328 -->|reason| n463
  n329 -->|input| n128
  n329 -->|premise| n611
  n330 -->|input| n134
  n330 -->|input| n138
  n330 -->|input| n139
  n330 -->|input| n141
  n330 -->|new| n619
  n330 -->|part| n625
  n330 -->|part| n683
  n331 -->|reason| n486
  n331 -->|left| n488
  n332 -->|input| n79
  n332 -->|source| n550
  n333 -->|input| n202
  n334 -->|example| n492
  n335 -->|input| n29
  n335 -->|input| n32
  n335 -->|challenger| n485
  n336 -->|input| n59
  n337 -->|original| n582
  n338 -->|input| n19
  n338 -->|challenger| n473
  n339 -->|input| n101
  n339 -->|dependent| n583
  n339 -->|original| n629
  n340 -->|input| n194
  n342 -->|input| n91
  n343 -->|input| n14
  n343 -->|original| n471
  n344 -->|source| n551
  n345 -->|input| n166
  n345 -->|reason| n651
  n346 -->|input| n198
  n347 -->|dependent| n676
  n348 -->|input| n9
  n348 -->|input| n27
  n349 -->|dependent| n699
  n350 -->|input| n7
  n350 -->|input| n23
  n350 -->|input| n58
  n350 -->|input| n85
  n350 -->|dependent| n523
  n350 -->|dependent| n524
  n350 -->|original| n558
  n351 -->|input| n46
  n351 -->|reason| n511
  n352 -->|input| n52
  n352 -->|source| n515
  n352 -->|original| n517
  n353 -->|input| n13
  n353 -->|original| n467
  n354 -->|input| n156
  n355 -->|input| n109
  n356 -->|input| n200
  n357 -->|input| n203
  n358 -->|input| n48
  n359 -->|input| n3
  n359 -->|challenger| n454
  n360 -->|input| n84
  n360 -->|input| n85
  n360 -->|source| n555
  n360 -->|reason| n557
  n360 -->|part| n679
  n361 -->|input| n59
  n361 -->|source| n525
  n361 -->|challenger| n526
  n363 -->|input| n39
  n364 -->|input| n26
  n365 -->|input| n11
  n366 -->|source| n540
  n367 -->|input| n22
  n367 -->|challenger| n476
  n368 -->|input| n16
  n368 -->|input| n17
  n368 -->|original| n487
  n369 -->|input| n63
  n369 -->|source| n533
  n370 -->|input| n117
  n370 -->|input| n129
  n370 -->|reason| n598
  n371 -->|dependent| n663
  n371 -->|dependent| n664
  n372 -->|input| n25
  n372 -->|reason| n481
  n373 -->|input| n54
  n373 -->|input| n69
  n373 -->|challenger| n518
  n374 -->|input| n144
  n375 -->|input| n36
  n375 -->|challenger| n497
  n376 -->|input| n68
  n376 -->|input| n75
  n377 -->|input| n37
  n377 -->|input| n40
  n377 -->|original| n504
  n377 -->|original| n538
  n378 -->|input| n41
  n378 -->|input| n42
  n378 -->|input| n62
  n379 -->|input| n30
  n379 -->|input| n31
  n380 -->|input| n130
  n380 -->|reason| n613
  n381 -->|input| n191
  n381 -->|input| n192
  n382 -->|input| n162
  n383 -->|input| n111
  n383 -->|input| n112
  n383 -->|input| n114
  n383 -->|reason| n592
  n383 -->|reason| n593
  n384 -->|input| n106
  n386 -->|dependent| n677
  n387 -->|input| n1
  n387 -->|input| n4
  n387 -->|input| n8
  n387 -->|input| n83
  n387 -->|reason| n457
  n387 -->|original| n460
  n387 -->|part| n678
  n388 -->|input| n126
  n388 -->|challenger| n609
  n389 -->|input| n5
  n389 -->|input| n93
  n389 -->|reason| n565
  n390 -->|dependent| n700
  n391 -->|input| n178
  n391 -->|input| n179
  n391 -->|reason| n688
  n392 -->|source| n584
  n393 -->|input| n76
  n393 -->|input| n81
  n393 -->|source| n547
  n393 -->|original| n553
  n394 -->|source| n489
  n395 -->|input| n139
  n395 -->|premise| n624
  n396 -->|part| n667
  n398 -->|input| n141
  n398 -->|part| n626
  n399 -->|input| n44
  n399 -->|input| n59
  n399 -->|input| n61
  n399 -->|part| n510
  n399 -->|reason| n527
  n400 -->|reason| n652
  n401 -->|input| n33
  n401 -->|input| n70
  n401 -->|challenger| n493
  n402 -->|challenger| n521
  n402 -->|source| n522
  n403 -->|input| n164
  n403 -->|input| n168
  n403 -->|source| n649
  n404 -->|input| n163
  n404 -->|input| n165
  n404 -->|answer| n648
  n404 -->|part| n662
  n405 -->|input| n123
  n405 -->|premise| n596
  n406 -->|source| n498
  n406 -->|answer| n499
  n407 -->|part| n681
  n408 -->|input| n15
  n408 -->|reason| n470
  n409 -->|input| n35
  n409 -->|input| n36
  n409 -->|candidate| n496
  n410 -->|input| n17
  n411 -->|premise| n695
  n412 -->|input| n23
  n412 -->|premise| n477
  n413 -->|input| n98
  n413 -->|input| n101
  n413 -->|answer| n575
  n413 -->|part| n585
  n413 -->|part| n682
  n414 -->|input| n99
  n414 -->|input| n118
  n414 -->|part| n570
  n415 -->|source| n546
  n416 -->|input| n160
  n416 -->|input| n168
  n416 -->|input| n171
  n416 -->|answer| n645
  n417 -->|part| n606
  n418 -->|premise| n616
  n419 -->|input| n182
  n419 -->|left| n690
  n420 -->|input| n74
  n420 -->|source| n545
  n421 -->|input| n127
  n421 -->|answer| n610
  n422 -->|input| n135
  n422 -->|input| n139
  n422 -->|part| n620
  n423 -->|input| n107
  n423 -->|answer| n588
  n424 -->|source| n627
  n425 -->|premise| n607
  n426 -->|input| n101
  n426 -->|source| n581
  n426 -->|part| n586
  n427 -->|input| n187
  n428 -->|input| n24
  n428 -->|input| n57
  n428 -->|candidate| n478
  n428 -->|dependent| n479
  n428 -->|reason| n480
  n429 -->|input| n199
  n430 -->|input| n142
  n430 -->|input| n146
  n430 -->|dependent| n608
  n431 -->|input| n169
  n431 -->|candidate| n630
  n431 -->|source| n631
  n432 -->|input| n145
  n432 -->|candidate| n632
  n433 -->|input| n196
  n434 -->|input| n43
  n434 -->|part| n507
  n435 -->|input| n119
  n435 -->|challenger| n599
  n436 -->|premise| n674
  n438 -->|dependent| n531
  n438 -->|dependent| n532
  n439 -->|input| n103
  n439 -->|input| n180
  n439 -->|candidate| n578
  n440 -->|input| n182
  n440 -->|reason| n689
  n441 -->|input| n183
  n441 -->|input| n184
  n441 -->|candidate| n694
  n441 -->|source| n701
  n441 -->|source| n702
  n441 -->|source| n703
  n442 -->|input| n102
  n442 -->|input| n104
  n442 -->|input| n173
  n442 -->|input| n177
  n442 -->|source| n577
  n443 -->|input| n181
  n443 -->|answer| n687
  n445 -->|part| n693
  n446 -->|input| n77
  n446 -->|reason| n548
  n447 -->|premise| n696
  n447 -->|challenger| n697
  n449 -->|left| n641
  n450 -->|input| n78
  n450 -->|input| n82
  n450 -->|source| n483
  n451 -->|candidate| n490
  n452 -->|example| n672
  n452 -->|subject| n675
  n453 -->|input| n60
  n453 -->|input| n61
  n453 -->|reason| n530
  n454 -->|target| n287
  n455 -->|old| n287
  n456 -->|question| n359
  n457 -->|result| n389
  n458 -->|problem| n389
  n459 -->|result| n350
  n460 -->|replacement| n348
  n461 -->|result| n348
  n462 -->|problem| n348
  n463 -->|result| n365
  n464 -->|question| n365
  n465 -->|target| n328
  n466 -->|problem| n353
  n467 -->|replacement| n343
  n468 -->|target| n278
  n469 -->|question| n343
  n470 -->|result| n368
  n471 -->|replacement| n368
  n472 -->|problem| n368
  n473 -->|target| n218
  n474 -->|question| n338
  n475 -->|target| n271
  n476 -->|target| n314
  n477 -->|conclusion| n428
  n478 -->|problem| n350
  n479 -->|prerequisite| n412
  n480 -->|result| n372
  n481 -->|result| n364
  n482 -->|target| n364
  n483 -->|target| n321
  n484 -->|problem| n348
  n485 -->|target| n289
  n486 -->|result| n379
  n487 -->|replacement| n379
  n488 -->|right| n397
  n489 -->|target| n379
  n490 -->|problem| n379
  n491 -->|problem| n379
  n492 -->|general| n335
  n493 -->|target| n335
  n494 -->|general| n401
  n495 -->|result| n377
  n496 -->|problem| n377
  n497 -->|target| n409
  n498 -->|target| n409
  n499 -->|question| n375
  n500 -->|problem| n377
  n501 -->|result| n363
  n502 -->|problem| n363
  n503 -->|problem| n377
  n504 -->|replacement| n378
  n505 -->|question| n378
  n506 -->|problem| n378
  n507 -->|whole| n399
  n508 -->|problem| n351
  n509 -->|problem| n351
  n510 -->|whole| n322
  n511 -->|result| n358
  n512 -->|problem| n358
  n513 -->|target| n219
  n514 -->|target| n219
  n515 -->|target| n219
  n516 -->|problem| n352
  n517 -->|replacement| n373
  n518 -->|target| n250
  n519 -->|prerequisite| n373
  n520 -->|old| n250
  n521 -->|target| n289
  n522 -->|target| n348
  n523 -->|prerequisite| n361
  n524 -->|prerequisite| n336
  n525 -->|target| n378
  n526 -->|target| n428
  n527 -->|result| n453
  n528 -->|whole| n453
  n529 -->|whole| n453
  n530 -->|result| n438
  n531 -->|prerequisite| n399
  n532 -->|prerequisite| n351
  n533 -->|target| n378
  n534 -->|question| n369
  n535 -->|problem| n377
  n536 -->|old| n221
  n537 -->|target| n326
  n538 -->|replacement| n376
  n539 -->|target| n297
  n540 -->|target| n373
  n541 -->|target| n401
  n542 -->|target| n289
  n543 -->|target| n251
  n544 -->|target| n294
  n545 -->|target| n294
  n546 -->|target| n420
  n547 -->|target| n389
  n548 -->|result| n393
  n549 -->|problem| n393
  n550 -->|target| n450
  n551 -->|target| n361
  n552 -->|target| n314
  n553 -->|replacement| n362
  n554 -->|right| n450
  n555 -->|target| n387
  n556 -->|target| n360
  n557 -->|result| n273
  n558 -->|replacement| n337
  n559 -->|problem| n337
  n560 -->|whole| n273
  n561 -->|problem| n337
  n562 -->|prerequisite| n407
  n563 -->|target| n307
  n564 -->|result| n230
  n565 -->|result| n232
  n566 -->|prerequisite| n232
  n567 -->|prerequisite| n230
  n568 -->|target| n314
  n569 -->|problem| n342
  n570 -->|whole| n413
  n571 -->|whole| n413
  n572 -->|whole| n413
  n573 -->|whole| n413
  n574 -->|whole| n413
  n575 -->|question| n342
  n576 -->|target| n360
  n577 -->|target| n393
  n578 -->|problem| n392
  n579 -->|conclusion| n439
  n580 -->|right| n442
  n581 -->|target| n413
  n582 -->|replacement| n339
  n583 -->|prerequisite| n224
  n584 -->|target| n389
  n585 -->|whole| n244
  n586 -->|whole| n244
  n587 -->|prerequisite| n339
  n588 -->|question| n384
  n589 -->|conclusion| n423
  n590 -->|result| n355
  n591 -->|problem| n355
  n592 -->|result| n238
  n593 -->|result| n239
  n594 -->|right| n239
  n595 -->|question| n383
  n596 -->|conclusion| n241
  n597 -->|target| n275
  n598 -->|result| n311
  n599 -->|target| n414
  n600 -->|problem| n370
  n601 -->|problem| n370
  n602 -->|whole| n245
  n603 -->|problem| n370
  n604 -->|whole| n425
  n605 -->|whole| n425
  n606 -->|whole| n425
  n607 -->|conclusion| n405
  n608 -->|prerequisite| n292
  n609 -->|target| n296
  n610 -->|question| n388
  n611 -->|conclusion| n421
  n612 -->|conclusion| n329
  n613 -->|result| n214
  n614 -->|problem| n388
  n615 -->|conclusion| n329
  n616 -->|conclusion| n215
  n617 -->|whole| n215
  n618 -->|whole| n215
  n619 -->|old| n296
  n620 -->|whole| n398
  n621 -->|whole| n398
  n622 -->|conclusion| n245
  n623 -->|target| n296
  n624 -->|conclusion| n398
  n625 -->|whole| n245
  n626 -->|whole| n245
  n627 -->|target| n245
  n628 -->|question| n370
  n629 -->|replacement| n341
  n630 -->|problem| n341
  n631 -->|target| n392
  n632 -->|problem| n374
  n633 -->|problem| n432
  n634 -->|target| n430
  n635 -->|right| n430
  n636 -->|problem| n341
  n637 -->|target| n292
  n638 -->|problem| n341
  n639 -->|problem| n370
  n640 -->|whole| n316
  n641 -->|right| n269
  n642 -->|question| n354
  n643 -->|problem| n354
  n644 -->|whole| n231
  n645 -->|question| n385
  n646 -->|whole| n416
  n647 -->|conclusion| n416
  n648 -->|question| n382
  n649 -->|target| n404
  n650 -->|conclusion| n403
  n651 -->|result| n242
  n652 -->|result| n242
  n653 -->|general| n231
  n654 -->|general| n404
  n655 -->|object| n245
  n656 -->|object| n245
  n657 -->|target| n410
  n658 -->|target| n311
  n659 -->|target| n393
  n660 -->|target| n350
  n661 -->|whole| n242
  n662 -->|whole| n242
  n663 -->|prerequisite| n416
  n664 -->|prerequisite| n403
  n665 -->|problem| n339
  n666 -->|whole| n225
  n667 -->|whole| n253
  n668 -->|conclusion| n225
  n669 -->|conclusion| n225
  n670 -->|conclusion| n225
  n671 -->|whole| n225
  n672 -->|general| n231
  n673 -->|target| n452
  n674 -->|conclusion| n225
  n675 -->|object| n231
  n676 -->|prerequisite| n225
  n677 -->|prerequisite| n452
  n678 -->|whole| n452
  n679 -->|whole| n452
  n680 -->|whole| n452
  n681 -->|whole| n452
  n682 -->|whole| n452
  n683 -->|whole| n452
  n684 -->|whole| n452
  n685 -->|whole| n452
  n686 -->|whole| n452
  n687 -->|question| n391
  n688 -->|result| n444
  n689 -->|result| n444
  n690 -->|right| n443
  n691 -->|whole| n419
  n692 -->|whole| n441
  n693 -->|whole| n441
  n694 -->|problem| n389
  n695 -->|conclusion| n441
  n696 -->|conclusion| n441
  n697 -->|target| n448
  n698 -->|conclusion| n441
  n699 -->|prerequisite| n257
  n700 -->|prerequisite| n247
  n701 -->|target| n225
  n702 -->|target| n330
  n703 -->|target| n416
```
