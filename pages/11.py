import streamlit as st

st. title(어울리는 자동차 찾기)

name = st.text_input('이름을 입력해주세요 : ')
car = st.selectbox('자동차를 선택해주세요:', [
  'BMW', 'Porsche', 'Hyundai', 'Aston_Martin', 'Mercedes', 'Lamborghini', 'Ferarri' ])

mbti_data = {
  'BMW': {
    '특징': ' 처음에는 비행기용 엔진을 만드는 회사로 출범했으며 1923년에 첫 이륜차를 만들고 자동차를 처음 만든 것은 1929년이다
