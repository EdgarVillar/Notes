import streamlit as st
import joblib
import numpy as np

# --- Deployment Step 1: Load the Model ---
# We use st.cache_resource so the model is only loaded into memory ONCE when the app starts
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

# We wrap this in a try-except block just in case the user hasn't run the training script yet
try:
    model = load_model()
    model_loaded = True
except FileNotFoundError:
    model_loaded = False

# --- Deployment Step 2: Build the Web Interface ---
st.title("🌺 Iris Flower Predictor")
st.write("Welcome to the production environment! This app takes user input from the UI, feeds it to our serialized model, and returns a real-time prediction.")

if not model_loaded:
    st.error("⚠️ Model not found! Please run `python train_and_save_model.py` first to generate `model.pkl`.")
else:
    st.subheader("Enter Flower Measurements:")
    
    # Create interactive sliders for the user
    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
        petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
    with col2:
        sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0, 3.0)
        petal_width = st.slider("Petal Width (cm)", 0.1, 3.0, 1.0)

    # --- Deployment Step 3: Run Inference ---
    if st.button("Predict Species"):
        # Format the input exactly as the model expects it (a 2D numpy array)
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        
        # Predict
        prediction = model.predict(features)[0]
        
        # Map numeric prediction back to human-readable strings
        species = ["Setosa", "Versicolor", "Virginica"]
        
        st.success(f"🤖 The model predicts this flower is a: **{species[prediction]}**")
