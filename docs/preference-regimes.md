# Preference regimes: Dung-compatible filtering now, full ABA+ as an escalation path

> **Status:** current implementation decision. This note corrects the earlier plan to "implement ABA+ next" after checking the preference literature more carefully.

## 1. The literature changes the implementation plan

ABA+ incorporates preferences over assumptions directly into attack.

Let:

\[
\alpha < \beta
\]

mean assumption \(\alpha\) is strictly less preferred than assumption \(\beta\).

If an assumption set \(S\) derives the contrary of \(\beta\):

\[
S\vdash\overline{\beta},
\]

ABA+ distinguishes:

- **normal attack** when no \(s\in S\) satisfies \(s<\beta\);
- **reverse attack** when some \(s\in S\) satisfies \(s<\beta\).

In the reverse case, the conflict is not simply deleted: its direction is reversed.

This is materially different from ordinary binary preference-filtered argumentation.

## 2. Why full ABA+ is not being projected into the current Dung graph

Recent work makes an important representation boundary explicit.

General ABA+ attacks are naturally **set-to-set** attacks over assumptions. Preference reversal can produce attacks whose target is a set rather than one individual argument/assumption.

Dimopoulos et al. (2026) show that general ABA+ does not have the straightforward ordinary binary-Dung instantiation available for basic ABA. They introduce Hyper Argumentation Frameworks (HYPAFs), whose attack relation is:

\[
R\subseteq 2^A\times(2^A\setminus\{\varnothing\}).
\]

That is a different abstract object from the project's current:

\[
\operatorname{Defeat}\subseteq Args\times Args.
\]

Therefore:

\[
\boxed{
\text{full ABA+}
\not\equiv
\text{binary attack reversal in the current Dung layer}.
}
\]

The project will not claim otherwise.

## 3. Immediate preference regime

The current executable preference regime keeps the **normal-attack** half and stays binary-Dung compatible.

For a basic ABA attack:

\[
A\leadsto B
\]

where source argument \(A\) derives the contrary of target assumption \(\beta\), define:

\[
\boxed{
A\hookrightarrow_{\mathfrak P_N}B
\iff
A\leadsto B
\land
\nexists\alpha\in\operatorname{Supp}(A):
\alpha<\beta.
}
\]

If such an \(\alpha\) exists, the attack is **blocked** in this regime.

It is not reversed.

Call this regime:

\[
\mathfrak P_N
\]

for **normal-attack preference filtering**.

## 4. Why this is legitimate

This is not presented as a new universal preference theory.

It is a deliberately restricted established-style regime that:

1. uses the same strict-preference condition as ABA+ normal attack;
2. preserves the project's binary Dung downstream semantics;
3. makes blocked attacks auditable;
4. conservatively reduces to basic ABA when the preference relation is empty;
5. allows the warrant pipeline to test preference-sensitive defeat without silently implementing an incorrect version of ABA+.

Preference-based argumentation and ASPIC+-style defeat filtering provide broader precedent for preferences disabling attacks while retaining a Dung-compatible defeat graph.

## 5. Preference representation

The implementation stores the strict part directly:

\[
<\;\subseteq A\times A.
\]

A pair:

\[
(\alpha,\beta)
\]

means:

\[
\alpha<\beta.
\]

The relation is transitively closed and must be acyclic.

This is sufficient for deciding whether a basic attack is blocked.

It does not attempt to represent indifference/equivalence classes explicitly yet.

## 6. Audit object

Preference resolution should not silently delete an attack.

For every basic ABA attack, retain an audit result:

\[
\operatorname{Resolve}_{\mathfrak P_N}(attack)
=
(
attack,
status,
blockingPreferences
).
\]

where:

\[
status\in\{\text{defeat},\text{blocked}\}.
\]

If blocked:

\[
blockingPreferences
=
\{
(\alpha,\beta):
\alpha\in\operatorname{Supp}(source),
\alpha<\beta
\}.
\]

This makes preference-sensitive loss of license inspectable.

## 7. Example

Let:

\[
a\vdash\overline b
\]

so an argument supported by \(a\) attacks assumption \(b\).

Without preferences:

\[
A_a\leadsto A_b.
\]

If:

\[
a<b,
\]

then under the implemented regime:

\[
A_a\not\hookrightarrow_{\mathfrak P_N}A_b.
\]

The attack is recorded as blocked because the attacker depends on an assumption strictly less preferred than the attacked assumption.

Under **full ABA+**, the conflict may instead become a reverse attack from the \(b\)-side toward the \(a\)-side. That behavior is intentionally outside the binary regime implemented here.

## 8. Relationship to warrant

This provides the first clean preference-sensitive defeasible warrant path:

\[
\text{support}
\to
\text{basic attack}
\to
\mathfrak P_N\text{-filtered defeat}
\to
\text{Dung acceptability}
\to
\text{warrant/license}.
\]

So a warrant certificate can lose dialectical acceptability because:

- a successful defeater appears; or
- a preference change makes a previously blocked attack succeed.

Conversely, strengthening preference for an attacked assumption can block a defeat.

The preference relation is therefore part of the warrant regime/context, not a truth value attached to the proposition.

## 9. Full ABA+ remains explicitly preserved

Full ABA+ is not discarded.

It is tracked as an architectural escalation path in GitHub issue #18.

Escalate when:

- attack reversal itself matters to a concrete warrant case;
- set-to-set attacks change outcomes;
- collective attack/defense becomes necessary;
- a benchmark explicitly requires faithful ABA+ semantics.

At that point, evaluate a HYPAF/set-to-set layer rather than modifying binary edges ad hoc.

## 10. Derivation structure remains a separate escalation

Issue #17 separately tracks first-class derivation/subargument structure.

These are independent escalation axes:

\[
\boxed{
\text{proof-structure richness}
\neq
\text{collective preference/attack richness}.
}
\]

A future system might need one, both, or neither.

## 11. Implementation

The ABA module now includes:

- AssumptionPreferences
- transitive strict-preference closure
- cycle validation
- ABAAttackResolution
- resolve_attacks
- preference_filtered_attacks
- to_preference_defeat_framework

The existing Dung DefeatFramework remains unchanged.

## 12. Current architecture

\[
\boxed{
\begin{array}{c}
\textbf{minimal positive support}
\\
\downarrow
\\
\textbf{basic ABA attack construction}
\\
\downarrow
\\
\textbf{preference regime }\mathfrak P_N
\\
\downarrow
\\
\textbf{binary defeat graph}
\\
\downarrow
\\
\textbf{Dung grounded semantics}
\\
\downarrow
\\
\textbf{defeasible warrant/license}
\end{array}
}
\]

with two documented escalation branches:

\[
\begin{array}{ll}
\text{issue \#17:} & \text{first-class derivation/subargument structure}\\
\text{issue \#18:} & \text{full ABA+ / set-to-set hyperargumentation}
\end{array}
\]

## 13. Next step

Now that preference-sensitive binary defeat is explicit, the next research task is to connect acceptability to the warrant judgment and exercise the whole pipeline on concrete cases.

That is preferable to adding another argumentation formalism before a benchmark shows it is needed.
