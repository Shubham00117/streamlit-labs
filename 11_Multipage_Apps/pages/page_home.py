"""
Topic 11 — Multipage Apps · Home Page
"""

import streamlit as st

st.title("📑 Topic 11 — Multipage Apps")
st.header("🏠 Home Page")

st.write(
    """
    Welcome to the **Multipage App** demo!
    
    Streamlit supports multipage apps through:
    1. **`pages/` directory** — Auto-discovered pages
    2. **`st.navigation()` + `st.Page()`** — Programmatic page control
    
    👈 Use the **sidebar navigation** to switch between pages.
    """
)

st.info(
    "Each page is a separate `.py` file. Streamlit automatically adds them "
    "to the sidebar navigation based on filename or explicit configuration."
)

st.markdown("---")

st.subheader("📁 Project Structure for Multipage")
st.code(
    """
11_Multipage_Apps/multipage_app.py                        ← Main entry point
11_Multipage_Apps/pages/
  ├── page_home.py               ← This page (Home)
  ├── page_analytics.py          ← Analytics page
  └── page_settings.py           ← Settings page
""",
    language="text",
)

st.markdown("---")

st.subheader("Code: Main Entry Point")
st.code(
    '''
import streamlit as st

# Define pages
home = st.Page("pages/page_home.py", title="Home", icon="🏠", default=True)
analytics = st.Page("pages/page_analytics.py", title="Analytics", icon="📈")
settings = st.Page("pages/page_settings.py", title="Settings", icon="⚙️")

# Build navigation
nav = st.navigation([home, analytics, settings])
nav.run()
''',
    language="python",
)
