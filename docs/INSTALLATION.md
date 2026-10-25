# Installation guide

## Prerequisites
- Python 3.11 or 3.12
- Git (optional, for cloning and publishing)
- Internet access to install dependencies
- OpenAI API key **only** for optional live model generation

## macOS / Linux
```bash
cd marketing-ai-workflow-accelerator
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m unittest discover -s tests -v
streamlit run app.py
```

## Windows PowerShell
```powershell
cd marketing-ai-workflow-accelerator
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m unittest discover -s tests -v
streamlit run app.py
```
If activation is blocked by local policy, use `.venv\Scripts\python.exe -m pip install -r requirements.txt` and `.venv\Scripts\python.exe -m streamlit run app.py` instead.

Open the local URL Streamlit prints, usually http://localhost:8501.

## Optional live AI
macOS/Linux: `export OPENAI_API_KEY='your-key'`
Windows PowerShell: `$env:OPENAI_API_KEY='your-key'`
Restart Streamlit if needed; choose `openai` in the sidebar. API calls cost money and transmit your entered inputs to the model provider. Never commit API keys. Model availability and account permissions vary; change the model field if necessary.

## Deploy
Push the repository to GitHub. On Streamlit Community Cloud, select the repository and `app.py` as the entry point. Keep the default `demo` mode for a publicly shareable no-key demonstration. If enabling live generation, store `OPENAI_API_KEY` in the host's secrets configuration and add rate limits, authentication, spend limits, and abuse protections before sharing. This starter does **not** provide those protections. Public deployments must not expose confidential data.

## Troubleshooting
- `streamlit: command not found`: activate the venv or use `python -m streamlit run app.py`.
- Missing module: reinstall `pip install -r requirements.txt` inside the venv.
- API error: check key, model access, connectivity, and billing; use demo mode offline.
- Test failures: use Python 3.11+, run from project root.
