import streamlit as st
import pickle

model = pickle.load(open("model_final.pkl","rb"))

st.title("IRIS PREDICTION APP")
st.header("Enter the details")
st.write("")

# st.text_input("Enter the sepal length")
# st.text_input("Enter the petal length")
# st.text_input("Enter the sepal width")
# st.text_input("Enter the petal width")
# st.button('predict')

with st.form('iris_app_form'):
    sl = st.number_input("Enter sepal length")
    pl = st.number_input("Enter petal length")
    sw = st.number_input("Enter sepal width")
    pw = st.number_input("Enter petal width")

    submitted = st.form_submit_button("Predict species")

if submitted:
    predition =model.predict([[sl,pl,sw,pw]])

    st.success(f"Predicted species {predition}")
