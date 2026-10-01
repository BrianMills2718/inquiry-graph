# Independent C5 adversarial recheck: 2026-09-30

**Decision reviewed:** use archive-search-then-read as the default for the
measured 30-chat, 13-question workload; retain linker data for the topic map.

**Verdict: REJECTED.** The cached scores and source checks reproduce, but two
gates do not support the recommendation:

1. **Validity: fail, partial evidence.** The reviewer could not authenticate or
   rerun the cited fresh grader control under its no-new-LLM-call constraint.
   Read-only lookup across three campaign databases and 15 local
   process-tracing databases found no row for the cited
   `inquiry-graph/c5-signoff/grader-positive-control` trace. The previous
   control aggregate is not execution-verifiable from the available databases.
2. **Bounded decision: fail.** `scale.py` answers A one question per call but
   answers all 13 questions in one call for each of B and C. The retrieval
   difference is therefore confounded with call granularity and cross-question
   context.

The reviewer independently recomputed the reported scores and heldout subset;
those matched the report. All 30 graphs validated, all 581 retained key quotes
were reverified, and the seven heldout IDs matched the artifact across all five
categories. These checks do not remove the batching confound or certify broad
generalization. A literal answer-evidence audit found only 9/33 A, 0/27 B, and
0/28 C quoted spans in the expected source messages; this is a literal check,
not semantic citation validation. The report itself limits the answer contract.

Fresh replay requirements: run B and C one question per call, matching A;
measure source-retrieval recall alongside answer coverage; run an
execution-verifiable fresh grader control; and obtain another independent
signoff before restoring any retrieval recommendation. The replay plan is
[`balanced-replay-2026-09-30.md`](balanced-replay-2026-09-30.md).
