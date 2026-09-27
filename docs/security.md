# Privacy, security and trust boundaries

The repository is private. Conversation text and all derived JSON/HTML/Markdown may contain personal information, intellectual work and third-party details. Do not publish the repository or a generated artifact by default. A public redistribution license has not been selected.

## Local versus external processing

Import, prepare, response-file extraction, validation, merge and views operate locally. The optional OpenAI adapter sends the selected normalized conversation to the provider. It does not search the user's account or obtain other chats. The provider must be configured through secure credential provisioning; no credentials are requested in source files, printed, or committed. Optional live processing has not been executed for V1.

The adapter sets `store=False`; this is not a blanket guarantee about all provider retention or account policies. Source-derived provider responses can be sensitive. Quarantine records are also private, even when validation fails.

## Untrusted transcript content

Transcript text is supplied as data, not concatenated into a shell command. The extraction prompt explicitly rejects instructions embedded in the transcript. More importantly, the application grants no tools or code execution to extracted content. Schema parsing and graph validation happen before canonical storage. Prompt injection can still distort semantic interpretation; it cannot be dismissed as solved merely because a system instruction exists.

Renderers escape source-derived text and use generated internal identifiers. The offline inspector has no JavaScript, CDN requests or telemetry. Mermaid and DOT output are textual interchange formats; render them with current trusted tools. Export identifiers are hashed for filenames, preventing path traversal via conversation IDs.

## Persistence and access

JSON writes are atomic and exclusive by default; `--force` explicitly permits replacement. Failed extractions are quarantined rather than replacing existing canonical data. `.gitignore` excludes local environments, private work directories and environment credential files. Git history preserves earlier private data: deleting a visible file does not erase historical commits. Use an appropriate repository-history cleanup procedure before any public release; that destructive operation is not performed automatically.

V1 has no multi-user access-control server. OS permissions and private GitHub access are its boundaries. It is not an authorization platform for sharing another person's inferred psychological profile. The model represents public expressed inquiry, not mental-state surveillance.

## Review obligations

Review exact spans, attribution, privacy scope and semantic interpretations before relying on a graph as a personal worldview. Optional auto-extraction resets all annotations to proposed. Validate candidate records, but do not equate validation with truth. A “confirmed” annotation should be changed only by an identifiable review commit; a fully in-graph reviewer audit protocol is future work.
