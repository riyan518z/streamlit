# import streamlit as st

# # Page configuration
# st.set_page_config(page_title="Iris Prediction App", layout="centered")

# # Sidebar
# st.sidebar.title("About")
# st.sidebar.info("This app predicts the species of an Iris flower based on its measurements.")

# # Main title and header
# st.title("🌸 IRIS PREDICTION APP")
# st.subheader("Enter the flower details below:")

# # Input fields in two columns
# col1, col2 = st.columns(2)

# with col1:
#     sepal_length = st.text_input("Sepal Length (cm)", placeholder="e.g. 5.1")
#     sepal_width = st.text_input("Sepal Width (cm)", placeholder="e.g. 3.5")

# with col2:
#     petal_length = st.text_input("Petal Length (cm)", placeholder="e.g. 1.4")
#     petal_width = st.text_input("Petal Width (cm)", placeholder="e.g. 0.2")

# # Buttons
# col3, col4 = st.columns([1, 1])
# with col3:
#     predict = st.button("🔍 Predict")
# with col4:
#     reset = st.button("🔄 Reset")

# # Placeholder for prediction result
# if predict:
#     st.success("Prediction logic goes here... (e.g., Iris-setosa)")
# elif reset:
#     st.experimental_rerun()



import streamlit as st
import pickle
import os
from PIL import Image

# Load the trained model
model_path = "model/model_final.pkl"
try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Model file not found at: {model_path}")
    st.stop()

# Page configuration
st.set_page_config(page_title="Iris Prediction App", layout="centered")
st.title("🌸 IRIS PREDICTION APP")
st.markdown("### Enter the flower measurements below:")

# Input form
with st.form("iris_form"):
    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, format="%.2f")
        sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, format="%.2f")
    with col2:
        petal_length = st.number_input("Petal Length (cm)", min_value=0.0, format="%.2f")
        petal_width = st.number_input("Petal Width (cm)", min_value=0.0, format="%.2f")

    submitted = st.form_submit_button("🔍 Predict Species")

# Prediction and image display
if submitted:
    # Correct feature order: [sepal_length, sepal_width, petal_length, petal_width]
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)[0]
    st.success(f"🌼 Predicted Species: **{prediction}**")

    # Image mapping
    image_map = {
        "Iris-setosa": "setosa.jpg",
        "Iris-versicolor": "versicolor.jpg",
        "Iris-virginica": "virginica.jpg"
    }

    image_filename = image_map.get(prediction)
    image_path = os.path.join("images", image_filename) if image_filename else None

    # Display image if available
    if image_path and os.path.exists(image_path):
        st.image(Image.open(image_path), caption=prediction, use_column_width=True)
    else:
        st.warning("No image available for this species or image file not found.")