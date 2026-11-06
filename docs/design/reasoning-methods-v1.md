# Brian's reasoning methods, v1 (draft for Brian's review)

Status: draft by an agent, 2026-10-06. Nothing here is confirmed by Brian. His keep / cut / reword marks are the review. No chat quotes are stored in git; dated examples live in `private/moves_labels/` and are shown to Brian in conversation.

How to read: an **instance** is something Brian did once; a **method** is a general move many instances share; a **policy** is a standing rule, kept apart (see `docs/design/semantic-spectrum-and-motifs.md` and the AES terms list `docs/terms/ecosystem-terms.md`). Moves are not a rung on the formalization ladder; where a move acts on one or two of the seven axes it may be a primitive, a move that spans several is probably a composition (hypothesis).

## Methods

| # | Method (one line) | In-house move kinds | Closest published term | Evidence in the archive | Confidence |
|---|---|---|---|---|---|
| M4 | Ask for a concrete example or specific case to ground an abstraction | request_example (gap move; Jev label) | Polya "specialize"; accountable-talk "say more" family | 223 messages, 136 chats, 2024 to 2026 (29 / 185 / 9); hand-checked sample 7 of 8 | High |
| M6 | Step back to the overall goal; police scope ("are we drifting?") | step_back (gap move), scope | Schoenfeld "monitor"; Thinking Moves "back / zoom out"; Lakatos exception-barring (for scope) | 87 labelled, 47 after a second check; 35 chats; 2024 to 2026 (9 / 29 / 9); sample 7 of 8 | High |
| M5 | Test an abstraction operationally ("how would it be assessed or used?") | test | Gandhi 2025 verification; Schoenfeld "verify"; Schon move-testing experiment | 42 labelled, 22 after second check; 19 chats; sample 5 of 8 | Medium |
| M1 | Define a thing by its role or intent, not its intrinsic nature | define_by_role (gap move) | No standard move; nearest is Walton "argument from definition" | 21 labelled, 12 after second check, but only 4 chats (2025 to 2026); sample 7 of 8 with two duplicates | Medium-low |
| M8 | Factor a whole into primitives, then check for too many or too few parts ("canonical factorization") | decompose, factor_and_check (gap move) | Gandhi "subgoal setting" and Polya "decompose and recombine" cover the splitting half; the check half has no standard term | 27 labelled, 7 after second check, 7 chats; sample 5 of 7; Brian also describes it in his own words as core to how he thinks (chat 6ab8563b) | Low from counts, medium from his statement |
| M2 | Treat a frame or boundary as a hypothesis and test it by acting | frame_as_hypothesis (gap move; a subtype of test) | Schon "frame experiment" | 6 messages in 6 chats; only 1 of 6 is genuine | Not established |
| M3 | Separate describing a thing from playing it well | (none; closest distinguish) | No standard term found | Not measured: no label exists | Unmeasured |
| M7 | Order dependencies first, then generalise the ordering | decompose + generalize | Gandhi backward chaining; Polya "work backwards" | Not measured: no label; one outside instance found earlier by retrieval | Unmeasured |

## Policies (kept separate from methods)

| Policy | Evidence | Note |
|---|---|---|
| Use what exists before building (prior art first) | Jev marker counts 27 messages at p >= 0.9, 134 at >= 0.8, 809 at >= 0.5; not hand-checked | Also stated as a standing rule in Brian's instructions |
| Reuse your own repo before building a new one | No label yet | Seen in two reasoning chats |
| Keep one consistent notation / substrate | No label yet | Seen in the second reasoning chat |
| Critique over-engineering ("overly complicated", "no historical baggage") | 82 at >= 0.9, 185 at >= 0.8, 458 at >= 0.5; not hand-checked | Surfaced by the first recurrence test as an unplanned candidate |

## How this was measured, and what it does not show

- Labels come from Jev v3 (`tools/label_moves.py`), gate stage plus choice stage, on 8,306 unique own-words messages of 15 to 1,500 characters; candidate labels got a second check by a model reading the full message.
- Precision comes from hand-checks of 8 messages per method by one agent reader. Samples of 8 give roughly +/- 25 points. There was no second reader.
- The Jev gate wording was reworded once after seeing the 152-message evaluation set, so its overall 93% is optimistic.
- Years are the archive's spread, not Brian's: it holds almost nothing before 2024 and is dominated by 2025 project chats.
- Recall is unknown: messages the labeller called "none" were checked only on the evaluation set (61 of 61 right).
- The move extractor (PR #175) produces few test, deduce, generalize and retract moves, so graph-level move data cannot yet back M5 or M7.

## For Brian

For each row: keep, cut, or reword the one-line statement. Also: should M3 and M7 get labels, and does M1 describe a method or a definition habit? Defaults if you say nothing: keep M4 and M6; keep M5, M1 and M8 as provisional; drop M2 until a better test exists; leave M3 and M7 unmeasured.
