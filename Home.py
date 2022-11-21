import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=500)

with col2:
    st.title("Zecil Jain")
    content1 = """
    Hi, I'm Zecil! A Computer Engineer having proficiency in Python, Machine Learning, Deep Learning, Natural Language Processing and PostgreSQL with varied experiences in different technologies from game development using Unity to Web scraping and Data Visualization. An enthusiast of ML/AI with demonstrative skills striving for a better tomorrow! 
    Anything about Sports, Formula1 and Gaming will be great conversational starters!
    """
    st.info(content1)

content2 = """
Below you can find some of the projects I have built using various languages, frameworks and tools. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:7].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[7:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")