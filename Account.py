# Account.py
import streamlit as st

def show_account():
    st.title("⚙️ My Account")

    user = st.session_state.get("user", "")
    st.write(f"👤 Logged in as **{user}**")

    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.session_state.user      = ""
        st.experimental_rerun()
