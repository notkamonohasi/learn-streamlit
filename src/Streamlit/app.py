import streamlit as st
from Streamlit.login import login
from Streamlit.main import main

if __name__ == "__main__":
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    st.title("streamlit test")

    if st.session_state.get("logged_in") is False:
        login()
    else:
        main()
