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
  n185["concept: A: hypotheses newly live after semantic alignment of the previous state."]
  n186["reference: AIF+ and Inference Anchoring Theory as candidate dialogue/argument representations."]
  n187["hypothesis: Candidate generation may be better modeled as an algebra over languages, expressions, theories and queries than as a short folk list of cognitive verbs."]
  n188["hypothesis: Ampliative warrant requires assumptions or constraints beyond bare logical entailment from finite evidence."]
  n189["claim: Nontrivial ampliative guarantees require restrictions on the admissible possible-world or problem class."]
  n190["claim: For an embedded observer, constraints used in derivations should be described as assumed rather than known."]
  n191["claim: Assumption is normally a role played by a sentence or theory rather than a base formal artifact type."]
  n192["concept: An ATMS-style environment is a consistent set of assumptions under which consequences can be evaluated."]
  n193["concept: A label records minimal consistent assumption environments sufficient to support a datum."]
  n194["reference: de Kleer's Assumption-based Truth Maintenance System as a precedent for multiple simultaneous assumption environments and dependency labels."]
  n195["hypothesis: Persistent epistemic organization can be represented as assumptions, explicit justifications and minimal support environments rather than one committed theory."]
  n196["goal: Derive a taxonomy from modest explicit assumptions rather than simply assuming it."]
  n197["claim: Conditionalization presupposes a hypothesis space, likelihoods and priors; it does not ground all of them."]
  n198["method: A Bayesian or causal DAG as a candidate representation of inferential relationships."]
  n199["hypothesis: Belief change depends on existing representations and an agent-specific updating process."]
  n200["claim: The black-box state maintains alternatives; a white-box move temporarily stipulates one context and inspects its consequences."]
  n201["reference: Bronstein and geometric deep learning as a candidate framework for learning primitives."]
  n202["claim: Bronstein/geometric deep learning should not be part of the foundational spine merely because it was suggested earlier."]
  n203["hypothesis: A generated candidate can have a compositional footprint spanning several formal artifact kinds rather than exactly one exclusive type."]
  n204["concept: Candidate generation maps current state and evidence to candidate propositions, models or structures before evaluation and commitment."]
  n205["hypothesis: Candidate generation is best modeled by an interface separating draft/search space, construction operators, strategy, elaboration, evaluation feedback and warrant."]
  n206["claim: The dialogue itself can serve as an adversarial test case for candidate-generation operators."]
  n207["claim: The earlier seven candidate types were not orthogonal; some mixed artifact kinds with epistemic roles."]
  n208["method: Test whether each observed candidate-generation move has a clear artifact footprint and compositional operator description."]
  n209["goal: Construct a canonical factorization of epistemic transitions relative to an explicit semantic representation contract."]
  n210["method: Canonical/primitive factorization: propose factors, test completeness/redundancy/independence/compositionality/canonicality, diagnose failures, and revise."]
  n211["goal: Classify hypothesis and model moves without requiring certainty or strong knowledge claims."]
  n212["claim: Explanations are only a subset of claims that go beyond observations."]
  n213["claim: Reasoning episodes, strategies and the meta-model should be representable targets, giving closure under self-description."]
  n214["claim: Internal coherence alone does not establish correspondence with reality."]
  n215["concept: Construction of a new expression or concept from constructors and vocabulary already available in the current language."]
  n216["concept: Introduction of genuinely new conceptual or predicate vocabulary not already definable in the current language."]
  n217["claim: A constraint is broader than an explanation or mechanism; empirical, causal and explanatory commitments can occupy different levels."]
  n218["claim: Concept construction inside an existing language and substantive concept invention are different problems."]
  n219["goal: Instantiate the abstract reasoning model on real conversations and identify strategy episodes and reflective relations with provenance."]
  n220["method: Test proposed exhaustive or primitive distinctions by constructing concrete counterexamples and edge cases."]
  n221["hypothesis: Current endpoint: factor epistemic state change relative to a representation contract, keep warrant separate, and treat candidate-generation factorization as open."]
  n222["hypothesis: Current architecture combines an institution-style logical substrate, ATMS-inspired persistent support state, temporary assumption environment, and external query."]
  n223["claim: Deduction and inference by an embedded empirical observer have different dependencies."]
  n224["claim: Defeasible warrant requires explicit attack/defeat relations and can lose license when new defeating information arrives."]
  n225["concept: Extend a signature with a fresh name explicitly defined from old-language expressions, ideally conservatively."]
  n226["concept: D: previously live aligned hypotheses no longer live after the update."]
  n227["hypothesis: Treat communication as a designed transformation of a recipient representation."]
  n228["example: Recognizing spatial separation of black and white dots from individual positions and colors."]
  n229["claim: A reachable draft may be incomplete or ill-formed and must be elaborated/checked before becoming a formal artifact."]
  n230["hypothesis: For reasoning episode R, a draft-generation system G_R=(D_R,d0,O_R,→_R) defines draft states, an initial draft, operators and generative transitions."]
  n231["hypothesis: Conditional deductive context is the closure C(Gamma)=Cl_J(Gamma) of a temporary assumption environment under justifications."]
  n232["example: This dialogue repeatedly split, merged and retyped candidate primitives after detecting over-, under- or misfactoring."]
  n233["example: This dialogue explicitly turned the developing meta-model back onto the process used to construct that same meta-model."]
  n234["concept: A typed epistemic action is the normalized target of warrant, e.g. derive, retain, raise support, accept, retract, use a report, or select a strategy."]
  n235["claim: Equivalence under predictive or causal consequence is better treated as a relevance or model-selection criterion than as the ontology of all patterns."]
  n236["goal: Evaluate reasoning-move trajectories and learn which strategies work under which conditions."]
  n237["claim: Verification or evaluation feedback does not automatically constitute epistemic warrant."]
  n238["concept: Evaluator feedback is a representable diagnostic such as a counterexample, violated constraint, failed proof obligation, empirical mismatch or warrant condition."]
  n239["claim: Evidence need not be a privileged top-level coordinate; reports and observations can be typed provenance-bearing nodes with their own dependencies."]
  n240["hypothesis: For a fixed hypothesis universe, hard live-set changes reduce to additions and deletions; preserve, restrict, expand and replace are derived cases."]
  n241["concept: Build an expression using constructors already licensed by the current language."]
  n242["concept: Underfactored, overfactored and misfactored are diagnostics for revising a proposed primitive decomposition."]
  n243["claim: Canonical-factorization analysis is one strategy that searches a factorization-specific draft space using local operators and evaluators."]
  n244["claim: Repeated detection of over- and underfactoring is a core recurring reasoning pattern in this inquiry."]
  n245["claim: The earlier five proposed move types were not a minimal state-update basis."]
  n246["concept: Elaboration/checking maps a draft candidate to a well-formed formal artifact or failure."]
  n247["method: Model an inference method as a function from evidence histories to hypotheses."]
  n248["claim: Institution semantics alone does not provide the concrete syntax/module layer needed to construct and transform formal artifacts."]
  n249["goal: Construct a coherent formalism for epistemic moves without preserving historical inference labels when they obscure the structure."]
  n250["goal: Formalize candidate generation using the dialogue as a test case while importing established operators where possible."]
  n251["claim: Generative space, construction operators and search/control strategy are distinct components."]
  n252["hypothesis: Generative structure could be the umbrella object for the inquiry."]
  n253["method: Symmetry, deformation stability and scale separation/locality as geometric learning priors."]
  n254["method: When inquiry drifts into downstream implementation or optimization, return explicitly to the original unresolved question."]
  n255["concept: mu: optional graded support or plausibility over live hypotheses."]
  n256["reference: Hoel, causal emergence, coarse-graining and entropy, raised as related work."]
  n257["goal: Develop a formal compositional calculus of hypothesis-space transformations with a separate warrant layer."]
  n258["claim: Observed conversations underdetermine a person's internal beliefs and update mechanism."]
  n259["claim: IIT is considered only for algorithmic partition, irreducibility and cause-effect-structure machinery, not for consciousness claims."]
  n260["hypothesis: Imagination might contribute an additional way to learn beyond observation."]
  n261["claim: Imagination can generate candidates without independently justifying them."]
  n262["hypothesis: Inductive pattern recognition could initialize a loop through abduction and deduction."]
  n263["claim: Institution theory handles language/model semantics while ATMS-like machinery handles support across assumption environments; they are complementary, not competing."]
  n264["hypothesis: Use an institution-style logical substrate (Sig, Sen, Mod, satisfaction) rather than one overloaded universe variable."]
  n265["reference: Institution theory as an abstract separation of signatures, sentences, models and satisfaction, with signature morphisms for translation."]
  n266["hypothesis: Distributed measurements may support joint relational representations not encoded by any individual sensor."]
  n267["hypothesis: An intermediate repair separates language, model space, live hypotheses and graded support as K=(L,M,H,mu)."]
  n268["hypothesis: An intermediate state proposal K=(Sigma,T,W,rho,E,Q) separates signature, explicit theory, semantic possibilities, support, evidence and query."]
  n269["hypothesis: A pattern can be represented by what remains invariant across specified transformations."]
  n270["claim: An unobserved explanatory variable need not specify the process by which an effect occurs."]
  n271["concept: Latent structure as an unobserved explanatory representation, not necessarily a causal mechanism."]
  n272["concept: License is the context- and regime-relative status that a specified epistemic action is permitted with a stated guarantee; it is not identical to warrant."]
  n273["method: When the problem appears well trodden, search existing formal literature before inventing new primitives."]
  n274["concept: H: the currently live hypotheses or possibilities within U."]
  n275["claim: Measurement theory can characterize accessible measured variables without by itself characterizing every structure recognized over those measurements."]
  n276["hypothesis: Sensors determine accessible distinctions, while memory enables relations across time."]
  n277["reference: Measurement theory, psychophysics, information theory and computational mechanics as relevant literatures."]
  n278["hypothesis: Relative to a current epistemic state, entailment versus non-entailment is an immediate MECE logical split."]
  n279["goal: Make exhaustiveness and non-overlap provable by construction rather than asserted from a folk taxonomy."]
  n280["claim: MECE is a desired property of the formalism, not the name of the formal object."]
  n281["claim: MECE is a special case of the broader search for a complete nonredundant compositional factorization."]
  n282["method: Force proposed external formalisms through the current meta-model and treat mismatches as evidence of a gap or bad factorization."]
  n283["method: Use established concept-generation formalisms as a stress test of the epistemic meta-model."]
  n284["claim: Meta-strategy is not a separate infinite type hierarchy; a strategy is meta-level relative to reasoning processes or strategies it monitors or controls."]
  n285["concept: Classes of evidence-to-conclusion mappings with shared properties."]
  n286["reference: MMT as a foundation-independent theory/declaration/object/morphism representation and module system."]
  n287["hypothesis: Use an MMT-like theory graph as the concrete formal representation substrate, with LF as a possible foundation inside it."]
  n288["hypothesis: Model-target effects can be represented as an exact subset of language, structure, parameter and state coordinates rather than one exclusive target."]
  n289["claim: Natural learning need not assume a designer; deliberate communication is an additional case."]
  n290["hypothesis: Optimal explanation or design is a further problem for an observer with an uncertain model of other observers."]
  n291["concept: God-view versus embedded-observer perspective."]
  n292["hypothesis: Combine AIF/IAT argument and dialogue structure with provenance and inquiry-transition records."]
  n293["concept: An open node is an unresolved question or epistemic obligation, not just a mentioned topic."]
  n294["claim: Choosing an optimal hypothesis is downstream of first characterizing the kinds of epistemic moves available."]
  n295["claim: Pattern recognition or relational feature extraction from a fully observed finite configuration need not be inductive."]
  n296["reference: Grenander/Brown Pattern Theory as a candidate formal language for generators, configurations, transformations, variation, observation and inference."]
  n297["claim: Pattern Theory supplies broad representational and inferential machinery but does not by itself derive all observer representations from physics."]
  n298["hypothesis: Induction concerns empirical patterns while abduction concerns mechanisms."]
  n299["claim: Persistent epistemic state and the active assumption context of a reasoning episode should be represented separately."]
  n300["hypothesis: Current persistent state: K_Sigma=(N,A,J,lambda,rho), with represented nodes, assumptions, justifications, minimal support environments and optional graded support."]
  n301["concept: Physically realizable pattern recognition, rather than normatively justified recognition."]
  n302["hypothesis: External reality plus partial observation plus logic yields a set of compatible possibilities, not by itself a unique ampliative conclusion."]
  n303["example: From the observed sequence 2, 4, 6, 8 to the expectation 10."]
  n304["claim: Recognizing a sample pattern and licensing its extension beyond the sample are distinct operations."]
  n305["question: What assumptions and criteria support abductive model selection?"]
  n306["question: Can ampliative epistemic moves be represented in a provably MECE or uniquely factorizable way?"]
  n307["question: Does Bayesian updating explain warrant or merely relocate assumptions?"]
  n308["question: Can candidate generation be given a small compositional or uniquely factorizable basis?"]
  n309["question: What is the minimal type system for generated epistemic candidates?"]
  n310["question: What factorization of epistemic state change can be canonical relative to an explicit representation contract?"]
  n311["question: What claims beyond observation can have support without being explanations?"]
  n312["question: What role does generation of candidate constraints play in black-box inference?"]
  n313["question: How can reusable strategies and meta-strategies be instantiated and identified in specific conversations?"]
  n314["question: What domain-independent structure, if any, constrains draft spaces, construction operators and generative transition relations?"]
  n315["question: Which beyond-observation inferences can an embedded observer make?"]
  n316["question: What is the minimal type system for epistemic actions that can be targets of warrant?"]
  n317["question: Can exhaustiveness of the proposed inference taxonomy be proved?"]
  n318["question: Which existing ontology captures temporal inquiry evolution and reasoning moves?"]
  n319["question: What general dynamics make explanations and visual presentations effective?"]
  n320["question: What is the space of possible explanatory hypotheses?"]
  n321["question: What general concept subsumes MECE-style primitive analysis when the decomposition is compositional rather than a partition?"]
  n322["question: What should be formalized next after separating state update from candidate generation?"]
  n323["question: What general heuristics or formal scaffolding improve thinking across problems?"]
  n324["question: Can imagination yield knowledge not reducible to inference or introspection?"]
  n325["question: Can the apparent overlap between induction and abduction be explained by a deeper compositional formalism?"]
  n326["question: What assumptions minimally support inductive generalization?"]
  n327["question: Under what conditions does evidence E contain information relevant to a proposition H?"]
  n328["question: Can symmetry, invariance and stability supply primitives of pattern recognition?"]
  n329["question: Is structure a set of constraints, or does emergence and computational irreducibility change the ontology?"]
  n330["question: How is latent structure different from a mechanism?"]
  n331["question: What is the minimal formalization of learning relevant to this inquiry?"]
  n332["question: Is algorithm classification the right level for a simple inference taxonomy?"]
  n333["question: What possible maps take current representations beyond the information currently explicit?"]
  n334["question: Is measurement theory sufficient to explain the observer-to-pattern problem?"]
  n335["question: Can candidate-generation formalisms fit the existing meta-model, and if not, what gap do they expose?"]
  n336["question: Which established metareasoning and reflection formalisms should constrain the strategy/self-application layer before it is frozen?"]
  n337["question: What minimal entities and relations does this inference sketch require?"]
  n338["question: How does an embedded observer learn from a non-designed world?"]
  n339["question: What should be attacked next after the assumption-context refinement?"]
  n340["question: What does higher order mean, and how does it differ from coarse-graining?"]
  n341["question: What, if anything, is fundamental about pattern formation before criteria for useful or optimal abstraction are imposed?"]
  n342["question: What operation makes a relational feature explicit to an observer?"]
  n343["question: Which dimensions of perceptual space are available to a physically embedded observer?"]
  n344["question: Which pattern-recognition mappings can physical embedded observers implement?"]
  n345["question: What established machinery should be checked before freezing the revised meta-model in documentation?"]
  n346["question: How should repeated self-application of the developing reasoning model be represented?"]
  n347["question: Is reframe a primitive operation, or is it masking several different transformations?"]
  n348["question: How does the developing epistemic framework characterize the reasoning occurring in this dialogue itself?"]
  n349["question: Where does canonical factorization live when treated as a reusable cognitive strategy?"]
  n350["question: Can the canonical-factorization strategy trace be represented without introducing another vague primitive?"]
  n351["question: Do deduction, induction and abduction exhaust learning beyond observation?"]
  n352["question: Should the model treat a theory used in a derivation as a durable commitment, or only as a temporary assumption context?"]
  n353["question: What warrants the standards by which an inference is warranted?"]
  n354["question: How should multiple independent, conflicting or defeasible warrants combine?"]
  n355["question: How does the earlier warrant work relate to the revised meta-model, and is warrant the same thing as license?"]
  n356["question: What minimal warrant postulates and representation theorems should govern non-entailing commitment changes?"]
  n357["question: How should warrant of warrant be formalized once certainty is removed from the target?"]
  n358["question: Does Wolfram observer theory characterize physically realizable pattern recognizers?"]
  n359["claim: The current query/task belongs to a reasoning episode rather than persistent epistemic state."]
  n360["concept: Reach(R) is the set of draft candidates reachable from d0 by finite sequences of available construction/refinement operators."]
  n361["claim: A mechanism being physically implementable does not establish that it tracks truth."]
  n362["hypothesis: A reasoning episode can be represented as R=(K_Sigma,Gamma,Q)."]
  n363["goal: Map the moves that changed the inquiry, not only the concepts mentioned."]
  n364["claim: Conversations can serve as source-grounded datasets of instantiated reasoning trajectories and proposed strategy episodes."]
  n365["hypothesis: Recognizing a pattern may itself perform the relevant beyond-token representational step."]
  n366["hypothesis: Induction, abduction and deduction can feed back into one another rather than forming a fixed pipeline."]
  n367["hypothesis: Meta-level status is relational: a reasoning episode is meta with respect to the reasoning artifact, strategy or episode it is about."]
  n368["method: Reflective/self-applicative modeling uses the reasoning model to analyze the reasoning process that is constructing the model."]
  n369["claim: Reframe is a dialogue-level macro that may decompose into query, language, theory/support or context transformations."]
  n370["claim: Extracting relations is not necessarily a many-to-one, information-discarding coarse-graining."]
  n371["claim: Any nontrivial target factorization is canonical only relative to a declared representation contract, because structure, parameters and state can be recoded."]
  n372["hypothesis: The relevant map may run between representations rather than raw observations and concepts."]
  n373["hypothesis: Representational lift may be a primitive operation prior to prediction."]
  n374["goal: Anchor the investigation in existing formal theories rather than reinventing terminology."]
  n375["claim: Warrant scope is normally encoded in applicability assumptions and the quantified/type semantics of the guarantee rather than as a separate primitive coordinate."]
  n376["hypothesis: Assume an external reality with sufficiently stable rules."]
  n377["hypothesis: Epistemic state change can be factored, relative to semantic alignment, into representation-space change, additions, deletions and graded-support change."]
  n378["concept: U: the current semantic universe or model space of expressible hypotheses."]
  n379["hypothesis: Stateful computation over an information stream is a general substrate for memory and integration, but does not by itself settle epistemic warrant."]
  n380["hypothesis: A strategy/control layer selects and sequences lower-level reasoning operators; strategy is distinct from primitive operator and candidate artifact."]
  n381["concept: Introduce new predicate/concept vocabulary whose semantics are not merely a definitional abbreviation of the old language."]
  n382["claim: Minimal supporting environments make conditional dependency provenance explicit without warranting the assumptions themselves."]
  n383["claim: Support, warrant, license and executed epistemic update are distinct stages."]
  n384["hypothesis: Memory can be treated abstractly as integration of measurements distributed across time."]
  n385["hypothesis: A set of premises can be stipulated only for a reasoning branch without becoming a durable belief theory."]
  n386["hypothesis: A white-box reasoning branch selects a temporary assumption environment Gamma subseteq A."]
  n387["claim: The dialogue is performing theoretical model construction under conceptual and literature constraints."]
  n388["claim: Theory graphs remain relevant for modular theory networks but are not required as an additional foundational layer yet."]
  n389["claim: Expression construction, definitional extension and substantive concept invention are distinct operations."]
  n390["claim: Candidate generation, warrant/evaluation and epistemic state update are distinct layers and should not be collapsed into a named inference method."]
  n391["hypothesis: Entailment, projection along stable structure and inversion toward generators may recover three inference forms."]
  n392["hypothesis: Generated epistemic candidates require types such as sentence, assumption, justification, model, signature extension, mapping or query."]
  n393["claim: Typed candidate generation remains the main unresolved formal layer after the assumption-context refinement."]
  n394["goal: Make typed candidate generation concrete using the conversation as a test corpus."]
  n395["goal: Represent the conversation with typed entities and relation roles."]
  n396["claim: The previous U/hypothesis-universe coordinate conflates language, expressibility, model space and live hypotheses."]
  n397["claim: The reusable cross-domain abstraction is the candidate-generation interface, not one universal operator set."]
  n398["goal: Deliver a coherent first-pass ontology, conversation instantiation, code and project documentation in GitHub."]
  n399["hypothesis: A warrant certificate records explicit assumptions, a claimed guarantee and support connecting the assumptions to that guarantee."]
  n400["claim: The earlier assumptions/guarantee/certificate warrant shape survives the later meta-model refinements."]
  n401["hypothesis: Core judgment: under warrant regime W and assumptions A, certificate pi warrants epistemic action a with guarantee G."]
  n402["concept: Warrant evaluates whether a candidate-to-commitment move has a specified justification or guarantee under explicit assumptions."]
  n403["hypothesis: Warrant is the structured basis for a derived license rather than a synonym for license."]
  n404["goal: Refactor the existing warrant proposal against the more precise candidate-generation, strategy and epistemic-state model rather than reinventing it."]
  n405["concept: A warrant regime specifies the rules, semantics and acceptance standard under which support can warrant an epistemic action."]
  n406["claim: The inquiry should return from implementation-level pattern and learning theories to the original warrant question."]
  n407["claim: Candidate, transition and strategy warrant need not be primitive warrant types; they are instances of one action-targeted warrant schema."]
  n408["hypothesis: Candidate, transition and strategy warrants appear as distinct descriptive targets before further factorization."]
  n409["claim: Formal well-formedness, typing or deductive validity does not establish epistemic warrant for generating or accepting a candidate."]
  n410["hypothesis: A stipulated model supports within-model reasoning; an embedded observer must infer the model from observations."]
  n411["reference: Wolfram observer theory and rulial space, raised as a related research direction."]
  n412["example: Worked trace of the founding dialogue from I/D/A partition through composition-space, representation-relative factorization, support-context refinement, candidate-type repair and strategy recognition."]
  n413["goal: Build a persistent cross-conversation map of worldview, questions, dependencies and revisions."]
  n414["relation: challenges"]
  n415["relation: supersedes"]
  n416["relation: answers"]
  n417["relation: motivates"]
  n418["relation: candidate_for"]
  n419["relation: motivates"]
  n420["relation: reframes"]
  n421["relation: motivates"]
  n422["relation: candidate_for"]
  n423["relation: motivates"]
  n424["relation: answers"]
  n425["relation: challenges"]
  n426["relation: candidate_for"]
  n427["relation: reframes"]
  n428["relation: challenges"]
  n429["relation: answers"]
  n430["relation: motivates"]
  n431["relation: reframes"]
  n432["relation: candidate_for"]
  n433["relation: challenges"]
  n434["relation: answers"]
  n435["relation: related_to"]
  n436["relation: challenges"]
  n437["relation: supports"]
  n438["relation: candidate_for"]
  n439["relation: depends_on"]
  n440["relation: motivates"]
  n441["relation: motivates"]
  n442["relation: related_to"]
  n443["relation: related_to"]
  n444["relation: candidate_for"]
  n445["relation: challenges"]
  n446["relation: motivates"]
  n447["relation: reframes"]
  n448["relation: distinguishes"]
  n449["relation: related_to"]
  n450["relation: candidate_for"]
  n451["relation: candidate_for"]
  n452["relation: exemplifies"]
  n453["relation: challenges"]
  n454["relation: exemplifies"]
  n455["relation: motivates"]
  n456["relation: candidate_for"]
  n457["relation: challenges"]
  n458["relation: related_to"]
  n459["relation: answers"]
  n460["relation: candidate_for"]
  n461["relation: motivates"]
  n462["relation: candidate_for"]
  n463["relation: candidate_for"]
  n464["relation: reframes"]
  n465["relation: answers"]
  n466["relation: candidate_for"]
  n467["relation: part_of"]
  n468["relation: candidate_for"]
  n469["relation: candidate_for"]
  n470["relation: part_of"]
  n471["relation: motivates"]
  n472["relation: candidate_for"]
  n473["relation: related_to"]
  n474["relation: related_to"]
  n475["relation: related_to"]
  n476["relation: candidate_for"]
  n477["relation: reframes"]
  n478["relation: challenges"]
  n479["relation: depends_on"]
  n480["relation: supersedes"]
  n481["relation: challenges"]
  n482["relation: related_to"]
  n483["relation: depends_on"]
  n484["relation: depends_on"]
  n485["relation: related_to"]
  n486["relation: challenges"]
  n487["relation: motivates"]
  n488["relation: part_of"]
  n489["relation: part_of"]
  n490["relation: motivates"]
  n491["relation: depends_on"]
  n492["relation: depends_on"]
  n493["relation: related_to"]
  n494["relation: answers"]
  n495["relation: candidate_for"]
  n496["relation: supersedes"]
  n497["relation: challenges"]
  n498["relation: reframes"]
  n499["relation: challenges"]
  n500["relation: related_to"]
  n501["relation: challenges"]
  n502["relation: challenges"]
  n503["relation: related_to"]
  n504["relation: related_to"]
  n505["relation: related_to"]
  n506["relation: related_to"]
  n507["relation: related_to"]
  n508["relation: motivates"]
  n509["relation: candidate_for"]
  n510["relation: related_to"]
  n511["relation: related_to"]
  n512["relation: challenges"]
  n513["relation: reframes"]
  n514["relation: distinguishes"]
  n515["relation: related_to"]
  n516["relation: related_to"]
  n517["relation: motivates"]
  n518["relation: reframes"]
  n519["relation: candidate_for"]
  n520["relation: part_of"]
  n521["relation: candidate_for"]
  n522["relation: depends_on"]
  n523["relation: related_to"]
  n524["relation: motivates"]
  n525["relation: motivates"]
  n526["relation: depends_on"]
  n527["relation: depends_on"]
  n528["relation: challenges"]
  n529["relation: candidate_for"]
  n530["relation: part_of"]
  n531["relation: part_of"]
  n532["relation: part_of"]
  n533["relation: part_of"]
  n534["relation: part_of"]
  n535["relation: answers"]
  n536["relation: related_to"]
  n537["relation: related_to"]
  n538["relation: candidate_for"]
  n539["relation: supports"]
  n540["relation: distinguishes"]
  n541["relation: related_to"]
  n542["relation: reframes"]
  n543["relation: depends_on"]
  n544["relation: related_to"]
  n545["relation: part_of"]
  n546["relation: part_of"]
  n547["relation: depends_on"]
  n548["relation: answers"]
  n549["relation: supports"]
  n550["relation: motivates"]
  n551["relation: candidate_for"]
  n552["relation: motivates"]
  n553["relation: motivates"]
  n554["relation: distinguishes"]
  n555["relation: answers"]
  n556["relation: supports"]
  n557["relation: related_to"]
  n558["relation: motivates"]
  n559["relation: challenges"]
  n560["relation: candidate_for"]
  n561["relation: candidate_for"]
  n562["relation: part_of"]
  n563["relation: candidate_for"]
  n564["relation: part_of"]
  n565["relation: part_of"]
  n566["relation: part_of"]
  n567["relation: supports"]
  n568["relation: depends_on"]
  n569["relation: challenges"]
  n570["relation: answers"]
  n571["relation: supports"]
  n572["relation: supports"]
  n573["relation: motivates"]
  n574["relation: candidate_for"]
  n575["relation: supports"]
  n576["relation: supports"]
  n577["relation: part_of"]
  n578["relation: part_of"]
  n579["relation: supersedes"]
  n580["relation: part_of"]
  n581["relation: part_of"]
  n582["relation: supports"]
  n583["relation: challenges"]
  n584["relation: supports"]
  n585["relation: part_of"]
  n586["relation: part_of"]
  n587["relation: related_to"]
  n588["relation: answers"]
  n589["relation: reframes"]
  n590["relation: candidate_for"]
  n591["relation: related_to"]
  n592["relation: candidate_for"]
  n593["relation: candidate_for"]
  n594["relation: challenges"]
  n595["relation: distinguishes"]
  n596["relation: candidate_for"]
  n597["relation: challenges"]
  n598["relation: candidate_for"]
  n599["relation: candidate_for"]
  n600["relation: part_of"]
  n601["relation: distinguishes"]
  n602["relation: answers"]
  n603["relation: candidate_for"]
  n604["relation: part_of"]
  n605["relation: answers"]
  n606["relation: part_of"]
  n607["relation: supports"]
  n608["relation: answers"]
  n609["relation: related_to"]
  n610["relation: supports"]
  n611["relation: motivates"]
  n612["relation: motivates"]
  n613["relation: exemplifies"]
  n614["relation: exemplifies"]
  n615["relation: about"]
  n616["relation: about"]
  n617["relation: related_to"]
  n618["relation: related_to"]
  n619["relation: related_to"]
  n620["relation: related_to"]
  n621["relation: part_of"]
  n622["relation: part_of"]
  n623["relation: depends_on"]
  n624["relation: depends_on"]
  n625["relation: candidate_for"]
  n626["relation: part_of"]
  n627["relation: part_of"]
  n628["relation: supports"]
  n629["relation: supports"]
  n630["relation: supports"]
  n631["relation: part_of"]
  n632["relation: exemplifies"]
  n633["relation: related_to"]
  n634["relation: supports"]
  n635["relation: about"]
  n636["relation: depends_on"]
  n637["relation: depends_on"]
  n638["relation: part_of"]
  n639["relation: part_of"]
  n640["relation: part_of"]
  n641["relation: part_of"]
  n642["relation: part_of"]
  n643["relation: part_of"]
  n644["relation: part_of"]
  n645["relation: part_of"]
  n646["relation: part_of"]
  n647["relation: answers"]
  n648["relation: motivates"]
  n649["relation: motivates"]
  n650["relation: distinguishes"]
  n651["relation: part_of"]
  n652["relation: part_of"]
  n653["relation: part_of"]
  n654["relation: candidate_for"]
  n655["relation: supports"]
  n656["relation: supports"]
  n657["relation: challenges"]
  n658["relation: supports"]
  n659["relation: depends_on"]
  n660["relation: depends_on"]
  n661["relation: related_to"]
  n662["relation: related_to"]
  n663["relation: related_to"]
  n0 -->|then| n1
  n0 -->|output| n351
  n1 -->|then| n2
  n1 -->|output| n260
  n2 -->|then| n3
  n2 -->|output| n324
  n3 -->|then| n4
  n3 -->|output| n261
  n4 -->|then| n5
  n4 -->|output| n353
  n5 -->|then| n6
  n5 -->|output| n196
  n6 -->|then| n7
  n6 -->|output| n317
  n7 -->|then| n8
  n7 -->|output| n223
  n8 -->|then| n9
  n8 -->|output| n315
  n9 -->|then| n10
  n9 -->|output| n198
  n9 -->|output| n298
  n10 -->|then| n11
  n10 -->|output| n330
  n11 -->|then| n12
  n11 -->|output| n270
  n12 -->|then| n13
  n12 -->|output| n320
  n13 -->|then| n14
  n13 -->|output| n311
  n14 -->|then| n15
  n14 -->|output| n372
  n15 -->|then| n16
  n15 -->|output| n333
  n16 -->|then| n17
  n16 -->|output| n374
  n17 -->|then| n18
  n17 -->|output| n247
  n18 -->|then| n19
  n18 -->|output| n307
  n19 -->|then| n20
  n19 -->|output| n197
  n20 -->|then| n21
  n20 -->|output| n285
  n21 -->|then| n22
  n21 -->|output| n332
  n22 -->|then| n23
  n22 -->|output| n376
  n23 -->|then| n24
  n23 -->|output| n391
  n24 -->|then| n25
  n24 -->|output| n337
  n25 -->|then| n26
  n25 -->|output| n329
  n26 -->|then| n27
  n26 -->|output| n291
  n27 -->|then| n28
  n27 -->|output| n262
  n28 -->|then| n29
  n28 -->|output| n304
  n29 -->|then| n30
  n29 -->|output| n301
  n29 -->|output| n344
  n30 -->|then| n31
  n30 -->|output| n358
  n31 -->|then| n32
  n31 -->|output| n256
  n32 -->|then| n33
  n32 -->|output| n365
  n33 -->|then| n34
  n33 -->|output| n228
  n33 -->|output| n342
  n34 -->|then| n35
  n34 -->|output| n373
  n35 -->|then| n36
  n35 -->|output| n340
  n36 -->|then| n37
  n36 -->|output| n370
  n37 -->|then| n38
  n37 -->|output| n201
  n38 -->|then| n39
  n38 -->|output| n328
  n39 -->|then| n40
  n39 -->|output| n253
  n40 -->|then| n41
  n40 -->|output| n343
  n41 -->|then| n42
  n41 -->|output| n276
  n42 -->|then| n43
  n42 -->|output| n395
  n43 -->|then| n44
  n43 -->|output| n363
  n44 -->|then| n45
  n44 -->|output| n186
  n45 -->|then| n46
  n45 -->|output| n318
  n46 -->|then| n47
  n46 -->|output| n292
  n47 -->|then| n48
  n47 -->|output| n323
  n48 -->|then| n49
  n48 -->|output| n236
  n49 -->|then| n50
  n49 -->|output| n199
  n50 -->|then| n51
  n50 -->|output| n258
  n51 -->|then| n52
  n51 -->|output| n319
  n52 -->|then| n53
  n52 -->|output| n227
  n53 -->|then| n54
  n53 -->|output| n338
  n54 -->|then| n55
  n54 -->|output| n290
  n55 -->|then| n56
  n55 -->|output| n289
  n56 -->|then| n57
  n56 -->|output| n366
  n57 -->|then| n58
  n57 -->|output| n326
  n58 -->|then| n59
  n58 -->|output| n305
  n59 -->|then| n60
  n59 -->|output| n413
  n60 -->|then| n61
  n60 -->|output| n293
  n61 -->|then| n62
  n61 -->|output| n398
  n62 -->|then| n63
  n62 -->|output| n334
  n63 -->|then| n64
  n63 -->|output| n275
  n64 -->|then| n65
  n64 -->|output| n296
  n65 -->|then| n66
  n65 -->|output| n202
  n66 -->|then| n67
  n66 -->|output| n297
  n67 -->|then| n68
  n67 -->|output| n341
  n68 -->|then| n69
  n68 -->|output| n235
  n69 -->|then| n70
  n69 -->|output| n331
  n70 -->|then| n71
  n70 -->|output| n295
  n71 -->|then| n72
  n71 -->|output| n266
  n72 -->|then| n73
  n72 -->|output| n259
  n73 -->|then| n74
  n73 -->|output| n384
  n74 -->|then| n75
  n74 -->|output| n379
  n75 -->|then| n76
  n75 -->|output| n357
  n76 -->|then| n77
  n76 -->|output| n406
  n77 -->|then| n78
  n77 -->|output| n188
  n78 -->|then| n79
  n78 -->|output| n302
  n79 -->|then| n80
  n79 -->|output| n312
  n80 -->|then| n81
  n80 -->|output| n294
  n81 -->|then| n82
  n81 -->|output| n327
  n82 -->|then| n83
  n82 -->|output| n190
  n83 -->|then| n84
  n83 -->|output| n325
  n84 -->|then| n85
  n84 -->|output| n217
  n85 -->|then| n86
  n85 -->|output| n249
  n86 -->|then| n87
  n86 -->|then| n88
  n86 -->|output| n278
  n87 -->|then| n89
  n87 -->|output| n279
  n88 -->|then| n89
  n88 -->|output| n306
  n89 -->|then| n90
  n89 -->|output| n288
  n90 -->|then| n91
  n90 -->|output| n310
  n91 -->|then| n93
  n91 -->|output| n280
  n92 -->|then| n157
  n92 -->|output| n209
  n93 -->|then| n94
  n93 -->|output| n211
  n94 -->|then| n95
  n94 -->|output| n257
  n95 -->|then| n96
  n95 -->|output| n245
  n96 -->|then| n97
  n96 -->|output| n240
  n97 -->|then| n98
  n97 -->|output| n204
  n97 -->|output| n377
  n97 -->|output| n402
  n98 -->|then| n99
  n98 -->|output| n255
  n98 -->|output| n274
  n98 -->|output| n378
  n99 -->|then| n100
  n99 -->|then| n101
  n99 -->|output| n377
  n100 -->|then| n102
  n100 -->|output| n308
  n101 -->|then| n102
  n101 -->|output| n221
  n102 -->|then| n103
  n102 -->|output| n399
  n103 -->|then| n104
  n103 -->|output| n189
  n104 -->|then| n106
  n104 -->|output| n402
  n105 -->|then| n164
  n105 -->|output| n348
  n106 -->|then| n107
  n106 -->|output| n387
  n107 -->|then| n108
  n107 -->|output| n206
  n108 -->|then| n109
  n108 -->|output| n322
  n109 -->|then| n110
  n109 -->|output| n250
  n110 -->|then| n111
  n110 -->|output| n347
  n111 -->|then| n112
  n111 -->|output| n215
  n112 -->|then| n113
  n112 -->|output| n216
  n113 -->|then| n114
  n113 -->|output| n218
  n114 -->|then| n115
  n114 -->|output| n369
  n115 -->|then| n116
  n115 -->|output| n187
  n116 -->|then| n117
  n116 -->|output| n335
  n117 -->|then| n118
  n117 -->|output| n283
  n118 -->|then| n119
  n118 -->|output| n396
  n119 -->|then| n120
  n119 -->|output| n267
  n120 -->|then| n121
  n120 -->|output| n264
  n120 -->|output| n265
  n121 -->|then| n122
  n121 -->|output| n268
  n122 -->|then| n123
  n122 -->|output| n225
  n122 -->|output| n241
  n122 -->|output| n381
  n122 -->|output| n389
  n123 -->|then| n124
  n123 -->|output| n369
  n124 -->|then| n125
  n124 -->|output| n392
  n125 -->|then| n126
  n125 -->|output| n352
  n126 -->|then| n127
  n126 -->|output| n385
  n127 -->|then| n128
  n127 -->|output| n299
  n128 -->|then| n129
  n128 -->|output| n200
  n129 -->|then| n130
  n129 -->|output| n345
  n130 -->|then| n131
  n130 -->|output| n194
  n131 -->|then| n132
  n131 -->|output| n195
  n132 -->|then| n133
  n132 -->|output| n192
  n132 -->|output| n193
  n133 -->|then| n134
  n133 -->|output| n300
  n134 -->|then| n135
  n134 -->|output| n386
  n135 -->|then| n136
  n135 -->|output| n231
  n136 -->|then| n137
  n136 -->|output| n263
  n137 -->|then| n138
  n137 -->|output| n239
  n138 -->|then| n139
  n138 -->|output| n359
  n139 -->|then| n140
  n139 -->|output| n362
  n140 -->|then| n141
  n140 -->|output| n388
  n141 -->|then| n142
  n141 -->|output| n222
  n142 -->|then| n143
  n142 -->|output| n309
  n142 -->|output| n393
  n143 -->|then| n144
  n143 -->|output| n339
  n144 -->|then| n145
  n144 -->|output| n394
  n145 -->|then| n146
  n145 -->|output| n208
  n146 -->|then| n147
  n146 -->|output| n207
  n147 -->|then| n148
  n147 -->|output| n191
  n148 -->|then| n149
  n148 -->|output| n203
  n149 -->|then| n150
  n149 -->|output| n248
  n150 -->|then| n151
  n150 -->|output| n286
  n150 -->|output| n287
  n151 -->|then| n152
  n151 -->|output| n246
  n152 -->|then| n153
  n152 -->|output| n409
  n153 -->|then| n154
  n153 -->|output| n321
  n154 -->|then| n155
  n154 -->|output| n244
  n155 -->|then| n92
  n155 -->|then| n156
  n155 -->|output| n281
  n156 -->|then| n157
  n156 -->|output| n210
  n157 -->|then| n158
  n157 -->|output| n242
  n158 -->|then| n159
  n158 -->|output| n349
  n159 -->|then| n160
  n159 -->|output| n380
  n160 -->|then| n161
  n160 -->|output| n284
  n161 -->|then| n165
  n161 -->|then| n166
  n161 -->|output| n346
  n162 -->|then| n105
  n162 -->|then| n163
  n162 -->|output| n368
  n163 -->|then| n164
  n163 -->|output| n367
  n164 -->|then| n167
  n164 -->|output| n213
  n165 -->|then| n162
  n165 -->|output| n313
  n166 -->|then| n162
  n166 -->|output| n219
  n167 -->|then| n168
  n167 -->|output| n364
  n168 -->|then| n169
  n168 -->|output| n336
  n169 -->|then| n170
  n169 -->|output| n205
  n170 -->|then| n171
  n170 -->|output| n230
  n170 -->|output| n360
  n171 -->|then| n172
  n171 -->|output| n251
  n172 -->|then| n173
  n172 -->|output| n229
  n173 -->|then| n174
  n173 -->|output| n237
  n173 -->|output| n238
  n174 -->|then| n175
  n174 -->|output| n243
  n175 -->|then| n176
  n175 -->|output| n397
  n176 -->|then| n177
  n176 -->|output| n314
  n176 -->|output| n350
  n176 -->|output| n412
  n177 -->|then| n178
  n177 -->|output| n355
  n178 -->|then| n179
  n178 -->|output| n403
  n178 -->|output| n408
  n179 -->|then| n180
  n179 -->|output| n404
  n180 -->|then| n181
  n180 -->|output| n400
  n181 -->|then| n182
  n181 -->|output| n272
  n181 -->|output| n383
  n182 -->|then| n183
  n182 -->|output| n234
  n182 -->|output| n401
  n182 -->|output| n405
  n183 -->|then| n184
  n183 -->|output| n375
  n183 -->|output| n407
  n184 -->|output| n224
  n184 -->|output| n316
  n184 -->|output| n354
  n185 -->|part| n533
  n186 -->|input| n45
  n186 -->|candidate| n468
  n187 -->|source| n557
  n188 -->|candidate| n509
  n189 -->|premise| n539
  n190 -->|left| n514
  n191 -->|left| n595
  n192 -->|part| n577
  n193 -->|part| n578
  n194 -->|input| n131
  n194 -->|candidate| n574
  n195 -->|input| n132
  n195 -->|input| n133
  n195 -->|input| n136
  n195 -->|premise| n575
  n196 -->|input| n6
  n196 -->|reason| n419
  n197 -->|answer| n434
  n198 -->|input| n18
  n198 -->|candidate| n422
  n199 -->|input| n50
  n199 -->|input| n51
  n200 -->|premise| n572
  n201 -->|input| n38
  n201 -->|input| n65
  n201 -->|candidate| n460
  n201 -->|reason| n461
  n202 -->|new| n496
  n203 -->|candidate| n596
  n204 -->|input| n100
  n204 -->|source| n536
  n204 -->|left| n540
  n205 -->|input| n170
  n205 -->|input| n173
  n205 -->|input| n175
  n205 -->|input| n176
  n205 -->|candidate| n625
  n206 -->|input| n108
  n206 -->|premise| n549
  n206 -->|reason| n550
  n207 -->|input| n147
  n207 -->|input| n148
  n207 -->|challenger| n594
  n207 -->|part| n644
  n208 -->|candidate| n593
  n209 -->|dependent| n522
  n210 -->|input| n157
  n210 -->|input| n158
  n210 -->|input| n159
  n210 -->|input| n174
  n210 -->|input| n176
  n210 -->|candidate| n603
  n210 -->|part| n606
  n210 -->|part| n621
  n211 -->|input| n94
  n212 -->|challenger| n428
  n212 -->|answer| n429
  n213 -->|premise| n610
  n214 -->|candidate| n418
  n215 -->|input| n113
  n215 -->|input| n122
  n215 -->|left| n554
  n216 -->|input| n113
  n216 -->|input| n122
  n217 -->|source| n516
  n218 -->|answer| n555
  n219 -->|input| n167
  n220 -->|source| n620
  n221 -->|input| n105
  n221 -->|dependent| n547
  n222 -->|input| n140
  n222 -->|input| n143
  n222 -->|input| n161
  n222 -->|input| n177
  n222 -->|answer| n588
  n223 -->|input| n8
  n223 -->|reason| n421
  n224 -->|premise| n658
  n225 -->|part| n565
  n226 -->|part| n534
  n227 -->|input| n53
  n227 -->|input| n55
  n227 -->|candidate| n476
  n228 -->|input| n34
  n228 -->|input| n71
  n228 -->|example| n454
  n228 -->|reason| n455
  n229 -->|premise| n629
  n230 -->|input| n171
  n230 -->|input| n172
  n230 -->|part| n626
  n231 -->|part| n581
  n232 -->|input| n154
  n232 -->|example| n613
  n232 -->|subject| n615
  n233 -->|example| n614
  n233 -->|subject| n616
  n234 -->|part| n652
  n235 -->|challenger| n499
  n236 -->|input| n49
  n236 -->|candidate| n472
  n236 -->|source| n473
  n236 -->|part| n489
  n237 -->|premise| n630
  n238 -->|part| n631
  n239 -->|challenger| n583
  n240 -->|candidate| n529
  n241 -->|part| n564
  n242 -->|part| n604
  n242 -->|part| n646
  n243 -->|source| n633
  n245 -->|input| n96
  n245 -->|challenger| n528
  n246 -->|input| n152
  n246 -->|part| n600
  n247 -->|input| n20
  n247 -->|candidate| n432
  n248 -->|input| n150
  n248 -->|challenger| n597
  n249 -->|input| n86
  n250 -->|input| n110
  n250 -->|input| n115
  n250 -->|input| n116
  n250 -->|input| n124
  n250 -->|candidate| n551
  n251 -->|premise| n628
  n252 -->|candidate| n426
  n253 -->|candidate| n462
  n254 -->|source| n619
  n255 -->|input| n99
  n255 -->|part| n532
  n256 -->|candidate| n451
  n257 -->|input| n95
  n257 -->|input| n97
  n257 -->|dependent| n526
  n257 -->|dependent| n527
  n258 -->|source| n474
  n259 -->|source| n504
  n260 -->|input| n2
  n260 -->|input| n3
  n261 -->|new| n415
  n261 -->|answer| n416
  n262 -->|input| n28
  n262 -->|input| n56
  n262 -->|candidate| n444
  n263 -->|premise| n582
  n264 -->|input| n121
  n264 -->|input| n136
  n264 -->|input| n141
  n264 -->|input| n149
  n264 -->|part| n562
  n265 -->|candidate| n561
  n266 -->|input| n72
  n266 -->|input| n73
  n266 -->|source| n503
  n267 -->|input| n120
  n267 -->|candidate| n560
  n268 -->|input| n125
  n268 -->|input| n137
  n268 -->|candidate| n563
  n269 -->|candidate| n463
  n270 -->|input| n12
  n270 -->|answer| n424
  n270 -->|challenger| n425
  n271 -->|input| n10
  n272 -->|part| n651
  n273 -->|source| n617
  n274 -->|input| n99
  n274 -->|part| n531
  n275 -->|input| n64
  n275 -->|answer| n494
  n276 -->|answer| n465
  n277 -->|candidate| n466
  n278 -->|input| n87
  n278 -->|candidate| n519
  n279 -->|input| n88
  n279 -->|input| n89
  n279 -->|input| n90
  n279 -->|input| n153
  n279 -->|input| n155
  n279 -->|part| n520
  n279 -->|reason| n524
  n280 -->|input| n92
  n280 -->|source| n523
  n281 -->|answer| n602
  n282 -->|source| n618
  n284 -->|premise| n607
  n285 -->|input| n21
  n285 -->|input| n80
  n285 -->|source| n435
  n286 -->|candidate| n598
  n287 -->|input| n151
  n287 -->|input| n172
  n287 -->|candidate| n599
  n287 -->|part| n645
  n288 -->|candidate| n521
  n288 -->|part| n640
  n289 -->|new| n480
  n290 -->|input| n56
  n290 -->|dependent| n479
  n291 -->|source| n442
  n292 -->|input| n47
  n292 -->|candidate| n469
  n293 -->|part| n488
  n294 -->|challenger| n512
  n295 -->|challenger| n501
  n295 -->|challenger| n502
  n296 -->|input| n66
  n296 -->|candidate| n495
  n297 -->|input| n67
  n297 -->|challenger| n497
  n298 -->|reason| n423
  n299 -->|input| n128
  n299 -->|premise| n571
  n300 -->|input| n134
  n300 -->|input| n138
  n300 -->|input| n139
  n300 -->|input| n141
  n300 -->|new| n579
  n300 -->|part| n585
  n300 -->|part| n643
  n301 -->|reason| n446
  n301 -->|left| n448
  n302 -->|input| n79
  n302 -->|source| n510
  n303 -->|example| n452
  n304 -->|input| n29
  n304 -->|input| n32
  n304 -->|challenger| n445
  n305 -->|input| n59
  n306 -->|original| n542
  n307 -->|input| n19
  n307 -->|challenger| n433
  n308 -->|input| n101
  n308 -->|dependent| n543
  n308 -->|original| n589
  n310 -->|input| n91
  n311 -->|input| n14
  n311 -->|original| n431
  n312 -->|source| n511
  n313 -->|input| n166
  n313 -->|reason| n611
  n314 -->|dependent| n636
  n315 -->|input| n9
  n315 -->|input| n27
  n316 -->|dependent| n659
  n317 -->|input| n7
  n317 -->|input| n23
  n317 -->|input| n58
  n317 -->|input| n85
  n317 -->|dependent| n483
  n317 -->|dependent| n484
  n317 -->|original| n518
  n318 -->|input| n46
  n318 -->|reason| n471
  n319 -->|input| n52
  n319 -->|source| n475
  n319 -->|original| n477
  n320 -->|input| n13
  n320 -->|original| n427
  n321 -->|input| n156
  n322 -->|input| n109
  n323 -->|input| n48
  n324 -->|input| n3
  n324 -->|challenger| n414
  n325 -->|input| n84
  n325 -->|input| n85
  n325 -->|source| n515
  n325 -->|reason| n517
  n325 -->|part| n639
  n326 -->|input| n59
  n326 -->|source| n485
  n326 -->|challenger| n486
  n328 -->|input| n39
  n329 -->|input| n26
  n330 -->|input| n11
  n331 -->|source| n500
  n332 -->|input| n22
  n332 -->|challenger| n436
  n333 -->|input| n16
  n333 -->|input| n17
  n333 -->|original| n447
  n334 -->|input| n63
  n334 -->|source| n493
  n335 -->|input| n117
  n335 -->|input| n129
  n335 -->|reason| n558
  n336 -->|dependent| n623
  n336 -->|dependent| n624
  n337 -->|input| n25
  n337 -->|reason| n441
  n338 -->|input| n54
  n338 -->|input| n69
  n338 -->|challenger| n478
  n339 -->|input| n144
  n340 -->|input| n36
  n340 -->|challenger| n457
  n341 -->|input| n68
  n341 -->|input| n75
  n342 -->|input| n37
  n342 -->|input| n40
  n342 -->|original| n464
  n342 -->|original| n498
  n343 -->|input| n41
  n343 -->|input| n42
  n343 -->|input| n62
  n344 -->|input| n30
  n344 -->|input| n31
  n345 -->|input| n130
  n345 -->|reason| n573
  n346 -->|input| n162
  n347 -->|input| n111
  n347 -->|input| n112
  n347 -->|input| n114
  n347 -->|reason| n552
  n347 -->|reason| n553
  n348 -->|input| n106
  n350 -->|dependent| n637
  n351 -->|input| n1
  n351 -->|input| n4
  n351 -->|input| n8
  n351 -->|input| n83
  n351 -->|reason| n417
  n351 -->|original| n420
  n351 -->|part| n638
  n352 -->|input| n126
  n352 -->|challenger| n569
  n353 -->|input| n5
  n353 -->|input| n93
  n353 -->|reason| n525
  n354 -->|dependent| n660
  n355 -->|input| n178
  n355 -->|input| n179
  n355 -->|reason| n648
  n356 -->|source| n544
  n357 -->|input| n76
  n357 -->|input| n81
  n357 -->|source| n507
  n357 -->|original| n513
  n358 -->|source| n449
  n359 -->|input| n139
  n359 -->|premise| n584
  n360 -->|part| n627
  n362 -->|input| n141
  n362 -->|part| n586
  n363 -->|input| n44
  n363 -->|input| n59
  n363 -->|input| n61
  n363 -->|part| n470
  n363 -->|reason| n487
  n364 -->|reason| n612
  n365 -->|input| n33
  n365 -->|input| n70
  n365 -->|challenger| n453
  n366 -->|challenger| n481
  n366 -->|source| n482
  n367 -->|input| n164
  n367 -->|input| n168
  n367 -->|source| n609
  n368 -->|input| n163
  n368 -->|input| n165
  n368 -->|answer| n608
  n368 -->|part| n622
  n369 -->|input| n123
  n369 -->|premise| n556
  n370 -->|source| n458
  n370 -->|answer| n459
  n371 -->|part| n641
  n372 -->|input| n15
  n372 -->|reason| n430
  n373 -->|input| n35
  n373 -->|input| n36
  n373 -->|candidate| n456
  n374 -->|input| n17
  n375 -->|premise| n655
  n376 -->|input| n23
  n376 -->|premise| n437
  n377 -->|input| n98
  n377 -->|input| n101
  n377 -->|answer| n535
  n377 -->|part| n545
  n377 -->|part| n642
  n378 -->|input| n99
  n378 -->|input| n118
  n378 -->|part| n530
  n379 -->|source| n506
  n380 -->|input| n160
  n380 -->|input| n168
  n380 -->|input| n171
  n380 -->|answer| n605
  n381 -->|part| n566
  n382 -->|premise| n576
  n383 -->|input| n182
  n383 -->|left| n650
  n384 -->|input| n74
  n384 -->|source| n505
  n385 -->|input| n127
  n385 -->|answer| n570
  n386 -->|input| n135
  n386 -->|input| n139
  n386 -->|part| n580
  n387 -->|input| n107
  n387 -->|answer| n548
  n388 -->|source| n587
  n389 -->|premise| n567
  n390 -->|input| n101
  n390 -->|source| n541
  n390 -->|part| n546
  n391 -->|input| n24
  n391 -->|input| n57
  n391 -->|candidate| n438
  n391 -->|dependent| n439
  n391 -->|reason| n440
  n392 -->|input| n142
  n392 -->|input| n146
  n392 -->|dependent| n568
  n393 -->|input| n169
  n393 -->|candidate| n590
  n393 -->|source| n591
  n394 -->|input| n145
  n394 -->|candidate| n592
  n395 -->|input| n43
  n395 -->|part| n467
  n396 -->|input| n119
  n396 -->|challenger| n559
  n397 -->|premise| n634
  n398 -->|dependent| n491
  n398 -->|dependent| n492
  n399 -->|input| n103
  n399 -->|input| n180
  n399 -->|candidate| n538
  n400 -->|input| n182
  n400 -->|reason| n649
  n401 -->|input| n183
  n401 -->|input| n184
  n401 -->|candidate| n654
  n401 -->|source| n661
  n401 -->|source| n662
  n401 -->|source| n663
  n402 -->|input| n102
  n402 -->|input| n104
  n402 -->|input| n173
  n402 -->|input| n177
  n402 -->|source| n537
  n403 -->|input| n181
  n403 -->|answer| n647
  n405 -->|part| n653
  n406 -->|input| n77
  n406 -->|reason| n508
  n407 -->|premise| n656
  n407 -->|challenger| n657
  n409 -->|left| n601
  n410 -->|input| n78
  n410 -->|input| n82
  n410 -->|source| n443
  n411 -->|candidate| n450
  n412 -->|example| n632
  n412 -->|subject| n635
  n413 -->|input| n60
  n413 -->|input| n61
  n413 -->|reason| n490
  n414 -->|target| n260
  n415 -->|old| n260
  n416 -->|question| n324
  n417 -->|result| n353
  n418 -->|problem| n353
  n419 -->|result| n317
  n420 -->|replacement| n315
  n421 -->|result| n315
  n422 -->|problem| n315
  n423 -->|result| n330
  n424 -->|question| n330
  n425 -->|target| n298
  n426 -->|problem| n320
  n427 -->|replacement| n311
  n428 -->|target| n252
  n429 -->|question| n311
  n430 -->|result| n333
  n431 -->|replacement| n333
  n432 -->|problem| n333
  n433 -->|target| n198
  n434 -->|question| n307
  n435 -->|target| n247
  n436 -->|target| n285
  n437 -->|conclusion| n391
  n438 -->|problem| n317
  n439 -->|prerequisite| n376
  n440 -->|result| n337
  n441 -->|result| n329
  n442 -->|target| n329
  n443 -->|target| n291
  n444 -->|problem| n315
  n445 -->|target| n262
  n446 -->|result| n344
  n447 -->|replacement| n344
  n448 -->|right| n361
  n449 -->|target| n344
  n450 -->|problem| n344
  n451 -->|problem| n344
  n452 -->|general| n304
  n453 -->|target| n304
  n454 -->|general| n365
  n455 -->|result| n342
  n456 -->|problem| n342
  n457 -->|target| n373
  n458 -->|target| n373
  n459 -->|question| n340
  n460 -->|problem| n342
  n461 -->|result| n328
  n462 -->|problem| n328
  n463 -->|problem| n342
  n464 -->|replacement| n343
  n465 -->|question| n343
  n466 -->|problem| n343
  n467 -->|whole| n363
  n468 -->|problem| n318
  n469 -->|problem| n318
  n470 -->|whole| n292
  n471 -->|result| n323
  n472 -->|problem| n323
  n473 -->|target| n199
  n474 -->|target| n199
  n475 -->|target| n199
  n476 -->|problem| n319
  n477 -->|replacement| n338
  n478 -->|target| n227
  n479 -->|prerequisite| n338
  n480 -->|old| n227
  n481 -->|target| n262
  n482 -->|target| n315
  n483 -->|prerequisite| n326
  n484 -->|prerequisite| n305
  n485 -->|target| n343
  n486 -->|target| n391
  n487 -->|result| n413
  n488 -->|whole| n413
  n489 -->|whole| n413
  n490 -->|result| n398
  n491 -->|prerequisite| n363
  n492 -->|prerequisite| n318
  n493 -->|target| n343
  n494 -->|question| n334
  n495 -->|problem| n342
  n496 -->|old| n201
  n497 -->|target| n296
  n498 -->|replacement| n341
  n499 -->|target| n269
  n500 -->|target| n338
  n501 -->|target| n365
  n502 -->|target| n262
  n503 -->|target| n228
  n504 -->|target| n266
  n505 -->|target| n266
  n506 -->|target| n384
  n507 -->|target| n353
  n508 -->|result| n357
  n509 -->|problem| n357
  n510 -->|target| n410
  n511 -->|target| n326
  n512 -->|target| n285
  n513 -->|replacement| n327
  n514 -->|right| n410
  n515 -->|target| n351
  n516 -->|target| n325
  n517 -->|result| n249
  n518 -->|replacement| n306
  n519 -->|problem| n306
  n520 -->|whole| n249
  n521 -->|problem| n306
  n522 -->|prerequisite| n371
  n523 -->|target| n279
  n524 -->|result| n209
  n525 -->|result| n211
  n526 -->|prerequisite| n211
  n527 -->|prerequisite| n209
  n528 -->|target| n285
  n529 -->|problem| n310
  n530 -->|whole| n377
  n531 -->|whole| n377
  n532 -->|whole| n377
  n533 -->|whole| n377
  n534 -->|whole| n377
  n535 -->|question| n310
  n536 -->|target| n325
  n537 -->|target| n357
  n538 -->|problem| n356
  n539 -->|conclusion| n399
  n540 -->|right| n402
  n541 -->|target| n377
  n542 -->|replacement| n308
  n543 -->|prerequisite| n204
  n544 -->|target| n353
  n545 -->|whole| n221
  n546 -->|whole| n221
  n547 -->|prerequisite| n308
  n548 -->|question| n348
  n549 -->|conclusion| n387
  n550 -->|result| n322
  n551 -->|problem| n322
  n552 -->|result| n215
  n553 -->|result| n216
  n554 -->|right| n216
  n555 -->|question| n347
  n556 -->|conclusion| n218
  n557 -->|target| n250
  n558 -->|result| n283
  n559 -->|target| n378
  n560 -->|problem| n335
  n561 -->|problem| n335
  n562 -->|whole| n222
  n563 -->|problem| n335
  n564 -->|whole| n389
  n565 -->|whole| n389
  n566 -->|whole| n389
  n567 -->|conclusion| n369
  n568 -->|prerequisite| n264
  n569 -->|target| n268
  n570 -->|question| n352
  n571 -->|conclusion| n385
  n572 -->|conclusion| n299
  n573 -->|result| n194
  n574 -->|problem| n352
  n575 -->|conclusion| n299
  n576 -->|conclusion| n195
  n577 -->|whole| n195
  n578 -->|whole| n195
  n579 -->|old| n268
  n580 -->|whole| n362
  n581 -->|whole| n362
  n582 -->|conclusion| n222
  n583 -->|target| n268
  n584 -->|conclusion| n362
  n585 -->|whole| n222
  n586 -->|whole| n222
  n587 -->|target| n222
  n588 -->|question| n335
  n589 -->|replacement| n309
  n590 -->|problem| n309
  n591 -->|target| n356
  n592 -->|problem| n339
  n593 -->|problem| n394
  n594 -->|target| n392
  n595 -->|right| n392
  n596 -->|problem| n309
  n597 -->|target| n264
  n598 -->|problem| n309
  n599 -->|problem| n335
  n600 -->|whole| n287
  n601 -->|right| n246
  n602 -->|question| n321
  n603 -->|problem| n321
  n604 -->|whole| n210
  n605 -->|question| n349
  n606 -->|whole| n380
  n607 -->|conclusion| n380
  n608 -->|question| n346
  n609 -->|target| n368
  n610 -->|conclusion| n367
  n611 -->|result| n219
  n612 -->|result| n219
  n613 -->|general| n210
  n614 -->|general| n368
  n615 -->|object| n222
  n616 -->|object| n222
  n617 -->|target| n374
  n618 -->|target| n283
  n619 -->|target| n357
  n620 -->|target| n317
  n621 -->|whole| n219
  n622 -->|whole| n219
  n623 -->|prerequisite| n380
  n624 -->|prerequisite| n367
  n625 -->|problem| n308
  n626 -->|whole| n205
  n627 -->|whole| n230
  n628 -->|conclusion| n205
  n629 -->|conclusion| n205
  n630 -->|conclusion| n205
  n631 -->|whole| n205
  n632 -->|general| n210
  n633 -->|target| n412
  n634 -->|conclusion| n205
  n635 -->|object| n210
  n636 -->|prerequisite| n205
  n637 -->|prerequisite| n412
  n638 -->|whole| n412
  n639 -->|whole| n412
  n640 -->|whole| n412
  n641 -->|whole| n412
  n642 -->|whole| n412
  n643 -->|whole| n412
  n644 -->|whole| n412
  n645 -->|whole| n412
  n646 -->|whole| n412
  n647 -->|question| n355
  n648 -->|result| n404
  n649 -->|result| n404
  n650 -->|right| n403
  n651 -->|whole| n383
  n652 -->|whole| n401
  n653 -->|whole| n401
  n654 -->|problem| n353
  n655 -->|conclusion| n401
  n656 -->|conclusion| n401
  n657 -->|target| n408
  n658 -->|conclusion| n401
  n659 -->|prerequisite| n234
  n660 -->|prerequisite| n224
  n661 -->|target| n205
  n662 -->|target| n300
  n663 -->|target| n380
```
