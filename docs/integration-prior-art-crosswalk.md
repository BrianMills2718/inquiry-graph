# Inquiry-graph integration: prior-art/standards crosswalk

**Status:** research note.  
**Goal:** avoid inventing a bespoke graph-integration method where established ontology/KG/argumentation machinery already applies.

## Conclusion

Do not start from a custom "merge two inquiry graphs" algorithm.

Use the established decomposition:

```text
candidate generation / matching
    -> typed correspondence set
    -> semantic/global validation
    -> review
    -> governed alignment
    -> optional derived integrated projection
```

The custom work should be limited mainly to **Inquiry-specific correspondence semantics and invariants**.

## 1. Mapping record / interchange: SSSOM

Use SSSOM as the primary design/interchange reference for cross-graph mappings.

A SSSOM mapping is fundamentally:

```text
(subject, mapping predicate, object) + mapping metadata
```

with mapping-set metadata, provenance/justification, confidence and review metadata.

Important consequence: do not create a proprietary alignment envelope unless OntoCanon requires extra governance fields. Prefer a superset that can project losslessly to SSSOM for ordinary pairwise mappings.

SSSOM permits arbitrary mapping predicates, so Inquiry-specific relations do not require changing SSSOM itself.

### Reuse directly

- subject/object identifiers
- predicate identifier
- mapping-set identity
- mapping justification
- author/reviewer provenance
- confidence / reviewer agreement where applicable
- timestamps/version metadata
- labels as conveniences, not identity

### Do not equate confidence with governance

A confidence score is evidence/metadata. Acceptance/rejection/activation remains an OntoCanon governance decision.

## 2. Mapping predicates: reuse standard semantics where they actually fit

Do not create `equivalent/refines/generalizes` as local terms when a standard relation has the same intended semantics.

### Identity/equivalence

Choose by semantic type:

- `owl:sameAs` only for genuine instance identity
- `owl:equivalentClass` for actual class equivalence
- `owl:equivalentProperty` for property equivalence
- `skos:exactMatch` for cross-scheme conceptual interchangeability without asserting OWL identity
- `skos:closeMatch` when near-equivalence is intentionally weaker

### Breadth / refinement

For concept-scheme mappings:

- `skos:broadMatch`
- `skos:narrowMatch`

For genuine ontology classes/properties:

- `rdfs:subClassOf`
- `rdfs:subPropertyOf`

Do not use class/subclass vocabulary for arbitrary inquiry episodes or questions unless they genuinely denote classes.

### Beyond equivalence

The OAEI BeyondEquivalence benchmark treats at least these relation families as first-class:

- equivalence
- superclass
- subclass
- overlap
- disjoint

Use that relation algebra where the aligned objects have extensional/class-like semantics.

For arbitrary Inquiry objects, SSSOM can still carry a domain predicate.

## 3. Complex/n:m alignment: Alignment API / EDOAL

Simple pairwise term mappings are not enough when correspondence involves:

- several source objects mapping to one target object;
- constructed expressions;
- restrictions;
- transformations;
- conditional identity/link keys.

EDOAL already exists for expressive, declarative ontology correspondences of this kind.

Do not invent a custom n:m mapping language before testing whether EDOAL or an equivalent established alignment representation covers the case.

Likely use:

- SSSOM for common pairwise correspondences and exchange/governance metadata;
- EDOAL-style expressive correspondence only when the mapping genuinely cannot be represented pairwise.

## 4. Matching/evaluation infrastructure: OAEI + MELT

Use OAEI methodology and MELT as the primary reference for matcher evaluation rather than defining a bespoke benchmark methodology.

Established pattern:

```text
source ontologies/graphs
    -> matcher(s)
    -> alignment
    -> reference-alignment comparison
    -> precision / recall / F-measure
    -> logical/coherence checks
```

For Inquiry Graph, adapt the benchmark objects, not the evaluation discipline.

The first two-trajectory reference set should therefore be treated as a **reference alignment**, with:

- accepted correspondences;
- explicit relation type;
- hard negatives where useful;
- unresolved/uncertain cases kept separate;
- provenance/reviewer identity;
- held-out evaluation cases.

Do not tune a matcher on the same correspondence set used for final evaluation.

## 5. Candidate generation: commodity matcher ensemble

Candidate generation should be treated as retrieval/blocking, not as semantic authority.

Potential signals:

- exact identifier / deterministic normalized identity
- lexical similarity
- embeddings
- type compatibility
- neighborhood/structural similarity
- relation-role compatibility
- source/provenance context

This is standard ontology/KG-matching territory. MELT-style matcher composition is a better conceptual model than one monolithic LLM prompt.

LLMs are appropriate as one adjudicator/matcher signal, especially for ambiguous semantic cases, but should not own identity or irreversible merge.

## 6. Repair / global validation: coherence + conservativity

Ontology integration literature conventionally separates:

```text
matching -> merging/integration -> repair
```

and evaluates mappings for:

- **consistency/coherence:** mappings should not make the integrated theory inconsistent/unsatisfiable;
- **conservativity:** mappings should not unintentionally induce new within-source semantic consequences.

For Inquiry Graph, OWL satisfiability is not the governing semantics, but the principles transfer directly.

### Inquiry analogues

Check accepted alignments for violations such as:

- incompatible object types mapped as identity;
- cycles in relations declared acyclic (e.g. supersession);
- question-state histories becoming impossible;
- actor/stance provenance collapsing;
- distinct source occurrences silently becoming one occurrence;
- an equivalence cluster forcing a contradiction between hard local invariants;
- a mapping causing new same-graph relations that neither source graph licensed.

Do not automatically "repair" by deleting mappings without an inspectable decision record.

## 7. Question-to-question mappings: use question semantics, not generic ontology words

Question relations are a genuine special case.

Established theories already provide stronger notions than vague `same_question` / `refines`:

### Inquisitive semantics

Issues/questions can be ordered by **issue refinement**: one issue is more inquisitive/refined when settling it also settles the less demanding issue.

This is a candidate formal semantics for some cross-trajectory question-refinement mappings.

### Inferential erotetic logic

**Erotetic implication** formalizes when one question follows usefully from another question plus declarative premises; each answer to the implied question narrows the possibilities relevant to the original question.

This is a candidate formal basis for question-progress relations such as:

- follow-up question
- decomposes inquiry
- advances/resolves part of an earlier question

Do not collapse all of these into SKOS broad/narrow matching.

## 8. Argument/discourse mappings: import argumentation machinery

Inquiry Graph already contains support/challenge and relation-targeting semantics.

Relevant established machinery includes:

- AIF / AIF+ for informational content, inferential/argument schemes, locutions and dialogue histories;
- Dung-style abstract argumentation for attack/acceptability;
- bipolar argumentation for support + attack;
- recursive bipolar argumentation when attacks/supports themselves may be targets.

This is especially relevant to the existing Inquiry Graph design where a challenge may target an inference relation rather than merely its premise/conclusion.

Do not invent a bespoke recursive support/attack semantics if an established argumentation formalism applies.

## 9. Proposed architecture of an alignment record

OntoCanon should govern an alignment object that is at least compatible with:

```text
subject_id
predicate_id
object_id
mapping_set_id

mapping_justification
evidence/provenance
author/proposer
reviewer
confidence (optional)
reviewer agreement (optional)

governance state
decision provenance
supersession lineage
profile/version
```

The last governance fields may be OntoCanon-specific while the semantic mapping core remains SSSOM-compatible.

## 10. What is actually Inquiry-specific

Likely custom work is small and should be justified one predicate/invariant at a time.

### Probably standard

- exact/same identity
- conceptual exact/close match
- broader/narrower
- subclass/superclass
- overlap/disjointness
- generic relatedness
- support/attack semantics
- question refinement / erotetic implication
- mapping provenance/confidence/review metadata
- benchmark methodology
- alignment coherence checking as a general pattern

### Potentially Inquiry-specific

- `sameStrategy`
- `continuesInquiryEpisode`
- `independentConvergence`
- `reframes` where the semantics are richer than question refinement
- cross-trajectory identity of Moves/StrategyEpisodes
- actor-relative stance-preservation constraints
- open-agenda / QuestionEvent invariants across aligned trajectories

Before adding any such predicate, search for a standard relation with the same semantics and document why it is inadequate.

## 11. Recommended first benchmark

Only after the standards crosswalk is fixed:

1. choose a small set of cross-trajectory candidate pairs;
2. type each pair using the most specific established predicate available;
3. use Inquiry-specific predicates only for demonstrated gaps;
4. record uncertain/no-decision separately from negative/distinct;
5. hold out part of the set;
6. evaluate candidate retrieval separately from semantic adjudication;
7. test global invariant/coherence effects separately from pairwise correctness.

This yields a benchmark compatible with established ontology-matching practice rather than a bespoke scoring scheme.

## 12. Adoption posture

### Adopt/reuse

- SSSOM data model/interchange concepts
- SKOS/OWL/RDFS mapping predicates where semantically correct
- OAEI benchmark discipline
- MELT concepts/tooling where implementation fit is good
- EDOAL for genuinely complex correspondences
- coherence/conservativity repair principles
- inquisitive semantics / erotetic logic for questions
- AIF/argumentation frameworks for argument/discourse structure

### Do not adopt blindly

- OWL identity predicates for non-OWL semantic objects
- automatic transitive closure of every mapping relation
- automatic mapping repair that silently deletes correspondences
- a single scalar confidence as truth/governance authority
- one matcher/LLM as canonical semantic authority

## References

- SSSOM specification and mapping model: https://mapping-commons.github.io/sssom/
- OAEI: https://oaei.ontologymatching.org/
- OAEI BeyondEquivalence: https://oaei.ontologymatching.org/2025/beyondequivalence/
- MELT: https://github.com/dwslab/melt
- EDOAL / Alignment API: https://moex.gitlabpages.inria.fr/alignapi/edoal.html
- Inquisitive Semantics: Ciardelli, Groenendijk, Roelofsen, *Inquisitive Semantics* (2018)
- Inferential erotetic logic: Wiśniewski and subsequent work on erotetic implication
- Argument Interchange Format / AIF+ and established abstract/bipolar/recursive argumentation literature
