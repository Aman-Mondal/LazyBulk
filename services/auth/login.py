import streamlit as st

def render_login():
    if st.session_state.get("user_id") is not None:
        return True

    st.title("Welcome to LazyBulk")
    st.markdown("Enter a username to enter session")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Username : ", placeholder="enter username")
        submit_button = st.form_submit_button("Start Session", width="stretch")

    if submit_button:
        if not username:
            st.error("Username cannot be empty!")
            return False

        st.session_state["username"] = username
        st.session_state["user_id"] = "i01"

        st.rerun()


    return False