import os

import streamlit as st

# streamlitはサーバーサイドで処理しているのでこれでも安全
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


def login() -> None:
    username_input = st.text_input("ユーザー名")
    password_input = st.text_input("パスワード", type="password")

    def check_login() -> None:
        st.session_state["login_error_message"] = None
        if username_input == USERNAME and password_input == PASSWORD:
            st.session_state["logged_in"] = True
        else:
            st.session_state["login_error_message"] = (
                "ユーザー名またはパスワードが違います"
            )

    # on_clickを噛ませないと正しく動かない
    st.button("ログイン", on_click=check_login)

    login_error_message = st.session_state.get("login_error_message")
    if login_error_message is not None:
        st.text(login_error_message)
