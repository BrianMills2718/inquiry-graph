# ADR-003: Small local toolkit, not a database project

**Status:** accepted for V1.

**Context.** The primary risk is semantic coherence and attribution, not database throughput. The user specifically requested an off-the-shelf structured-output project with little custom infrastructure.

**Decision.** Use Pydantic for schema/validation, NetworkX for graph structure, argparse for the CLI, canonical JSON in Git, and generated Mermaid/DOT/Markdown/HTML views. Keep the provider SDK optional.

**Alternatives.** TypeDB, Neo4j, RDF stores and custom web stacks are plausible later, but impose deployment, schema migration and access-control work before a validated fixture exists.

**Consequences.** Offline execution and deterministic diffs are easy. Query performance is in-memory, review editing is file-based, and there is no concurrent service. A future database adapter must preserve IDs, role semantics, source spans and actor-scoped history rather than redefining them.
