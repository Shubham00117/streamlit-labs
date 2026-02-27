"""
Topic 06 — Caching & Connections
=================================
Demonstrates:
  • @st.cache_data    → caches serializable data (returns copies)
  • @st.cache_resource → caches global shared objects (returns same instance)
  • st.connection()   → built-in connector pattern
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Topic 06 · Caching & Connections", page_icon="⚡")
st.title("⚡ Topic 06 — Caching & Connections")

# ── 1. @st.cache_data ───────────────────────────────────────────────────────
st.header("1 · `@st.cache_data` — Cache Serializable Data")
st.write(
    "Caches function results and returns a **copy** each time. "
    "Great for DataFrames, API responses, CSV loads."
)


@st.cache_data
def load_data(n_rows: int) -> pd.DataFrame:
    """Simulates an expensive data load."""
    time.sleep(2)  # Simulate slow I/O
    return pd.DataFrame(
        np.random.randn(n_rows, 3), columns=["Feature A", "Feature B", "Feature C"]
    )


n = st.slider("Number of rows", 100, 5000, 1000, step=100, key="cache_data_slider")

start = time.time()
df = load_data(n)
elapsed = time.time() - start

st.dataframe(df.head(10), use_container_width=True)
st.info(f"⏱ Load time: **{elapsed:.3f}s** (first call ~2s, cached calls ~0s)")

if st.button("🗑 Clear Data Cache"):
    load_data.clear()
    st.success("Cache cleared! Next load will take ~2s again.")

st.markdown("---")

# ── 2. @st.cache_resource ───────────────────────────────────────────────────
st.header("2 · `@st.cache_resource` — Cache Shared Objects")
st.write(
    "Caches and returns the **same object** (no copy). "
    "Use for ML models, DB connections, or any non-serializable resource."
)


class MockModel:
    """Simulates a heavy ML model."""
    def __init__(self):
        time.sleep(2)  # Simulate slow model loading
        self.name = "SentimentClassifier-v2"
        self.version = "2.1.0"

    def predict(self, text: str) -> str:
        return "positive" if len(text) % 2 == 0 else "negative"


@st.cache_resource
def get_model():
    return MockModel()


start = time.time()
model = get_model()
elapsed = time.time() - start

st.write(f"✅ Model loaded: **{model.name}** (v{model.version})")
st.info(f"⏱ Load time: **{elapsed:.3f}s** (first call ~2s, cached calls ~0s)")

user_text = st.text_input("Enter text for prediction", "Streamlit is awesome!")
if user_text:
    result = model.predict(user_text)
    st.success(f"Prediction: **{result}**")

st.markdown("---")

# ── 3. st.connection() ──────────────────────────────────────────────────────
st.header("3 · `st.connection()` — Database Connector")
st.write(
    "Streamlit provides built-in connectors for SQL databases and more. "
    "Below is an example using the built-in **SQLite** connection."
)

st.code(
    '''
# Example: Using st.connection() with SQLite
# 1. Add to .streamlit/secrets.toml:
#    [connections.mydb]
#    url = "sqlite:///mydata.db"

# 2. In your app:
conn = st.connection("mydb", type="sql")
df = conn.query("SELECT * FROM users LIMIT 10")
st.dataframe(df)
''',
    language="python",
)

st.info(
    "💡 **Tip:** `st.connection()` supports SQL, Snowflake, and custom connectors. "
    "It automatically caches the connection as a resource."
)

st.markdown("---")

# ── 4. cache_data vs cache_resource ──────────────────────────────────────────
st.header("4 · Comparison: `cache_data` vs `cache_resource`")

comparison = pd.DataFrame(
    {
        "Feature": ["Returns", "Use for", "Thread-safe copies", "Serialization"],
        "@st.cache_data": [
            "Copy of cached object",
            "DataFrames, API responses, CSVs",
            "Yes (each caller gets own copy)",
            "Requires picklable data",
        ],
        "@st.cache_resource": [
            "Same shared instance",
            "ML models, DB connections",
            "No (shared across all users)",
            "Any Python object",
        ],
    }
)
st.table(comparison.set_index("Feature"))

st.markdown("---")
st.caption("End of Topic 06 · Caching & Connections")
