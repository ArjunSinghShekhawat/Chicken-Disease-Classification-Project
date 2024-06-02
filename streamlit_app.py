import streamlit as st
from src.utils.common import decodeImage
from src.pipeline.prediction import PredictionPipeline
import os

# Setting environment variables for UTF-8 encoding
os.environ['LANG'] = 'en_US.UTF-8'
os.environ['LC_ALL'] = 'en_US.UTF-8'

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# Initialize ClientApp instance
clApp = ClientApp()

# Streamlit App
st.title("Chicken Disease Classification")

# Home Page
st.write("Welcome to the Chicken Disease Classification App")

# Training Route
if st.button('Train Model'):
    with st.spinner('Training...'):
        try:
            os.system("python main.py")
            st.success("Training done successfully!")
        except Exception as e:
            st.error(f"Training failed: {e}")

# Prediction Route
st.header("Predict Disease")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save uploaded file to the filename specified in ClientApp
    with open(clApp.filename, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    
    try:
        result = clApp.classifier.predict()
        st.write(f"Prediction: {result}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
