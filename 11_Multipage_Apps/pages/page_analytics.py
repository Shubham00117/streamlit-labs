"""
Topic 85 — Multipage Apps · Analytics Page
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Analytics Page")
st.write("This is a separate page in the multipage app. Each page runs independently.")

st.markdown("---")

# Sample analytics dashboard
st.subheader("Monthly Performance")

col1, col2, col3 = st.columns(3)
col1.metric("Revenue", "$8,420", "+12.3%")
col2.metric("Users", "2,150", "+7.8%")
col3.metric("Retention", "68%", "-2.1%")

st.markdown("---")

st.subheader("Trend Chart")
chart_data = pd.DataFrame(
    np.random.randn(30, 3) + [10, 20, 15],
    columns=["Product A", "Product B", "Product C"],
)
st.line_chart(chart_data)

st.markdown("---")
st.caption("Topic 85 · Analytics Page — Multipage Demo")
