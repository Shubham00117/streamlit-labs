"""
Topic 11 — Multipage Apps (Main Entry Point)
==============================================
Demonstrates:
  • pages/ directory → automatic routing for multipage setup
  
Run this file:  streamlit run 11_multipage_app.py

Streamlit auto-discovers .py files in the companion 
'11_pages/' directory and adds them to the sidebar navigation.

NOTE: For this demo, we use st.navigation() with st.Page() for 
explicit multipage control (works with any folder name).
"""

import streamlit as st

st.set_page_config(page_title="Topic 11 · Multipage Apps", page_icon="📑")

# ── Define pages explicitly ──────────────────────────────────────────────────
home = st.Page("11_pages/page_home.py", title="Home", icon="🏠", default=True)
analytics = st.Page("11_pages/page_analytics.py", title="Analytics", icon="📈")
settings = st.Page("11_pages/page_settings.py", title="Settings", icon="⚙️")

# ── Build navigation ────────────────────────────────────────────────────────
nav = st.navigation([home, analytics, settings])
nav.run()
