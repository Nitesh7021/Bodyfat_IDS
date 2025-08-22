import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("Bodyfat_IDS.joblib")

st.title("Body Fat Prediction App 🧍")

st.write("Enter your body measurements to estimate body fat percentage.")

# Input fields (no min/max/default values)
density = st.number_input("Density", format="%.4f")
age = st.number_input("Age")
weight = st.number_input("Weight (kg)")
height = st.number_input("Height (cm)")
neck = st.number_input("Neck (cm)")
chest = st.number_input("Chest (cm)")
abdomen = st.number_input("Abdomen (cm)")
hip = st.number_input("Hip (cm)")
thigh = st.number_input("Thigh (cm)")
knee = st.number_input("Knee (cm)")
ankle = st.number_input("Ankle (cm)")
biceps = st.number_input("Biceps (cm)")
forearm = st.number_input("Forearm (cm)")
wrist = st.number_input("Wrist (cm)")

# Collect inputs into numpy array
features = np.array([[density, age, weight, height, neck, chest, abdomen, hip,
                      thigh, knee, ankle, biceps, forearm, wrist]])

# Predict button
if st.button("Predict Body Fat"):
    prediction = model.predict(features)
    st.success(f"Estimated Body Fat: {prediction[0]:.2f}%")
