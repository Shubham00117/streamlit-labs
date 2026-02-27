"""
Topic 03 — Input Widgets
=========================
Demonstrates:
  • st.text_input(), st.text_area()
  • st.selectbox(), st.multiselect()
  • st.slider(), st.number_input()
  • st.file_uploader()
  • st.button()
  • st.download_button()
  • st.chat_input()
"""

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Topic 03 · Input Widgets", page_icon="🎛️")
st.title("🎛️ Topic 03 — Input Widgets")

# ── 1. Text Inputs ──────────────────────────────────────────────────────────
st.header("1 · Text Inputs")

name = st.text_input("Your Name", placeholder="Enter your name…")
if name:
    st.success(f"Hello, **{name}**! 👋")

bio = st.text_area("Short Bio", placeholder="Tell us about yourself…", height=100)
if bio:
    st.write(f"Bio ({len(bio)} chars): {bio}")

st.markdown("---")

# ── 2. Selection Widgets ────────────────────────────────────────────────────
st.header("2 · Selection Widgets")

col1, col2 = st.columns(2)

with col1:
    language = st.selectbox(
        "Favorite Language",
        ["Python", "JavaScript", "Go", "Rust", "Java"],
    )
    st.write(f"You selected: **{language}**")

with col2:
    frameworks = st.multiselect(
        "Frameworks you use",
        ["Streamlit", "FastAPI", "Django", "Flask", "React", "Next.js"],
        default=["Streamlit"],
    )
    st.write(f"Selected: {', '.join(frameworks)}")

st.markdown("---")

# ── 3. Numeric Inputs ───────────────────────────────────────────────────────
st.header("3 · Numeric / Range Inputs")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", min_value=10, max_value=100, value=25)
    st.write(f"Age: **{age}**")

with col2:
    salary = st.number_input(
        "Expected Salary ($)", min_value=0, max_value=500000, value=60000, step=5000
    )
    st.write(f"Salary: **${salary:,}**")

st.markdown("---")

# ── 4. File Uploader ────────────────────────────────────────────────────────
st.header("4 · `st.file_uploader()`")

uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.write(f"📄 **{uploaded.name}** — {df.shape[0]} rows × {df.shape[1]} cols")
    st.dataframe(df.head(), use_container_width=True)

st.markdown("---")

# ── 5. Button ────────────────────────────────────────────────────────────────
st.header("5 · `st.button()`")

if st.button("🎉 Click Me"):
    st.balloons()
    st.success("Button was clicked!")

st.markdown("---")

# ── 6. Download Button ──────────────────────────────────────────────────────
st.header("6 · `st.download_button()`")

sample_csv = pd.DataFrame(
    {"Name": ["Alice", "Bob", "Charlie"], "Score": [95, 87, 72]}
).to_csv(index=False)

st.download_button(
    label="⬇️ Download Sample CSV",
    data=sample_csv,
    file_name="sample_data.csv",
    mime="text/csv",
)

st.markdown("---")

# ── 7. Chat Input ───────────────────────────────────────────────────────────
st.header("7 · `st.chat_input()`")
st.write("Type a message in the sticky chat input at the bottom of the page.")

prompt = st.chat_input("Say something…")
if prompt:
    st.write(f"You said: **{prompt}**")

st.markdown("---")
st.caption("End of Topic 03 · Input Widgets")
