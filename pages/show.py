import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 불러오기
df = pd.read_csv('data.csv')

# 키워드 목록 (첫 번째 컬럼은 날짜라고 가정)
klist = df.columns.tolist()[1:]  # 날짜 제외

st.title("News data")

# 키워드 선택
keyword = st.selectbox("Select keyword:", klist)
st.write(keyword)

plt.figure(figsize=(10,5))
plt.plot(df['날짜'], df[keyword])
plt.xlabel('Year')
plt.ylabel('cnt')
plt.title('Trends')
st.pyplot(plt)

