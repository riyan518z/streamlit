import streamlit as st
st.title("New app in streamlit")
st.header("This is the header in the page")
st.subheader("this is the subheader")
st.write("")

st.text_input("enter your name")
#st.radio
#st.image



import pandas as pd

data = pd.DataFrame({'city':['kochi','chennai','banglore'],'temperature':[30,40,35]})
st.dataframe(data)
st.slider("select your age ",10,60)
st.selectbox('how would u like to contact ?',('email','phone','whatsapp'))