import streamlit as st
import numpy as np
import joblib
import tensorflow as tf
import os

# Project folder path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load Model
model = tf.keras.models.load_model(
    os.path.join(BASE_DIR, "models", "wine_quality_model.keras")
)

# Load Scaler
scaler = joblib.load(
    os.path.join(BASE_DIR, "models", "wine_quality_scaler.pkl")
)

# App Title
st.title("Wine Quality Prediction")

st.write("Enter Wine Details Below:")

# User Inputs
fixed_acidity = st.number_input("Fixed Acidity", value=7.4)
volatile_acidity = st.number_input("Volatile Acidity", value=0.70)
citric_acid = st.number_input("Citric Acid", value=0.00)
residual_sugar = st.number_input("Residual Sugar", value=1.9)
chlorides = st.number_input("Chlorides", value=0.076)
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", value=11.0)
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", value=34.0)
density = st.number_input("Density", value=0.9978)
ph = st.number_input("pH", value=3.51)
sulphates = st.number_input("Sulphates", value=0.56)
alcohol = st.number_input("Alcohol", value=9.4)

# Prediction Button
if st.button("Predict Wine Quality"):

    input_data = np.array([[
        fixed_acidity,
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur_dioxide,
        total_sulfur_dioxide,
        density,
        ph,
        sulphates,
        alcohol
    ]])

    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)

    quality = round(float(prediction[0][0]))

    st.subheader("Prediction Result")
    st.success(f"Predicted Wine Quality: {quality}")