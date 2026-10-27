window.PAGE_DATA = {
 "manifest": {
  "schema_version": "1.0",
  "record_type": "planning_package",
  "repository": "BrianMills2718/inquiry-graph",
  "subject_revision": "4a8bba0e96d5aa4115a67507b26acb810e6ac7cf",
  "request": "Company Planning compliance workflow, 2026-10-27 (workflow-computed task, run for Brian; his standing request, 2026-10-25: \"i have asked 100s of times to make ure that my proejcts are always company plannign complaint\"): build the first planning package for inquiry-graph. This lane touched only docs/planning/, the review page and one wiki link, because another session may own the rest of the repository. docs/planning/run_checks.sh reruns the checks into docs/planning/checks.txt.",
  "parts": {
   "checks": {
    "status": "present",
    "path": "docs/planning/checks.txt",
    "results": [
     {
      "name": "wiki rule (Markdown cap, reachability, layout, durable documents)",
      "command": "python3 $HOME/code/project-meta/scripts/md_file_cap.py --repo .",
      "exit_status": 1,
      "counts": {
       "markdown_files": 109,
       "cap": 100,
       "orphans": 19,
       "layout_findings": 0,
       "layout_undeclared": 1,
       "durable_findings": 1,
       "findings": 3
      },
      "tracked_by": "Q1"
     },
     {
      "name": "durable documents (arc42)",
      "command": "python3 $HOME/code2/company-planning/plugins/company-planning/scripts/durable_docs_check.py --repo . --arc42",
      "exit_status": 1,
      "counts": {
       "findings": 1,
       "stale": 1
      },
      "tracked_by": "Q2"
     },
     {
      "name": "project navigation",
      "command": "python3 $HOME/code2/company-planning/plugins/company-planning/scripts/validate_project_navigation.py .",
      "exit_status": 0,
      "counts": {
       "findings": 0,
       "delegated": 2
      },
      "note": "report-only; wiki/index.md delegated to the wiki rule, docs/roadmap.md accepted as the native roadmap"
     },
     {
      "name": "plan adoption recheck",
      "command": "python3 $HOME/code2/company-planning/plugins/company-planning/scripts/method_conformance/cli.py lint --repo-root . --recheck",
      "exit_status": 1,
      "counts": {
       "current": 0,
       "stale": 3,
       "finished": 0
      },
      "tracked_by": "Q3",
      "note": "all three plans are delivered (R4); they still say status: proposed, so the recheck counts them stale"
     },
     {
      "name": "plan lint, each adopted plan against its own adoption record",
      "command": "python3 $HOME/code2/company-planning/plugins/company-planning/scripts/method_conformance/cli.py lint --repo-root . --plan <plan> (coding-sessions, report-relations-rescore, session-launch-kind)",
      "exit_status": 0,
      "counts": {
       "plans_passed": 3,
       "plans_failed": 0,
       "checks_passed": 490,
       "checks_failed": 0
      }
     },
     {
      "name": "repository check (make check: trace, sources, import contracts, OpenSpec, pytest, artifact drift, seed validation, architecture, test-first)",
      "command": "make check",
      "exit_status": 0,
      "counts": {
       "tests_passed": 171,
       "tests_skipped": 2,
       "failed": 0,
       "import_contracts_kept": 19,
       "import_contracts_broken": 0,
       "specs_valid": 7,
       "seed_validation_errors": 0
      }
     },
     {
      "name": "typed-graph/v1 schema (domain graph and open-questions map)",
      "command": "python3 with jsonschema.Draft202012Validator over the two graphs against $HOME/code2/representation-router/schemas/typed-graph.schema.json (code in docs/planning/run_checks.sh)",
      "exit_status": 0,
      "counts": {
       "graphs_valid": 2,
       "graphs_invalid": 0
      }
     },
     {
      "name": "doc reachability (the repository's own pre-commit docs check)",
      "command": "python3 $HOME/code2/workspace/scripts/doc_reachability.py",
      "exit_status": 0,
      "counts": {
       "reachable": 103,
       "unreachable": 0,
       "tracked_md": 103
      },
      "note": "8 documents were unreachable at ef9a5ce; this package linked them from docs/index.md"
     }
    ]
   },
   "open_questions": {
    "status": "present",
    "path": "docs/planning/open-questions.json"
   },
   "system_model": {
    "status": "present",
    "path": "docs/planning/system-model.md",
    "executes_typed_rules": false,
    "basis": "src/inquiry_graph/validate.py:67"
   },
   "domain_model": {
    "status": "present",
    "path": "docs/planning/domain.graph.json",
    "glossary": "docs/planning/DOMAIN.md",
    "implemented": {
     "conversation": "src/inquiry_graph/model.py:27",
     "participant": "src/inquiry_graph/model.py:12",
     "message": "src/inquiry_graph/model.py:18",
     "anchor": "src/inquiry_graph/model.py:36",
     "content-node": "src/inquiry_graph/model.py:54",
     "question": "src/inquiry_graph/model.py:51",
     "task": "src/inquiry_graph/model.py:50",
     "work": "src/inquiry_graph/model.py:50",
     "relation": "src/inquiry_graph/model.py:70",
     "binding": "src/inquiry_graph/model.py:59",
     "relation-signature": "src/inquiry_graph/model.py:136",
     "move": "src/inquiry_graph/model.py:82",
     "inference-family": "src/inquiry_graph/model.py:89",
     "stance-event": "src/inquiry_graph/model.py:92",
     "question-event": "src/inquiry_graph/model.py:99",
     "open-question-agenda": "src/inquiry_graph/views.py:23",
     "review-status": "src/inquiry_graph/model.py:43",
     "extraction": "src/inquiry_graph/model.py:110",
     "candidates": "src/inquiry_graph/model.py:118",
     "graph": "src/inquiry_graph/model.py:126",
     "quarantine": "src/inquiry_graph/io.py:177",
     "coding-session": "src/inquiry_graph/coding_session.py:104",
     "launch-kind": "src/inquiry_graph/coding_session.py:34",
     "reply-fields": "src/inquiry_graph/coding_session.py:183",
     "closure-word": "src/inquiry_graph/coding_session.py:38",
     "resume-digest": "src/inquiry_graph/coding_session.py:244",
     "brian-position": "tools/ask_positions.py:22",
     "position-link": "src/inquiry_graph/linker.py:40",
     "topic-map": "tools/position_topics.py:91",
     "topic-name": "tools/name_topics.py:23"
    }
   },
   "diagrams": {
    "status": "present",
    "items": [
     {
      "path": "docs/model/ARCHITECTURE.md",
      "question": "Who and what does Inquiry Graph work with (Brian, agents, chat exports, llm_client, onto-canon6), and which blocks inside it write and read the canonical JSON? (context view, section 3, and containers, section 5)"
     },
     {
      "path": "docs/planning/domain.graph.json",
      "question": "What does a conversation become in Inquiry Graph (source records, content, relations, moves, stance and question events, sessions, positions), which of those does this repository implement, and how do they relate?"
     },
     {
      "path": "docs/planning/open-questions.graph.json",
      "question": "Which questions are still open, whose call is each, what does each block, and which concepts does it bear on?"
     }
    ]
   },
   "plan": {
    "status": "present",
    "path": "docs/planning/next-plan.md",
    "relies_on": [
     "coding-session",
     "launch-kind",
     "reply-fields",
     "resume-digest",
     "brian-position",
     "topic-map",
     "topic-name",
     "extraction",
     "quarantine",
     "conversation"
    ]
   },
   "review_page": {
    "status": "present",
    "path": "proposals/planning-package/review-page/index.html",
    "url": "https://hive.brianmills.dev/plans/inquiry-graph/main/proposals/planning-package/review-page/index.html"
   },
   "cold_review": {
    "status": "present",
    "path": "docs/planning/cold-review.md",
    "verdict": "revise",
    "reviewed_revision": "PLACEHOLDER"
   }
  }
 },
 "questions": [
  {
   "id": "Q1",
   "short": "Wiki rule: 109 docs, 19 unreachable",
   "question": "How should the repository get back under the wiki rule: 109 Markdown files against a cap of 100, and 19 reader documents not reachable from wiki/index.md within two links (for example evaluation/terminal_state/README.md)?",
   "blocks": "whether the wiki-compliance check (md_file_cap.py) can exit 0, which the package's checks part needs",
   "resolves_with": "Argument, no test: either archive superseded handoffs and evaluation notes into docs/archive/ (the rule counts them too) and link the live ones from wiki/index.md, or add .md-file-cap.yaml with a limit and a reason the evaluation records must stay as files. Pick by reading which of the 19 are still read; the check's own output names them.",
   "owner": "agent",
   "status": "open",
   "sources": [
    "docs/planning/checks.txt",
    "wiki/index.md:1",
    "docs/index.md:52"
   ],
   "touches": [
    "conversation"
   ]
  },
  {
   "id": "Q2",
   "short": "Stale rule review: live grounding",
   "question": "Does RULE-LIVE-GROUNDING still describe live_extract.py after the commit that changed its owner file since the rule was last reviewed (8b063a0)?",
   "blocks": "whether the durable-documents check can exit 0 and whether the trace can be trusted for live extraction",
   "resolves_with": "Reading settles it: on 2026-10-27 the rule still holds on reading (quotes are located at src/inquiry_graph/live_extract.py:88, wrong-speaker items dropped in convert at :302, prune_to_valid at :439). What remains is setting reviewed_at on the rule in docs/model/trace.yaml, outside this package's lane.",
   "owner": "agent",
   "status": "open",
   "sources": [
    "docs/model/trace.yaml:85",
    "src/inquiry_graph/live_extract.py:439"
   ],
   "touches": [
    "extraction",
    "anchor"
   ]
  },
  {
   "id": "Q3",
   "short": "Three delivered plans still say proposed",
   "question": "Should the three adopted plans (coding-sessions, report-relations-rescore, session-launch-kind), all delivered, have their front-matter status set to done so the plan-adoption recheck stops counting them as stale?",
   "blocks": "whether the plan-adoption recheck can exit 0",
   "resolves_with": "Argument: R4 shows all three are delivered, and a finished plan keeps the method it was adopted under, so re-running check against bounded-design@18 is not needed. Setting status: done in each plan's front matter (docs/plans/, outside this lane) clears the check.",
   "owner": "agent",
   "status": "open",
   "sources": [
    "docs/plans/coding-sessions.md:6",
    "docs/plans/report-relations-rescore.md:5",
    "docs/plans/session-launch-kind.md:6"
   ],
   "touches": [
    "coding-session",
    "launch-kind"
   ]
  },
  {
   "id": "Q4",
   "short": "Two system models, drifted line citations",
   "question": "Which document is the system model, and when are its line citations repaired? .agentic/repo.yaml names docs/model/ARCHITECTURE.md, docs/index.md calls it an earlier document replaced by arc42.md, and its runtime view cites lines that moved (ingest io.py:120 is now :126, quarantine io.py:171 is now :177, cli run :70 is now :81).",
   "blocks": "whether a new agent can follow the runtime view to the right code, and which file the next system-model change edits",
   "resolves_with": "Argument: keep ARCHITECTURE.md as the runtime and record-type model (arc42.md points back to it for the runtime view) and correct its line numbers; the package's docs/planning/system-model.md carries the current lines until then.",
   "owner": "agent",
   "status": "open",
   "sources": [
    ".agentic/repo.yaml:8",
    "docs/index.md:38",
    "docs/model/ARCHITECTURE.md:93",
    "docs/architecture/arc42.md:39",
    "src/inquiry_graph/io.py:126"
   ],
   "touches": [
    "graph",
    "quarantine",
    "candidates"
   ]
  },
  {
   "id": "Q5",
   "short": "Nightly positions map red: topic naming",
   "question": "Why do topic-name calls through the Codex CLI fail (149 of 867 on 2026-10-26, 481 on 2026-10-19), and why did one night need 867 names and 5.2 hours although names carry over between builds?",
   "blocks": "whether the nightly session import and positions map stay green, which is how the brian-positions skill stays current (the next plan)",
   "resolves_with": "Running settles it, not an evaluation: reproduce one failing call with the full stderr (the concern keeps only its first line), then compare the previous and new topics.json to see what the carry-over matched. See docs/planning/next-plan.md step 1.",
   "owner": "agent",
   "status": "open",
   "sources": [
    "tools/nightly_sessions.py:86",
    "tools/name_topics.py:51",
    "tools/name_topics.py:99",
    "https://github.com/BrianMills2718/inquiry-graph/issues/227",
    "https://github.com/BrianMills2718/inquiry-graph/issues/229"
   ],
   "touches": [
    "topic-map",
    "topic-name",
    "coding-session"
   ]
  },
  {
   "id": "Q6",
   "short": "extract-or-run restart loop",
   "question": "Is the OpenRouter extraction run behind extract-or-run.service finished (disable the unit) or still wanted (give it a capture contract)? On 2026-10-27 the unit was still in auto-restart, refused at every start for --budget 25 without --contract.",
   "blocks": "how issue #191 closes, and whether the full-archive extraction resumes",
   "resolves_with": "Reading settles it: inspect private/extract_full_20261003/or_run for remaining queue items. See docs/planning/next-plan.md step 2.",
   "owner": "agent",
   "status": "open",
   "sources": [
    "tools/extract_queue.py:71",
    "https://github.com/BrianMills2718/inquiry-graph/issues/191"
   ],
   "touches": [
    "extraction",
    "brian-position"
   ]
  },
  {
   "id": "Q7",
   "short": "798 or 858 proposed annotations",
   "question": "How many proposed annotations does the founding seed hold?",
   "blocks": "which number issue #3's review covers",
   "resolves_with": "Counting settles it: examples/seed/graph.json holds 250 nodes, 250 relations, 204 moves, 68 stance events and 86 question events, 858 records, all proposed (counted 2026-10-27), matching README.md:7. The 798 at docs/project-status.md:67 and docs/verification.md:131 predates the 2026-09-30 continuation. Open only until those two lines are corrected (outside this lane).",
   "owner": "agent",
   "status": "open",
   "sources": [
    "README.md:7",
    "docs/project-status.md:67",
    "docs/verification.md:131"
   ],
   "touches": [
    "review-status"
   ]
  },
  {
   "id": "Q8",
   "short": "Project status page is stale",
   "question": "When is docs/project-status.md brought up to date? It reports 67 tests (make check ran 171 passed, 2 skipped on 2026-10-27), says issue #2 should still be closed (it is closed), and does not mention the coding-session import, the positions map or the nightly pipeline.",
   "blocks": "whether a new agent can trust the status page instead of rediscovering state",
   "resolves_with": "Argument: rewrite the status page from the live checks in docs/planning/checks.txt and this ledger; no test is needed.",
   "owner": "agent",
   "status": "open",
   "sources": [
    "docs/project-status.md:75",
    "docs/project-status.md:94",
    "docs/planning/checks.txt"
   ],
   "touches": [
    "graph"
   ]
  },
  {
   "id": "Q9",
   "short": "Extract moves for the archive?",
   "question": "Should the archive of 2,176 graphs get moves (how Brian argues) through the moves prompt live extraction now has behind a switch? No archive graph has moves today.",
   "blocks": "any use of reasoning motifs or move sequences across conversations (tools/mine_motifs.py works only on the hand-built fixtures)",
   "resolves_with": "A priority call, not a test: it costs a full re-extraction. The stop rule says no ontology expansion without a concrete product failure; moves are already in the ontology, so the question is only whether a consumer needs them.",
   "owner": "brian",
   "recommendation": "Not now: no consumer needs moves today; revisit when a named use (for example 'how does Brian usually challenge a claim') is asked for.",
   "default": "The archive stays without moves; the switch stays off.",
   "status": "open",
   "sources": [
    "docs/project-status.md:118",
    "src/inquiry_graph/live_extract.py:35",
    "docs/project-status.md:105"
   ],
   "touches": [
    "move",
    "strategy-episode",
    "inference-family"
   ]
  },
  {
   "id": "Q10",
   "short": "Reconcile the seed and review 858 records?",
   "question": "Should the curated founding seed be reconciled against the full ChatGPT export and its 858 proposed annotations reviewed by a person (issue #3)?",
   "blocks": "whether the seed can ever be called source-complete or confirmed, and depends on a fresh export reaching the laptop (issue #205)",
   "resolves_with": "A priority call: only a person confirms records (ADR-004), so it costs Brian's review time; no argument settles whether that time is worth it.",
   "owner": "brian",
   "recommendation": "Leave it unscheduled: the seed is a labelled curated fixture, the product value is the archive-wide positions memory, and nothing reads the seed as confirmed.",
   "default": "The seed stays all proposed and labelled not source-complete; issue #3 stays open.",
   "status": "open",
   "sources": [
    "docs/project-status.md:63",
    "docs/project-status.md:69",
    "https://github.com/BrianMills2718/inquiry-graph/issues/3"
   ],
   "touches": [
    "review-status",
    "conversation"
   ]
  },
  {
   "id": "Q11",
   "short": "Run the five-condition reader benchmark (#225)?",
   "question": "Should the five-condition terminal-state reader benchmark (issue #225: does the corrected extractor improve an independent reader's resumption accuracy on the 2026-10-18 conversation) be run with live models?",
   "blocks": "whether the 2026-10-18 extractor task and status corrections are judged by reader accuracy, and whether any schema change is considered for resumption",
   "resolves_with": "Prior art and argument first: the roadmap forbids another benchmark without explicit approval, and the harness's own README says a schema change is considered only if existing elements cannot encode the terminal state, which the deterministic part already showed they can. A run would change one decision, whether to keep investing in resumption from graphs versus reading the raw tail; it is a single conversation, so it cannot generalize.",
   "owner": "brian",
   "recommendation": "Do not run it now; the deterministic result already settles the schema question, and a one-conversation reader score would not change the roadmap.",
   "default": "Issue #225 stays open and unrun; PR #218's protocol stays unmerged until someone needs it.",
   "status": "open",
   "sources": [
    "docs/roadmap.md:29",
    "evaluation/terminal_state/README.md:49",
    "https://github.com/BrianMills2718/inquiry-graph/issues/225"
   ],
   "touches": [
    "question-event",
    "task",
    "open-question-agenda",
    "extraction"
   ]
  },
  {
   "id": "Q12",
   "short": "Export watcher depends on a flaky browser",
   "question": "How should new ChatGPT exports reach the laptop when the watcher scrapes Gmail through a robot browser that is often down (it missed a ready export for 8 days)?",
   "blocks": "whether new chats ever reach the positions memory, and issue #3's reconciliation",
   "resolves_with": "Prior art: read Gmail through an API or connector instead of the browser, and raise a keyed concern when the check cannot run. See docs/planning/next-plan.md step 3.",
   "owner": "agent",
   "status": "open",
   "sources": [
    "tools/watch_chatgpt_export.sh:2",
    "https://github.com/BrianMills2718/inquiry-graph/issues/205"
   ],
   "touches": [
    "conversation",
    "brian-position"
   ]
  },
  {
   "id": "Q13",
   "short": "Four open research PRs from 2026-10-16 to 10-18",
   "question": "Are open pull requests #211, #216, #217 and #218 still wanted, given #219 to #226 merged the terminal-state and semantic-factorization work after them (#216 and #217 now conflict with main)?",
   "blocks": "whether the evaluation records in those branches land or are closed as superseded",
   "resolves_with": "Reading settles most of it: compare each branch's files with main. Whether to keep the research captures (#211 benchmark-design inquiry, #216 Hets smoke test) is Brian's interest, so the recommendation goes to him.",
   "owner": "brian",
   "recommendation": "Merge #218 with #225 only if the benchmark is approved (Q11); close #216 and #217 as superseded if their files are already on main, otherwise rebase them; leave #211 for Brian.",
   "default": "All four stay open; nothing is lost.",
   "status": "open",
   "sources": [
    "https://github.com/BrianMills2718/inquiry-graph/pull/211",
    "https://github.com/BrianMills2718/inquiry-graph/pull/216",
    "https://github.com/BrianMills2718/inquiry-graph/pull/217",
    "https://github.com/BrianMills2718/inquiry-graph/pull/218",
    "evaluation/terminal_state/README.md:1"
   ],
   "touches": [
    "conversation",
    "task"
   ]
  },
  {
   "id": "R1",
   "short": "Is there an outside consumer?",
   "question": "Does any consumer outside this repository use the positions for a decision (the third disproof condition of the thesis)?",
   "blocks": "whether the thesis's consumer condition is already failed",
   "resolves_with": "Reading settled it.",
   "owner": "agent",
   "status": "resolved",
   "evidence": "Yes: the shared brian-positions skill in agent-skills runs tools/brian_positions.py (agent-skills skills/brian-positions/SKILL.md:18) and its description tells agents to use it before asking Brian what he thinks. Whether answers from it change decisions is not measured; the consumer exists.",
   "sources": [
    "docs/architecture/GOAL.md:76",
    "/home/brian/code2/agent-skills/skills/brian-positions/SKILL.md:18"
   ],
   "touches": [
    "brian-position"
   ]
  },
  {
   "id": "R2",
   "short": "Graph or archive search for answers?",
   "question": "Should answers to cross-chat questions come from the graph route or from archive search then read?",
   "blocks": "which route agents use for general answer retrieval",
   "resolves_with": "Settled by the recorded 30-chat result.",
   "owner": "agent",
   "status": "resolved",
   "evidence": "Archive search then read is the default for that workload (0.67 against 0.63 and 0.61 key-point coverage), independently signed off; the graph is kept for attribution, open questions and history.",
   "sources": [
    "docs/project-status.md:48",
    "docs/project-status.md:50"
   ],
   "touches": [
    "brian-position",
    "position-link"
   ]
  },
  {
   "id": "R3",
   "short": "Does the code execute typed rules?",
   "question": "Does Inquiry Graph evaluate typed rules, so that its system model needs a metamodel mapped onto the shared kernel?",
   "blocks": "system_model.executes_typed_rules and whether a metamodel is owed",
   "resolves_with": "Reading the code and the metamodel reference settled it.",
   "owner": "agent",
   "status": "resolved",
   "evidence": "No. Relations have named roles, but SIGNATURES only constrains which node kinds each role may bind and validate() checks shape (src/inquiry_graph/validate.py:67-82); no relation carries a formula, condition or effect that is evaluated, which is the trigger in bounded-design's typed-relational-metamodels reference. A kernel crosswalk exists as PR #15, kept unmerged on purpose.",
   "sources": [
    "src/inquiry_graph/model.py:136",
    "src/inquiry_graph/validate.py:67",
    "docs/roadmap.md:63"
   ],
   "touches": [
    "relation",
    "relation-signature",
    "binding"
   ]
  },
  {
   "id": "R4",
   "short": "Are the three adopted plans finished?",
   "question": "Are the adopted plans coding-sessions, report-relations-rescore and session-launch-kind finished, or still in progress under bounded-design@13?",
   "blocks": "whether the stale recheck means re-adopting them under the current profile",
   "resolves_with": "Reading the code and results settled it.",
   "owner": "agent",
   "status": "resolved",
   "evidence": "All three are delivered: import-session and sessions are CLI commands (src/inquiry_graph/cli.py:64-68); headless launches are labelled automated (src/inquiry_graph/coding_session.py:31-35); the re-score is recorded (C2 0.62 against old C 0.63, evaluation/usefulness_pilot/results.md:74). Each plan lints PASS against its own adoption record. A finished plan keeps the method it was adopted under, so no re-adoption is needed; only the front-matter status is wrong (Q3).",
   "sources": [
    "src/inquiry_graph/cli.py:64",
    "src/inquiry_graph/coding_session.py:31",
    "evaluation/usefulness_pilot/results.md:74"
   ],
   "touches": [
    "coding-session",
    "launch-kind",
    "relation"
   ]
  },
  {
   "id": "R5",
   "short": "Merge historical PRs #8 and #15?",
   "question": "Should the historical PR stack #8 and #15 be merged?",
   "blocks": "whether the formal inquiry substrate and kernel crosswalk enter main",
   "resolves_with": "The docs already decide it.",
   "owner": "agent",
   "status": "resolved",
   "evidence": "No: both are intentionally separate historical trajectories, not to be merged casually (docs/roadmap.md:63, docs/project-status.md:79).",
   "sources": [
    "docs/roadmap.md:63",
    "docs/project-status.md:79"
   ],
   "touches": [
    "canonical-identity"
   ]
  }
 ],
 "fixed_here": [],
 "domain": {
  "schema": "typed-graph/v1",
  "kinds": {
   "Source": {
    "label": "Source record",
    "color": "#3b6fa8",
    "explain": "What is actually in the conversation, before any interpretation."
   },
   "Content": {
    "label": "Content",
    "color": "#5a87bf",
    "explain": "What was said: concepts, claims, questions, tasks and other content nodes."
   },
   "Argument": {
    "label": "Relations",
    "color": "#7fa3cf",
    "explain": "Role-typed connections between content, each grounded in a quote."
   },
   "Process": {
    "label": "Inquiry process and state",
    "color": "#d9822b",
    "explain": "Who did what (moves), and actor-relative stance and question-status histories."
   },
   "Review": {
    "label": "Extraction and review",
    "color": "#7a8491",
    "explain": "How records were produced, checked, kept apart from bad output and confirmed."
   },
   "Session": {
    "label": "Coding sessions",
    "color": "#a8642b",
    "explain": "Claude Code and Codex session records read as conversations with tasks."
   },
   "Cross": {
    "label": "Across conversations",
    "color": "#4a525c",
    "explain": "Brian's verbatim positions gathered from many graphs, linked and mapped by topic."
   },
   "Elsewhere": {
    "label": "Elsewhere or theory only",
    "color": "#9aa3ad",
    "explain": "Named in the docs but owned by another repository, or not a record type yet."
   }
  },
  "layout": {
   "direction": "RIGHT",
   "algorithm": "layered"
  },
  "nodes": [
   {
    "id": "conversation",
    "label": "Conversation",
    "kind": "Source",
    "explain": "One visible transcript (chat export, bridge capture, meeting or coding session) with its participants, ordered messages and a coverage note saying what was left out. Source: src/inquiry_graph/model.py:27."
   },
   {
    "id": "participant",
    "label": "Participant",
    "kind": "Source",
    "explain": "A speaker in a conversation, with role user, assistant or other. Source: src/inquiry_graph/model.py:12."
   },
   {
    "id": "message",
    "label": "Message",
    "kind": "Source",
    "explain": "One visible turn: speaker, ordinal and exact text; the only thing quotes are checked against. Source: src/inquiry_graph/model.py:18."
   },
   {
    "id": "anchor",
    "label": "Anchor",
    "kind": "Source",
    "explain": "A quote with its message id and Unicode start and end offsets; it must equal the message text at those offsets. Source: src/inquiry_graph/model.py:36."
   },
   {
    "id": "content-node",
    "label": "Content node",
    "kind": "Content",
    "explain": "Something said, of kind concept, claim, question, hypothesis, method, example, goal, reference, task or work; not the same as an utterance. Source: docs/ontology.md:16."
   },
   {
    "id": "question",
    "label": "Question",
    "kind": "Content",
    "explain": "A content node of kind question; whether it is open is recorded by question events, never by the node itself. Source: docs/ontology.md:20."
   },
   {
    "id": "task",
    "label": "Task",
    "kind": "Content",
    "explain": "A unit of work an agent lists as open in a coding session; carries the same status events as a question, plus dropped. Source: docs/ontology.md:18."
   },
   {
    "id": "work",
    "label": "Work",
    "kind": "Content",
    "explain": "A delivered product (a pull request, a commit) seen in a tool record of a coding session. Source: docs/ontology.md:18."
   },
   {
    "id": "relation",
    "label": "Relation",
    "kind": "Argument",
    "explain": "A reified, grounded connection of one of 13 kinds (supports, challenges, answers, supersedes...) whose players are bound by role; it can itself be challenged. Source: docs/ontology.md:22."
   },
   {
    "id": "binding",
    "label": "Role binding",
    "kind": "Argument",
    "explain": "One (role, ref) pair of a relation, such as premise -> a claim id. Source: src/inquiry_graph/model.py:59."
   },
   {
    "id": "relation-signature",
    "label": "Relation signature",
    "kind": "Argument",
    "explain": "For each relation kind, the roles it must have and the node kinds each role may bind; checked by validate(). Source: docs/ontology.md:26."
   },
   {
    "id": "move",
    "label": "Inquiry move",
    "kind": "Process",
    "explain": "An act by one participant (ask, clarify, challenge, retract, reframe ... 15 kinds) with inputs, outputs, the message it happened at and previous moves. Source: docs/ontology.md:44."
   },
   {
    "id": "inference-family",
    "label": "Inference family",
    "kind": "Process",
    "explain": "Optional label on a move: induction, abduction, deduction or unspecified; the seed leaves it unspecified on purpose. Source: docs/ontology.md:50."
   },
   {
    "id": "stance-event",
    "label": "Stance event",
    "kind": "Process",
    "explain": "One participant's stance (posits, endorses, questions, rejects, suspends, retracts) toward a target, at a message; content is never belief without one. Source: src/inquiry_graph/model.py:92."
   },
   {
    "id": "question-event",
    "label": "Question event",
    "kind": "Process",
    "explain": "A status change of a question or task (open, answered, resolved, deferred, superseded, reopened, dropped) by one actor, at a message. Source: src/inquiry_graph/model.py:99."
   },
   {
    "id": "open-question-agenda",
    "label": "Open-question agenda",
    "kind": "Process",
    "explain": "The view of which questions are still open for which actor, folded from question events; an assistant's answer does not close a user's question. Source: src/inquiry_graph/views.py:23."
   },
   {
    "id": "review-status",
    "label": "Grounded record and review status",
    "kind": "Review",
    "explain": "Every semantic record carries anchors, an origin (explicit or inferred) and review status proposed, confirmed or rejected; extraction output is always proposed. Source: src/inquiry_graph/model.py:43."
   },
   {
    "id": "extraction",
    "label": "Extraction record",
    "kind": "Review",
    "explain": "How a graph's annotations were produced: method, provider, model, prompt version and notes. Source: src/inquiry_graph/model.py:110."
   },
   {
    "id": "candidates",
    "label": "Candidates",
    "kind": "Review",
    "explain": "The proposed nodes, relations, moves and events from one extraction, before they are ingested into a graph. Source: src/inquiry_graph/model.py:118."
   },
   {
    "id": "graph",
    "label": "Inquiry graph",
    "kind": "Review",
    "explain": "The canonical JSON record: conversations, all records, extractions and notes; written exclusively, never silently replaced. Source: src/inquiry_graph/model.py:126."
   },
   {
    "id": "quarantine",
    "label": "Quarantine",
    "kind": "Review",
    "explain": "The private folder where a failed extraction's raw response and error go, so bad output never replaces a graph. Source: src/inquiry_graph/io.py:177."
   },
   {
    "id": "coding-session",
    "label": "Coding session",
    "kind": "Session",
    "explain": "A Claude Code or Codex .jsonl session normalized into a conversation; prompts from headless runs are given to an automation participant. Source: src/inquiry_graph/coding_session.py:104."
   },
   {
    "id": "launch-kind",
    "label": "Launch kind (typed or automated)",
    "kind": "Session",
    "explain": "Whether a person or a program typed a session's prompts, read from Claude Code entrypoint and Codex originator values. Source: src/inquiry_graph/coding_session.py:31."
   },
   {
    "id": "reply-fields",
    "label": "End-of-reply fields",
    "kind": "Session",
    "explain": "The Session goal, Active subgoals, Done and Need anything from human lines an agent ends each reply with, read into tasks and question events. Source: src/inquiry_graph/coding_session.py:41."
   },
   {
    "id": "closure-word",
    "label": "Closure word",
    "kind": "Session",
    "explain": "The fixed word in 'Closed: <item> (<word>)' that maps to a task status (done -> resolved, put off -> deferred ...). Source: docs/ontology.md:18."
   },
   {
    "id": "resume-digest",
    "label": "Resume digest",
    "kind": "Session",
    "explain": "Per session: goals, open, unknown-status and closed items, delivered work and requests waiting on Brian. Source: src/inquiry_graph/coding_session.py:244."
   },
   {
    "id": "brian-position",
    "label": "Brian position",
    "kind": "Cross",
    "explain": "A stance or question event whose actor and anchored speaker are Brian and whose quote is verbatim in that message; the evidence unit agents ask for. Source: tools/ask_positions.py:4."
   },
   {
    "id": "position-link",
    "label": "Cross-conversation link",
    "kind": "Cross",
    "explain": "A judged pair of positions or questions Brian expressed in different conversations, proposed by embedding recall then a model judgment. Source: src/inquiry_graph/linker.py:40."
   },
   {
    "id": "topic-map",
    "label": "Positions topic map",
    "kind": "Cross",
    "explain": "Brian's statements from chats and session prompts embedded and clustered into nested topics after the fact (topics are not stored on records). Source: wiki/index.md:29."
   },
   {
    "id": "topic-name",
    "label": "Topic name",
    "kind": "Cross",
    "explain": "A short model-written name for one topic of the map, carried over between builds when the topic barely changed. Source: tools/name_topics.py:23."
   },
   {
    "id": "strategy-episode",
    "label": "Strategy episode",
    "kind": "Elsewhere",
    "explain": "A reusable reasoning strategy and its occurrences; not a record type: stored as method and example nodes joined by part_of and exemplifies. Source: docs/ontology.md:54.",
    "dashed": true
   },
   {
    "id": "canonical-identity",
    "label": "Cross-source identity and conflict",
    "kind": "Elsewhere",
    "explain": "Deciding that records from different sources are the same thing, aligning them and detecting tension; owned by onto-canon6, which consumes these graphs. Source: docs/architecture/GOAL.md:48.",
    "dashed": true
   },
   {
    "id": "warrant",
    "label": "Warrant (support and defeat theory)",
    "kind": "Elsewhere",
    "explain": "A formal theory of when support beats challenge; moved to epistemic-warrant on 2026-09-29 and reached only through tools/warrant_adapter.py. Source: docs/architecture/GOAL.md:87.",
    "dashed": true
   }
  ],
  "edges": [
   {
    "id": "e0",
    "source": "participant",
    "target": "conversation",
    "label": "takes part in"
   },
   {
    "id": "e1",
    "source": "message",
    "target": "conversation",
    "label": "is part of"
   },
   {
    "id": "e2",
    "source": "message",
    "target": "participant",
    "label": "is spoken by"
   },
   {
    "id": "e3",
    "source": "anchor",
    "target": "message",
    "label": "quotes exact offsets of"
   },
   {
    "id": "e4",
    "source": "content-node",
    "target": "anchor",
    "label": "is grounded by"
   },
   {
    "id": "e5",
    "source": "question",
    "target": "content-node",
    "label": "is a kind of"
   },
   {
    "id": "e6",
    "source": "task",
    "target": "content-node",
    "label": "is a kind of"
   },
   {
    "id": "e7",
    "source": "work",
    "target": "content-node",
    "label": "is a kind of"
   },
   {
    "id": "e8",
    "source": "relation",
    "target": "binding",
    "label": "binds players through"
   },
   {
    "id": "e9",
    "source": "binding",
    "target": "content-node",
    "label": "plays"
   },
   {
    "id": "e10",
    "source": "relation-signature",
    "target": "relation",
    "label": "constrains roles of"
   },
   {
    "id": "e11",
    "source": "move",
    "target": "participant",
    "label": "is done by"
   },
   {
    "id": "e12",
    "source": "move",
    "target": "content-node",
    "label": "takes inputs and gives outputs"
   },
   {
    "id": "e13",
    "source": "inference-family",
    "target": "move",
    "label": "labels"
   },
   {
    "id": "e14",
    "source": "stance-event",
    "target": "participant",
    "label": "is held by"
   },
   {
    "id": "e15",
    "source": "stance-event",
    "target": "content-node",
    "label": "targets"
   },
   {
    "id": "e16",
    "source": "question-event",
    "target": "question",
    "label": "changes status of"
   },
   {
    "id": "e17",
    "source": "question-event",
    "target": "task",
    "label": "changes status of"
   },
   {
    "id": "e18",
    "source": "open-question-agenda",
    "target": "question-event",
    "label": "is folded from"
   },
   {
    "id": "e19",
    "source": "review-status",
    "target": "content-node",
    "label": "is carried by every grounded record, like"
   },
   {
    "id": "e20",
    "source": "extraction",
    "target": "candidates",
    "label": "produces"
   },
   {
    "id": "e21",
    "source": "candidates",
    "target": "graph",
    "label": "are ingested into"
   },
   {
    "id": "e22",
    "source": "extraction",
    "target": "quarantine",
    "label": "on failure goes to"
   },
   {
    "id": "e23",
    "source": "graph",
    "target": "conversation",
    "label": "holds"
   },
   {
    "id": "e24",
    "source": "coding-session",
    "target": "conversation",
    "label": "is normalized into"
   },
   {
    "id": "e25",
    "source": "launch-kind",
    "target": "coding-session",
    "label": "labels prompts of"
   },
   {
    "id": "e26",
    "source": "reply-fields",
    "target": "task",
    "label": "become"
   },
   {
    "id": "e27",
    "source": "closure-word",
    "target": "question-event",
    "label": "sets status of"
   },
   {
    "id": "e28",
    "source": "resume-digest",
    "target": "coding-session",
    "label": "summarizes"
   },
   {
    "id": "e29",
    "source": "brian-position",
    "target": "stance-event",
    "label": "is a verbatim Brian-attributed"
   },
   {
    "id": "e30",
    "source": "brian-position",
    "target": "question-event",
    "label": "or a verbatim Brian-attributed"
   },
   {
    "id": "e31",
    "source": "position-link",
    "target": "brian-position",
    "label": "pairs two"
   },
   {
    "id": "e32",
    "source": "topic-map",
    "target": "brian-position",
    "label": "clusters"
   },
   {
    "id": "e33",
    "source": "topic-name",
    "target": "topic-map",
    "label": "labels a topic of"
   },
   {
    "id": "e34",
    "source": "strategy-episode",
    "target": "move",
    "label": "would group"
   },
   {
    "id": "e35",
    "source": "canonical-identity",
    "target": "graph",
    "label": "consumes"
   },
   {
    "id": "e36",
    "source": "warrant",
    "target": "relation",
    "label": "would evaluate"
   }
  ]
 },
 "question_map": {
  "schema": "typed-graph/v1",
  "kinds": {
   "AgentQuestion": {
    "label": "Agent question (checking can settle it)",
    "color": "#3b6fa8",
    "explain": "An open question an agent settles by argument, prior art or a run."
   },
   "BrianQuestion": {
    "label": "Brian's call",
    "color": "#d9822b",
    "explain": "An open question only Brian can decide; it carries a recommendation and a default."
   },
   "Decision": {
    "label": "Decision it blocks",
    "color": "#4a525c",
    "explain": "The decision or next step that waits on the question."
   },
   "Concept": {
    "label": "Domain concept",
    "color": "#9aa3ad",
    "explain": "A concept from docs/planning/domain.graph.json that the question bears on."
   }
  },
  "layout": {
   "direction": "RIGHT",
   "algorithm": "layered"
  },
  "nodes": [
   {
    "id": "Q1",
    "label": "Q1: Wiki rule: 109 docs, 19 unreachable",
    "kind": "AgentQuestion",
    "explain": "How should the repository get back under the wiki rule: 109 Markdown files against a cap of 100 (this package adds 4 more), and 19 reader documents not reachable from wiki/index.md within two links (for example evaluation/terminal_state/README.md)? Settled by: Argument, no test: either archive superseded handoffs and evaluation notes into docs/archive/ (the rule counts them too) and link the live ones from wiki/index.md, or add .md-file-cap.yaml with a limit and a reason the evaluation records must stay as files. Pick by reading which of the 19 are still read; the check's own output names them."
   },
   {
    "id": "Q1-blocks",
    "label": "whether the wiki-compliance check (md_file_cap.py) can exit 0, which the package's checks …",
    "kind": "Decision",
    "explain": "whether the wiki-compliance check (md_file_cap.py) can exit 0, which the package's checks part needs"
   },
   {
    "id": "conversation",
    "label": "Conversation",
    "kind": "Concept",
    "dashed": false,
    "explain": "One visible transcript (chat export, bridge capture, meeting or coding session) with its participants, ordered messages and a coverage note saying what was left out. Source: src/inquiry_graph/model.py:27."
   },
   {
    "id": "Q2",
    "label": "Q2: Stale rule review: live grounding",
    "kind": "AgentQuestion",
    "explain": "Does RULE-LIVE-GROUNDING still describe live_extract.py after the commit that changed its owner file since the rule was last reviewed (8b063a0)? Settled by: Reading settles it: on 2026-10-27 the rule still holds on reading (quotes are located at src/inquiry_graph/live_extract.py:88, wrong-speaker items dropped in convert at :302, prune_to_valid at :439). What remains is setting reviewed_at on the rule in docs/model/trace.yaml, outside this package's lane."
   },
   {
    "id": "Q2-blocks",
    "label": "whether the durable-documents check can exit 0 and whether the trace can be trusted for …",
    "kind": "Decision",
    "explain": "whether the durable-documents check can exit 0 and whether the trace can be trusted for live extraction"
   },
   {
    "id": "extraction",
    "label": "Extraction record",
    "kind": "Concept",
    "dashed": false,
    "explain": "How a graph's annotations were produced: method, provider, model, prompt version and notes. Source: src/inquiry_graph/model.py:110."
   },
   {
    "id": "anchor",
    "label": "Anchor",
    "kind": "Concept",
    "dashed": false,
    "explain": "A quote with its message id and Unicode start and end offsets; it must equal the message text at those offsets. Source: src/inquiry_graph/model.py:36."
   },
   {
    "id": "Q3",
    "label": "Q3: Three delivered plans still say proposed",
    "kind": "AgentQuestion",
    "explain": "Should the three adopted plans (coding-sessions, report-relations-rescore, session-launch-kind), all delivered, have their front-matter status set to done so the plan-adoption recheck stops counting them as stale? Settled by: Argument: R4 shows all three are delivered, and a finished plan keeps the method it was adopted under, so re-running check against bounded-design@18 is not needed. Setting status: done in each plan's front matter (docs/plans/, outside this lane) clears the check."
   },
   {
    "id": "Q3-blocks",
    "label": "whether the plan-adoption recheck can exit 0",
    "kind": "Decision",
    "explain": "whether the plan-adoption recheck can exit 0"
   },
   {
    "id": "coding-session",
    "label": "Coding session",
    "kind": "Concept",
    "dashed": false,
    "explain": "A Claude Code or Codex .jsonl session normalized into a conversation; prompts from headless runs are given to an automation participant. Source: src/inquiry_graph/coding_session.py:104."
   },
   {
    "id": "launch-kind",
    "label": "Launch kind (typed or automated)",
    "kind": "Concept",
    "dashed": false,
    "explain": "Whether a person or a program typed a session's prompts, read from Claude Code entrypoint and Codex originator values. Source: src/inquiry_graph/coding_session.py:31."
   },
   {
    "id": "Q4",
    "label": "Q4: Two system models, drifted line citations",
    "kind": "AgentQuestion",
    "explain": "Which document is the system model, and when are its line citations repaired? .agentic/repo.yaml names docs/model/ARCHITECTURE.md, docs/index.md calls it an earlier document replaced by arc42.md, and its runtime view cites lines that moved (ingest io.py:120 is now :126, quarantine io.py:171 is now :177, cli run :70 is now :81). Settled by: Argument: keep ARCHITECTURE.md as the runtime and record-type model (arc42.md points back to it for the runtime view) and correct its line numbers; the package's docs/planning/system-model.md carries the current lines until then."
   },
   {
    "id": "Q4-blocks",
    "label": "whether a new agent can follow the runtime view to the right code, and which file the …",
    "kind": "Decision",
    "explain": "whether a new agent can follow the runtime view to the right code, and which file the next system-model change edits"
   },
   {
    "id": "graph",
    "label": "Inquiry graph",
    "kind": "Concept",
    "dashed": false,
    "explain": "The canonical JSON record: conversations, all records, extractions and notes; written exclusively, never silently replaced. Source: src/inquiry_graph/model.py:126."
   },
   {
    "id": "quarantine",
    "label": "Quarantine",
    "kind": "Concept",
    "dashed": false,
    "explain": "The private folder where a failed extraction's raw response and error go, so bad output never replaces a graph. Source: src/inquiry_graph/io.py:177."
   },
   {
    "id": "candidates",
    "label": "Candidates",
    "kind": "Concept",
    "dashed": false,
    "explain": "The proposed nodes, relations, moves and events from one extraction, before they are ingested into a graph. Source: src/inquiry_graph/model.py:118."
   },
   {
    "id": "Q5",
    "label": "Q5: Nightly positions map red: topic naming",
    "kind": "AgentQuestion",
    "explain": "Why do topic-name calls through the Codex CLI fail (149 of 867 on 2026-10-26, 481 on 2026-10-19), and why did one night need 867 names and 5.2 hours although names carry over between builds? Settled by: Running settles it, not an evaluation: reproduce one failing call with the full stderr (the concern keeps only its first line), then compare the previous and new topics.json to see what the carry-over matched. See docs/planning/next-plan.md step 1."
   },
   {
    "id": "Q5-blocks",
    "label": "whether the nightly session import and positions map stay green, which is how the …",
    "kind": "Decision",
    "explain": "whether the nightly session import and positions map stay green, which is how the brian-positions skill stays current (the next plan)"
   },
   {
    "id": "topic-map",
    "label": "Positions topic map",
    "kind": "Concept",
    "dashed": false,
    "explain": "Brian's statements from chats and session prompts embedded and clustered into nested topics after the fact (topics are not stored on records). Source: wiki/index.md:23."
   },
   {
    "id": "topic-name",
    "label": "Topic name",
    "kind": "Concept",
    "dashed": false,
    "explain": "A short model-written name for one topic of the map, carried over between builds when the topic barely changed. Source: tools/name_topics.py:23."
   },
   {
    "id": "Q6",
    "label": "Q6: extract-or-run restart loop",
    "kind": "AgentQuestion",
    "explain": "Is the OpenRouter extraction run behind extract-or-run.service finished (disable the unit) or still wanted (give it a capture contract)? On 2026-10-27 the unit was still in auto-restart, refused at every start for --budget 25 without --contract. Settled by: Reading settles it: inspect private/extract_full_20261003/or_run for remaining queue items. See docs/planning/next-plan.md step 2."
   },
   {
    "id": "Q6-blocks",
    "label": "how issue #191 closes, and whether the full-archive extraction resumes",
    "kind": "Decision",
    "explain": "how issue #191 closes, and whether the full-archive extraction resumes"
   },
   {
    "id": "brian-position",
    "label": "Brian position",
    "kind": "Concept",
    "dashed": false,
    "explain": "A stance or question event whose actor and anchored speaker are Brian and whose quote is verbatim in that message; the evidence unit agents ask for. Source: tools/ask_positions.py:4."
   },
   {
    "id": "Q7",
    "label": "Q7: 798 or 858 proposed annotations",
    "kind": "AgentQuestion",
    "explain": "How many proposed annotations does the founding seed hold? Settled by: Counting settles it: examples/seed/graph.json holds 250 nodes, 250 relations, 204 moves, 68 stance events and 86 question events, 858 records, all proposed (counted 2026-10-27), matching README.md:7. The 798 at docs/project-status.md:67 and docs/verification.md:131 predates the 2026-09-30 continuation. Open only until those two lines are corrected (outside this lane)."
   },
   {
    "id": "Q7-blocks",
    "label": "which number issue #3's review covers",
    "kind": "Decision",
    "explain": "which number issue #3's review covers"
   },
   {
    "id": "review-status",
    "label": "Grounded record and review status",
    "kind": "Concept",
    "dashed": false,
    "explain": "Every semantic record carries anchors, an origin (explicit or inferred) and review status proposed, confirmed or rejected; extraction output is always proposed. Source: src/inquiry_graph/model.py:43."
   },
   {
    "id": "Q8",
    "label": "Q8: Project status page is stale",
    "kind": "AgentQuestion",
    "explain": "When is docs/project-status.md brought up to date? It reports 67 tests (make check ran 171 passed, 2 skipped on 2026-10-27), says issue #2 should still be closed (it is closed), and does not mention the coding-session import, the positions map or the nightly pipeline. Settled by: Argument: rewrite the status page from the live checks in docs/planning/checks.txt and this ledger; no test is needed."
   },
   {
    "id": "Q8-blocks",
    "label": "whether a new agent can trust the status page instead of rediscovering state",
    "kind": "Decision",
    "explain": "whether a new agent can trust the status page instead of rediscovering state"
   },
   {
    "id": "Q9",
    "label": "Q9: Extract moves for the archive?",
    "kind": "BrianQuestion",
    "explain": "Should the archive of 2,176 graphs get moves (how Brian argues) through the moves prompt live extraction now has behind a switch? No archive graph has moves today. Recommendation: Not now: no consumer needs moves today; revisit when a named use (for example 'how does Brian usually challenge a claim') is asked for. Default: The archive stays without moves; the switch stays off."
   },
   {
    "id": "Q9-blocks",
    "label": "any use of reasoning motifs or move sequences across conversations (tools/mine_motifs.py …",
    "kind": "Decision",
    "explain": "any use of reasoning motifs or move sequences across conversations (tools/mine_motifs.py works only on the hand-built fixtures)"
   },
   {
    "id": "move",
    "label": "Inquiry move",
    "kind": "Concept",
    "dashed": false,
    "explain": "An act by one participant (ask, clarify, challenge, retract, reframe ... 15 kinds) with inputs, outputs, the message it happened at and previous moves. Source: docs/ontology.md:44."
   },
   {
    "id": "strategy-episode",
    "label": "Strategy episode",
    "kind": "Concept",
    "dashed": true,
    "explain": "A reusable reasoning strategy and its occurrences; not a record type: stored as method and example nodes joined by part_of and exemplifies. Source: docs/ontology.md:54."
   },
   {
    "id": "inference-family",
    "label": "Inference family",
    "kind": "Concept",
    "dashed": false,
    "explain": "Optional label on a move: induction, abduction, deduction or unspecified; the seed leaves it unspecified on purpose. Source: docs/ontology.md:50."
   },
   {
    "id": "Q10",
    "label": "Q10: Reconcile the seed and review 858 records?",
    "kind": "BrianQuestion",
    "explain": "Should the curated founding seed be reconciled against the full ChatGPT export and its 858 proposed annotations reviewed by a person (issue #3)? Recommendation: Leave it unscheduled: the seed is a labelled curated fixture, the product value is the archive-wide positions memory, and nothing reads the seed as confirmed. Default: The seed stays all proposed and labelled not source-complete; issue #3 stays open."
   },
   {
    "id": "Q10-blocks",
    "label": "whether the seed can ever be called source-complete or confirmed, and depends on a fresh …",
    "kind": "Decision",
    "explain": "whether the seed can ever be called source-complete or confirmed, and depends on a fresh export reaching the laptop (issue #205)"
   },
   {
    "id": "Q11",
    "label": "Q11: Run the five-condition reader benchmark (#225)?",
    "kind": "BrianQuestion",
    "explain": "Should the five-condition terminal-state reader benchmark (issue #225: does the corrected extractor improve an independent reader's resumption accuracy on the 2026-10-18 conversation) be run with live models? Recommendation: Do not run it now; the deterministic result already settles the schema question, and a one-conversation reader score would not change the roadmap. Default: Issue #225 stays open and unrun; PR #218's protocol stays unmerged until someone needs it."
   },
   {
    "id": "Q11-blocks",
    "label": "whether the 2026-10-18 extractor task and status corrections are judged by reader …",
    "kind": "Decision",
    "explain": "whether the 2026-10-18 extractor task and status corrections are judged by reader accuracy, and whether any schema change is considered for resumption"
   },
   {
    "id": "question-event",
    "label": "Question event",
    "kind": "Concept",
    "dashed": false,
    "explain": "A status change of a question or task (open, answered, resolved, deferred, superseded, reopened, dropped) by one actor, at a message. Source: src/inquiry_graph/model.py:99."
   },
   {
    "id": "task",
    "label": "Task",
    "kind": "Concept",
    "dashed": false,
    "explain": "A unit of work an agent lists as open in a coding session; carries the same status events as a question, plus dropped. Source: docs/ontology.md:18."
   },
   {
    "id": "open-question-agenda",
    "label": "Open-question agenda",
    "kind": "Concept",
    "dashed": false,
    "explain": "The view of which questions are still open for which actor, folded from question events; an assistant's answer does not close a user's question. Source: src/inquiry_graph/views.py:23."
   },
   {
    "id": "Q12",
    "label": "Q12: Export watcher depends on a flaky browser",
    "kind": "AgentQuestion",
    "explain": "How should new ChatGPT exports reach the laptop when the watcher scrapes Gmail through a robot browser that is often down (it missed a ready export for 8 days)? Settled by: Prior art: read Gmail through an API or connector instead of the browser, and raise a keyed concern when the check cannot run. See docs/planning/next-plan.md step 3."
   },
   {
    "id": "Q12-blocks",
    "label": "whether new chats ever reach the positions memory, and issue #3's reconciliation",
    "kind": "Decision",
    "explain": "whether new chats ever reach the positions memory, and issue #3's reconciliation"
   },
   {
    "id": "Q13",
    "label": "Q13: Four open research PRs from 2026-10-16 to 10-18",
    "kind": "BrianQuestion",
    "explain": "Are open pull requests #211, #216, #217 and #218 still wanted, given #219 to #226 merged the terminal-state and semantic-factorization work after them (#216 and #217 now conflict with main)? Recommendation: Merge #218 with #225 only if the benchmark is approved (Q11); close #216 and #217 as superseded if their files are already on main, otherwise rebase them; leave #211 for Brian. Default: All four stay open; nothing is lost."
   },
   {
    "id": "Q13-blocks",
    "label": "whether the evaluation records in those branches land or are closed as superseded",
    "kind": "Decision",
    "explain": "whether the evaluation records in those branches land or are closed as superseded"
   }
  ],
  "edges": [
   {
    "id": "Q1-to-decision",
    "source": "Q1",
    "target": "Q1-blocks",
    "label": "blocks"
   },
   {
    "id": "Q1-conversation",
    "source": "Q1",
    "target": "conversation",
    "label": "bears on"
   },
   {
    "id": "Q2-to-decision",
    "source": "Q2",
    "target": "Q2-blocks",
    "label": "blocks"
   },
   {
    "id": "Q2-extraction",
    "source": "Q2",
    "target": "extraction",
    "label": "bears on"
   },
   {
    "id": "Q2-anchor",
    "source": "Q2",
    "target": "anchor",
    "label": "bears on"
   },
   {
    "id": "Q3-to-decision",
    "source": "Q3",
    "target": "Q3-blocks",
    "label": "blocks"
   },
   {
    "id": "Q3-coding-session",
    "source": "Q3",
    "target": "coding-session",
    "label": "bears on"
   },
   {
    "id": "Q3-launch-kind",
    "source": "Q3",
    "target": "launch-kind",
    "label": "bears on"
   },
   {
    "id": "Q4-to-decision",
    "source": "Q4",
    "target": "Q4-blocks",
    "label": "blocks"
   },
   {
    "id": "Q4-graph",
    "source": "Q4",
    "target": "graph",
    "label": "bears on"
   },
   {
    "id": "Q4-quarantine",
    "source": "Q4",
    "target": "quarantine",
    "label": "bears on"
   },
   {
    "id": "Q4-candidates",
    "source": "Q4",
    "target": "candidates",
    "label": "bears on"
   },
   {
    "id": "Q5-to-decision",
    "source": "Q5",
    "target": "Q5-blocks",
    "label": "blocks"
   },
   {
    "id": "Q5-topic-map",
    "source": "Q5",
    "target": "topic-map",
    "label": "bears on"
   },
   {
    "id": "Q5-topic-name",
    "source": "Q5",
    "target": "topic-name",
    "label": "bears on"
   },
   {
    "id": "Q5-coding-session",
    "source": "Q5",
    "target": "coding-session",
    "label": "bears on"
   },
   {
    "id": "Q6-to-decision",
    "source": "Q6",
    "target": "Q6-blocks",
    "label": "blocks"
   },
   {
    "id": "Q6-extraction",
    "source": "Q6",
    "target": "extraction",
    "label": "bears on"
   },
   {
    "id": "Q6-brian-position",
    "source": "Q6",
    "target": "brian-position",
    "label": "bears on"
   },
   {
    "id": "Q7-to-decision",
    "source": "Q7",
    "target": "Q7-blocks",
    "label": "blocks"
   },
   {
    "id": "Q7-review-status",
    "source": "Q7",
    "target": "review-status",
    "label": "bears on"
   },
   {
    "id": "Q8-to-decision",
    "source": "Q8",
    "target": "Q8-blocks",
    "label": "blocks"
   },
   {
    "id": "Q8-graph",
    "source": "Q8",
    "target": "graph",
    "label": "bears on"
   },
   {
    "id": "Q9-to-decision",
    "source": "Q9",
    "target": "Q9-blocks",
    "label": "blocks"
   },
   {
    "id": "Q9-move",
    "source": "Q9",
    "target": "move",
    "label": "bears on"
   },
   {
    "id": "Q9-strategy-episode",
    "source": "Q9",
    "target": "strategy-episode",
    "label": "bears on"
   },
   {
    "id": "Q9-inference-family",
    "source": "Q9",
    "target": "inference-family",
    "label": "bears on"
   },
   {
    "id": "Q10-to-decision",
    "source": "Q10",
    "target": "Q10-blocks",
    "label": "blocks"
   },
   {
    "id": "Q10-review-status",
    "source": "Q10",
    "target": "review-status",
    "label": "bears on"
   },
   {
    "id": "Q10-conversation",
    "source": "Q10",
    "target": "conversation",
    "label": "bears on"
   },
   {
    "id": "Q11-to-decision",
    "source": "Q11",
    "target": "Q11-blocks",
    "label": "blocks"
   },
   {
    "id": "Q11-question-event",
    "source": "Q11",
    "target": "question-event",
    "label": "bears on"
   },
   {
    "id": "Q11-task",
    "source": "Q11",
    "target": "task",
    "label": "bears on"
   },
   {
    "id": "Q11-open-question-agenda",
    "source": "Q11",
    "target": "open-question-agenda",
    "label": "bears on"
   },
   {
    "id": "Q11-extraction",
    "source": "Q11",
    "target": "extraction",
    "label": "bears on"
   },
   {
    "id": "Q12-to-decision",
    "source": "Q12",
    "target": "Q12-blocks",
    "label": "blocks"
   },
   {
    "id": "Q12-conversation",
    "source": "Q12",
    "target": "conversation",
    "label": "bears on"
   },
   {
    "id": "Q12-brian-position",
    "source": "Q12",
    "target": "brian-position",
    "label": "bears on"
   },
   {
    "id": "Q13-to-decision",
    "source": "Q13",
    "target": "Q13-blocks",
    "label": "blocks"
   },
   {
    "id": "Q13-conversation",
    "source": "Q13",
    "target": "conversation",
    "label": "bears on"
   },
   {
    "id": "Q13-task",
    "source": "Q13",
    "target": "task",
    "label": "bears on"
   }
  ]
 },
 "context_diagrams": [
  "C4Context\n  title Inquiry Graph system context\n  Person(brian, \"Brian\", \"Supplies exports and reviews proposed records\")\n  Person(agent, \"AI agent\", \"Asks what Brian has said on a topic\")\n  System(ig, \"Inquiry Graph\", \"Import, extract, validate, merge, query and render conversation graphs\")\n  System_Ext(exports, \"Chat exports\", \"ChatGPT, Claude, Gemini exports; chatgpt-bridge and meeting transcripts\")\n  System_Ext(llm, \"llm_client\", \"Shared LLM client: OpenRouter or Codex structured calls with traces\")\n  System_Ext(git, \"Git repository\", \"Canonical graph JSON under examples/ and private/\")\n  System_Ext(onto, \"onto-canon6\", \"Downstream cross-source identity and conflict detection\")\n  Rel(brian, exports, \"exports conversations\")\n  Rel(ig, exports, \"reads visible text\")\n  Rel(ig, llm, \"structured extraction calls\", \"acall_llm_structured\")\n  Rel(ig, git, \"writes canonical JSON exclusively\")\n  Rel(agent, ig, \"tools/ask_positions.py, query open, query trace\")\n  Rel(onto, git, \"consumes graphs\")\n",
  "C4Container\n  title Inquiry Graph containers\n  Container(cli, \"cli.py\", \"argparse\", \"Commands: schema, import*, prepare, extract, validate, merge, query, render\")\n  Container(io, \"io.py\", \"Python\", \"import_export, ingest, merge, write_json, quarantine\")\n  Container(live, \"live_extract.py\", \"llm_client\", \"Chunked live extraction, quote grounding, prune_to_valid\")\n  Container(model, \"model.py\", \"Pydantic\", \"Conversation, Graph, Candidates, relation SIGNATURES\")\n  Container(validate, \"validate.py\", \"Python\", \"Anchors, role signatures, events, cycles\")\n  Container(views, \"views.py / render.py\", \"NetworkX\", \"Open-question agenda, trace, Mermaid, DOT, report, HTML\")\n  Container(ask, \"tools/ask_positions.py\", \"Python\", \"Verbatim-checked Brian positions across graphs\")\n  Container(build, \"tools/build_artifacts.py\", \"Python\", \"Schemas and review artifacts; --check drift gate\")\n  ContainerDb(store, \"Canonical JSON\", \"Git files\", \"examples/seed/graph.json, examples/*/, private/quarantine/\")\n  Rel(cli, io, \"load, ingest, merge, write\")\n  Rel(cli, live, \"--llm extraction\")\n  Rel(cli, validate, \"require_valid\")\n  Rel(cli, views, \"query, render\")\n  Rel(io, store, \"exclusive write\")\n  Rel(ask, store, \"reads graphs\")\n  Rel(build, model, \"model_json_schema\")\n"
 ],
 "disagreements": [
  "The seed's proposed-annotation count is 858 in README.md:7, docs/project-status.md:38 and the seed itself (counted 2026-10-27), but 798 in docs/project-status.md:67 and docs/verification.md:131, which predate the 2026-09-30 continuation (open question Q7).",
  "docs/model/ARCHITECTURE.md cites line numbers that moved: ingest at src/inquiry_graph/io.py:120 is now :126, merge :149 is now :155, quarantine :171 is now :177. The package's system model (docs/planning/system-model.md) uses current lines (Q4).",
  "docs/project-status.md:94 reports 67 tests passed and :75 says issue #2 is still to be closed; on 2026-10-27 make check ran 171 passed, 2 skipped, and issue #2 is closed (Q8).",
  ".agentic/repo.yaml names docs/model/ARCHITECTURE.md as the system model, while docs/index.md lists it among 'Earlier documents' replaced by docs/architecture/arc42.md and the specs. Both are still read; arc42.md points back to ARCHITECTURE.md for the runtime view, so neither alone is the model (Q4).",
  "docs/project-status.md:118 says the archive holds 0 moves because live extraction skips them; live_extract.py now has a moves prompt behind a switch (src/inquiry_graph/live_extract.py:35), but no archive run used it (Q9)."
 ],
 "next_plan": "\n# Next plan: keep the positions memory current\n\nPlanning package: docs/planning/planning-package.json\n\nAnswers open questions: Q5, Q6, Q12\n\nStatus: proposed on 2026-10-27 by the planning-package agent. It is ordinary agent-owned repair work\n(open questions Q5, Q6 and Q12 are all `owner: agent`); in `~/code2` a change this size needs no\nadopted design plan, the pull request is the record (`~/code2/AGENTS.md`). If the work grows beyond\nthe three steps below, adopt it first under `bounded-design`.\n\n## Why this is next\n\nThe one capability of this repository that has a consumer outside it is the positions memory:\nthe `brian-positions` skill runs `tools/brian_positions.py` over Brian's verbatim positions and,\nwith `--sessions`, over what he typed in coding sessions (open question R1). That memory is only as\ncurrent as the private pipeline that feeds it, and on 2026-10-27 that pipeline is red in three\nplaces:\n\n1. `inquiry-graph-nightly.service` has failed since 2026-10-26 08:35. Session import worked (1,133\n   imported) and both map builds exited 0, but 149 of 867 topic names failed with\n   `CODEX_CLI_ERROR` and the naming step alone took 18,690 s (5.2 h). More than 20 failed names\n   fails the step (`tools/nightly_sessions.py:86`). Issues #227 and #229.\n2. `extract-or-run.service` restarts every few seconds: `tools/extract_queue.py` refuses a run with\n   `--budget 25` and no `--contract` (`tools/extract_queue.py:71`), and the unit predates that rule.\n   Issue #191, open since 2026-10-07.\n3. The ChatGPT export watcher scrapes Gmail through a robot browser that is often down; it missed a\n   ready export for 8 days and the link went stale (issue #205). New chats stop reaching the\n   positions memory without anyone being told.\n\nThe other open questions are either Brian's priority calls (Q10, Q11, Q13) or small documentation\nrepairs (Q1 to Q4, Q7, Q8) that any session can do; none blocks this plan.\n\n## Steps\n\n1. **Topic naming.** Reproduce one failing `name_topics.py` call with the full Codex CLI stderr\n   (the concern keeps only its first line). Fix the cause where it originates (llm_client's Codex\n   transport, or the naming call's working directory and sandbox options,\n   `tools/name_topics.py:31`-`:33`). Then find out why 867 topics needed names on one night although names\n   are carried over from the previous build when a topic barely changed (`tools/name_topics.py:51`,\n   threshold 0.5); if the carry-over is not matching, fix it so a nightly run names only new topics. Record per-call traces through llm_client as today (`trace_id=\"inquiry-graph/name-topics\"`).\n2. **extract-or-run.** Read `private/extract_full_20261003/or_run` to learn whether that run is\n   finished. If finished, disable the unit and say so on #191; if not, write its capture contract\n   (`tools/capture_contract.py`) and add `--contract` to the unit.\n3. **Export watcher.** Replace the browser scrape with a Gmail read through an API or connector that\n   does not depend on the robot browser, and alert (keyed concern) when the check itself cannot run.\n\n## Done when\n\n- Two consecutive nightly runs end with `systemctl --user is-failed inquiry-graph-nightly.service`\n  printing `inactive` (not `failed`), each log under `private/logs/` showing fewer than 20 failed\n  names, and a sample of five named topics read against their records (names match the quotes).\n- `systemctl --user status extract-or-run.service` shows the unit disabled or running under a\n  contract, not `auto-restart`.\n- The watcher's log shows a successful check that did not use the robot browser.\n- Issues #227, #229, #191 and #205 are closed with that evidence, and the planning package is\n  rebuilt at the merge revision.\n\n## Domain concepts it relies on\n\n`coding-session`, `launch-kind`, `reply-fields`, `resume-digest`, `brian-position`, `topic-map`,\n`topic-name`, `extraction`, `quarantine`, `conversation` (see [DOMAIN.md](https://github.com/BrianMills2718/inquiry-graph/blob/main/docs/planning/DOMAIN.md)). All are\nimplemented; the plan changes how they are produced on schedule, not what they are.\n\n## Not in scope\n\nNo schema change, no new evaluation, and no change to what the map shows. The five-condition reader\nbenchmark (#225) is Brian's call (Q11).\n",
 "cold_review": "\n# Cold review\n\nPending: the first review has not run yet.\n\nVerdict: revise\n",
 "evidence_links": {
  "checks.txt (full output of every check)": "https://github.com/BrianMills2718/inquiry-graph/blob/main/docs/planning/checks.txt",
  "cold-review.md (independent review)": "https://github.com/BrianMills2718/inquiry-graph/blob/main/docs/planning/cold-review.md",
  "planning-package.json (the manifest)": "https://github.com/BrianMills2718/inquiry-graph/blob/main/docs/planning/planning-package.json",
  "open-questions.json (the ledger)": "https://github.com/BrianMills2718/inquiry-graph/blob/main/docs/planning/open-questions.json",
  "system-model.md (system model: record types, writers, nightly pipeline)": "https://github.com/BrianMills2718/inquiry-graph/blob/main/docs/planning/system-model.md",
  "ARCHITECTURE.md (context, blocks, runtime)": "https://github.com/BrianMills2718/inquiry-graph/blob/main/docs/model/ARCHITECTURE.md",
  "DOMAIN.md (domain glossary)": "https://github.com/BrianMills2718/inquiry-graph/blob/main/docs/planning/DOMAIN.md",
  "next-plan.md (the next plan)": "https://github.com/BrianMills2718/inquiry-graph/blob/main/docs/planning/next-plan.md"
 },
 "built_from": "4a8bba0",
 "checks_commit": "4a8fa90"
};
