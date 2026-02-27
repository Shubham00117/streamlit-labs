"""
Topic 5 — Session State
=========================
Demonstrates:
  • st.session_state  → per-user data persistence across reruns
  • Callbacks (on_click, on_change) → event-driven logic
"""

import streamlit as st

st.set_page_config(page_title="Topic 5 · Session State", page_icon="💾")
st.title("💾 Topic 5 — Session State")

# ── 1. st.session_state — Persistent Counter ────────────────────────────────
st.header("1 · `st.session_state` — Persistent Counter")
st.write(
    "Variables stored in `st.session_state` survive across reruns. "
    "Without it, the counter would reset to 0 every time."
)

# Initialize
if "counter" not in st.session_state:
    st.session_state.counter = 0

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("➕ Increment"):
        st.session_state.counter += 1
with col2:
    if st.button("➖ Decrement"):
        st.session_state.counter -= 1
with col3:
    if st.button("🔄 Reset"):
        st.session_state.counter = 0

st.metric("Counter Value", st.session_state.counter)

st.markdown("---")

# ── 2. Viewing All Session State ────────────────────────────────────────────
st.header("2 · Inspecting Session State")
st.write("All keys currently stored in `st.session_state`:")
st.json(dict(st.session_state))

st.markdown("---")

# ── 3. Callbacks — on_click ─────────────────────────────────────────────────
st.header("3 · Callbacks — `on_click`")
st.write("Callbacks run **before** the script reruns, so state is ready when the page renders.")

if "click_log" not in st.session_state:
    st.session_state.click_log = []


def log_click(btn_name):
    st.session_state.click_log.append(btn_name)


col1, col2 = st.columns(2)
with col1:
    st.button("🟢 Green Button", on_click=log_click, args=("Green",))
with col2:
    st.button("🔵 Blue Button", on_click=log_click, args=("Blue",))

st.write(f"Click history: {st.session_state.click_log}")

st.markdown("---")

# ── 4. Callbacks — on_change ────────────────────────────────────────────────
st.header("4 · Callbacks — `on_change`")
st.write("Fires whenever the widget value changes.")

if "slider_changes" not in st.session_state:
    st.session_state.slider_changes = 0


def on_slider_change():
    st.session_state.slider_changes += 1


val = st.slider(
    "Move this slider",
    0,
    100,
    50,
    key="my_slider",
    on_change=on_slider_change,
)

st.write(f"Current value: **{val}** | Times changed: **{st.session_state.slider_changes}**")

st.markdown("---")

# ── 5. Widget Keys & session_state ──────────────────────────────────────────
st.header("5 · Widget Keys Sync with Session State")
st.write("Every widget with a `key` is accessible via `st.session_state[key]`.")

st.text_input("Enter a city", key="city_input")
st.write(f"Value from session_state: `{st.session_state.get('city_input', '')}`")

st.markdown("---")
st.caption("End of Topic 5 · Session State")
