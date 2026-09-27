# ADR-005: Conservative identity and recoverable history

**Status:** accepted for V1.

**Context.** Similar formulations may conceal different scopes or commitments. Silent fuzzy merging is particularly damaging in a personal worldview graph.

**Decision.** Merge identical IDs only when their records agree exactly. Reject identity conflicts. Preserve new claims and events under new IDs; use explicit relations for revisions. Git commits preserve snapshot and review history. Only within-conversation source order is used for temporal after-links.

**Alternatives.** Embedding-based automatic same-as and timestamp-only chronology can be convenient but erase distinctions or invent ordering. A full event-sourced distributed store exceeds the V1 scope.

**Consequences.** Duplicate concepts may remain. Human-reviewed identity proposals are a next feature. A merged graph does not imply all questions have a single global status. Recovery depends on committed/pushed snapshots, not an uncommitted local worktree.
