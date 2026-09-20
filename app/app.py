import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="NASA Battery Capacity Prediction",
    page_icon="🔋",
    layout="centered"
)

st.title("🔋 NASA Battery Capacity Prediction")
st.write("Predict battery capacity using battery cycle information.")

st.header("Battery Information")

cycle = st.number_input(
    "Cycle Number",
    min_value=1,
    value=1,
    step=1
)

voltage = st.number_input(
    "Voltage",
    value=4.0
)

current = st.number_input(
    "Current",
    value=1.0
)

temperature = st.number_input(
    "Temperature",
    value=25.0
)

time = st.number_input(
    "Time",
    min_value=0.0,
    value=100.0
)

if st.button("Predict Capacity"):

    # Temporary prediction formula for app demonstration
    # Replace this with the trained model after saving the final model.
    predicted_capacity = max(
        0,
        2.0
        - (cycle * 0.00005)
        + (voltage * 0.01)
        - (current * 0.005)
        - (temperature - 25) * 0.001
        + (time * 0.00001)
    )

    st.success(
        f"Predicted Battery Capacity: {predicted_capacity:.4f} Ah"
    )