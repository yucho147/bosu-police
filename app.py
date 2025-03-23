import os

import streamlit as st
from bosu_checker import contains_bosu, ask_openai_about_bosu

st.set_page_config(page_title="bosu-police", page_icon="🚓")

st.title(":cop: 母数警察 :cop:")
st.write("「母数」という言葉が正しく使われているかどうか、AIでチェックします。")

# APIキー入力
os.environ["OPENAI_API_KEY"] = st.text_input("OpenAI API Key", type="password")

# モデル選択
model_name = st.selectbox(
    "使用するモデルを選んでください",
    options=["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"],
    index=1,  # デフォルトで "gpt-4o-mini"
)

# 入力文
text = st.text_area("判定したい文章を入力してください")

if st.button("チェック！"):
    if not os.getenv("OPENAI_API_KEY"):
        st.warning("OpenAI API Key を入力してください。")
    elif not text.strip():
        st.warning("文章を入力してください。")
    elif not contains_bosu(text):
        st.success(":white_check_mark: 「母数」は含まれていません。問題なしです!")
    else:
        with st.spinner("AIが判定中..."):
            try:
                result = ask_openai_about_bosu(text, model_name)
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
                st.stop()
            if result["valid_flag"]:
                st.success(f":white_check_mark: 「母数」は適切に使われています！\n\nAIの回答：{result['answer']}")
            else:
                st.error(f":x: 「母数」の使い方が適切ではありません。\n\nAIの回答：{result['answer']}")
