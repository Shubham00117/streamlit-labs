"""
Topic 12 — Page Config
========================
Demonstrates:
  • st.set_page_config() → initial page layout and metadata settings

NOTE: st.set_page_config() MUST be the first Streamlit command in the script.
"""

import streamlit as st

# ── st.set_page_config() — MUST be first Streamlit call ─────────────────────
st.set_page_config(
    page_title="Topic 12 · Page Config",
    page_icon="⚙️",
    layout="wide",                        # "centered" (default) or "wide"
    initial_sidebar_state="expanded",     # "auto", "expanded", or "collapsed"
    menu_items={
        "Get Help": "https://docs.streamlit.io",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": "# Topic 12 Demo\nThis app demonstrates `st.set_page_config()`.",
    },
)

st.title("⚙️ Topic 12 — Page Config")

# ── 1. Overview ──────────────────────────────────────────────────────────────
st.header("1 · What is `st.set_page_config()`?")
st.write(
    """
    `st.set_page_config()` controls the **page-level settings** of your Streamlit app.
    It **must** be the first Streamlit command in your script (before any other `st.*` call).
    """
)

st.markdown("---")

# ── 2. All Parameters ───────────────────────────────────────────────────────
st.header("2 · All Parameters")

st.code(
    '''
st.set_page_config(
    page_title="My App",                   # Browser tab title
    page_icon="🚀",                        # Favicon (emoji or image path)
    layout="wide",                         # "centered" | "wide"
    initial_sidebar_state="expanded",      # "auto" | "expanded" | "collapsed"
    menu_items={
        "Get Help": "https://docs.streamlit.io",
        "Report a bug": "https://github.com/...",
        "About": "# My App\\nBuilt with Streamlit",
    }
)
''',
    language="python",
)

st.markdown("---")

# ── 3. Parameter Details ────────────────────────────────────────────────────
st.header("3 · Parameter Details")

params = {
    "Parameter": [
        "page_title",
        "page_icon",
        "layout",
        "initial_sidebar_state",
        "menu_items",
    ],
    "Type": ["str", "str / emoji", "str", "str", "dict"],
    "Default": ["None", "None", '"centered"', '"auto"', "None"],
    "Description": [
        "Sets the browser tab title.",
        "Favicon — emoji string or path to image file.",
        '"centered" (max-width container) or "wide" (full screen).',
        '"auto" (heuristic), "expanded", or "collapsed".',
        'Dict with keys: "Get Help", "Report a bug", "About".',
    ],
}

st.table(params)

st.markdown("---")

# ── 4. Current Config ───────────────────────────────────────────────────────
st.header("4 · This Page's Config")
st.info("Check the browser tab and the ☰ menu (top-right) to see the config in action!")

col1, col2 = st.columns(2)
with col1:
    st.metric("Layout", "wide")
    st.metric("Sidebar", "expanded")
with col2:
    st.metric("Page Title", "Topic 12 · Page Config")
    st.metric("Page Icon", "⚙️")

st.markdown("---")

# ── 5. Common Patterns ──────────────────────────────────────────────────────
st.header("5 · Common Patterns")

st.subheader("Dashboard Layout")
st.code(
    '''
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)
''',
    language="python",
)

st.subheader("Chat App Layout")
st.code(
    '''
st.set_page_config(
    page_title="AI Chat",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed",
)
''',
    language="python",
)

st.markdown("---")
st.caption("End of Topic 12 · Page Config")
