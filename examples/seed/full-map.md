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
  n169["concept: A: hypotheses newly live after semantic alignment of the previous state."]
  n170["reference: AIF+ and Inference Anchoring Theory as candidate dialogue/argument representations."]
  n171["hypothesis: Candidate generation may be better modeled as an algebra over languages, expressions, theories and queries than as a short folk list of cognitive verbs."]
  n172["hypothesis: Ampliative warrant requires assumptions or constraints beyond bare logical entailment from finite evidence."]
  n173["claim: Nontrivial ampliative guarantees require restrictions on the admissible possible-world or problem class."]
  n174["claim: For an embedded observer, constraints used in derivations should be described as assumed rather than known."]
  n175["claim: Assumption is normally a role played by a sentence or theory rather than a base formal artifact type."]
  n176["concept: An ATMS-style environment is a consistent set of assumptions under which consequences can be evaluated."]
  n177["concept: A label records minimal consistent assumption environments sufficient to support a datum."]
  n178["reference: de Kleer's Assumption-based Truth Maintenance System as a precedent for multiple simultaneous assumption environments and dependency labels."]
  n179["hypothesis: Persistent epistemic organization can be represented as assumptions, explicit justifications and minimal support environments rather than one committed theory."]
  n180["goal: Derive a taxonomy from modest explicit assumptions rather than simply assuming it."]
  n181["claim: Conditionalization presupposes a hypothesis space, likelihoods and priors; it does not ground all of them."]
  n182["method: A Bayesian or causal DAG as a candidate representation of inferential relationships."]
  n183["hypothesis: Belief change depends on existing representations and an agent-specific updating process."]
  n184["claim: The black-box state maintains alternatives; a white-box move temporarily stipulates one context and inspects its consequences."]
  n185["reference: Bronstein and geometric deep learning as a candidate framework for learning primitives."]
  n186["claim: Bronstein/geometric deep learning should not be part of the foundational spine merely because it was suggested earlier."]
  n187["hypothesis: A generated candidate can have a compositional footprint spanning several formal artifact kinds rather than exactly one exclusive type."]
  n188["concept: Candidate generation maps current state and evidence to candidate propositions, models or structures before evaluation and commitment."]
  n189["claim: The dialogue itself can serve as an adversarial test case for candidate-generation operators."]
  n190["claim: The earlier seven candidate types were not orthogonal; some mixed artifact kinds with epistemic roles."]
  n191["method: Test whether each observed candidate-generation move has a clear artifact footprint and compositional operator description."]
  n192["goal: Construct a canonical factorization of epistemic transitions relative to an explicit semantic representation contract."]
  n193["method: Canonical/primitive factorization: propose factors, test completeness/redundancy/independence/compositionality/canonicality, diagnose failures, and revise."]
  n194["goal: Classify hypothesis and model moves without requiring certainty or strong knowledge claims."]
  n195["claim: Explanations are only a subset of claims that go beyond observations."]
  n196["claim: Reasoning episodes, strategies and the meta-model should be representable targets, giving closure under self-description."]
  n197["claim: Internal coherence alone does not establish correspondence with reality."]
  n198["concept: Construction of a new expression or concept from constructors and vocabulary already available in the current language."]
  n199["concept: Introduction of genuinely new conceptual or predicate vocabulary not already definable in the current language."]
  n200["claim: A constraint is broader than an explanation or mechanism; empirical, causal and explanatory commitments can occupy different levels."]
  n201["claim: Concept construction inside an existing language and substantive concept invention are different problems."]
  n202["goal: Instantiate the abstract reasoning model on real conversations and identify strategy episodes and reflective relations with provenance."]
  n203["method: Test proposed exhaustive or primitive distinctions by constructing concrete counterexamples and edge cases."]
  n204["hypothesis: Current endpoint: factor epistemic state change relative to a representation contract, keep warrant separate, and treat candidate-generation factorization as open."]
  n205["hypothesis: Current architecture combines an institution-style logical substrate, ATMS-inspired persistent support state, temporary assumption environment, and external query."]
  n206["claim: Deduction and inference by an embedded empirical observer have different dependencies."]
  n207["concept: Extend a signature with a fresh name explicitly defined from old-language expressions, ideally conservatively."]
  n208["concept: D: previously live aligned hypotheses no longer live after the update."]
  n209["hypothesis: Treat communication as a designed transformation of a recipient representation."]
  n210["example: Recognizing spatial separation of black and white dots from individual positions and colors."]
  n211["hypothesis: Conditional deductive context is the closure C(Gamma)=Cl_J(Gamma) of a temporary assumption environment under justifications."]
  n212["example: This dialogue repeatedly split, merged and retyped candidate primitives after detecting over-, under- or misfactoring."]
  n213["example: This dialogue explicitly turned the developing meta-model back onto the process used to construct that same meta-model."]
  n214["claim: Equivalence under predictive or causal consequence is better treated as a relevance or model-selection criterion than as the ontology of all patterns."]
  n215["goal: Evaluate reasoning-move trajectories and learn which strategies work under which conditions."]
  n216["claim: Evidence need not be a privileged top-level coordinate; reports and observations can be typed provenance-bearing nodes with their own dependencies."]
  n217["hypothesis: For a fixed hypothesis universe, hard live-set changes reduce to additions and deletions; preserve, restrict, expand and replace are derived cases."]
  n218["concept: Build an expression using constructors already licensed by the current language."]
  n219["concept: Underfactored, overfactored and misfactored are diagnostics for revising a proposed primitive decomposition."]
  n220["claim: Repeated detection of over- and underfactoring is a core recurring reasoning pattern in this inquiry."]
  n221["claim: The earlier five proposed move types were not a minimal state-update basis."]
  n222["concept: Elaboration/checking maps a draft candidate to a well-formed formal artifact or failure."]
  n223["method: Model an inference method as a function from evidence histories to hypotheses."]
  n224["claim: Institution semantics alone does not provide the concrete syntax/module layer needed to construct and transform formal artifacts."]
  n225["goal: Construct a coherent formalism for epistemic moves without preserving historical inference labels when they obscure the structure."]
  n226["goal: Formalize candidate generation using the dialogue as a test case while importing established operators where possible."]
  n227["hypothesis: Generative structure could be the umbrella object for the inquiry."]
  n228["method: Symmetry, deformation stability and scale separation/locality as geometric learning priors."]
  n229["method: When inquiry drifts into downstream implementation or optimization, return explicitly to the original unresolved question."]
  n230["concept: mu: optional graded support or plausibility over live hypotheses."]
  n231["reference: Hoel, causal emergence, coarse-graining and entropy, raised as related work."]
  n232["goal: Develop a formal compositional calculus of hypothesis-space transformations with a separate warrant layer."]
  n233["claim: Observed conversations underdetermine a person's internal beliefs and update mechanism."]
  n234["claim: IIT is considered only for algorithmic partition, irreducibility and cause-effect-structure machinery, not for consciousness claims."]
  n235["hypothesis: Imagination might contribute an additional way to learn beyond observation."]
  n236["claim: Imagination can generate candidates without independently justifying them."]
  n237["hypothesis: Inductive pattern recognition could initialize a loop through abduction and deduction."]
  n238["claim: Institution theory handles language/model semantics while ATMS-like machinery handles support across assumption environments; they are complementary, not competing."]
  n239["hypothesis: Use an institution-style logical substrate (Sig, Sen, Mod, satisfaction) rather than one overloaded universe variable."]
  n240["reference: Institution theory as an abstract separation of signatures, sentences, models and satisfaction, with signature morphisms for translation."]
  n241["hypothesis: Distributed measurements may support joint relational representations not encoded by any individual sensor."]
  n242["hypothesis: An intermediate repair separates language, model space, live hypotheses and graded support as K=(L,M,H,mu)."]
  n243["hypothesis: An intermediate state proposal K=(Sigma,T,W,rho,E,Q) separates signature, explicit theory, semantic possibilities, support, evidence and query."]
  n244["hypothesis: A pattern can be represented by what remains invariant across specified transformations."]
  n245["claim: An unobserved explanatory variable need not specify the process by which an effect occurs."]
  n246["concept: Latent structure as an unobserved explanatory representation, not necessarily a causal mechanism."]
  n247["method: When the problem appears well trodden, search existing formal literature before inventing new primitives."]
  n248["concept: H: the currently live hypotheses or possibilities within U."]
  n249["claim: Measurement theory can characterize accessible measured variables without by itself characterizing every structure recognized over those measurements."]
  n250["hypothesis: Sensors determine accessible distinctions, while memory enables relations across time."]
  n251["reference: Measurement theory, psychophysics, information theory and computational mechanics as relevant literatures."]
  n252["hypothesis: Relative to a current epistemic state, entailment versus non-entailment is an immediate MECE logical split."]
  n253["goal: Make exhaustiveness and non-overlap provable by construction rather than asserted from a folk taxonomy."]
  n254["claim: MECE is a desired property of the formalism, not the name of the formal object."]
  n255["claim: MECE is a special case of the broader search for a complete nonredundant compositional factorization."]
  n256["method: Force proposed external formalisms through the current meta-model and treat mismatches as evidence of a gap or bad factorization."]
  n257["method: Use established concept-generation formalisms as a stress test of the epistemic meta-model."]
  n258["claim: Meta-strategy is not a separate infinite type hierarchy; a strategy is meta-level relative to reasoning processes or strategies it monitors or controls."]
  n259["concept: Classes of evidence-to-conclusion mappings with shared properties."]
  n260["reference: MMT as a foundation-independent theory/declaration/object/morphism representation and module system."]
  n261["hypothesis: Use an MMT-like theory graph as the concrete formal representation substrate, with LF as a possible foundation inside it."]
  n262["hypothesis: Model-target effects can be represented as an exact subset of language, structure, parameter and state coordinates rather than one exclusive target."]
  n263["claim: Natural learning need not assume a designer; deliberate communication is an additional case."]
  n264["hypothesis: Optimal explanation or design is a further problem for an observer with an uncertain model of other observers."]
  n265["concept: God-view versus embedded-observer perspective."]
  n266["hypothesis: Combine AIF/IAT argument and dialogue structure with provenance and inquiry-transition records."]
  n267["concept: An open node is an unresolved question or epistemic obligation, not just a mentioned topic."]
  n268["claim: Choosing an optimal hypothesis is downstream of first characterizing the kinds of epistemic moves available."]
  n269["claim: Pattern recognition or relational feature extraction from a fully observed finite configuration need not be inductive."]
  n270["reference: Grenander/Brown Pattern Theory as a candidate formal language for generators, configurations, transformations, variation, observation and inference."]
  n271["claim: Pattern Theory supplies broad representational and inferential machinery but does not by itself derive all observer representations from physics."]
  n272["hypothesis: Induction concerns empirical patterns while abduction concerns mechanisms."]
  n273["claim: Persistent epistemic state and the active assumption context of a reasoning episode should be represented separately."]
  n274["hypothesis: Current persistent state: K_Sigma=(N,A,J,lambda,rho), with represented nodes, assumptions, justifications, minimal support environments and optional graded support."]
  n275["concept: Physically realizable pattern recognition, rather than normatively justified recognition."]
  n276["hypothesis: External reality plus partial observation plus logic yields a set of compatible possibilities, not by itself a unique ampliative conclusion."]
  n277["example: From the observed sequence 2, 4, 6, 8 to the expectation 10."]
  n278["claim: Recognizing a sample pattern and licensing its extension beyond the sample are distinct operations."]
  n279["question: What assumptions and criteria support abductive model selection?"]
  n280["question: Can ampliative epistemic moves be represented in a provably MECE or uniquely factorizable way?"]
  n281["question: Does Bayesian updating explain warrant or merely relocate assumptions?"]
  n282["question: Can candidate generation be given a small compositional or uniquely factorizable basis?"]
  n283["question: What is the minimal type system for generated epistemic candidates?"]
  n284["question: What factorization of epistemic state change can be canonical relative to an explicit representation contract?"]
  n285["question: What claims beyond observation can have support without being explanations?"]
  n286["question: What role does generation of candidate constraints play in black-box inference?"]
  n287["question: How can reusable strategies and meta-strategies be instantiated and identified in specific conversations?"]
  n288["question: Which beyond-observation inferences can an embedded observer make?"]
  n289["question: Can exhaustiveness of the proposed inference taxonomy be proved?"]
  n290["question: Which existing ontology captures temporal inquiry evolution and reasoning moves?"]
  n291["question: What general dynamics make explanations and visual presentations effective?"]
  n292["question: What is the space of possible explanatory hypotheses?"]
  n293["question: What general concept subsumes MECE-style primitive analysis when the decomposition is compositional rather than a partition?"]
  n294["question: What should be formalized next after separating state update from candidate generation?"]
  n295["question: What general heuristics or formal scaffolding improve thinking across problems?"]
  n296["question: Can imagination yield knowledge not reducible to inference or introspection?"]
  n297["question: Can the apparent overlap between induction and abduction be explained by a deeper compositional formalism?"]
  n298["question: What assumptions minimally support inductive generalization?"]
  n299["question: Under what conditions does evidence E contain information relevant to a proposition H?"]
  n300["question: Can symmetry, invariance and stability supply primitives of pattern recognition?"]
  n301["question: Is structure a set of constraints, or does emergence and computational irreducibility change the ontology?"]
  n302["question: How is latent structure different from a mechanism?"]
  n303["question: What is the minimal formalization of learning relevant to this inquiry?"]
  n304["question: Is algorithm classification the right level for a simple inference taxonomy?"]
  n305["question: What possible maps take current representations beyond the information currently explicit?"]
  n306["question: Is measurement theory sufficient to explain the observer-to-pattern problem?"]
  n307["question: Can candidate-generation formalisms fit the existing meta-model, and if not, what gap do they expose?"]
  n308["question: Which established metareasoning and reflection formalisms should constrain the strategy/self-application layer before it is frozen?"]
  n309["question: What minimal entities and relations does this inference sketch require?"]
  n310["question: How does an embedded observer learn from a non-designed world?"]
  n311["question: What should be attacked next after the assumption-context refinement?"]
  n312["question: What does higher order mean, and how does it differ from coarse-graining?"]
  n313["question: What, if anything, is fundamental about pattern formation before criteria for useful or optimal abstraction are imposed?"]
  n314["question: What operation makes a relational feature explicit to an observer?"]
  n315["question: Which dimensions of perceptual space are available to a physically embedded observer?"]
  n316["question: Which pattern-recognition mappings can physical embedded observers implement?"]
  n317["question: What established machinery should be checked before freezing the revised meta-model in documentation?"]
  n318["question: How should repeated self-application of the developing reasoning model be represented?"]
  n319["question: Is reframe a primitive operation, or is it masking several different transformations?"]
  n320["question: How does the developing epistemic framework characterize the reasoning occurring in this dialogue itself?"]
  n321["question: Where does canonical factorization live when treated as a reusable cognitive strategy?"]
  n322["question: Do deduction, induction and abduction exhaust learning beyond observation?"]
  n323["question: Should the model treat a theory used in a derivation as a durable commitment, or only as a temporary assumption context?"]
  n324["question: What warrants the standards by which an inference is warranted?"]
  n325["question: What minimal warrant postulates and representation theorems should govern non-entailing commitment changes?"]
  n326["question: How should warrant of warrant be formalized once certainty is removed from the target?"]
  n327["question: Does Wolfram observer theory characterize physically realizable pattern recognizers?"]
  n328["claim: The current query/task belongs to a reasoning episode rather than persistent epistemic state."]
  n329["claim: A mechanism being physically implementable does not establish that it tracks truth."]
  n330["hypothesis: A reasoning episode can be represented as R=(K_Sigma,Gamma,Q)."]
  n331["goal: Map the moves that changed the inquiry, not only the concepts mentioned."]
  n332["claim: Conversations can serve as source-grounded datasets of instantiated reasoning trajectories and proposed strategy episodes."]
  n333["hypothesis: Recognizing a pattern may itself perform the relevant beyond-token representational step."]
  n334["hypothesis: Induction, abduction and deduction can feed back into one another rather than forming a fixed pipeline."]
  n335["hypothesis: Meta-level status is relational: a reasoning episode is meta with respect to the reasoning artifact, strategy or episode it is about."]
  n336["method: Reflective/self-applicative modeling uses the reasoning model to analyze the reasoning process that is constructing the model."]
  n337["claim: Reframe is a dialogue-level macro that may decompose into query, language, theory/support or context transformations."]
  n338["claim: Extracting relations is not necessarily a many-to-one, information-discarding coarse-graining."]
  n339["claim: Any nontrivial target factorization is canonical only relative to a declared representation contract, because structure, parameters and state can be recoded."]
  n340["hypothesis: The relevant map may run between representations rather than raw observations and concepts."]
  n341["hypothesis: Representational lift may be a primitive operation prior to prediction."]
  n342["goal: Anchor the investigation in existing formal theories rather than reinventing terminology."]
  n343["hypothesis: Assume an external reality with sufficiently stable rules."]
  n344["hypothesis: Epistemic state change can be factored, relative to semantic alignment, into representation-space change, additions, deletions and graded-support change."]
  n345["concept: U: the current semantic universe or model space of expressible hypotheses."]
  n346["hypothesis: Stateful computation over an information stream is a general substrate for memory and integration, but does not by itself settle epistemic warrant."]
  n347["hypothesis: A strategy/control layer selects and sequences lower-level reasoning operators; strategy is distinct from primitive operator and candidate artifact."]
  n348["concept: Introduce new predicate/concept vocabulary whose semantics are not merely a definitional abbreviation of the old language."]
  n349["claim: Minimal supporting environments make conditional dependency provenance explicit without warranting the assumptions themselves."]
  n350["hypothesis: Memory can be treated abstractly as integration of measurements distributed across time."]
  n351["hypothesis: A set of premises can be stipulated only for a reasoning branch without becoming a durable belief theory."]
  n352["hypothesis: A white-box reasoning branch selects a temporary assumption environment Gamma subseteq A."]
  n353["claim: The dialogue is performing theoretical model construction under conceptual and literature constraints."]
  n354["claim: Theory graphs remain relevant for modular theory networks but are not required as an additional foundational layer yet."]
  n355["claim: Expression construction, definitional extension and substantive concept invention are distinct operations."]
  n356["claim: Candidate generation, warrant/evaluation and epistemic state update are distinct layers and should not be collapsed into a named inference method."]
  n357["hypothesis: Entailment, projection along stable structure and inversion toward generators may recover three inference forms."]
  n358["hypothesis: Generated epistemic candidates require types such as sentence, assumption, justification, model, signature extension, mapping or query."]
  n359["claim: Typed candidate generation remains the main unresolved formal layer after the assumption-context refinement."]
  n360["goal: Make typed candidate generation concrete using the conversation as a test corpus."]
  n361["goal: Represent the conversation with typed entities and relation roles."]
  n362["claim: The previous U/hypothesis-universe coordinate conflates language, expressibility, model space and live hypotheses."]
  n363["goal: Deliver a coherent first-pass ontology, conversation instantiation, code and project documentation in GitHub."]
  n364["hypothesis: A warrant certificate records explicit assumptions, a claimed guarantee and support connecting the assumptions to that guarantee."]
  n365["concept: Warrant evaluates whether a candidate-to-commitment move has a specified justification or guarantee under explicit assumptions."]
  n366["claim: The inquiry should return from implementation-level pattern and learning theories to the original warrant question."]
  n367["claim: Formal well-formedness, typing or deductive validity does not establish epistemic warrant for generating or accepting a candidate."]
  n368["hypothesis: A stipulated model supports within-model reasoning; an embedded observer must infer the model from observations."]
  n369["reference: Wolfram observer theory and rulial space, raised as a related research direction."]
  n370["goal: Build a persistent cross-conversation map of worldview, questions, dependencies and revisions."]
  n371["relation: challenges"]
  n372["relation: supersedes"]
  n373["relation: answers"]
  n374["relation: motivates"]
  n375["relation: candidate_for"]
  n376["relation: motivates"]
  n377["relation: reframes"]
  n378["relation: motivates"]
  n379["relation: candidate_for"]
  n380["relation: motivates"]
  n381["relation: answers"]
  n382["relation: challenges"]
  n383["relation: candidate_for"]
  n384["relation: reframes"]
  n385["relation: challenges"]
  n386["relation: answers"]
  n387["relation: motivates"]
  n388["relation: reframes"]
  n389["relation: candidate_for"]
  n390["relation: challenges"]
  n391["relation: answers"]
  n392["relation: related_to"]
  n393["relation: challenges"]
  n394["relation: supports"]
  n395["relation: candidate_for"]
  n396["relation: depends_on"]
  n397["relation: motivates"]
  n398["relation: motivates"]
  n399["relation: related_to"]
  n400["relation: related_to"]
  n401["relation: candidate_for"]
  n402["relation: challenges"]
  n403["relation: motivates"]
  n404["relation: reframes"]
  n405["relation: distinguishes"]
  n406["relation: related_to"]
  n407["relation: candidate_for"]
  n408["relation: candidate_for"]
  n409["relation: exemplifies"]
  n410["relation: challenges"]
  n411["relation: exemplifies"]
  n412["relation: motivates"]
  n413["relation: candidate_for"]
  n414["relation: challenges"]
  n415["relation: related_to"]
  n416["relation: answers"]
  n417["relation: candidate_for"]
  n418["relation: motivates"]
  n419["relation: candidate_for"]
  n420["relation: candidate_for"]
  n421["relation: reframes"]
  n422["relation: answers"]
  n423["relation: candidate_for"]
  n424["relation: part_of"]
  n425["relation: candidate_for"]
  n426["relation: candidate_for"]
  n427["relation: part_of"]
  n428["relation: motivates"]
  n429["relation: candidate_for"]
  n430["relation: related_to"]
  n431["relation: related_to"]
  n432["relation: related_to"]
  n433["relation: candidate_for"]
  n434["relation: reframes"]
  n435["relation: challenges"]
  n436["relation: depends_on"]
  n437["relation: supersedes"]
  n438["relation: challenges"]
  n439["relation: related_to"]
  n440["relation: depends_on"]
  n441["relation: depends_on"]
  n442["relation: related_to"]
  n443["relation: challenges"]
  n444["relation: motivates"]
  n445["relation: part_of"]
  n446["relation: part_of"]
  n447["relation: motivates"]
  n448["relation: depends_on"]
  n449["relation: depends_on"]
  n450["relation: related_to"]
  n451["relation: answers"]
  n452["relation: candidate_for"]
  n453["relation: supersedes"]
  n454["relation: challenges"]
  n455["relation: reframes"]
  n456["relation: challenges"]
  n457["relation: related_to"]
  n458["relation: challenges"]
  n459["relation: challenges"]
  n460["relation: related_to"]
  n461["relation: related_to"]
  n462["relation: related_to"]
  n463["relation: related_to"]
  n464["relation: related_to"]
  n465["relation: motivates"]
  n466["relation: candidate_for"]
  n467["relation: related_to"]
  n468["relation: related_to"]
  n469["relation: challenges"]
  n470["relation: reframes"]
  n471["relation: distinguishes"]
  n472["relation: related_to"]
  n473["relation: related_to"]
  n474["relation: motivates"]
  n475["relation: reframes"]
  n476["relation: candidate_for"]
  n477["relation: part_of"]
  n478["relation: candidate_for"]
  n479["relation: depends_on"]
  n480["relation: related_to"]
  n481["relation: motivates"]
  n482["relation: motivates"]
  n483["relation: depends_on"]
  n484["relation: depends_on"]
  n485["relation: challenges"]
  n486["relation: candidate_for"]
  n487["relation: part_of"]
  n488["relation: part_of"]
  n489["relation: part_of"]
  n490["relation: part_of"]
  n491["relation: part_of"]
  n492["relation: answers"]
  n493["relation: related_to"]
  n494["relation: related_to"]
  n495["relation: candidate_for"]
  n496["relation: supports"]
  n497["relation: distinguishes"]
  n498["relation: related_to"]
  n499["relation: reframes"]
  n500["relation: depends_on"]
  n501["relation: related_to"]
  n502["relation: part_of"]
  n503["relation: part_of"]
  n504["relation: depends_on"]
  n505["relation: answers"]
  n506["relation: supports"]
  n507["relation: motivates"]
  n508["relation: candidate_for"]
  n509["relation: motivates"]
  n510["relation: motivates"]
  n511["relation: distinguishes"]
  n512["relation: answers"]
  n513["relation: supports"]
  n514["relation: related_to"]
  n515["relation: motivates"]
  n516["relation: challenges"]
  n517["relation: candidate_for"]
  n518["relation: candidate_for"]
  n519["relation: part_of"]
  n520["relation: candidate_for"]
  n521["relation: part_of"]
  n522["relation: part_of"]
  n523["relation: part_of"]
  n524["relation: supports"]
  n525["relation: depends_on"]
  n526["relation: challenges"]
  n527["relation: answers"]
  n528["relation: supports"]
  n529["relation: supports"]
  n530["relation: motivates"]
  n531["relation: candidate_for"]
  n532["relation: supports"]
  n533["relation: supports"]
  n534["relation: part_of"]
  n535["relation: part_of"]
  n536["relation: supersedes"]
  n537["relation: part_of"]
  n538["relation: part_of"]
  n539["relation: supports"]
  n540["relation: challenges"]
  n541["relation: supports"]
  n542["relation: part_of"]
  n543["relation: part_of"]
  n544["relation: related_to"]
  n545["relation: answers"]
  n546["relation: reframes"]
  n547["relation: candidate_for"]
  n548["relation: related_to"]
  n549["relation: candidate_for"]
  n550["relation: candidate_for"]
  n551["relation: challenges"]
  n552["relation: distinguishes"]
  n553["relation: candidate_for"]
  n554["relation: challenges"]
  n555["relation: candidate_for"]
  n556["relation: candidate_for"]
  n557["relation: part_of"]
  n558["relation: distinguishes"]
  n559["relation: answers"]
  n560["relation: candidate_for"]
  n561["relation: part_of"]
  n562["relation: answers"]
  n563["relation: part_of"]
  n564["relation: supports"]
  n565["relation: answers"]
  n566["relation: related_to"]
  n567["relation: supports"]
  n568["relation: motivates"]
  n569["relation: motivates"]
  n570["relation: exemplifies"]
  n571["relation: exemplifies"]
  n572["relation: about"]
  n573["relation: about"]
  n574["relation: related_to"]
  n575["relation: related_to"]
  n576["relation: related_to"]
  n577["relation: related_to"]
  n578["relation: part_of"]
  n579["relation: part_of"]
  n580["relation: depends_on"]
  n581["relation: depends_on"]
  n0 -->|then| n1
  n0 -->|output| n322
  n1 -->|then| n2
  n1 -->|output| n235
  n2 -->|then| n3
  n2 -->|output| n296
  n3 -->|then| n4
  n3 -->|output| n236
  n4 -->|then| n5
  n4 -->|output| n324
  n5 -->|then| n6
  n5 -->|output| n180
  n6 -->|then| n7
  n6 -->|output| n289
  n7 -->|then| n8
  n7 -->|output| n206
  n8 -->|then| n9
  n8 -->|output| n288
  n9 -->|then| n10
  n9 -->|output| n182
  n9 -->|output| n272
  n10 -->|then| n11
  n10 -->|output| n302
  n11 -->|then| n12
  n11 -->|output| n245
  n12 -->|then| n13
  n12 -->|output| n292
  n13 -->|then| n14
  n13 -->|output| n285
  n14 -->|then| n15
  n14 -->|output| n340
  n15 -->|then| n16
  n15 -->|output| n305
  n16 -->|then| n17
  n16 -->|output| n342
  n17 -->|then| n18
  n17 -->|output| n223
  n18 -->|then| n19
  n18 -->|output| n281
  n19 -->|then| n20
  n19 -->|output| n181
  n20 -->|then| n21
  n20 -->|output| n259
  n21 -->|then| n22
  n21 -->|output| n304
  n22 -->|then| n23
  n22 -->|output| n343
  n23 -->|then| n24
  n23 -->|output| n357
  n24 -->|then| n25
  n24 -->|output| n309
  n25 -->|then| n26
  n25 -->|output| n301
  n26 -->|then| n27
  n26 -->|output| n265
  n27 -->|then| n28
  n27 -->|output| n237
  n28 -->|then| n29
  n28 -->|output| n278
  n29 -->|then| n30
  n29 -->|output| n275
  n29 -->|output| n316
  n30 -->|then| n31
  n30 -->|output| n327
  n31 -->|then| n32
  n31 -->|output| n231
  n32 -->|then| n33
  n32 -->|output| n333
  n33 -->|then| n34
  n33 -->|output| n210
  n33 -->|output| n314
  n34 -->|then| n35
  n34 -->|output| n341
  n35 -->|then| n36
  n35 -->|output| n312
  n36 -->|then| n37
  n36 -->|output| n338
  n37 -->|then| n38
  n37 -->|output| n185
  n38 -->|then| n39
  n38 -->|output| n300
  n39 -->|then| n40
  n39 -->|output| n228
  n40 -->|then| n41
  n40 -->|output| n315
  n41 -->|then| n42
  n41 -->|output| n250
  n42 -->|then| n43
  n42 -->|output| n361
  n43 -->|then| n44
  n43 -->|output| n331
  n44 -->|then| n45
  n44 -->|output| n170
  n45 -->|then| n46
  n45 -->|output| n290
  n46 -->|then| n47
  n46 -->|output| n266
  n47 -->|then| n48
  n47 -->|output| n295
  n48 -->|then| n49
  n48 -->|output| n215
  n49 -->|then| n50
  n49 -->|output| n183
  n50 -->|then| n51
  n50 -->|output| n233
  n51 -->|then| n52
  n51 -->|output| n291
  n52 -->|then| n53
  n52 -->|output| n209
  n53 -->|then| n54
  n53 -->|output| n310
  n54 -->|then| n55
  n54 -->|output| n264
  n55 -->|then| n56
  n55 -->|output| n263
  n56 -->|then| n57
  n56 -->|output| n334
  n57 -->|then| n58
  n57 -->|output| n298
  n58 -->|then| n59
  n58 -->|output| n279
  n59 -->|then| n60
  n59 -->|output| n370
  n60 -->|then| n61
  n60 -->|output| n267
  n61 -->|then| n62
  n61 -->|output| n363
  n62 -->|then| n63
  n62 -->|output| n306
  n63 -->|then| n64
  n63 -->|output| n249
  n64 -->|then| n65
  n64 -->|output| n270
  n65 -->|then| n66
  n65 -->|output| n186
  n66 -->|then| n67
  n66 -->|output| n271
  n67 -->|then| n68
  n67 -->|output| n313
  n68 -->|then| n69
  n68 -->|output| n214
  n69 -->|then| n70
  n69 -->|output| n303
  n70 -->|then| n71
  n70 -->|output| n269
  n71 -->|then| n72
  n71 -->|output| n241
  n72 -->|then| n73
  n72 -->|output| n234
  n73 -->|then| n74
  n73 -->|output| n350
  n74 -->|then| n75
  n74 -->|output| n346
  n75 -->|then| n76
  n75 -->|output| n326
  n76 -->|then| n77
  n76 -->|output| n366
  n77 -->|then| n78
  n77 -->|output| n172
  n78 -->|then| n79
  n78 -->|output| n276
  n79 -->|then| n80
  n79 -->|output| n286
  n80 -->|then| n81
  n80 -->|output| n268
  n81 -->|then| n82
  n81 -->|output| n299
  n82 -->|then| n83
  n82 -->|output| n174
  n83 -->|then| n84
  n83 -->|output| n297
  n84 -->|then| n85
  n84 -->|output| n200
  n85 -->|then| n86
  n85 -->|output| n225
  n86 -->|then| n87
  n86 -->|then| n88
  n86 -->|output| n252
  n87 -->|then| n89
  n87 -->|output| n253
  n88 -->|then| n89
  n88 -->|output| n280
  n89 -->|then| n90
  n89 -->|output| n262
  n90 -->|then| n91
  n90 -->|output| n284
  n91 -->|then| n93
  n91 -->|output| n254
  n92 -->|then| n157
  n92 -->|output| n192
  n93 -->|then| n94
  n93 -->|output| n194
  n94 -->|then| n95
  n94 -->|output| n232
  n95 -->|then| n96
  n95 -->|output| n221
  n96 -->|then| n97
  n96 -->|output| n217
  n97 -->|then| n98
  n97 -->|output| n188
  n97 -->|output| n344
  n97 -->|output| n365
  n98 -->|then| n99
  n98 -->|output| n230
  n98 -->|output| n248
  n98 -->|output| n345
  n99 -->|then| n100
  n99 -->|then| n101
  n99 -->|output| n344
  n100 -->|then| n102
  n100 -->|output| n282
  n101 -->|then| n102
  n101 -->|output| n204
  n102 -->|then| n103
  n102 -->|output| n364
  n103 -->|then| n104
  n103 -->|output| n173
  n104 -->|then| n106
  n104 -->|output| n365
  n105 -->|then| n164
  n105 -->|output| n320
  n106 -->|then| n107
  n106 -->|output| n353
  n107 -->|then| n108
  n107 -->|output| n189
  n108 -->|then| n109
  n108 -->|output| n294
  n109 -->|then| n110
  n109 -->|output| n226
  n110 -->|then| n111
  n110 -->|output| n319
  n111 -->|then| n112
  n111 -->|output| n198
  n112 -->|then| n113
  n112 -->|output| n199
  n113 -->|then| n114
  n113 -->|output| n201
  n114 -->|then| n115
  n114 -->|output| n337
  n115 -->|then| n116
  n115 -->|output| n171
  n116 -->|then| n117
  n116 -->|output| n307
  n117 -->|then| n118
  n117 -->|output| n257
  n118 -->|then| n119
  n118 -->|output| n362
  n119 -->|then| n120
  n119 -->|output| n242
  n120 -->|then| n121
  n120 -->|output| n239
  n120 -->|output| n240
  n121 -->|then| n122
  n121 -->|output| n243
  n122 -->|then| n123
  n122 -->|output| n207
  n122 -->|output| n218
  n122 -->|output| n348
  n122 -->|output| n355
  n123 -->|then| n124
  n123 -->|output| n337
  n124 -->|then| n125
  n124 -->|output| n358
  n125 -->|then| n126
  n125 -->|output| n323
  n126 -->|then| n127
  n126 -->|output| n351
  n127 -->|then| n128
  n127 -->|output| n273
  n128 -->|then| n129
  n128 -->|output| n184
  n129 -->|then| n130
  n129 -->|output| n317
  n130 -->|then| n131
  n130 -->|output| n178
  n131 -->|then| n132
  n131 -->|output| n179
  n132 -->|then| n133
  n132 -->|output| n176
  n132 -->|output| n177
  n133 -->|then| n134
  n133 -->|output| n274
  n134 -->|then| n135
  n134 -->|output| n352
  n135 -->|then| n136
  n135 -->|output| n211
  n136 -->|then| n137
  n136 -->|output| n238
  n137 -->|then| n138
  n137 -->|output| n216
  n138 -->|then| n139
  n138 -->|output| n328
  n139 -->|then| n140
  n139 -->|output| n330
  n140 -->|then| n141
  n140 -->|output| n354
  n141 -->|then| n142
  n141 -->|output| n205
  n142 -->|then| n143
  n142 -->|output| n283
  n142 -->|output| n359
  n143 -->|then| n144
  n143 -->|output| n311
  n144 -->|then| n145
  n144 -->|output| n360
  n145 -->|then| n146
  n145 -->|output| n191
  n146 -->|then| n147
  n146 -->|output| n190
  n147 -->|then| n148
  n147 -->|output| n175
  n148 -->|then| n149
  n148 -->|output| n187
  n149 -->|then| n150
  n149 -->|output| n224
  n150 -->|then| n151
  n150 -->|output| n260
  n150 -->|output| n261
  n151 -->|then| n152
  n151 -->|output| n222
  n152 -->|then| n153
  n152 -->|output| n367
  n153 -->|then| n154
  n153 -->|output| n293
  n154 -->|then| n155
  n154 -->|output| n220
  n155 -->|then| n92
  n155 -->|then| n156
  n155 -->|output| n255
  n156 -->|then| n157
  n156 -->|output| n193
  n157 -->|then| n158
  n157 -->|output| n219
  n158 -->|then| n159
  n158 -->|output| n321
  n159 -->|then| n160
  n159 -->|output| n347
  n160 -->|then| n161
  n160 -->|output| n258
  n161 -->|then| n165
  n161 -->|then| n166
  n161 -->|output| n318
  n162 -->|then| n105
  n162 -->|then| n163
  n162 -->|output| n336
  n163 -->|then| n164
  n163 -->|output| n335
  n164 -->|then| n167
  n164 -->|output| n196
  n165 -->|then| n162
  n165 -->|output| n287
  n166 -->|then| n162
  n166 -->|output| n202
  n167 -->|then| n168
  n167 -->|output| n332
  n168 -->|output| n308
  n169 -->|part| n490
  n170 -->|input| n45
  n170 -->|candidate| n425
  n171 -->|source| n514
  n172 -->|candidate| n466
  n173 -->|premise| n496
  n174 -->|left| n471
  n175 -->|left| n552
  n176 -->|part| n534
  n177 -->|part| n535
  n178 -->|input| n131
  n178 -->|candidate| n531
  n179 -->|input| n132
  n179 -->|input| n133
  n179 -->|input| n136
  n179 -->|premise| n532
  n180 -->|input| n6
  n180 -->|reason| n376
  n181 -->|answer| n391
  n182 -->|input| n18
  n182 -->|candidate| n379
  n183 -->|input| n50
  n183 -->|input| n51
  n184 -->|premise| n529
  n185 -->|input| n38
  n185 -->|input| n65
  n185 -->|candidate| n417
  n185 -->|reason| n418
  n186 -->|new| n453
  n187 -->|candidate| n553
  n188 -->|input| n100
  n188 -->|source| n493
  n188 -->|left| n497
  n189 -->|input| n108
  n189 -->|premise| n506
  n189 -->|reason| n507
  n190 -->|input| n147
  n190 -->|input| n148
  n190 -->|challenger| n551
  n191 -->|candidate| n550
  n192 -->|dependent| n479
  n193 -->|input| n157
  n193 -->|input| n158
  n193 -->|input| n159
  n193 -->|candidate| n560
  n193 -->|part| n563
  n193 -->|part| n578
  n194 -->|input| n94
  n195 -->|challenger| n385
  n195 -->|answer| n386
  n196 -->|premise| n567
  n197 -->|candidate| n375
  n198 -->|input| n113
  n198 -->|input| n122
  n198 -->|left| n511
  n199 -->|input| n113
  n199 -->|input| n122
  n200 -->|source| n473
  n201 -->|answer| n512
  n202 -->|input| n167
  n203 -->|source| n577
  n204 -->|input| n105
  n204 -->|dependent| n504
  n205 -->|input| n140
  n205 -->|input| n143
  n205 -->|input| n161
  n205 -->|answer| n545
  n206 -->|input| n8
  n206 -->|reason| n378
  n207 -->|part| n522
  n208 -->|part| n491
  n209 -->|input| n53
  n209 -->|input| n55
  n209 -->|candidate| n433
  n210 -->|input| n34
  n210 -->|input| n71
  n210 -->|example| n411
  n210 -->|reason| n412
  n211 -->|part| n538
  n212 -->|input| n154
  n212 -->|example| n570
  n212 -->|subject| n572
  n213 -->|example| n571
  n213 -->|subject| n573
  n214 -->|challenger| n456
  n215 -->|input| n49
  n215 -->|candidate| n429
  n215 -->|source| n430
  n215 -->|part| n446
  n216 -->|challenger| n540
  n217 -->|candidate| n486
  n218 -->|part| n521
  n219 -->|part| n561
  n221 -->|input| n96
  n221 -->|challenger| n485
  n222 -->|input| n152
  n222 -->|part| n557
  n223 -->|input| n20
  n223 -->|candidate| n389
  n224 -->|input| n150
  n224 -->|challenger| n554
  n225 -->|input| n86
  n226 -->|input| n110
  n226 -->|input| n115
  n226 -->|input| n116
  n226 -->|input| n124
  n226 -->|candidate| n508
  n227 -->|candidate| n383
  n228 -->|candidate| n419
  n229 -->|source| n576
  n230 -->|input| n99
  n230 -->|part| n489
  n231 -->|candidate| n408
  n232 -->|input| n95
  n232 -->|input| n97
  n232 -->|dependent| n483
  n232 -->|dependent| n484
  n233 -->|source| n431
  n234 -->|source| n461
  n235 -->|input| n2
  n235 -->|input| n3
  n236 -->|new| n372
  n236 -->|answer| n373
  n237 -->|input| n28
  n237 -->|input| n56
  n237 -->|candidate| n401
  n238 -->|premise| n539
  n239 -->|input| n121
  n239 -->|input| n136
  n239 -->|input| n141
  n239 -->|input| n149
  n239 -->|part| n519
  n240 -->|candidate| n518
  n241 -->|input| n72
  n241 -->|input| n73
  n241 -->|source| n460
  n242 -->|input| n120
  n242 -->|candidate| n517
  n243 -->|input| n125
  n243 -->|input| n137
  n243 -->|candidate| n520
  n244 -->|candidate| n420
  n245 -->|input| n12
  n245 -->|answer| n381
  n245 -->|challenger| n382
  n246 -->|input| n10
  n247 -->|source| n574
  n248 -->|input| n99
  n248 -->|part| n488
  n249 -->|input| n64
  n249 -->|answer| n451
  n250 -->|answer| n422
  n251 -->|candidate| n423
  n252 -->|input| n87
  n252 -->|candidate| n476
  n253 -->|input| n88
  n253 -->|input| n89
  n253 -->|input| n90
  n253 -->|input| n153
  n253 -->|input| n155
  n253 -->|part| n477
  n253 -->|reason| n481
  n254 -->|input| n92
  n254 -->|source| n480
  n255 -->|answer| n559
  n256 -->|source| n575
  n258 -->|premise| n564
  n259 -->|input| n21
  n259 -->|input| n80
  n259 -->|source| n392
  n260 -->|candidate| n555
  n261 -->|input| n151
  n261 -->|candidate| n556
  n262 -->|candidate| n478
  n263 -->|new| n437
  n264 -->|input| n56
  n264 -->|dependent| n436
  n265 -->|source| n399
  n266 -->|input| n47
  n266 -->|candidate| n426
  n267 -->|part| n445
  n268 -->|challenger| n469
  n269 -->|challenger| n458
  n269 -->|challenger| n459
  n270 -->|input| n66
  n270 -->|candidate| n452
  n271 -->|input| n67
  n271 -->|challenger| n454
  n272 -->|reason| n380
  n273 -->|input| n128
  n273 -->|premise| n528
  n274 -->|input| n134
  n274 -->|input| n138
  n274 -->|input| n139
  n274 -->|input| n141
  n274 -->|new| n536
  n274 -->|part| n542
  n275 -->|reason| n403
  n275 -->|left| n405
  n276 -->|input| n79
  n276 -->|source| n467
  n277 -->|example| n409
  n278 -->|input| n29
  n278 -->|input| n32
  n278 -->|challenger| n402
  n279 -->|input| n59
  n280 -->|original| n499
  n281 -->|input| n19
  n281 -->|challenger| n390
  n282 -->|input| n101
  n282 -->|dependent| n500
  n282 -->|original| n546
  n284 -->|input| n91
  n285 -->|input| n14
  n285 -->|original| n388
  n286 -->|source| n468
  n287 -->|input| n166
  n287 -->|reason| n568
  n288 -->|input| n9
  n288 -->|input| n27
  n289 -->|input| n7
  n289 -->|input| n23
  n289 -->|input| n58
  n289 -->|input| n85
  n289 -->|dependent| n440
  n289 -->|dependent| n441
  n289 -->|original| n475
  n290 -->|input| n46
  n290 -->|reason| n428
  n291 -->|input| n52
  n291 -->|source| n432
  n291 -->|original| n434
  n292 -->|input| n13
  n292 -->|original| n384
  n293 -->|input| n156
  n294 -->|input| n109
  n295 -->|input| n48
  n296 -->|input| n3
  n296 -->|challenger| n371
  n297 -->|input| n84
  n297 -->|input| n85
  n297 -->|source| n472
  n297 -->|reason| n474
  n298 -->|input| n59
  n298 -->|source| n442
  n298 -->|challenger| n443
  n300 -->|input| n39
  n301 -->|input| n26
  n302 -->|input| n11
  n303 -->|source| n457
  n304 -->|input| n22
  n304 -->|challenger| n393
  n305 -->|input| n16
  n305 -->|input| n17
  n305 -->|original| n404
  n306 -->|input| n63
  n306 -->|source| n450
  n307 -->|input| n117
  n307 -->|input| n129
  n307 -->|reason| n515
  n308 -->|dependent| n580
  n308 -->|dependent| n581
  n309 -->|input| n25
  n309 -->|reason| n398
  n310 -->|input| n54
  n310 -->|input| n69
  n310 -->|challenger| n435
  n311 -->|input| n144
  n312 -->|input| n36
  n312 -->|challenger| n414
  n313 -->|input| n68
  n313 -->|input| n75
  n314 -->|input| n37
  n314 -->|input| n40
  n314 -->|original| n421
  n314 -->|original| n455
  n315 -->|input| n41
  n315 -->|input| n42
  n315 -->|input| n62
  n316 -->|input| n30
  n316 -->|input| n31
  n317 -->|input| n130
  n317 -->|reason| n530
  n318 -->|input| n162
  n319 -->|input| n111
  n319 -->|input| n112
  n319 -->|input| n114
  n319 -->|reason| n509
  n319 -->|reason| n510
  n320 -->|input| n106
  n322 -->|input| n1
  n322 -->|input| n4
  n322 -->|input| n8
  n322 -->|input| n83
  n322 -->|reason| n374
  n322 -->|original| n377
  n323 -->|input| n126
  n323 -->|challenger| n526
  n324 -->|input| n5
  n324 -->|input| n93
  n324 -->|reason| n482
  n325 -->|source| n501
  n326 -->|input| n76
  n326 -->|input| n81
  n326 -->|source| n464
  n326 -->|original| n470
  n327 -->|source| n406
  n328 -->|input| n139
  n328 -->|premise| n541
  n330 -->|input| n141
  n330 -->|part| n543
  n331 -->|input| n44
  n331 -->|input| n59
  n331 -->|input| n61
  n331 -->|part| n427
  n331 -->|reason| n444
  n332 -->|reason| n569
  n333 -->|input| n33
  n333 -->|input| n70
  n333 -->|challenger| n410
  n334 -->|challenger| n438
  n334 -->|source| n439
  n335 -->|input| n164
  n335 -->|input| n168
  n335 -->|source| n566
  n336 -->|input| n163
  n336 -->|input| n165
  n336 -->|answer| n565
  n336 -->|part| n579
  n337 -->|input| n123
  n337 -->|premise| n513
  n338 -->|source| n415
  n338 -->|answer| n416
  n340 -->|input| n15
  n340 -->|reason| n387
  n341 -->|input| n35
  n341 -->|input| n36
  n341 -->|candidate| n413
  n342 -->|input| n17
  n343 -->|input| n23
  n343 -->|premise| n394
  n344 -->|input| n98
  n344 -->|input| n101
  n344 -->|answer| n492
  n344 -->|part| n502
  n345 -->|input| n99
  n345 -->|input| n118
  n345 -->|part| n487
  n346 -->|source| n463
  n347 -->|input| n160
  n347 -->|input| n168
  n347 -->|answer| n562
  n348 -->|part| n523
  n349 -->|premise| n533
  n350 -->|input| n74
  n350 -->|source| n462
  n351 -->|input| n127
  n351 -->|answer| n527
  n352 -->|input| n135
  n352 -->|input| n139
  n352 -->|part| n537
  n353 -->|input| n107
  n353 -->|answer| n505
  n354 -->|source| n544
  n355 -->|premise| n524
  n356 -->|input| n101
  n356 -->|source| n498
  n356 -->|part| n503
  n357 -->|input| n24
  n357 -->|input| n57
  n357 -->|candidate| n395
  n357 -->|dependent| n396
  n357 -->|reason| n397
  n358 -->|input| n142
  n358 -->|input| n146
  n358 -->|dependent| n525
  n359 -->|candidate| n547
  n359 -->|source| n548
  n360 -->|input| n145
  n360 -->|candidate| n549
  n361 -->|input| n43
  n361 -->|part| n424
  n362 -->|input| n119
  n362 -->|challenger| n516
  n363 -->|dependent| n448
  n363 -->|dependent| n449
  n364 -->|input| n103
  n364 -->|candidate| n495
  n365 -->|input| n102
  n365 -->|input| n104
  n365 -->|source| n494
  n366 -->|input| n77
  n366 -->|reason| n465
  n367 -->|left| n558
  n368 -->|input| n78
  n368 -->|input| n82
  n368 -->|source| n400
  n369 -->|candidate| n407
  n370 -->|input| n60
  n370 -->|input| n61
  n370 -->|reason| n447
  n371 -->|target| n235
  n372 -->|old| n235
  n373 -->|question| n296
  n374 -->|result| n324
  n375 -->|problem| n324
  n376 -->|result| n289
  n377 -->|replacement| n288
  n378 -->|result| n288
  n379 -->|problem| n288
  n380 -->|result| n302
  n381 -->|question| n302
  n382 -->|target| n272
  n383 -->|problem| n292
  n384 -->|replacement| n285
  n385 -->|target| n227
  n386 -->|question| n285
  n387 -->|result| n305
  n388 -->|replacement| n305
  n389 -->|problem| n305
  n390 -->|target| n182
  n391 -->|question| n281
  n392 -->|target| n223
  n393 -->|target| n259
  n394 -->|conclusion| n357
  n395 -->|problem| n289
  n396 -->|prerequisite| n343
  n397 -->|result| n309
  n398 -->|result| n301
  n399 -->|target| n301
  n400 -->|target| n265
  n401 -->|problem| n288
  n402 -->|target| n237
  n403 -->|result| n316
  n404 -->|replacement| n316
  n405 -->|right| n329
  n406 -->|target| n316
  n407 -->|problem| n316
  n408 -->|problem| n316
  n409 -->|general| n278
  n410 -->|target| n278
  n411 -->|general| n333
  n412 -->|result| n314
  n413 -->|problem| n314
  n414 -->|target| n341
  n415 -->|target| n341
  n416 -->|question| n312
  n417 -->|problem| n314
  n418 -->|result| n300
  n419 -->|problem| n300
  n420 -->|problem| n314
  n421 -->|replacement| n315
  n422 -->|question| n315
  n423 -->|problem| n315
  n424 -->|whole| n331
  n425 -->|problem| n290
  n426 -->|problem| n290
  n427 -->|whole| n266
  n428 -->|result| n295
  n429 -->|problem| n295
  n430 -->|target| n183
  n431 -->|target| n183
  n432 -->|target| n183
  n433 -->|problem| n291
  n434 -->|replacement| n310
  n435 -->|target| n209
  n436 -->|prerequisite| n310
  n437 -->|old| n209
  n438 -->|target| n237
  n439 -->|target| n288
  n440 -->|prerequisite| n298
  n441 -->|prerequisite| n279
  n442 -->|target| n315
  n443 -->|target| n357
  n444 -->|result| n370
  n445 -->|whole| n370
  n446 -->|whole| n370
  n447 -->|result| n363
  n448 -->|prerequisite| n331
  n449 -->|prerequisite| n290
  n450 -->|target| n315
  n451 -->|question| n306
  n452 -->|problem| n314
  n453 -->|old| n185
  n454 -->|target| n270
  n455 -->|replacement| n313
  n456 -->|target| n244
  n457 -->|target| n310
  n458 -->|target| n333
  n459 -->|target| n237
  n460 -->|target| n210
  n461 -->|target| n241
  n462 -->|target| n241
  n463 -->|target| n350
  n464 -->|target| n324
  n465 -->|result| n326
  n466 -->|problem| n326
  n467 -->|target| n368
  n468 -->|target| n298
  n469 -->|target| n259
  n470 -->|replacement| n299
  n471 -->|right| n368
  n472 -->|target| n322
  n473 -->|target| n297
  n474 -->|result| n225
  n475 -->|replacement| n280
  n476 -->|problem| n280
  n477 -->|whole| n225
  n478 -->|problem| n280
  n479 -->|prerequisite| n339
  n480 -->|target| n253
  n481 -->|result| n192
  n482 -->|result| n194
  n483 -->|prerequisite| n194
  n484 -->|prerequisite| n192
  n485 -->|target| n259
  n486 -->|problem| n284
  n487 -->|whole| n344
  n488 -->|whole| n344
  n489 -->|whole| n344
  n490 -->|whole| n344
  n491 -->|whole| n344
  n492 -->|question| n284
  n493 -->|target| n297
  n494 -->|target| n326
  n495 -->|problem| n325
  n496 -->|conclusion| n364
  n497 -->|right| n365
  n498 -->|target| n344
  n499 -->|replacement| n282
  n500 -->|prerequisite| n188
  n501 -->|target| n324
  n502 -->|whole| n204
  n503 -->|whole| n204
  n504 -->|prerequisite| n282
  n505 -->|question| n320
  n506 -->|conclusion| n353
  n507 -->|result| n294
  n508 -->|problem| n294
  n509 -->|result| n198
  n510 -->|result| n199
  n511 -->|right| n199
  n512 -->|question| n319
  n513 -->|conclusion| n201
  n514 -->|target| n226
  n515 -->|result| n257
  n516 -->|target| n345
  n517 -->|problem| n307
  n518 -->|problem| n307
  n519 -->|whole| n205
  n520 -->|problem| n307
  n521 -->|whole| n355
  n522 -->|whole| n355
  n523 -->|whole| n355
  n524 -->|conclusion| n337
  n525 -->|prerequisite| n239
  n526 -->|target| n243
  n527 -->|question| n323
  n528 -->|conclusion| n351
  n529 -->|conclusion| n273
  n530 -->|result| n178
  n531 -->|problem| n323
  n532 -->|conclusion| n273
  n533 -->|conclusion| n179
  n534 -->|whole| n179
  n535 -->|whole| n179
  n536 -->|old| n243
  n537 -->|whole| n330
  n538 -->|whole| n330
  n539 -->|conclusion| n205
  n540 -->|target| n243
  n541 -->|conclusion| n330
  n542 -->|whole| n205
  n543 -->|whole| n205
  n544 -->|target| n205
  n545 -->|question| n307
  n546 -->|replacement| n283
  n547 -->|problem| n283
  n548 -->|target| n325
  n549 -->|problem| n311
  n550 -->|problem| n360
  n551 -->|target| n358
  n552 -->|right| n358
  n553 -->|problem| n283
  n554 -->|target| n239
  n555 -->|problem| n283
  n556 -->|problem| n307
  n557 -->|whole| n261
  n558 -->|right| n222
  n559 -->|question| n293
  n560 -->|problem| n293
  n561 -->|whole| n193
  n562 -->|question| n321
  n563 -->|whole| n347
  n564 -->|conclusion| n347
  n565 -->|question| n318
  n566 -->|target| n336
  n567 -->|conclusion| n335
  n568 -->|result| n202
  n569 -->|result| n202
  n570 -->|general| n193
  n571 -->|general| n336
  n572 -->|object| n205
  n573 -->|object| n205
  n574 -->|target| n342
  n575 -->|target| n257
  n576 -->|target| n326
  n577 -->|target| n289
  n578 -->|whole| n202
  n579 -->|whole| n202
  n580 -->|prerequisite| n347
  n581 -->|prerequisite| n335
```
