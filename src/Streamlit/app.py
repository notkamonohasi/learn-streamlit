import os

import streamlit as st

# タイトル
st.title("Streamlit サンプルアプリ")

# テキスト入力
name = st.text_input("あなたの名前を入力してください:")

# 挨拶メッセージ
if name:
    st.write(f"こんにちは、{name}さん！ようこそ 🎉")
    st.write(f"{os.environ=}")
