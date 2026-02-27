import streamlit as st
import uuid

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Pro-Chat AI Interface",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- STYLING ---
st.markdown("""
    <style>
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .main {
        background-color: #0e1117;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# --- SIDEBAR ---
with st.sidebar:
    st.title("⚙️ Chat Settings")
    st.write("Manage your conversation thread.")
    
    # LLM Selection
    llm_choice = st.selectbox(
        "Choose LLM Model",
        options=[
            "GPT-5.3 Codex", 
            "Claude 4.5 Sonnet", 
            "Gemini 3.6 Pro", 
            "Llama 4 Maverick", 
            "DeepSeek R1", 
            "Grok 4.20"
        ],
        help="Select the latest AI brain for this conversation."
    )
    
    st.divider()
    
    # Navigation Actions
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ New Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.session_id = str(uuid.uuid4())
            st.rerun()
            
    with col2:
        if st.button("🗑️ Delete Chat", use_container_width=True):
            st.session_state.messages = []
            st.warning("Chat history cleared.")
            st.rerun()
            
    st.divider()
    st.caption(f"Session ID: {st.session_state.session_id[:8]}")
    st.caption("Developed by Antigravity")

# --- MAIN CHAT UI ---
st.title("🤖 Pro-Chat AI")
st.markdown("---")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Bottom sticky input area
# Note: st.chat_input is the modern, premium way for chatbot inputs in Streamlit
if prompt := st.chat_input("How can I help you today?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generate bot response placeholder
    with st.chat_message("assistant"):
        response_text = f"Hello! You are using **{llm_choice}**. Your message was: '{prompt}'. This is a frontend demo."
        st.markdown(response_text)
        
    # Store assistant message
    st.session_state.messages.append({"role": "assistant", "content": response_text})

# Custom message for empty state
if not st.session_state.messages:
    st.info("👋 Welcome! Start a conversation by typing in the box below.")
