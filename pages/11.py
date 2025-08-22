import streamlit as st

st. title(어울리는 자동차 찾기)

name = st.text_input('이름을 입력해주세요 : ')
car = st.selectbox('자동차를 선택해주세요:', [
