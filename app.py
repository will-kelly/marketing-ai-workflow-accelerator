"""Streamlit UI for a demonstrable human-approved marketing workflow."""
import json
import os
import time
import streamlit as st
from accelerator.core import make_draft, inspect_copy, export_package, digest

st.set_page_config(page_title="Marketing AI workflow accelerator", page_icon="🛠️", layout="wide")
st.title("Marketing AI workflow accelerator")
st.caption("Brief → draft → claim flags → human review → auditable export | Demonstration, not a production compliance system")
with st.sidebar:
    st.header("Execution")
    provider = st.selectbox("Generation mode", ["demo", "openai"], help="Demo uses deterministic templates and makes no model calls.")
    model = st.text_input("OpenAI model", "gpt-4.1-mini", disabled=provider != "openai")
    st.info("Do not enter confidential customer or company data. Live mode sends inputs to an external API.")

left, right = st.columns(2)
with left:
    st.subheader("1. Intake")
    brief = st.text_area("Marketing brief", value="A fictional SaaS product helps marketing teams coordinate content reviews and track approvals.", height=140)
    audience = st.text_input("Audience", "B2B marketing operations leaders")
    channel = st.selectbox("Asset type", ["LinkedIn post", "Email", "Landing page excerpt", "Product announcement"])
with right:
    st.subheader("Approved materials")
    approved_raw = st.text_area("Approved claims (one per line)", value="Keep content reviews and decisions in one workflow.\nGive reviewers a shared view of approval status.", height=105)
    banned_raw = st.text_input("Banned terms (comma-separated)", "guaranteed, zero risk")

approved_claims = [x.strip() for x in approved_raw.splitlines() if x.strip()]
banned = [x.strip() for x in banned_raw.split(",") if x.strip()]
if st.button("Generate draft", type="primary"):
    start = time.perf_counter()
    try:
        draft = make_draft(brief, audience, channel, approved_claims, provider, os.getenv("OPENAI_API_KEY"), model)
        st.session_state["draft"] = draft
        st.session_state["generation_seconds"] = round(time.perf_counter()-start, 3)
        st.session_state.pop("package", None)
        st.session_state.pop("edited_draft", None)
    except Exception as exc:
        st.error(f"Generation failed: {exc}")

if "draft" in st.session_state:
    st.subheader("2. Edit and inspect")
    edited = st.text_area("Editable draft", st.session_state["draft"], height=250, key="edited_draft")
    findings = inspect_copy(edited, approved_claims, banned)
    st.metric("Generation elapsed (seconds)", st.session_state.get("generation_seconds", 0))
    st.metric("Review flags", len(findings))
    if findings:
        st.warning("Flags are heuristic prompts for review, not proof that a claim is true or false.")
        st.dataframe(findings, use_container_width=True)
    else:
        st.success("No pattern-based flags. Manual fact-checking is still required.")
    st.subheader("3. Human approval")
    reviewer = st.text_input("Reviewer name")
    rationale = st.text_area("Approval rationale / source verification notes", placeholder="Record links or identifiers for supporting evidence, and what was checked.")
    confirmed = st.checkbox("I reviewed this exact copy and verified relevant claims against authoritative sources.")
    if st.button("Approve and prepare export"):
        try:
            package = export_package(edited, findings, reviewer, rationale, confirmed, brief, provider)
            st.session_state["package"] = package
            st.success("Approval recorded for this version.")
        except ValueError as exc:
            st.error(str(exc))
    pkg = st.session_state.get("package")
    if pkg and pkg["draft_sha256_prefix"] == digest(edited):
        st.download_button("Download approved package (JSON)", json.dumps(pkg, indent=2), "approved-package.json", "application/json")
        st.download_button("Download approved copy (TXT)", pkg["copy"], "approved-copy.txt", "text/plain")
    elif pkg:
        st.warning("Copy changed after approval. Reapprove before exporting.")
