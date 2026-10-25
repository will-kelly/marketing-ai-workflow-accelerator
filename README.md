# Marketing AI workflow accelerator

A runnable Streamlit proof of concept for **brief → draft → review flags → human approval → auditable export**. Designed as a portfolio demonstration of AI workflow enablement, editorial governance, and operational measurement.

**Modes:** `demo` is an offline deterministic template (not AI generation); `openai` uses the OpenAI Responses API and requires a key. The UI labels the mode explicitly.

## Quick start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
See [installation guide](docs/INSTALLATION.md) for Windows, testing, deployment, and troubleshooting. See [operational playbook](docs/PLAYBOOK.md) for roles, demo script, governance, and measurement.

## What works
- Marketing brief, audience, channel, approved-language intake
- Offline template draft or optional LLM-generated draft
- Editable draft and regex-based flags for numeric, absolute, comparative, and blocked language
- Human approval with named reviewer and rationale
- Approval invalidation when copy changes, block on banned terms
- Downloadable approved TXT and JSON containing findings and audit metadata
- Standard-library unit tests and GitHub Actions test workflow

## What it does not do
This is not automatic fact checking, claim substantiation, production-grade governance, or a hosted application. No independent verification, persistent database, SSO, multi-reviewer permissions, or server-side audit trail. **Never use sensitive or proprietary content in the public demo.**

## Architecture
```text
Brief + approved language
         |
         v
Draft generator (offline template | optional OpenAI API)
         |
         v
Editable draft → heuristic risk flags
         |
         v
Named human review + evidence notes
         |
         v
Approved export (TXT + JSON, content hash)
```

## Tests
`python -m unittest discover -s tests -v`

## License
MIT. See LICENSE.
