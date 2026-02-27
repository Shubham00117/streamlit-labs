"""
Topic 1 — Execution Model & Performance
=========================================
Demonstrates:
  • Top-to-bottom execution (rerun on every interaction)
  • st.rerun()  → programmatic rerun
  • @st.fragment → independent partial reruns
"""

import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Topic 1 · Execution Model", page_icon="⚡")
st.title("⚡ Topic 1 — Execution Model & Performance")

# ── 1. Top-to-bottom Execution ──────────────────────────────────────────────
st.header("1 · Top-to-bottom Execution")
st.info("Every time you interact with any widget, the **entire** script reruns from top to bottom.")

# This timestamp changes on every rerun, proving the full re-execution
st.write(f"🕐 Script last ran at: **{datetime.now().strftime('%H:%M:%S.%f')[:-3]}**")

if "rerun_count" not in st.session_state:
    st.session_state.rerun_count = 0
st.session_state.rerun_count += 1
st.metric("Total Reruns (this session)", st.session_state.rerun_count)

st.markdown("---")

# ── 2. st.rerun() ───────────────────────────────────────────────────────────
st.header("2 · `st.rerun()`")
st.write("Click the button below to force a **programmatic rerun**.")

if st.button("🔄 Force Rerun"):
    st.session_state.rerun_count += 1  # will be counted again on rerun
    st.rerun()

st.markdown("---")

# ── 3. @st.fragment ─────────────────────────────────────────────────────────
st.header("3 · `@st.fragment`")
st.write(
    "Fragments rerun **independently** without re-executing the entire script. "
    "Notice the main-script timestamp above stays the same when you click "
    "the button inside the fragment."
)


@st.fragment
def live_fragment():
    """This block reruns on its own when widgets inside it change."""
    st.subheader("🧩 Fragment Section")
    if st.button("Click me (fragment only reruns)"):
        st.balloons()
    st.write(f"Fragment ran at: **{datetime.now().strftime('%H:%M:%S.%f')[:-3]}**")


live_fragment()

st.markdown("---")
st.caption("End of Topic 1 · Execution Model & Performance")
