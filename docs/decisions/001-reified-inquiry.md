# ADR-001: Reified relations and inquiry moves

**Status:** accepted for V1.

**Context.** A concept graph loses the difference between “X supports Y” and “we challenged the inference from X to Y, then reformulated the question.” Linked premises, multi-output distinctions and provenance require more than unlabeled binary edges.

**Decision.** Store relations as ID-bearing records with typed role bindings. Store inquiry moves as separate activities with actor, multiple inputs/outputs, occurrence and anchors. An inference relation can itself be targeted. Use a derived bipartite NetworkX/Mermaid view for navigation.

**Alternatives.** Generic entity triples are simpler but flatten linked premises and make edge provenance awkward. A complete AIF/PROV or TypeDB implementation would add interoperability/storage work before the basic annotation task is validated.

**Consequences.** JSON is more verbose, but role cardinality and participant types are checkable. The format is TypeDB-shaped without requiring TypeDB. AIF/IAT and PROV alignments are documented as partial; no false standards-conformance claim is made.
