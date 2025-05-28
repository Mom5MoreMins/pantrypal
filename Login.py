# Login.py
import streamlit as st
from storage import init_db, create_user, verify_user

def show_login():
    init_db()  # ensure DB & table exist

    st.title("🔑 Login or Sign Up")
    form = st.radio("Action", ["Login", "Sign Up"])
    user = st.text_input("Username", key="li_user")
    pw   = st.text_input("Password", type="password", key="li_pw")

    if form == "Sign Up":
        if st.button("Create Account"):
            if not user or not pw:
                st.error("Please provide both username and password.")
            elif create_user(user, pw):
                st.success("Account created! You can now log in.")
            else:
                st.error("That username is already taken.")
    else:  # Login
        if st.button("Log In"):
            if verify_user(user, pw):
                st.session_state.logged_in = True
                st.session_state.user      = user
                st.experimental_rerun()
            else:
                st.error("❌ Incorrect username or password.")
