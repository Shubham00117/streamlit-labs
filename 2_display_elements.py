"""
Topic 2 — Display Elements
============================
Demonstrates:
  • st.write()
  • st.title(), st.header(), st.subheader()
  • st.markdown()
  • st.dataframe()
  • st.metric()
  • st.json()
  • st.plotly_chart() / st.altair_chart()
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Topic 2 · Display Elements", page_icon="📄", layout="wide")
st.title("📄 Topic 2 — Display Elements")

# ── 1. st.write() ───────────────────────────────────────────────────────────
st.header("1 · `st.write()` — Universal Display")
st.write("**st.write()** is Streamlit's Swiss-army knife. It auto-detects the input type.")
st.write("A plain string")
st.write(42)
st.write({"key": "value", "nested": [1, 2, 3]})
st.write(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}))

st.markdown("---")

# ── 2. Typography ───────────────────────────────────────────────────────────
st.header("2 · Typography Hierarchy")
st.title("This is st.title()")
st.header("This is st.header()")
st.subheader("This is st.subheader()")
st.caption("This is st.caption() — small muted text")

st.markdown("---")

# ── 3. st.markdown() ────────────────────────────────────────────────────────
st.header("3 · `st.markdown()` — Rich Markdown")
st.markdown(
    """
    ### Markdown Features
    - **Bold**, *italic*, `inline code`
    - [Streamlit Docs](https://docs.streamlit.io)
    - Emoji support: 🚀 🎉 ✅

    > Blockquote: Streamlit makes data apps easy!

    ```python
    import streamlit as st
    st.write("Hello, World!")
    ```
    """
)

st.markdown("---")

# ── 4. st.dataframe() ───────────────────────────────────────────────────────
st.header("4 · `st.dataframe()` — Interactive Table")
df = pd.DataFrame(
    np.random.randn(10, 4),
    columns=["Revenue", "Profit", "Users", "Growth"],
)
st.dataframe(df, use_container_width=True)

st.markdown("---")

# ── 5. st.metric() ──────────────────────────────────────────────────────────
st.header("5 · `st.metric()` — KPI Cards")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", "$12,450", "+8.2%")
col2.metric("Active Users", "1,284", "-3.1%")
col3.metric("Conversion", "4.7%", "+0.5%")

st.markdown("---")

# ── 6. st.json() ────────────────────────────────────────────────────────────
st.header("6 · `st.json()` — Collapsible JSON Tree")
st.json(
    {
        "user": "shubham",
        "role": "admin",
        "permissions": ["read", "write", "delete"],
        "metadata": {"created": "2026-01-15", "active": True},
    }
)

st.markdown("---")

# ── 7. Charts ────────────────────────────────────────────────────────────────
st.header("7 · Interactive Charts")

tab1, tab2 = st.tabs(["📊 Plotly Chart", "📈 Altair Chart"])

with tab1:
    try:
        import plotly.express as px

        fig = px.bar(
            x=["Jan", "Feb", "Mar", "Apr", "May"],
            y=[120, 200, 150, 250, 180],
            labels={"x": "Month", "y": "Sales ($)"},
            title="Monthly Sales — Plotly",
            color_discrete_sequence=["#7c5cfc"],
        )
        fig.update_layout(template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
    except ImportError:
        st.warning("Install plotly: `pip install plotly`")

with tab2:
    try:
        import altair as alt

        source = pd.DataFrame(
            {"x": np.random.randn(200), "y": np.random.randn(200)}
        )
        chart = (
            alt.Chart(source)
            .mark_circle(size=60, opacity=0.6)
            .encode(x="x", y="y", color=alt.value("#00e5a0"))
            .properties(title="Random Scatter — Altair", width="container", height=350)
        )
        st.altair_chart(chart, use_container_width=True)
    except ImportError:
        st.warning("Install altair: `pip install altair`")

st.markdown("---")
st.caption("End of Topic 2 · Display Elements")
