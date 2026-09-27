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
  n143["concept: A: hypotheses newly live after semantic alignment of the previous state."]
  n144["reference: AIF+ and Inference Anchoring Theory as candidate dialogue/argument representations."]
  n145["hypothesis: Candidate generation may be better modeled as an algebra over languages, expressions, theories and queries than as a short folk list of cognitive verbs."]
  n146["hypothesis: Ampliative warrant requires assumptions or constraints beyond bare logical entailment from finite evidence."]
  n147["claim: Nontrivial ampliative guarantees require restrictions on the admissible possible-world or problem class."]
  n148["claim: For an embedded observer, constraints used in derivations should be described as assumed rather than known."]
  n149["concept: An ATMS-style environment is a consistent set of assumptions under which consequences can be evaluated."]
  n150["concept: A label records minimal consistent assumption environments sufficient to support a datum."]
  n151["reference: de Kleer's Assumption-based Truth Maintenance System as a precedent for multiple simultaneous assumption environments and dependency labels."]
  n152["hypothesis: Persistent epistemic organization can be represented as assumptions, explicit justifications and minimal support environments rather than one committed theory."]
  n153["goal: Derive a taxonomy from modest explicit assumptions rather than simply assuming it."]
  n154["claim: Conditionalization presupposes a hypothesis space, likelihoods and priors; it does not ground all of them."]
  n155["method: A Bayesian or causal DAG as a candidate representation of inferential relationships."]
  n156["hypothesis: Belief change depends on existing representations and an agent-specific updating process."]
  n157["claim: The black-box state maintains alternatives; a white-box move temporarily stipulates one context and inspects its consequences."]
  n158["reference: Bronstein and geometric deep learning as a candidate framework for learning primitives."]
  n159["claim: Bronstein/geometric deep learning should not be part of the foundational spine merely because it was suggested earlier."]
  n160["concept: Candidate generation maps current state and evidence to candidate propositions, models or structures before evaluation and commitment."]
  n161["claim: The dialogue itself can serve as an adversarial test case for candidate-generation operators."]
  n162["goal: Construct a canonical factorization of epistemic transitions relative to an explicit semantic representation contract."]
  n163["goal: Classify hypothesis and model moves without requiring certainty or strong knowledge claims."]
  n164["claim: Explanations are only a subset of claims that go beyond observations."]
  n165["claim: Internal coherence alone does not establish correspondence with reality."]
  n166["concept: Construction of a new expression or concept from constructors and vocabulary already available in the current language."]
  n167["concept: Introduction of genuinely new conceptual or predicate vocabulary not already definable in the current language."]
  n168["claim: A constraint is broader than an explanation or mechanism; empirical, causal and explanatory commitments can occupy different levels."]
  n169["claim: Concept construction inside an existing language and substantive concept invention are different problems."]
  n170["hypothesis: Current endpoint: factor epistemic state change relative to a representation contract, keep warrant separate, and treat candidate-generation factorization as open."]
  n171["hypothesis: Current architecture combines an institution-style logical substrate, ATMS-inspired persistent support state, temporary assumption environment, and external query."]
  n172["claim: Deduction and inference by an embedded empirical observer have different dependencies."]
  n173["concept: Extend a signature with a fresh name explicitly defined from old-language expressions, ideally conservatively."]
  n174["concept: D: previously live aligned hypotheses no longer live after the update."]
  n175["hypothesis: Treat communication as a designed transformation of a recipient representation."]
  n176["example: Recognizing spatial separation of black and white dots from individual positions and colors."]
  n177["hypothesis: Conditional deductive context is the closure C(Gamma)=Cl_J(Gamma) of a temporary assumption environment under justifications."]
  n178["claim: Equivalence under predictive or causal consequence is better treated as a relevance or model-selection criterion than as the ontology of all patterns."]
  n179["goal: Evaluate reasoning-move trajectories and learn which strategies work under which conditions."]
  n180["claim: Evidence need not be a privileged top-level coordinate; reports and observations can be typed provenance-bearing nodes with their own dependencies."]
  n181["hypothesis: For a fixed hypothesis universe, hard live-set changes reduce to additions and deletions; preserve, restrict, expand and replace are derived cases."]
  n182["concept: Build an expression using constructors already licensed by the current language."]
  n183["claim: The earlier five proposed move types were not a minimal state-update basis."]
  n184["method: Model an inference method as a function from evidence histories to hypotheses."]
  n185["goal: Construct a coherent formalism for epistemic moves without preserving historical inference labels when they obscure the structure."]
  n186["goal: Formalize candidate generation using the dialogue as a test case while importing established operators where possible."]
  n187["hypothesis: Generative structure could be the umbrella object for the inquiry."]
  n188["method: Symmetry, deformation stability and scale separation/locality as geometric learning priors."]
  n189["concept: mu: optional graded support or plausibility over live hypotheses."]
  n190["reference: Hoel, causal emergence, coarse-graining and entropy, raised as related work."]
  n191["goal: Develop a formal compositional calculus of hypothesis-space transformations with a separate warrant layer."]
  n192["claim: Observed conversations underdetermine a person's internal beliefs and update mechanism."]
  n193["claim: IIT is considered only for algorithmic partition, irreducibility and cause-effect-structure machinery, not for consciousness claims."]
  n194["hypothesis: Imagination might contribute an additional way to learn beyond observation."]
  n195["claim: Imagination can generate candidates without independently justifying them."]
  n196["hypothesis: Inductive pattern recognition could initialize a loop through abduction and deduction."]
  n197["claim: Institution theory handles language/model semantics while ATMS-like machinery handles support across assumption environments; they are complementary, not competing."]
  n198["hypothesis: Use an institution-style logical substrate (Sig, Sen, Mod, satisfaction) rather than one overloaded universe variable."]
  n199["reference: Institution theory as an abstract separation of signatures, sentences, models and satisfaction, with signature morphisms for translation."]
  n200["hypothesis: Distributed measurements may support joint relational representations not encoded by any individual sensor."]
  n201["hypothesis: An intermediate repair separates language, model space, live hypotheses and graded support as K=(L,M,H,mu)."]
  n202["hypothesis: An intermediate state proposal K=(Sigma,T,W,rho,E,Q) separates signature, explicit theory, semantic possibilities, support, evidence and query."]
  n203["hypothesis: A pattern can be represented by what remains invariant across specified transformations."]
  n204["claim: An unobserved explanatory variable need not specify the process by which an effect occurs."]
  n205["concept: Latent structure as an unobserved explanatory representation, not necessarily a causal mechanism."]
  n206["concept: H: the currently live hypotheses or possibilities within U."]
  n207["claim: Measurement theory can characterize accessible measured variables without by itself characterizing every structure recognized over those measurements."]
  n208["hypothesis: Sensors determine accessible distinctions, while memory enables relations across time."]
  n209["reference: Measurement theory, psychophysics, information theory and computational mechanics as relevant literatures."]
  n210["hypothesis: Relative to a current epistemic state, entailment versus non-entailment is an immediate MECE logical split."]
  n211["goal: Make exhaustiveness and non-overlap provable by construction rather than asserted from a folk taxonomy."]
  n212["claim: MECE is a desired property of the formalism, not the name of the formal object."]
  n213["method: Use established concept-generation formalisms as a stress test of the epistemic meta-model."]
  n214["concept: Classes of evidence-to-conclusion mappings with shared properties."]
  n215["hypothesis: Model-target effects can be represented as an exact subset of language, structure, parameter and state coordinates rather than one exclusive target."]
  n216["claim: Natural learning need not assume a designer; deliberate communication is an additional case."]
  n217["hypothesis: Optimal explanation or design is a further problem for an observer with an uncertain model of other observers."]
  n218["concept: God-view versus embedded-observer perspective."]
  n219["hypothesis: Combine AIF/IAT argument and dialogue structure with provenance and inquiry-transition records."]
  n220["concept: An open node is an unresolved question or epistemic obligation, not just a mentioned topic."]
  n221["claim: Choosing an optimal hypothesis is downstream of first characterizing the kinds of epistemic moves available."]
  n222["claim: Pattern recognition or relational feature extraction from a fully observed finite configuration need not be inductive."]
  n223["reference: Grenander/Brown Pattern Theory as a candidate formal language for generators, configurations, transformations, variation, observation and inference."]
  n224["claim: Pattern Theory supplies broad representational and inferential machinery but does not by itself derive all observer representations from physics."]
  n225["hypothesis: Induction concerns empirical patterns while abduction concerns mechanisms."]
  n226["claim: Persistent epistemic state and the active assumption context of a reasoning episode should be represented separately."]
  n227["hypothesis: Current persistent state: K_Sigma=(N,A,J,lambda,rho), with represented nodes, assumptions, justifications, minimal support environments and optional graded support."]
  n228["concept: Physically realizable pattern recognition, rather than normatively justified recognition."]
  n229["hypothesis: External reality plus partial observation plus logic yields a set of compatible possibilities, not by itself a unique ampliative conclusion."]
  n230["example: From the observed sequence 2, 4, 6, 8 to the expectation 10."]
  n231["claim: Recognizing a sample pattern and licensing its extension beyond the sample are distinct operations."]
  n232["question: What assumptions and criteria support abductive model selection?"]
  n233["question: Can ampliative epistemic moves be represented in a provably MECE or uniquely factorizable way?"]
  n234["question: Does Bayesian updating explain warrant or merely relocate assumptions?"]
  n235["question: Can candidate generation be given a small compositional or uniquely factorizable basis?"]
  n236["question: What is the minimal type system for generated epistemic candidates?"]
  n237["question: What factorization of epistemic state change can be canonical relative to an explicit representation contract?"]
  n238["question: What claims beyond observation can have support without being explanations?"]
  n239["question: What role does generation of candidate constraints play in black-box inference?"]
  n240["question: Which beyond-observation inferences can an embedded observer make?"]
  n241["question: Can exhaustiveness of the proposed inference taxonomy be proved?"]
  n242["question: Which existing ontology captures temporal inquiry evolution and reasoning moves?"]
  n243["question: What general dynamics make explanations and visual presentations effective?"]
  n244["question: What is the space of possible explanatory hypotheses?"]
  n245["question: What should be formalized next after separating state update from candidate generation?"]
  n246["question: What general heuristics or formal scaffolding improve thinking across problems?"]
  n247["question: Can imagination yield knowledge not reducible to inference or introspection?"]
  n248["question: Can the apparent overlap between induction and abduction be explained by a deeper compositional formalism?"]
  n249["question: What assumptions minimally support inductive generalization?"]
  n250["question: Under what conditions does evidence E contain information relevant to a proposition H?"]
  n251["question: Can symmetry, invariance and stability supply primitives of pattern recognition?"]
  n252["question: Is structure a set of constraints, or does emergence and computational irreducibility change the ontology?"]
  n253["question: How is latent structure different from a mechanism?"]
  n254["question: What is the minimal formalization of learning relevant to this inquiry?"]
  n255["question: Is algorithm classification the right level for a simple inference taxonomy?"]
  n256["question: What possible maps take current representations beyond the information currently explicit?"]
  n257["question: Is measurement theory sufficient to explain the observer-to-pattern problem?"]
  n258["question: Can candidate-generation formalisms fit the existing meta-model, and if not, what gap do they expose?"]
  n259["question: What minimal entities and relations does this inference sketch require?"]
  n260["question: How does an embedded observer learn from a non-designed world?"]
  n261["question: What does higher order mean, and how does it differ from coarse-graining?"]
  n262["question: What, if anything, is fundamental about pattern formation before criteria for useful or optimal abstraction are imposed?"]
  n263["question: What operation makes a relational feature explicit to an observer?"]
  n264["question: Which dimensions of perceptual space are available to a physically embedded observer?"]
  n265["question: Which pattern-recognition mappings can physical embedded observers implement?"]
  n266["question: What established machinery should be checked before freezing the revised meta-model in documentation?"]
  n267["question: Is reframe a primitive operation, or is it masking several different transformations?"]
  n268["question: How does the developing epistemic framework characterize the reasoning occurring in this dialogue itself?"]
  n269["question: Do deduction, induction and abduction exhaust learning beyond observation?"]
  n270["question: Should the model treat a theory used in a derivation as a durable commitment, or only as a temporary assumption context?"]
  n271["question: What warrants the standards by which an inference is warranted?"]
  n272["question: What minimal warrant postulates and representation theorems should govern non-entailing commitment changes?"]
  n273["question: How should warrant of warrant be formalized once certainty is removed from the target?"]
  n274["question: Does Wolfram observer theory characterize physically realizable pattern recognizers?"]
  n275["claim: The current query/task belongs to a reasoning episode rather than persistent epistemic state."]
  n276["claim: A mechanism being physically implementable does not establish that it tracks truth."]
  n277["hypothesis: A reasoning episode can be represented as R=(K_Sigma,Gamma,Q)."]
  n278["goal: Map the moves that changed the inquiry, not only the concepts mentioned."]
  n279["hypothesis: Recognizing a pattern may itself perform the relevant beyond-token representational step."]
  n280["hypothesis: Induction, abduction and deduction can feed back into one another rather than forming a fixed pipeline."]
  n281["claim: Reframe is a dialogue-level macro that may decompose into query, language, theory/support or context transformations."]
  n282["claim: Extracting relations is not necessarily a many-to-one, information-discarding coarse-graining."]
  n283["claim: Any nontrivial target factorization is canonical only relative to a declared representation contract, because structure, parameters and state can be recoded."]
  n284["hypothesis: The relevant map may run between representations rather than raw observations and concepts."]
  n285["hypothesis: Representational lift may be a primitive operation prior to prediction."]
  n286["goal: Anchor the investigation in existing formal theories rather than reinventing terminology."]
  n287["hypothesis: Assume an external reality with sufficiently stable rules."]
  n288["hypothesis: Epistemic state change can be factored, relative to semantic alignment, into representation-space change, additions, deletions and graded-support change."]
  n289["concept: U: the current semantic universe or model space of expressible hypotheses."]
  n290["hypothesis: Stateful computation over an information stream is a general substrate for memory and integration, but does not by itself settle epistemic warrant."]
  n291["concept: Introduce new predicate/concept vocabulary whose semantics are not merely a definitional abbreviation of the old language."]
  n292["claim: Minimal supporting environments make conditional dependency provenance explicit without warranting the assumptions themselves."]
  n293["hypothesis: Memory can be treated abstractly as integration of measurements distributed across time."]
  n294["hypothesis: A set of premises can be stipulated only for a reasoning branch without becoming a durable belief theory."]
  n295["hypothesis: A white-box reasoning branch selects a temporary assumption environment Gamma subseteq A."]
  n296["claim: The dialogue is performing theoretical model construction under conceptual and literature constraints."]
  n297["claim: Theory graphs remain relevant for modular theory networks but are not required as an additional foundational layer yet."]
  n298["claim: Expression construction, definitional extension and substantive concept invention are distinct operations."]
  n299["claim: Candidate generation, warrant/evaluation and epistemic state update are distinct layers and should not be collapsed into a named inference method."]
  n300["hypothesis: Entailment, projection along stable structure and inversion toward generators may recover three inference forms."]
  n301["hypothesis: Generated epistemic candidates require types such as sentence, assumption, justification, model, signature extension, mapping or query."]
  n302["claim: Typed candidate generation remains the main unresolved formal layer after the assumption-context refinement."]
  n303["goal: Represent the conversation with typed entities and relation roles."]
  n304["claim: The previous U/hypothesis-universe coordinate conflates language, expressibility, model space and live hypotheses."]
  n305["goal: Deliver a coherent first-pass ontology, conversation instantiation, code and project documentation in GitHub."]
  n306["hypothesis: A warrant certificate records explicit assumptions, a claimed guarantee and support connecting the assumptions to that guarantee."]
  n307["concept: Warrant evaluates whether a candidate-to-commitment move has a specified justification or guarantee under explicit assumptions."]
  n308["claim: The inquiry should return from implementation-level pattern and learning theories to the original warrant question."]
  n309["hypothesis: A stipulated model supports within-model reasoning; an embedded observer must infer the model from observations."]
  n310["reference: Wolfram observer theory and rulial space, raised as a related research direction."]
  n311["goal: Build a persistent cross-conversation map of worldview, questions, dependencies and revisions."]
  n312["relation: challenges"]
  n313["relation: supersedes"]
  n314["relation: answers"]
  n315["relation: motivates"]
  n316["relation: candidate_for"]
  n317["relation: motivates"]
  n318["relation: reframes"]
  n319["relation: motivates"]
  n320["relation: candidate_for"]
  n321["relation: motivates"]
  n322["relation: answers"]
  n323["relation: challenges"]
  n324["relation: candidate_for"]
  n325["relation: reframes"]
  n326["relation: challenges"]
  n327["relation: answers"]
  n328["relation: motivates"]
  n329["relation: reframes"]
  n330["relation: candidate_for"]
  n331["relation: challenges"]
  n332["relation: answers"]
  n333["relation: related_to"]
  n334["relation: challenges"]
  n335["relation: supports"]
  n336["relation: candidate_for"]
  n337["relation: depends_on"]
  n338["relation: motivates"]
  n339["relation: motivates"]
  n340["relation: related_to"]
  n341["relation: related_to"]
  n342["relation: candidate_for"]
  n343["relation: challenges"]
  n344["relation: motivates"]
  n345["relation: reframes"]
  n346["relation: distinguishes"]
  n347["relation: related_to"]
  n348["relation: candidate_for"]
  n349["relation: candidate_for"]
  n350["relation: exemplifies"]
  n351["relation: challenges"]
  n352["relation: exemplifies"]
  n353["relation: motivates"]
  n354["relation: candidate_for"]
  n355["relation: challenges"]
  n356["relation: related_to"]
  n357["relation: answers"]
  n358["relation: candidate_for"]
  n359["relation: motivates"]
  n360["relation: candidate_for"]
  n361["relation: candidate_for"]
  n362["relation: reframes"]
  n363["relation: answers"]
  n364["relation: candidate_for"]
  n365["relation: part_of"]
  n366["relation: candidate_for"]
  n367["relation: candidate_for"]
  n368["relation: part_of"]
  n369["relation: motivates"]
  n370["relation: candidate_for"]
  n371["relation: related_to"]
  n372["relation: related_to"]
  n373["relation: related_to"]
  n374["relation: candidate_for"]
  n375["relation: reframes"]
  n376["relation: challenges"]
  n377["relation: depends_on"]
  n378["relation: supersedes"]
  n379["relation: challenges"]
  n380["relation: related_to"]
  n381["relation: depends_on"]
  n382["relation: depends_on"]
  n383["relation: related_to"]
  n384["relation: challenges"]
  n385["relation: motivates"]
  n386["relation: part_of"]
  n387["relation: part_of"]
  n388["relation: motivates"]
  n389["relation: depends_on"]
  n390["relation: depends_on"]
  n391["relation: related_to"]
  n392["relation: answers"]
  n393["relation: candidate_for"]
  n394["relation: supersedes"]
  n395["relation: challenges"]
  n396["relation: reframes"]
  n397["relation: challenges"]
  n398["relation: related_to"]
  n399["relation: challenges"]
  n400["relation: challenges"]
  n401["relation: related_to"]
  n402["relation: related_to"]
  n403["relation: related_to"]
  n404["relation: related_to"]
  n405["relation: related_to"]
  n406["relation: motivates"]
  n407["relation: candidate_for"]
  n408["relation: related_to"]
  n409["relation: related_to"]
  n410["relation: challenges"]
  n411["relation: reframes"]
  n412["relation: distinguishes"]
  n413["relation: related_to"]
  n414["relation: related_to"]
  n415["relation: motivates"]
  n416["relation: reframes"]
  n417["relation: candidate_for"]
  n418["relation: part_of"]
  n419["relation: candidate_for"]
  n420["relation: depends_on"]
  n421["relation: related_to"]
  n422["relation: motivates"]
  n423["relation: motivates"]
  n424["relation: depends_on"]
  n425["relation: depends_on"]
  n426["relation: challenges"]
  n427["relation: candidate_for"]
  n428["relation: part_of"]
  n429["relation: part_of"]
  n430["relation: part_of"]
  n431["relation: part_of"]
  n432["relation: part_of"]
  n433["relation: answers"]
  n434["relation: related_to"]
  n435["relation: related_to"]
  n436["relation: candidate_for"]
  n437["relation: supports"]
  n438["relation: distinguishes"]
  n439["relation: related_to"]
  n440["relation: reframes"]
  n441["relation: depends_on"]
  n442["relation: related_to"]
  n443["relation: part_of"]
  n444["relation: part_of"]
  n445["relation: depends_on"]
  n446["relation: answers"]
  n447["relation: supports"]
  n448["relation: motivates"]
  n449["relation: candidate_for"]
  n450["relation: motivates"]
  n451["relation: motivates"]
  n452["relation: distinguishes"]
  n453["relation: answers"]
  n454["relation: supports"]
  n455["relation: related_to"]
  n456["relation: motivates"]
  n457["relation: challenges"]
  n458["relation: candidate_for"]
  n459["relation: candidate_for"]
  n460["relation: part_of"]
  n461["relation: candidate_for"]
  n462["relation: part_of"]
  n463["relation: part_of"]
  n464["relation: part_of"]
  n465["relation: supports"]
  n466["relation: depends_on"]
  n467["relation: challenges"]
  n468["relation: answers"]
  n469["relation: supports"]
  n470["relation: supports"]
  n471["relation: motivates"]
  n472["relation: candidate_for"]
  n473["relation: supports"]
  n474["relation: supports"]
  n475["relation: part_of"]
  n476["relation: part_of"]
  n477["relation: supersedes"]
  n478["relation: part_of"]
  n479["relation: part_of"]
  n480["relation: supports"]
  n481["relation: challenges"]
  n482["relation: supports"]
  n483["relation: part_of"]
  n484["relation: part_of"]
  n485["relation: related_to"]
  n486["relation: answers"]
  n487["relation: reframes"]
  n488["relation: candidate_for"]
  n489["relation: related_to"]
  n0 -->|then| n1
  n0 -->|output| n269
  n1 -->|then| n2
  n1 -->|output| n194
  n2 -->|then| n3
  n2 -->|output| n247
  n3 -->|then| n4
  n3 -->|output| n195
  n4 -->|then| n5
  n4 -->|output| n271
  n5 -->|then| n6
  n5 -->|output| n153
  n6 -->|then| n7
  n6 -->|output| n241
  n7 -->|then| n8
  n7 -->|output| n172
  n8 -->|then| n9
  n8 -->|output| n240
  n9 -->|then| n10
  n9 -->|output| n155
  n9 -->|output| n225
  n10 -->|then| n11
  n10 -->|output| n253
  n11 -->|then| n12
  n11 -->|output| n204
  n12 -->|then| n13
  n12 -->|output| n244
  n13 -->|then| n14
  n13 -->|output| n238
  n14 -->|then| n15
  n14 -->|output| n284
  n15 -->|then| n16
  n15 -->|output| n256
  n16 -->|then| n17
  n16 -->|output| n286
  n17 -->|then| n18
  n17 -->|output| n184
  n18 -->|then| n19
  n18 -->|output| n234
  n19 -->|then| n20
  n19 -->|output| n154
  n20 -->|then| n21
  n20 -->|output| n214
  n21 -->|then| n22
  n21 -->|output| n255
  n22 -->|then| n23
  n22 -->|output| n287
  n23 -->|then| n24
  n23 -->|output| n300
  n24 -->|then| n25
  n24 -->|output| n259
  n25 -->|then| n26
  n25 -->|output| n252
  n26 -->|then| n27
  n26 -->|output| n218
  n27 -->|then| n28
  n27 -->|output| n196
  n28 -->|then| n29
  n28 -->|output| n231
  n29 -->|then| n30
  n29 -->|output| n228
  n29 -->|output| n265
  n30 -->|then| n31
  n30 -->|output| n274
  n31 -->|then| n32
  n31 -->|output| n190
  n32 -->|then| n33
  n32 -->|output| n279
  n33 -->|then| n34
  n33 -->|output| n176
  n33 -->|output| n263
  n34 -->|then| n35
  n34 -->|output| n285
  n35 -->|then| n36
  n35 -->|output| n261
  n36 -->|then| n37
  n36 -->|output| n282
  n37 -->|then| n38
  n37 -->|output| n158
  n38 -->|then| n39
  n38 -->|output| n251
  n39 -->|then| n40
  n39 -->|output| n188
  n40 -->|then| n41
  n40 -->|output| n264
  n41 -->|then| n42
  n41 -->|output| n208
  n42 -->|then| n43
  n42 -->|output| n303
  n43 -->|then| n44
  n43 -->|output| n278
  n44 -->|then| n45
  n44 -->|output| n144
  n45 -->|then| n46
  n45 -->|output| n242
  n46 -->|then| n47
  n46 -->|output| n219
  n47 -->|then| n48
  n47 -->|output| n246
  n48 -->|then| n49
  n48 -->|output| n179
  n49 -->|then| n50
  n49 -->|output| n156
  n50 -->|then| n51
  n50 -->|output| n192
  n51 -->|then| n52
  n51 -->|output| n243
  n52 -->|then| n53
  n52 -->|output| n175
  n53 -->|then| n54
  n53 -->|output| n260
  n54 -->|then| n55
  n54 -->|output| n217
  n55 -->|then| n56
  n55 -->|output| n216
  n56 -->|then| n57
  n56 -->|output| n280
  n57 -->|then| n58
  n57 -->|output| n249
  n58 -->|then| n59
  n58 -->|output| n232
  n59 -->|then| n60
  n59 -->|output| n311
  n60 -->|then| n61
  n60 -->|output| n220
  n61 -->|then| n62
  n61 -->|output| n305
  n62 -->|then| n63
  n62 -->|output| n257
  n63 -->|then| n64
  n63 -->|output| n207
  n64 -->|then| n65
  n64 -->|output| n223
  n65 -->|then| n66
  n65 -->|output| n159
  n66 -->|then| n67
  n66 -->|output| n224
  n67 -->|then| n68
  n67 -->|output| n262
  n68 -->|then| n69
  n68 -->|output| n178
  n69 -->|then| n70
  n69 -->|output| n254
  n70 -->|then| n71
  n70 -->|output| n222
  n71 -->|then| n72
  n71 -->|output| n200
  n72 -->|then| n73
  n72 -->|output| n193
  n73 -->|then| n74
  n73 -->|output| n293
  n74 -->|then| n75
  n74 -->|output| n290
  n75 -->|then| n76
  n75 -->|output| n273
  n76 -->|then| n77
  n76 -->|output| n308
  n77 -->|then| n78
  n77 -->|output| n146
  n78 -->|then| n79
  n78 -->|output| n229
  n79 -->|then| n80
  n79 -->|output| n239
  n80 -->|then| n81
  n80 -->|output| n221
  n81 -->|then| n82
  n81 -->|output| n250
  n82 -->|then| n83
  n82 -->|output| n148
  n83 -->|then| n84
  n83 -->|output| n248
  n84 -->|then| n85
  n84 -->|output| n168
  n85 -->|then| n86
  n85 -->|output| n185
  n86 -->|then| n87
  n86 -->|then| n88
  n86 -->|output| n210
  n87 -->|then| n89
  n87 -->|output| n211
  n88 -->|then| n89
  n88 -->|output| n233
  n89 -->|then| n90
  n89 -->|output| n215
  n90 -->|then| n91
  n90 -->|output| n237
  n91 -->|then| n92
  n91 -->|output| n212
  n92 -->|then| n93
  n92 -->|output| n162
  n93 -->|then| n94
  n93 -->|output| n163
  n94 -->|then| n95
  n94 -->|output| n191
  n95 -->|then| n96
  n95 -->|output| n183
  n96 -->|then| n97
  n96 -->|output| n181
  n97 -->|then| n98
  n97 -->|output| n160
  n97 -->|output| n288
  n97 -->|output| n307
  n98 -->|then| n99
  n98 -->|output| n189
  n98 -->|output| n206
  n98 -->|output| n289
  n99 -->|then| n100
  n99 -->|then| n101
  n99 -->|output| n288
  n100 -->|then| n102
  n100 -->|output| n235
  n101 -->|then| n102
  n101 -->|output| n170
  n102 -->|then| n103
  n102 -->|output| n306
  n103 -->|then| n104
  n103 -->|output| n147
  n104 -->|then| n105
  n104 -->|output| n307
  n105 -->|then| n106
  n105 -->|output| n268
  n106 -->|then| n107
  n106 -->|output| n296
  n107 -->|then| n108
  n107 -->|output| n161
  n108 -->|then| n109
  n108 -->|output| n245
  n109 -->|then| n110
  n109 -->|output| n186
  n110 -->|then| n111
  n110 -->|output| n267
  n111 -->|then| n112
  n111 -->|output| n166
  n112 -->|then| n113
  n112 -->|output| n167
  n113 -->|then| n114
  n113 -->|output| n169
  n114 -->|then| n115
  n114 -->|output| n281
  n115 -->|then| n116
  n115 -->|output| n145
  n116 -->|then| n117
  n116 -->|output| n258
  n117 -->|then| n118
  n117 -->|output| n213
  n118 -->|then| n119
  n118 -->|output| n304
  n119 -->|then| n120
  n119 -->|output| n201
  n120 -->|then| n121
  n120 -->|output| n198
  n120 -->|output| n199
  n121 -->|then| n122
  n121 -->|output| n202
  n122 -->|then| n123
  n122 -->|output| n173
  n122 -->|output| n182
  n122 -->|output| n291
  n122 -->|output| n298
  n123 -->|then| n124
  n123 -->|output| n281
  n124 -->|then| n125
  n124 -->|output| n301
  n125 -->|then| n126
  n125 -->|output| n270
  n126 -->|then| n127
  n126 -->|output| n294
  n127 -->|then| n128
  n127 -->|output| n226
  n128 -->|then| n129
  n128 -->|output| n157
  n129 -->|then| n130
  n129 -->|output| n266
  n130 -->|then| n131
  n130 -->|output| n151
  n131 -->|then| n132
  n131 -->|output| n152
  n132 -->|then| n133
  n132 -->|output| n149
  n132 -->|output| n150
  n133 -->|then| n134
  n133 -->|output| n227
  n134 -->|then| n135
  n134 -->|output| n295
  n135 -->|then| n136
  n135 -->|output| n177
  n136 -->|then| n137
  n136 -->|output| n197
  n137 -->|then| n138
  n137 -->|output| n180
  n138 -->|then| n139
  n138 -->|output| n275
  n139 -->|then| n140
  n139 -->|output| n277
  n140 -->|then| n141
  n140 -->|output| n297
  n141 -->|then| n142
  n141 -->|output| n171
  n142 -->|output| n236
  n142 -->|output| n302
  n143 -->|part| n431
  n144 -->|input| n45
  n144 -->|candidate| n366
  n145 -->|source| n455
  n146 -->|candidate| n407
  n147 -->|premise| n437
  n148 -->|left| n412
  n149 -->|part| n475
  n150 -->|part| n476
  n151 -->|input| n131
  n151 -->|candidate| n472
  n152 -->|input| n132
  n152 -->|input| n133
  n152 -->|input| n136
  n152 -->|premise| n473
  n153 -->|input| n6
  n153 -->|reason| n317
  n154 -->|answer| n332
  n155 -->|input| n18
  n155 -->|candidate| n320
  n156 -->|input| n50
  n156 -->|input| n51
  n157 -->|premise| n470
  n158 -->|input| n38
  n158 -->|input| n65
  n158 -->|candidate| n358
  n158 -->|reason| n359
  n159 -->|new| n394
  n160 -->|input| n100
  n160 -->|source| n434
  n160 -->|left| n438
  n161 -->|input| n108
  n161 -->|premise| n447
  n161 -->|reason| n448
  n162 -->|dependent| n420
  n163 -->|input| n94
  n164 -->|challenger| n326
  n164 -->|answer| n327
  n165 -->|candidate| n316
  n166 -->|input| n113
  n166 -->|input| n122
  n166 -->|left| n452
  n167 -->|input| n113
  n167 -->|input| n122
  n168 -->|source| n414
  n169 -->|answer| n453
  n170 -->|input| n105
  n170 -->|dependent| n445
  n171 -->|input| n140
  n171 -->|answer| n486
  n172 -->|input| n8
  n172 -->|reason| n319
  n173 -->|part| n463
  n174 -->|part| n432
  n175 -->|input| n53
  n175 -->|input| n55
  n175 -->|candidate| n374
  n176 -->|input| n34
  n176 -->|input| n71
  n176 -->|example| n352
  n176 -->|reason| n353
  n177 -->|part| n479
  n178 -->|challenger| n397
  n179 -->|input| n49
  n179 -->|candidate| n370
  n179 -->|source| n371
  n179 -->|part| n387
  n180 -->|challenger| n481
  n181 -->|candidate| n427
  n182 -->|part| n462
  n183 -->|input| n96
  n183 -->|challenger| n426
  n184 -->|input| n20
  n184 -->|candidate| n330
  n185 -->|input| n86
  n186 -->|input| n110
  n186 -->|input| n115
  n186 -->|input| n116
  n186 -->|input| n124
  n186 -->|candidate| n449
  n187 -->|candidate| n324
  n188 -->|candidate| n360
  n189 -->|input| n99
  n189 -->|part| n430
  n190 -->|candidate| n349
  n191 -->|input| n95
  n191 -->|input| n97
  n191 -->|dependent| n424
  n191 -->|dependent| n425
  n192 -->|source| n372
  n193 -->|source| n402
  n194 -->|input| n2
  n194 -->|input| n3
  n195 -->|new| n313
  n195 -->|answer| n314
  n196 -->|input| n28
  n196 -->|input| n56
  n196 -->|candidate| n342
  n197 -->|premise| n480
  n198 -->|input| n121
  n198 -->|input| n136
  n198 -->|input| n141
  n198 -->|part| n460
  n199 -->|candidate| n459
  n200 -->|input| n72
  n200 -->|input| n73
  n200 -->|source| n401
  n201 -->|input| n120
  n201 -->|candidate| n458
  n202 -->|input| n125
  n202 -->|input| n137
  n202 -->|candidate| n461
  n203 -->|candidate| n361
  n204 -->|input| n12
  n204 -->|answer| n322
  n204 -->|challenger| n323
  n205 -->|input| n10
  n206 -->|input| n99
  n206 -->|part| n429
  n207 -->|input| n64
  n207 -->|answer| n392
  n208 -->|answer| n363
  n209 -->|candidate| n364
  n210 -->|input| n87
  n210 -->|candidate| n417
  n211 -->|input| n88
  n211 -->|input| n89
  n211 -->|input| n90
  n211 -->|part| n418
  n211 -->|reason| n422
  n212 -->|input| n92
  n212 -->|source| n421
  n214 -->|input| n21
  n214 -->|input| n80
  n214 -->|source| n333
  n215 -->|candidate| n419
  n216 -->|new| n378
  n217 -->|input| n56
  n217 -->|dependent| n377
  n218 -->|source| n340
  n219 -->|input| n47
  n219 -->|candidate| n367
  n220 -->|part| n386
  n221 -->|challenger| n410
  n222 -->|challenger| n399
  n222 -->|challenger| n400
  n223 -->|input| n66
  n223 -->|candidate| n393
  n224 -->|input| n67
  n224 -->|challenger| n395
  n225 -->|reason| n321
  n226 -->|input| n128
  n226 -->|premise| n469
  n227 -->|input| n134
  n227 -->|input| n138
  n227 -->|input| n139
  n227 -->|input| n141
  n227 -->|new| n477
  n227 -->|part| n483
  n228 -->|reason| n344
  n228 -->|left| n346
  n229 -->|input| n79
  n229 -->|source| n408
  n230 -->|example| n350
  n231 -->|input| n29
  n231 -->|input| n32
  n231 -->|challenger| n343
  n232 -->|input| n59
  n233 -->|original| n440
  n234 -->|input| n19
  n234 -->|challenger| n331
  n235 -->|input| n101
  n235 -->|dependent| n441
  n235 -->|original| n487
  n237 -->|input| n91
  n238 -->|input| n14
  n238 -->|original| n329
  n239 -->|source| n409
  n240 -->|input| n9
  n240 -->|input| n27
  n241 -->|input| n7
  n241 -->|input| n23
  n241 -->|input| n58
  n241 -->|input| n85
  n241 -->|dependent| n381
  n241 -->|dependent| n382
  n241 -->|original| n416
  n242 -->|input| n46
  n242 -->|reason| n369
  n243 -->|input| n52
  n243 -->|source| n373
  n243 -->|original| n375
  n244 -->|input| n13
  n244 -->|original| n325
  n245 -->|input| n109
  n246 -->|input| n48
  n247 -->|input| n3
  n247 -->|challenger| n312
  n248 -->|input| n84
  n248 -->|input| n85
  n248 -->|source| n413
  n248 -->|reason| n415
  n249 -->|input| n59
  n249 -->|source| n383
  n249 -->|challenger| n384
  n251 -->|input| n39
  n252 -->|input| n26
  n253 -->|input| n11
  n254 -->|source| n398
  n255 -->|input| n22
  n255 -->|challenger| n334
  n256 -->|input| n16
  n256 -->|input| n17
  n256 -->|original| n345
  n257 -->|input| n63
  n257 -->|source| n391
  n258 -->|input| n117
  n258 -->|input| n129
  n258 -->|reason| n456
  n259 -->|input| n25
  n259 -->|reason| n339
  n260 -->|input| n54
  n260 -->|input| n69
  n260 -->|challenger| n376
  n261 -->|input| n36
  n261 -->|challenger| n355
  n262 -->|input| n68
  n262 -->|input| n75
  n263 -->|input| n37
  n263 -->|input| n40
  n263 -->|original| n362
  n263 -->|original| n396
  n264 -->|input| n41
  n264 -->|input| n42
  n264 -->|input| n62
  n265 -->|input| n30
  n265 -->|input| n31
  n266 -->|input| n130
  n266 -->|reason| n471
  n267 -->|input| n111
  n267 -->|input| n112
  n267 -->|input| n114
  n267 -->|reason| n450
  n267 -->|reason| n451
  n268 -->|input| n106
  n269 -->|input| n1
  n269 -->|input| n4
  n269 -->|input| n8
  n269 -->|input| n83
  n269 -->|reason| n315
  n269 -->|original| n318
  n270 -->|input| n126
  n270 -->|challenger| n467
  n271 -->|input| n5
  n271 -->|input| n93
  n271 -->|reason| n423
  n272 -->|source| n442
  n273 -->|input| n76
  n273 -->|input| n81
  n273 -->|source| n405
  n273 -->|original| n411
  n274 -->|source| n347
  n275 -->|input| n139
  n275 -->|premise| n482
  n277 -->|input| n141
  n277 -->|part| n484
  n278 -->|input| n44
  n278 -->|input| n59
  n278 -->|input| n61
  n278 -->|part| n368
  n278 -->|reason| n385
  n279 -->|input| n33
  n279 -->|input| n70
  n279 -->|challenger| n351
  n280 -->|challenger| n379
  n280 -->|source| n380
  n281 -->|input| n123
  n281 -->|premise| n454
  n282 -->|source| n356
  n282 -->|answer| n357
  n284 -->|input| n15
  n284 -->|reason| n328
  n285 -->|input| n35
  n285 -->|input| n36
  n285 -->|candidate| n354
  n286 -->|input| n17
  n287 -->|input| n23
  n287 -->|premise| n335
  n288 -->|input| n98
  n288 -->|input| n101
  n288 -->|answer| n433
  n288 -->|part| n443
  n289 -->|input| n99
  n289 -->|input| n118
  n289 -->|part| n428
  n290 -->|source| n404
  n291 -->|part| n464
  n292 -->|premise| n474
  n293 -->|input| n74
  n293 -->|source| n403
  n294 -->|input| n127
  n294 -->|answer| n468
  n295 -->|input| n135
  n295 -->|input| n139
  n295 -->|part| n478
  n296 -->|input| n107
  n296 -->|answer| n446
  n297 -->|source| n485
  n298 -->|premise| n465
  n299 -->|input| n101
  n299 -->|source| n439
  n299 -->|part| n444
  n300 -->|input| n24
  n300 -->|input| n57
  n300 -->|candidate| n336
  n300 -->|dependent| n337
  n300 -->|reason| n338
  n301 -->|input| n142
  n301 -->|dependent| n466
  n302 -->|candidate| n488
  n302 -->|source| n489
  n303 -->|input| n43
  n303 -->|part| n365
  n304 -->|input| n119
  n304 -->|challenger| n457
  n305 -->|dependent| n389
  n305 -->|dependent| n390
  n306 -->|input| n103
  n306 -->|candidate| n436
  n307 -->|input| n102
  n307 -->|input| n104
  n307 -->|source| n435
  n308 -->|input| n77
  n308 -->|reason| n406
  n309 -->|input| n78
  n309 -->|input| n82
  n309 -->|source| n341
  n310 -->|candidate| n348
  n311 -->|input| n60
  n311 -->|input| n61
  n311 -->|reason| n388
  n312 -->|target| n194
  n313 -->|old| n194
  n314 -->|question| n247
  n315 -->|result| n271
  n316 -->|problem| n271
  n317 -->|result| n241
  n318 -->|replacement| n240
  n319 -->|result| n240
  n320 -->|problem| n240
  n321 -->|result| n253
  n322 -->|question| n253
  n323 -->|target| n225
  n324 -->|problem| n244
  n325 -->|replacement| n238
  n326 -->|target| n187
  n327 -->|question| n238
  n328 -->|result| n256
  n329 -->|replacement| n256
  n330 -->|problem| n256
  n331 -->|target| n155
  n332 -->|question| n234
  n333 -->|target| n184
  n334 -->|target| n214
  n335 -->|conclusion| n300
  n336 -->|problem| n241
  n337 -->|prerequisite| n287
  n338 -->|result| n259
  n339 -->|result| n252
  n340 -->|target| n252
  n341 -->|target| n218
  n342 -->|problem| n240
  n343 -->|target| n196
  n344 -->|result| n265
  n345 -->|replacement| n265
  n346 -->|right| n276
  n347 -->|target| n265
  n348 -->|problem| n265
  n349 -->|problem| n265
  n350 -->|general| n231
  n351 -->|target| n231
  n352 -->|general| n279
  n353 -->|result| n263
  n354 -->|problem| n263
  n355 -->|target| n285
  n356 -->|target| n285
  n357 -->|question| n261
  n358 -->|problem| n263
  n359 -->|result| n251
  n360 -->|problem| n251
  n361 -->|problem| n263
  n362 -->|replacement| n264
  n363 -->|question| n264
  n364 -->|problem| n264
  n365 -->|whole| n278
  n366 -->|problem| n242
  n367 -->|problem| n242
  n368 -->|whole| n219
  n369 -->|result| n246
  n370 -->|problem| n246
  n371 -->|target| n156
  n372 -->|target| n156
  n373 -->|target| n156
  n374 -->|problem| n243
  n375 -->|replacement| n260
  n376 -->|target| n175
  n377 -->|prerequisite| n260
  n378 -->|old| n175
  n379 -->|target| n196
  n380 -->|target| n240
  n381 -->|prerequisite| n249
  n382 -->|prerequisite| n232
  n383 -->|target| n264
  n384 -->|target| n300
  n385 -->|result| n311
  n386 -->|whole| n311
  n387 -->|whole| n311
  n388 -->|result| n305
  n389 -->|prerequisite| n278
  n390 -->|prerequisite| n242
  n391 -->|target| n264
  n392 -->|question| n257
  n393 -->|problem| n263
  n394 -->|old| n158
  n395 -->|target| n223
  n396 -->|replacement| n262
  n397 -->|target| n203
  n398 -->|target| n260
  n399 -->|target| n279
  n400 -->|target| n196
  n401 -->|target| n176
  n402 -->|target| n200
  n403 -->|target| n200
  n404 -->|target| n293
  n405 -->|target| n271
  n406 -->|result| n273
  n407 -->|problem| n273
  n408 -->|target| n309
  n409 -->|target| n249
  n410 -->|target| n214
  n411 -->|replacement| n250
  n412 -->|right| n309
  n413 -->|target| n269
  n414 -->|target| n248
  n415 -->|result| n185
  n416 -->|replacement| n233
  n417 -->|problem| n233
  n418 -->|whole| n185
  n419 -->|problem| n233
  n420 -->|prerequisite| n283
  n421 -->|target| n211
  n422 -->|result| n162
  n423 -->|result| n163
  n424 -->|prerequisite| n163
  n425 -->|prerequisite| n162
  n426 -->|target| n214
  n427 -->|problem| n237
  n428 -->|whole| n288
  n429 -->|whole| n288
  n430 -->|whole| n288
  n431 -->|whole| n288
  n432 -->|whole| n288
  n433 -->|question| n237
  n434 -->|target| n248
  n435 -->|target| n273
  n436 -->|problem| n272
  n437 -->|conclusion| n306
  n438 -->|right| n307
  n439 -->|target| n288
  n440 -->|replacement| n235
  n441 -->|prerequisite| n160
  n442 -->|target| n271
  n443 -->|whole| n170
  n444 -->|whole| n170
  n445 -->|prerequisite| n235
  n446 -->|question| n268
  n447 -->|conclusion| n296
  n448 -->|result| n245
  n449 -->|problem| n245
  n450 -->|result| n166
  n451 -->|result| n167
  n452 -->|right| n167
  n453 -->|question| n267
  n454 -->|conclusion| n169
  n455 -->|target| n186
  n456 -->|result| n213
  n457 -->|target| n289
  n458 -->|problem| n258
  n459 -->|problem| n258
  n460 -->|whole| n171
  n461 -->|problem| n258
  n462 -->|whole| n298
  n463 -->|whole| n298
  n464 -->|whole| n298
  n465 -->|conclusion| n281
  n466 -->|prerequisite| n198
  n467 -->|target| n202
  n468 -->|question| n270
  n469 -->|conclusion| n294
  n470 -->|conclusion| n226
  n471 -->|result| n151
  n472 -->|problem| n270
  n473 -->|conclusion| n226
  n474 -->|conclusion| n152
  n475 -->|whole| n152
  n476 -->|whole| n152
  n477 -->|old| n202
  n478 -->|whole| n277
  n479 -->|whole| n277
  n480 -->|conclusion| n171
  n481 -->|target| n202
  n482 -->|conclusion| n277
  n483 -->|whole| n171
  n484 -->|whole| n171
  n485 -->|target| n171
  n486 -->|question| n258
  n487 -->|replacement| n236
  n488 -->|problem| n236
  n489 -->|target| n272
```
