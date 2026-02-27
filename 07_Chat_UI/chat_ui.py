"""
Topic 07 — Chat UI
===================
Demonstrates:
  • st.chat_message() → chat bubble container
  • st.chat_input()   → sticky chat input widget
  
Implements a simple echo-bot that stores conversation history in session state.
"""

import streamlit as st

st.set_page_config(page_title="Topic 07 · Chat UI", page_icon="💬")
st.title("💬 Topic 07 — Chat UI")

st.write(
    "A simple **echo-bot** demonstrating `st.chat_message()` and `st.chat_input()`. "
    "Messages persist across reruns using `st.session_state`."
)

st.markdown("---")

# ── Initialize chat history ─────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there! 👋 I'm an echo bot. Type anything and I'll repeat it back!"}
    ]

# ── Display chat history ────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Handle new user input ───────────────────────────────────────────────────
prompt = st.chat_input("Type your message…")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Echo-bot response
    response = f"🔁 You said: **{prompt}**"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
