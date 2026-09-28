# ADR 008 — Keep preference-sensitive binary defeat Dung-compatible; do not call it full ABA+

## Status

Accepted for the current research architecture.

## Context

The next planned step after the basic ABA bridge was preference-sensitive defeat, initially expected to use ABA+ directly.

A closer literature check exposed a representation mismatch.

ABA+ uses preferences over assumptions and may **reverse** attacks. General ABA+ attacks are naturally attacks between sets of assumptions. Recent work shows that full ABA+ does not in general admit a faithful ordinary binary Dung instantiation and instead motivates set-to-set / hyperargumentation structures.

The current project downstream layer is binary:

\[
Defeat\subseteq Args\times Args.
\]

## Decision

Do not represent full ABA+ by reversing individual binary argument edges.

For the current binary-Dung warrant pipeline, implement a restricted **normal-attack preference regime**:

A basic ABA attack against assumption \(\beta\) succeeds only if the attacking support contains no assumption \(\alpha\) with:

\[
\alpha<\beta.
\]

Otherwise the attack is recorded as blocked.

No reverse edge is created.

## Rationale

This preserves:

- a sound and auditable binary attack-to-defeat step;
- conservative behavior when no preferences are present;
- compatibility with the existing Dung grounded-semantics implementation;
- the project distinction between attack, preference resolution, defeat, and acceptability.

It also avoids falsely labelling a binary approximation as full ABA+.

Preference-filtering traditions in abstract/structured argumentation provide established precedent for blocking attacks when the target is preferred.

## Consequences

The executable ABA module gains:

- a strict assumption-preference relation;
- transitive closure and cycle rejection;
- explicit resolution records for successful versus blocked attacks;
- projection of successful preference-filtered attacks to the existing binary DefeatFramework.

The project may now integrate preference-sensitive acceptability with warrant/license.

## Explicit escalation

Full ABA+ remains a documented future branch in GitHub issue #18.

If reverse/collective attacks are required, evaluate a set-to-set/hyperargumentation representation rather than extending the binary DefeatFramework ad hoc.

First-class derivation/subargument structure is a separate escalation branch tracked in issue #17 and ADR 007.

## References

- Čyras & Toni, *ABA+: Assumption-Based Argumentation with Preferences*.
- Dimopoulos et al., *Sets attacking sets in abstract argumentation – redefining ABA+ semantics via hyper argumentation frameworks*, Artificial Intelligence 357 (2026), 104558.
- Amgoud & Cayrol, preference-based argumentation.
- Modgil & Prakken, ASPIC+ structured argumentation.
