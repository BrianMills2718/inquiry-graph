# Primary references and alignment boundary

Checked during V1 development, 2026-09-27. These references informed the design; they do not certify that the custom JSON is an implementation of each standard.

- **Inference Anchoring Theory quick-start guide**, ARG-tech: https://arg.tech/~chris/acl2019tut/IAT-guidelines.pdf . Distinguishes informational/argumentative structure, locutions, transitions and anchoring; supports linked premises and attacks on inference relations. Particularly relevant: an assertion in the dialogue is not proof of sincere belief. The PDF and its diagrams were inspected.
- **IAT-related argument parsing**, primary proceedings paper: https://aclanthology.org/2024.argmining-1.13/ . Relevant comparator for extracting argument/dialogue structure; not a claim that our extra inquiry-state semantics are already standardized.
- **Coherence of Argumentative Dialogue Snippets: A New Method for Large Scale Evaluation with an Application to Inference Anchoring Theory**, Piwek, Amidei and Stoyanchev (2025): https://aclanthology.org/2025.findings-emnlp.758/ . Relevant evaluation literature. No numerical performance claims are imported into this project.
- **PROV-O**, W3C Recommendation: https://www.w3.org/TR/prov-o/ . Entity, Activity, Agent and qualified provenance inform the separation of content, moves and participants.
- **Web Annotation Data Model**, W3C Recommendation: https://www.w3.org/TR/annotation-model/ . Text quote/position selectors inform our grounded source spans; V1 uses a smaller custom representation and Unicode-offset convention.
- **SKOS Reference**, W3C: https://www.w3.org/TR/skos-reference/ . Relevant for controlled vocabularies and concept relationships, not sufficient on its own for inquiry-state change.
- **LangExtract**, official Google repository: https://github.com/google/langextract . Source-grounded structured extraction is closely related. Mention extraction and source grounding do not themselves ensure a coherent, attributed, temporally consistent inquiry graph.
- **Pydantic JSON Schema**, official documentation: https://docs.pydantic.dev/latest/concepts/json_schema/ . Executable models generate committed JSON Schemas.
- **OpenAI structured outputs**, official documentation: https://developers.openai.com/api/docs/guides/structured-outputs . The optional adapter uses the SDK's Pydantic structured-output parsing interface. Schema adherence does not establish semantic fidelity, and refusal/incomplete cases still require handling.

IBIS, discourse-relation frameworks, proof provenance and belief revision remain potential alignment investigations. This release does not claim to have exhaustively searched all existing inquiry ontologies, does not assert that no integrated ontology exists, and does not fabricate an interoperability mapping where semantics have not been checked.
