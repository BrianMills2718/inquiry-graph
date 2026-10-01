# NYC-QC-1 recovered six-hearing qualitative result

Status: authentic method-owned run recovered; pipeline completed; independent claim-discipline review completed; **not separately recorded as human-accepted for Workbench integration**.

## Provenance

- QC project: `544fad18-e10e-4fef-9443-3d6299c2ef24`
- project name: `NYC CRZ six-hearing Describe accepted-candidate`
- project artifact SHA-256: `f3e24515c7fcb3b5ac471d422b1e73fb938a93d2664d4e0554f793b45a9bf0bc`
- pipeline status: `completed`
- completed phases: ingest, thematic coding, perspective, relationship, synthesis, cross-interview, negative-case analysis
- segments: 58,798
- claims: 11,803
- observed patterns: 43
- six frozen hearing documents: 2022-08-25, 08-27, 08-28, 08-29, 08-30, 08-31
- independent claim-discipline review SHA-256: `d6627b34b90029e9595144aa9b6f2113654fb3dd6528c6d960e1a5bd160f5be0`
- reviewer: GPT-5.6 Luna
- producer: DeepSeek V4 Flash
- review trace: `qualitative_coding/claim_discipline_review/544fad18-e10e-4fef-9443-3d6299c2ef24/20260914T185939Z`

The independent reviewer assessed 34 synthesis-level outputs: **22 violated at least one declared claim limit and 12 were compliant**. The original overclaiming language is therefore not promoted below.

## Declared analytic question

> What concerns, support, affected groups, alternatives, contradictions, and variation appear across the six frozen August 2022 NYC congestion relief zone hearings?

Intended use: descriptive mapping.

Predeclared non-claims:

- no population prevalence or representativeness claim;
- no causal effect or policy-effect claim;
- no inference that absence of a code means absence of the underlying concern;
- no policy recommendation inferred from theme frequency.

## Bounded findings retained after independent review

### 1. MTA management and fiscal trust

**Retained finding:** In these hearings, speakers raised concerns about the MTA's fiscal responsibility, citing alleged mismanagement and describing congestion pricing as a money grab rather than a solution to congestion.

The raw synthesis said the distrust was “pervasive” and that speakers “consistently” made the argument. Those prevalence-like formulations were rejected.

Representative internal anchors:
- application `81e0e8e8-02c5-42d4-b122-2479e609ff18`, hearing 2022-08-25, quote hash `ca5c469e...`
- application `1c7ccd07-ff38-4fa8-9a1a-e268827b597b`, hearing 2022-08-31, quote hash `45d49aa7...`

### 2. Economic-burden arguments

**Retained finding:** Speakers in these hearings described the program as imposing a regressive economic burden, using calculations of the toll's annual cost to argue that it would create severe hardship for low-income, middle-class, and fixed-income individuals, particularly essential workers and seniors.

The raw “widely perceived” and “will cause” wording was rejected as prevalence and policy-effect overclaiming.

Representative internal anchors span at least hearings 2022-08-25, 08-27, and 08-30.

### 3. Transit alternatives and necessity of driving

**Retained finding:** A counter-narrative in the hearings challenged the assumption that people can switch to transit, citing reliability, safety, accessibility, disability, night-work, and transit-desert concerns.

The independent reviewer found this synthesis compliant as a description of the hearing discourse, not a finding that transit is objectively inadequate for the population.

Representative internal anchors span hearings 2022-08-25, 08-27, and 08-28.

### 4. Taxi and for-hire-vehicle concerns

**Retained finding:** A distinct body of testimony from taxi and for-hire-vehicle drivers or advocates argued that the toll would harm their industry, including in the context of existing surcharges and post-pandemic recovery.

This is a description of testimony, not an estimated industry-wide effect.

Representative internal anchors span hearings 2022-08-25, 08-27, and 08-31.

### 5. Exemption proposals

**Retained finding:** Requests for exemptions recurred in the hearings, including proposals concerning people with disabilities and vehicles transporting them, CBD residents, and particular services or vehicles.

The raw synthesis's “central theme” / “near-consensus” formulation was rejected.

The cross-interview artifact records anchored applications for disability-exemption, resident-exemption, and service/vehicle-exemption codes in all six hearing documents. That is a **document-coverage fact**, not a population-prevalence estimate.

### 6. Congestion-diversion and environmental-justice concerns

**Retained finding:** Speakers raised concerns that tolling could shift traffic and pollution to surrounding neighborhoods and environmental-justice communities, including areas around the Cross Bronx Expressway.

This reports a concern in the hearing record. It does not establish that diversion occurred or caused health effects.

Representative internal anchors span hearings 2022-08-25, 08-27, and 08-31.

### 7. Support existed and was sometimes conditional

**Retained finding:** Support for congestion pricing was present in the hearings, including arguments about environmental and transit benefits; some supportive testimony also raised concerns about equity, design, or MTA management.

This is important variation against a one-sided reading of the corpus.

The support code has anchored application evidence in all six loaded hearing documents. Again, this is corpus coverage, not a statement about public-opinion prevalence.

### 8. Criticism of the hearing process

**Retained finding:** Speakers criticized the hearing process as rushed, poorly timed, or insufficiently reaching some non-English-speaking and minority communities; some speakers said these features undermined the legitimacy of the input process.

The original synthesis's direct “delegitimizing” effect language was rejected and replaced with attributed speaker claims.

## Cross-hearing variation and disagreement

The method output preserves several tensions rather than forcing a single position:

- support for congestion pricing as an environmental/transit tool versus opposition framing it as regressive or a revenue grab;
- support in principle paired with concerns about equity, exemptions, or MTA accountability;
- claims that driving is necessary for work, medical care, disability, or caregiving versus the policy premise that some trips can shift to transit;
- concern about congestion/pollution diversion versus arguments that the program could improve environmental conditions;
- demands for broad exemptions versus concern that too many exemptions could weaken the program's objectives;
- a recorded case of openness to a well-designed congestion-pricing policy while opposing features of the specific proposal.

These are within-corpus analytical contrasts, not estimates of how common each view was in the broader population.

## Negative-case / challenge search

The final negative-case stage examined:

- 250 claim-candidate links;
- 110 unique retrieved source passages;
- 50 claim targets;
- retrieval mode: lexical BM25 across codes, followed by model interpretation.

It found no disconfirming passage **within that targeted retrieved sample**.

This is not promoted to “there were no negative cases in the hearings.” The method's own memo explicitly says absence in this sample does not establish absence in the full corpus. Conditional and mixed support remain meaningful variation.

## Rejected recommendation behavior

The raw synthesis generated recommendations such as:
- create an MTA oversight board;
- adopt disability/resident exemptions;
- fund transit improvements;
- create taxi/FHV assistance;
- extend outreach;
- commission diversion/health studies;
- lower the toll or add rebates.

The independent reviewer rejected these as analyst recommendations because the declared design forbids deriving policy recommendations from theme frequency.

They may only be retained as **proposals voiced by some hearing participants**, where source-grounded.

## Source-custody status

The frozen source-unit receipt covers:
- 6 exact hearing PDFs;
- 2,179 PDF pages;
- 54,475 court-reporter printed-line atoms;
- exact source SHA-256 per hearing;
- exact line-atom/content hashes;
- no source-unit validation failures.

The project-level synthesis links retained findings to code-application IDs containing hearing document identity, quote text, character offsets, speaker attribution, and quote SHA-256.

## What this result establishes

It establishes a method-produced, source-anchored qualitative description of themes, proposals, support, concerns, and variation in the **six-hearing corpus**.

It does **not** establish:
- NYC population opinion;
- prevalence among affected groups;
- causal or realized policy effects;
- whether a concern later materialized;
- what policy should be chosen.

## Integration status

The earlier NYC baseline labeled `NYC-QC-1` as missing. That is now known to be stale project-state information.

Corrected status:

> **method-owned result exists and completed; independent claim-discipline review exists; separate human acceptance / Workbench integration remains unverified.**

The historical baseline should not be rewritten. Downstream work should add this result as a new discovered artifact/version and selectively reopen the “missing qualitative result” dependency.
