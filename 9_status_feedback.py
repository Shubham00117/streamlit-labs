"""
Topic 9 — Status & Feedback
==============================
Demonstrates:
  • st.success(), st.error(), st.warning(), st.info() → banner alerts
  • st.spinner() → loading animation
  • st.status()  → expandable progress box
"""

import streamlit as st
import time

st.set_page_config(page_title="Topic 9 · Status & Feedback", page_icon="🔔")
st.title("🔔 Topic 9 — Status & Feedback")

# ── 1. Alert Banners ────────────────────────────────────────────────────────
st.header("1 · Alert Banners")
st.write("Four built-in alert types for user feedback:")

st.success("✅ **Success** — Operation completed successfully!")
st.info("ℹ️ **Info** — Here's some helpful information.")
st.warning("⚠️ **Warning** — Proceed with caution!")
st.error("❌ **Error** — Something went wrong!")

st.markdown("---")

# ── 2. st.spinner() ─────────────────────────────────────────────────────────
st.header("2 · `st.spinner()` — Loading Animation")
st.write("Shows a spinner while a long-running task executes.")

if st.button("🔄 Run Slow Task"):
    with st.spinner("Processing… please wait ⏳"):
        time.sleep(3)
    st.success("Task completed! 🎉")

st.markdown("---")

# ── 3. st.status() ──────────────────────────────────────────────────────────
st.header("3 · `st.status()` — Expandable Progress Box")
st.write("An expandable container that shows multi-step progress.")

if st.button("🚀 Run Multi-Step Pipeline"):
    with st.status("Running pipeline…", expanded=True) as status:
        st.write("📥 Step 1: Loading data…")
        time.sleep(1)

        st.write("🔧 Step 2: Processing data…")
        time.sleep(1)

        st.write("📊 Step 3: Generating report…")
        time.sleep(1)

        st.write("✅ Step 4: Saving results…")
        time.sleep(0.5)

        status.update(label="Pipeline complete!", state="complete", expanded=False)

    st.success("All steps finished successfully!")

st.markdown("---")

# ── 4. Toast & Balloons ─────────────────────────────────────────────────────
st.header("4 · Bonus — Toast & Balloons")

col1, col2 = st.columns(2)
with col1:
    if st.button("🎈 Balloons!"):
        st.balloons()
with col2:
    if st.button("❄️ Snow!"):
        st.snow()

if st.button("🍞 Show Toast"):
    st.toast("This is a toast notification!", icon="🔔")

st.markdown("---")
st.caption("End of Topic 9 · Status & Feedback")
