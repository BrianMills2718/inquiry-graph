# ABA versus ASPIC+: six-case architecture benchmark

> **Status:** decision benchmark. This document tests the two structured-argumentation families against concrete requirements from the current inquiry meta-model. The goal is not to choose a universally superior framework; it is to determine the smallest faithful bridge from the existing ATMS-style support layer into structured defeat.

## 1. Decision rule

Use the weakest framework that represents every distinction we actually need **without systematic semantic distortion**.

For each case, distinguish:

- **native** — the distinction exists explicitly in the formalism;
- **systematic encoding** — representable by a uniform translation with recoverable meaning;
- **extension** — requires a recognized extension such as ABA+;
- **lossy unless annotated** — representable extensionally, but the original attack locus/type is not recoverable without extra metadata.

The benchmark tests:

1. assumption conflict;
2. simple rebuttal;
3. rule undercutting;
4. premise attack;
5. preference-sensitive conflict;
6. strict versus defeasible inference.

## 2. Baseline structures

### 2.1 Current project state

The project already has:

\[
\lambda(h)\in\mathsf{Supp}(X)
\]

where support is a finite antichain of minimal assumption environments.

Arguments therefore naturally have the shape:

\[
A=(\Gamma\vdash c)
\]

with explicit assumption support \(\Gamma\).

This is structurally close to ABA.

### 2.2 ABA

An ABA framework has:

- a deductive system/rule set;
- a distinguished set of assumptions;
- a contrary mapping for assumptions.

An argument is a deduction supported by assumptions.

An argument attacks another when its conclusion is the contrary of an assumption in the target's support.

Thus ABA intentionally reduces attack to attacks on assumptions.

### 2.3 ASPIC+

ASPIC+ explicitly represents:

- axioms and ordinary premises;
- strict inference rules;
- defeasible inference rules;
- arguments as structured inference trees;
- contraries/contradictories;
- preferences;
- attack locations.

Its core attack types are:

- rebuttal;
- undercutting;
- undermining.

Attacks are subsequently resolved into defeats, potentially using preferences.

## 3. Case 1 — assumption conflict

### Requirement

An argument for \(h\) depends on assumption \(a\):

\[
A_1:\{a\}\vdash h.
\]

Another argument derives the contrary of \(a\):

\[
A_2:\Gamma\vdash \overline a.
\]

We need \(A_2\) to attack \(A_1\).

### ABA

This is exactly the native ABA attack rule:

\[
\operatorname{conc}(A_2)=\overline a
\quad\Rightarrow\quad
A_2\leadsto A_1.
\]

**Classification: native.**

It maps directly onto the current minimal-assumption support representation.

### ASPIC+

Represent \(a\) as an ordinary/defeasible premise and construct an argument concluding its contrary. The resulting conflict can be represented as an undermining attack.

**Classification: native, but richer than required.**

### Benchmark result

No semantic distinction forces ASPIC+ here.

For the current support architecture, ABA has the lower representation gap.

## 4. Case 2 — simple rebuttal

### Requirement

Two defeasible arguments conclude incompatible claims:

\[
A_1:\Gamma_1\Rightarrow h,
\qquad
A_2:\Gamma_2\Rightarrow\neg h.
\]

The conflict is specifically conclusion-versus-conclusion.

### ASPIC+

This is native rebuttal: an argument attacks a subargument whose top defeasible conclusion conflicts with the attacker's conclusion.

**Classification: native.**

The attack location remains explicit.

### ABA

Basic ABA only attacks assumptions.

To encode a defeasible conclusion \(h\), introduce an assumption representing the defeasible availability of the inference, for example:

\[
d_r
\]

with:

\[
h\leftarrow p,d_r.
\]

The contrary argument attacks \(d_r\), or an analogous assumption underlying the conclusion.

This is a systematic encoding strategy, not an isolated hack.

However, after projection to ordinary ABA attack, the fact that the original conflict was a **rebuttal of a conclusion** is not intrinsically recoverable.

**Classification: systematic encoding; lossy unless attack-origin metadata is retained.**

### Benchmark result

ABA can execute the conflict, but ASPIC+ represents the attack locus directly.

Therefore the project should retain typed attack-origin metadata even if ABA constructs the attack.

## 5. Case 3 — rule undercutting

### Requirement

We have:

\[
p\Rightarrow_r h.
\]

New information does **not** support \(\neg h\). Instead, it says rule \(r\) is inapplicable or unreliable in this case.

This distinction is foundational for the warrant model.

### ASPIC+

Defeasible rules are named. An argument concluding the contrary of the rule's applicability/name undercuts the inference step.

**Classification: native.**

No opposing conclusion \(\neg h\) is needed.

### ABA

Reify applicability of \(r\) as an assumption:

\[
app(r)
\]

and rewrite:

\[
h\leftarrow p,app(r).
\]

An undercutter derives:

\[
\overline{app(r)}.
\]

Then ordinary ABA assumption attack blocks the argument.

This is systematic and compositional.

But after flattening, ABA sees an attack on an assumption. The semantic distinction

\[
\text{undercut rule }r
\]

is recoverable only because the assumption was explicitly typed as a rule-applicability assumption.

**Classification: systematic encoding; faithful if typed applicability assumptions are preserved.**

### Benchmark result

This is the key case.

ABA is not semantically inadequate if the translation contract says:

\[
\boxed{
\text{defeasible rule applicability}
\mapsto
\text{typed ABA assumption}
}
\]

and preserves the origin metadata.

Without that contract, the encoding becomes opaque.

## 6. Case 4 — premise attack

### Requirement

An argument depends on an uncertain ordinary premise \(p\), and another argument attacks \(p\).

### ASPIC+

This is native undermining.

**Classification: native.**

### ABA

If \(p\) is an ABA assumption, a contrary of \(p\) attacks any argument supported by \(p\).

**Classification: native for defeasible assumptions.**

If the project wants a separate ontological distinction between "ordinary premise" and "assumption," that distinction must be retained as metadata or represented above ABA.

### Benchmark result

Both frameworks cover the behavior directly.

ASPIC+ names the premise role more richly; ABA aligns more directly with the existing assumption environments.

## 7. Case 5 — preference-sensitive conflict

### Requirement

Two arguments attack each other, but a declared preference determines whether an attack succeeds as a defeat.

Examples include:

- source priority;
- rule priority;
- more-specific rule;
- explicit assumption preference.

### ASPIC+

Preferences are part of the framework's intended architecture. Attack and defeat are explicitly distinct.

**Classification: native.**

### Basic ABA

Basic ABA has no primitive preference ordering.

Preferences can be encoded into rules/assumptions, which is part of the ABA philosophy described in the comparative literature.

**Classification: systematic encoding, but no longer minimal if preferences are common.**

### ABA+

ABA+ extends ABA with preferences over assumptions and modifies/reverses attack according to those preferences.

**Classification: extension.**

### Benchmark result

If preference-sensitive conflicts are rare, basic ABA plus an explicit upstream resolver is adequate.

If assumption preferences become central, ABA+ is the natural minimal extension.

If preferences target arbitrary rules, premises and argument structures, ASPIC+ is more direct.

## 8. Case 6 — strict versus defeasible inference

### Requirement

The representation must distinguish:

\[
p\to q
\]

as strict/truth-preserving relative to the logic from:

\[
r\Rightarrow s
\]

as defeasible.

Attack behavior should respect the distinction.

### ASPIC+

Strict and defeasible rules are primitive categories.

**Classification: native.**

### ABA

ABA has a deductive rule system plus defeasible assumptions.

A defeasible rule can be compiled into a strict rule whose applicability depends on a defeasible assumption:

\[
s\leftarrow r,d_s.
\]

Thus the distinction can be represented as:

\[
\text{strict rule}
\quad\text{vs}\quad
\text{strict rule + defeasible applicability assumption}.
\]

**Classification: systematic encoding.**

Again, the original distinction remains recoverable if the generated assumption carries typed provenance back to the defeasible rule.

### Benchmark result

ABA can represent the semantics using a uniform translation.

ASPIC+ exposes the distinction directly.

## 9. Comparison matrix

| Case | ABA | ASPIC+ | Information-preserving requirement |
|---|---|---|---|
| Assumption contrary | native | native | none beyond ordinary provenance |
| Conclusion rebuttal | systematic encoding | native | preserve "rebut" origin |
| Rule undercut | systematic encoding | native | typed rule-applicability assumption |
| Premise attack | native when premise is assumption | native undermine | preserve premise/assumption role if needed |
| Preferences | ABA+/encoding | native | explicit preference provenance |
| Strict vs defeasible rules | systematic encoding | native | map generated applicability assumption back to rule |

## 10. Does the benchmark force an exclusive choice?

No.

The benchmark exposes a factorization that is more useful than "ABA versus ASPIC+."

The frameworks optimize different coordinates:

\[
\boxed{
\text{ABA}
\approx
\text{assumption-centred executable attack construction}
}
\]

while:

\[
\boxed{
\text{ASPIC+}
\approx
\text{explicit structured-inference and attack-location model}
}
\]

The ASPIC+ tutorial itself notes that ABA can be formalized within ASPIC+, while the ABA philosophy systematically translates defeasible rules, preferences, rebutting and undercutting behavior into rules plus assumptions so attacks reduce to premise attack.

That is precisely the tradeoff observed in the six cases.

## 11. Architecture decision

The benchmark supports the following current architecture:

\[
\boxed{
\begin{array}{c}
\textbf{ATMS / minimal support}\\
\lambda(h)\in\mathsf{Supp}(X)
\\[4pt]
\downarrow
\\[4pt]
\textbf{ABA-like executable bridge}\\
\text{rules + assumptions + contraries}
\\[4pt]
\downarrow
\\[4pt]
\textbf{typed attack-origin metadata}\\
\text{rebut / undercut / undermine}
\\[4pt]
\downarrow
\\[4pt]
\textbf{attack-to-defeat resolution}\\
\text{preferences when present}
\\[4pt]
\downarrow
\\[4pt]
\textbf{Dung semantics}\\
\text{grounded initially}
\end{array}
}
\]

with **ASPIC+ as the richer reference model for structured attack semantics**.

So the current decision is:

\[
\boxed{
\textbf{implement ABA first, but do not flatten away ASPIC+-level distinctions.}
}
\]

This is not a claim that ABA is universally preferable.

It is a claim about the current project's minimal bridge from an already assumption-centric support representation.

## 12. Why this is not an encoding hack

A translation is acceptable when it is:

1. uniform;
2. compositional;
3. semantics-preserving for the target questions;
4. reversible enough to recover the distinctions the project cares about.

For defeasible rule \(r\), use a generated assumption:

\[
\alpha_r=\operatorname{applicable}(r)
\]

and translate:

\[
p_1,\ldots,p_n\Rightarrow_r q
\]

into:

\[
q\leftarrow p_1,\ldots,p_n,\alpha_r.
\]

An undercutter derives:

\[
\overline{\alpha_r}.
\]

If \(\alpha_r\) retains:

- source rule \(r\);
- role = rule-applicability;
- original rule type = defeasible;

then the original undercut is recoverable.

The unacceptable version would introduce anonymous assumptions with no typed provenance and later pretend all assumption attacks have the same semantics.

## 13. Implementation consequence

The deliberately small ABA core is now implemented as `src/inquiry_graph/aba.py`:

\[
\mathcal B=(L,R,A,\overline{\cdot})
\]

supporting:

- facts/rules;
- assumptions;
- contraries;
- argument construction;
- attacks induced by derived contraries.

Generated assumptions should carry a role/type such as:

- ordinary defeasible premise;
- rule applicability;
- preference guard.

Attack objects should retain their reconstructed structured origin:

- undermine;
- undercut;
- rebut.

The existing defeat framework remains downstream. `ABAFramework.to_defeat_framework()` projects basic-ABA attacks to the Dung layer because basic ABA has no preference-sensitive attack-to-defeat filter.

The implementation computes a least Horn closure annotated with the existing minimal-support antichains. It then quotients ABA deductions by **conclusion + minimal assumption environment**. This intentionally discards proof multiplicity, matching the project's current support-provenance semantics. If future argument comparison needs distinct proof trees with the same conclusion/support set, this quotient must be refined.

## 14. Revisit conditions

Escalate from the ABA-first bridge toward a fuller ASPIC+ executable model when one or more of these become common:

1. preferences over arbitrary rules rather than assumptions;
2. multiple conflict points inside deep argument trees must be inspected directly;
3. argument comparison depends materially on strict/defeasible subargument structure;
4. translation-generated assumptions dominate the representation;
5. users need explanations in native structured-rule vocabulary rather than translated assumption vocabulary;
6. benchmark cases show loss of information even with typed translation provenance.

Until then, implementing the richer framework wholesale would add machinery without yet supplying a demonstrated missing distinction.

## 15. Bottom line

The six cases do **not** yield:

\[
ABA\;\text{or}\;ASPIC+.
\]

They yield:

\[
\boxed{
\text{ABA execution substrate}
+
\text{ASPIC+-compatible semantic metadata}
+
\text{Dung acceptability}.
}
\]

That is the current minimal, compositional architecture.
