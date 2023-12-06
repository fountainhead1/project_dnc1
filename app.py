# Streamlit 라이브러리
#  - Python으로 손쉽게 웹사이트를 생성할 수 있는 라이브러리
#  - 기존에는 HTML, CSS, JS등과 같은 기술을 공부해야만 웹 사이트 구현이 가능했으나
#  - Streamlit을 사용하면 위의 기술을 모르더라도 블럭 쌓듯이 손쉽게 구현 가능
#  - 단, 우리가 원하는 디테일한 작업은 불가능

import streamlit as st

news_category = {
    "society": "사회",
    "politics": "정치",
    "economic": "경제",
    "foreign": "국제",
    "culture": "문화",
    "entertain": "연예",
    "sports": "스포츠",
    "digital": "IT"
}

st.set_page_config(
    page_title="뉴스 수집기",
    page_icon="./image/favicon_01.png"
)


st.title(":red[NEWS] COLLECTOR")
st.text("DAUM 뉴스를 수집합니다.")  # text : 특별한 조건 없이 그냥 출력

with st.form(key="form"):
    category = st.text_input("Category").strip()
    submitted = st.form_submit_button("Collect")

    if submitted:
        st.write(category)  # write : 어떠한 조건을 만족할 때 출력