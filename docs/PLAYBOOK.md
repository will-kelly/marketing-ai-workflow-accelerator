# Operational playbook

## Purpose and audience
Show a marketing leader how an AI-assisted draft moves through human-controlled editorial operations. This is a proof of concept, not an enterprise content management, claims substantiation, or compliance platform.

## Roles
- Marketing requester: supplies brief, audience, channel, and approved language.
- Workflow operator: runs generation and reviews heuristic flags.
- Accountable reviewer: independently verifies claims, edits copy, and signs off with rationale.
- Owner: maintains approved claims, blocked terms, testing, and access policy.

## Procedure
1. **Intake**: Use fictional or non-sensitive briefs. Define audience, channel, goal, source materials, and approved claims.
2. **Generate**: Start with offline demo mode. Use optional live mode only when data handling is approved.
3. **Inspect**: Review flags for numeric, absolute, comparative, and banned-language patterns. These are incomplete heuristics, not fact checking.
4. **Verify**: Check all substantive assertions, including those not flagged. Record supporting source references in approval rationale.
5. **Edit**: Fix unsubstantiated statements and prohibited terms. Rerun inspection automatically through the UI.
6. **Approve**: Named reviewer checks the exact copy and records rationale. Blocked terminology prevents export.
7. **Export**: Download TXT and JSON, retaining timestamps, content hash prefix, findings, reviewer, and rationale.
8. **Evaluate**: Record end-to-end elapsed time, manual review time, number of revisions, unsupported-claim rate, and reviewer satisfaction.

## Five-minute demo script
- 0:00–0:45: Explain the fictional marketing problem and paste the sample brief.
- 0:45–1:30: Generate a draft in demo mode; explicitly state it is a template, not AI inference.
- 1:30–2:30: Add `Guaranteed 40% faster and zero risk` to the editable copy. Show quantified, absolute, and banned-term flags.
- 2:30–3:30: Remove the unsupported claim, explain why pattern matching cannot prove factual accuracy, and enter evidence notes.
- 3:30–4:15: Approve and download both exports. Edit after approval to show the export is invalidated.
- 4:15–5:00: Show the GitHub tests, architecture, measurement plan, and production gaps. If you have a working API key, optionally repeat generation in live mode.

## Measurement plan
Use the same brief and review rubric for assisted and manual runs, with multiple trials. Record total task time, generation time, review time, number of edits, number of unsupported claims, and approval outcome. Report sample size, model, environment, and variability. Do not imply productivity gains from a single demo.

## Risks and production backlog
- **Critical**: no user authentication, access controls, tenant isolation, retention controls, or rate limiting.
- **Critical**: no independent claim-to-source retrieval or fact verification; approved claims are text prompts only.
- **Important**: audit records are client-downloadable only, not immutable server-side logs.
- **Important**: session state is ephemeral; no workflow persistence, reviewer separation, or multi-user concurrency.
- **Important**: model output and briefs may contain prompt injection or sensitive information; use non-sensitive demo data.
- **Next**: structured source registry, evidence-linked claims, approval roles, persistent audit log, secure deployment, API budget controls, accessibility review, integration tests, and evaluation harness.

## Stripe interview framing
Lead with the operating problem, demonstrate the working flow, explain precisely what is and is not AI-powered, show quality gates, and discuss how you'd pilot it with a cohort of marketers. Keep any historic Docker productivity results separate from measurements made with this application.
