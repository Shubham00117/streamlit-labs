"""
Topic 10 — Secrets Management
===============================
Demonstrates:
  • st.secrets → secure dictionary for credentials
  
Reads from .streamlit/secrets.toml. If the file doesn't exist,
this script creates a sample one so the demo works out of the box.
"""

import streamlit as st
import os

st.set_page_config(page_title="Topic 10 · Secrets", page_icon="🔐")
st.title("🔐 Topic 10 — Secrets Management")

# ── 1. What are Streamlit Secrets? ──────────────────────────────────────────
st.header("1 · What are Streamlit Secrets?")
st.write(
    """
    Streamlit provides `st.secrets` to securely manage API keys, database 
    credentials, and other sensitive data. Values are stored in 
    `.streamlit/secrets.toml` and accessed like a dictionary.
    """
)

st.markdown("---")

# ── 2. secrets.toml Format ──────────────────────────────────────────────────
st.header("2 · `secrets.toml` Format")
st.code(
    """
# .streamlit/secrets.toml

API_KEY = "sk-abc123xyz"
DEBUG_MODE = true

[database]
host = "localhost"
port = 5432
name = "myapp_db"
user = "admin"
password = "s3cret!"
""",
    language="toml",
)

st.markdown("---")

# ── 3. Create sample secrets file if missing ─────────────────────────────────
secrets_dir = os.path.join(os.path.dirname(__file__) or ".", ".streamlit")
secrets_file = os.path.join(secrets_dir, "secrets.toml")

if not os.path.exists(secrets_file):
    os.makedirs(secrets_dir, exist_ok=True)
    with open(secrets_file, "w") as f:
        f.write(
            '# Auto-generated sample secrets for Topic 10 demo\n'
            'API_KEY = "sk-demo-key-12345"\n'
            'DEBUG_MODE = true\n\n'
            '[database]\n'
            'host = "localhost"\n'
            'port = 5432\n'
            'name = "demo_db"\n'
            'user = "demo_user"\n'
            'password = "demo_pass"\n'
        )
    st.info(f"📁 Created sample secrets file at `{secrets_file}`")

# ── 4. Accessing Secrets ────────────────────────────────────────────────────
st.header("3 · Accessing Secrets in Code")

st.code(
    """
# Top-level key
api_key = st.secrets["API_KEY"]

# Nested section
db_host = st.secrets["database"]["host"]
db_name = st.secrets["database"]["name"]

# Check existence
if "API_KEY" in st.secrets:
    print("Key found!")
""",
    language="python",
)

st.markdown("---")

# ── 5. Live Demo ────────────────────────────────────────────────────────────
st.header("4 · Live Demo — Reading Secrets")

try:
    api_key = st.secrets["API_KEY"]
    debug = st.secrets.get("DEBUG_MODE", False)

    st.success("Secrets loaded successfully!")
    # Mask the API key for security
    masked = api_key[:6] + "•" * (len(api_key) - 6)
    st.write(f"🔑 API Key (masked): `{masked}`")
    st.write(f"🐛 Debug Mode: `{debug}`")

    if "database" in st.secrets:
        st.subheader("Database Config")
        db = st.secrets["database"]
        st.json(
            {
                "host": db["host"],
                "port": db["port"],
                "name": db["name"],
                "user": db["user"],
                "password": "••••••••",  # Never expose passwords
            }
        )
except Exception as e:
    st.error(f"Could not read secrets: {e}")
    st.write("Make sure `.streamlit/secrets.toml` exists.")

st.markdown("---")

# ── 6. Best Practices ───────────────────────────────────────────────────────
st.header("5 · Best Practices")
st.warning(
    """
    ⚠️ **Never commit `secrets.toml` to version control!**
    
    Add this to your `.gitignore`:
    ```
    .streamlit/secrets.toml
    ```
    """
)

st.info(
    """
    💡 **On Streamlit Community Cloud**, secrets are configured via the 
    dashboard UI (Settings → Secrets) — no local file needed in production.
    """
)

st.markdown("---")
st.caption("End of Topic 10 · Secrets Management")
