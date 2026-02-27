"""
Topic 4 — Layout & Containers
================================
Demonstrates:
  • st.sidebar
  • st.columns()
  • st.tabs()
  • st.expander()
  • st.container(), st.empty()
  • @st.dialog
"""

import streamlit as st
import time

st.set_page_config(page_title="Topic 4 · Layout & Containers", page_icon="🗂️", layout="wide")
st.title("🗂️ Topic 4 — Layout & Containers")

# ── 1. Sidebar ──────────────────────────────────────────────────────────────
st.sidebar.header("🔧 Sidebar Controls")
sidebar_name = st.sidebar.text_input("Your Name", "Streamlit User")
sidebar_theme = st.sidebar.selectbox("Preferred Theme", ["Dark", "Light", "System"])
st.sidebar.info(f"Hello **{sidebar_name}**, theme set to **{sidebar_theme}**")

# ── 2. Columns ──────────────────────────────────────────────────────────────
st.header("1 · `st.columns()` — Side-by-Side Layout")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("📊 Column 1")
    st.metric("Revenue", "$10,200", "+12%")
with col2:
    st.subheader("👥 Column 2")
    st.metric("Users", "3,452", "+5%")
with col3:
    st.subheader("⚡ Column 3")
    st.metric("Uptime", "99.9%", "+0.1%")

st.markdown("---")

# ── 3. Tabs ─────────────────────────────────────────────────────────────────
st.header("2 · `st.tabs()` — Tab Panels")

tab1, tab2, tab3 = st.tabs(["🏠 Overview", "📈 Analytics", "⚙️ Settings"])

with tab1:
    st.subheader("Overview")
    st.write("Welcome to the overview panel. This is the default landing tab.")

with tab2:
    st.subheader("Analytics")
    st.write("Charts and analytics would go here.")
    st.line_chart({"data": [10, 30, 20, 50, 40, 60, 55]})

with tab3:
    st.subheader("Settings")
    st.toggle("Enable notifications", value=True)
    st.toggle("Dark mode", value=False)

st.markdown("---")

# ── 4. Expander ─────────────────────────────────────────────────────────────
st.header("3 · `st.expander()` — Collapsible Panel")

with st.expander("📖 Click to expand — What is Streamlit?"):
    st.write(
        """
        **Streamlit** is an open-source Python framework that turns data scripts 
        into shareable web apps in minutes. No front-end experience required!
        
        Key features:
        - 🔄 Auto-rerun on code save
        - 📊 Built-in charting
        - 🧩 Widget ecosystem
        - ☁️ One-click deploy via Streamlit Community Cloud
        """
    )

st.markdown("---")

# ── 5. Container & Empty ────────────────────────────────────────────────────
st.header("4 · `st.container()` & `st.empty()`")

st.subheader("Container — Grouped Content")
with st.container(border=True):
    st.write("This content is inside a **container** with a visible border.")
    st.write("You can group related widgets and text together.")

st.subheader("Empty — Placeholder")
placeholder = st.empty()
placeholder.info("⏳ This placeholder will update in 3 seconds…")

if st.button("Update Placeholder"):
    time.sleep(1)
    placeholder.success("✅ Placeholder updated!")

st.markdown("---")

# ── 6. @st.dialog ───────────────────────────────────────────────────────────
st.header("5 · `@st.dialog` — Modal Pop-up")


@st.dialog("Feedback Form")
def feedback_dialog():
    rating = st.slider("Rate your experience", 1, 5, 3)
    comment = st.text_area("Comments")
    if st.button("Submit Feedback"):
        st.session_state["last_feedback"] = {"rating": rating, "comment": comment}
        st.rerun()


if st.button("💬 Open Feedback Dialog"):
    feedback_dialog()

if "last_feedback" in st.session_state:
    st.success(
        f"Feedback received! Rating: {st.session_state['last_feedback']['rating']}/5"
    )

st.markdown("---")
st.caption("End of Topic 4 · Layout & Containers")
