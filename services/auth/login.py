import streamlit as st

def render_login():
    if st.session_state.get("user_id") is not None:
        return True

    left, right = st.columns([1.1, 0.9], gap="large", vertical_alignment="center")

    # Left side: Branding
    with left:
        st.markdown(
            """
            <div style="background-color: #382820; height: 100vh; padding: 2rem 2rem; margin-right:4rem;">
                <p style="
                    color: #E8AD70;
                    font-size: 1.5rem;
                    letter-spacing: 4px;
                    font-weight: 700;
                ">
                    LAZYBULK
                </p>
                <h1 style="
                    color: #F3E8DC;
                    font-size: 3rem;
                    line-height: 1.15;
                    margin-bottom: 1rem;
                ">
                    BUILD YOUR<br>STRONGER SELF.
                </h1>
                <p style="
                    color: #D8C6B8;
                    font-size: 1.1rem;
                ">
                    Train smarter. Track progress. Get stronger.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Right side: Login form
    with right:
        st.subheader("Welcome back")
        st.write("Enter your details to start your session.")

        with st.form("login_form", clear_on_submit=False):
            username = st.text_input(
                "Username",
                placeholder="Enter your username",
            )

            submit_button = st.form_submit_button(
                "Start Session",
                width="stretch",
            )

        if submit_button:
            if not username.strip():
                st.error("Username cannot be empty!")
                return False

            st.session_state["username"] = username.strip()
            st.session_state["user_id"] = "i01"

            st.rerun()

    return False