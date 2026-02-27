"""
Topic 85 — Multipage Apps · Settings Page
"""

import streamlit as st

st.title("⚙️ Settings Page")
st.write("Configure app preferences. These persist via `st.session_state`.")

st.markdown("---")

# Initialize defaults
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"
if "notifications" not in st.session_state:
    st.session_state.notifications = True

st.subheader("Preferences")

theme = st.selectbox(
    "Theme",
    ["Dark", "Light", "System"],
    index=["Dark", "Light", "System"].index(st.session_state.theme),
    key="theme",
)

notifications = st.toggle("Enable Notifications", key="notifications")

st.markdown("---")

st.subheader("Current Settings")
st.json(
    {
        "theme": st.session_state.theme,
        "notifications": st.session_state.notifications,
    }
)

st.info("💡 Settings are stored in `st.session_state` and shared across all pages in the app.")

st.markdown("---")
st.caption("Topic 85 · Settings Page — Multipage Demo")
