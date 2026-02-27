"""
Topic 8 — Forms
=================
Demonstrates:
  • st.form()               → widget batching container
  • st.form_submit_button() → form submission trigger

Forms prevent individual widget reruns — the script only reruns 
when the submit button is pressed.
"""

import streamlit as st

st.set_page_config(page_title="Topic 8 · Forms", page_icon="📝")
st.title("📝 Topic 8 — Forms")

# ── 1. Basic Form ────────────────────────────────────────────────────────────
st.header("1 · Basic Form")
st.write(
    "Widgets inside a `st.form()` do **not** trigger reruns individually. "
    "The script only reruns when `st.form_submit_button()` is clicked."
)

with st.form("basic_form"):
    st.subheader("📋 Registration Form")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    age = st.slider("Age", 18, 80, 25)
    role = st.selectbox("Role", ["Developer", "Designer", "Manager", "Data Scientist"])
    agree = st.checkbox("I agree to the terms and conditions")

    submitted = st.form_submit_button("✅ Submit")

if submitted:
    if not name or not email:
        st.error("⚠️ Please fill in all required fields!")
    elif not agree:
        st.warning("You must agree to the terms and conditions.")
    else:
        st.success("🎉 Form submitted successfully!")
        st.json(
            {
                "name": name,
                "email": email,
                "age": age,
                "role": role,
                "agreed": agree,
            }
        )

st.markdown("---")

# ── 2. Form with Columns ────────────────────────────────────────────────────
st.header("2 · Form with Columns Layout")

with st.form("survey_form"):
    st.subheader("📊 Quick Survey")

    col1, col2 = st.columns(2)
    with col1:
        fav_language = st.selectbox("Favorite Language", ["Python", "JavaScript", "Go", "Rust"])
        experience = st.number_input("Years of Experience", 0, 40, 3)
    with col2:
        satisfaction = st.slider("Job Satisfaction (1-10)", 1, 10, 7)
        remote = st.radio("Work Mode", ["Remote", "Hybrid", "On-site"])

    comments = st.text_area("Additional Comments", placeholder="Any feedback…")
    submitted2 = st.form_submit_button("📤 Submit Survey")

if submitted2:
    st.success("Survey submitted!")
    st.write(
        f"**Language:** {fav_language} | **Experience:** {experience}yr | "
        f"**Satisfaction:** {satisfaction}/10 | **Mode:** {remote}"
    )
    if comments:
        st.info(f"Comments: {comments}")

st.markdown("---")

# ── 3. Multiple Forms ───────────────────────────────────────────────────────
st.header("3 · Multiple Independent Forms")
st.write("You can have **multiple forms** on the same page, each with its own submit button.")

col1, col2 = st.columns(2)

with col1:
    with st.form("login_form"):
        st.subheader("🔑 Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")
    if login_btn:
        if username and password:
            st.success(f"Welcome back, **{username}**!")
        else:
            st.error("Enter both username and password.")

with col2:
    with st.form("search_form"):
        st.subheader("🔍 Search")
        query = st.text_input("Search query")
        category = st.selectbox("Category", ["All", "Articles", "Videos", "Code"])
        search_btn = st.form_submit_button("Search")
    if search_btn:
        st.info(f"Searching for **'{query}'** in **{category}**…")

st.markdown("---")
st.caption("End of Topic 8 · Forms")
