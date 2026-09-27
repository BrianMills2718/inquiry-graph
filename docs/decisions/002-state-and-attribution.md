# ADR-002: Content is not belief; answer is not resolution

**Status:** accepted for V1.

**Context.** The conversation contains proposals, corrections, objections and uncertain agreement. A global status field such as “accepted claim” would silently assign beliefs to the wrong participant.

**Decision.** Separate node kind, actor-relative stance events, actor/context-relative question events, and extraction-review metadata. Preserve history. Proposed resolutions remain in the agenda until confirmed; assistant answers cannot close the user's scope.

**Alternatives.** One mutable truth/status property is convenient but conflates proposition truth, participant acceptance, inquiry progress and extraction quality. Treating every utterance as belief misrepresents questioning and exploratory dialogue.

**Consequences.** A question may have multiple agenda rows. This is intentional. V1 records review authorship through Git commits rather than a separate in-graph reviewer entity. No private mental state is asserted.
