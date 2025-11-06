import streamlit as st
import joblib
import numpy as np

# Page setup
st.set_page_config(
    page_title="EV Resale Value Predictor",
    page_icon="🚗",
    layout="centered",  # keeps it all centered in one frame
    initial_sidebar_state="collapsed",
)

# Custom CSS for better visuals
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #FFFFFF;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 750px;
            margin: auto;
            background-color: #161a25;
            border-radius: 20px;
            box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.1);
        }
        h1 {
            text-align: center;
            color: #4DB8FF;
        }
        label {
            font-size: 1.1rem;
        }
        div[data-testid="stNumberInput"] {
            margin-bottom: 0.8rem;
        }
        div.stButton > button {
            background: linear-gradient(to right, #0099ff, #66ccff);
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 10px;
            font-size: 1.1rem;
        }
        div.stButton > button:hover {
            background: linear-gradient(to right, #007acc, #33bbff);
        }
        .stSlider label {
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("ev_price_prediction_model.pkl")

# Title
st.markdown("<h1>🚗 Electric Vehicle Resale Value Prediction</h1>", unsafe_allow_html=True)
st.write("### Enter the specifications below to get the **predicted resale value** of your EV.")

# Input fields in 2-column layout to save space
col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Manufacturing Year", 2010, 2025, 2022)
    battery = st.number_input("Battery Capacity (kWh)", 20.0, 200.0, 75.0)
    battery_health = st.slider("Battery Health (%)", 60, 100, 90)
    range_km = st.number_input("Range (km)", 100, 1000, 350)
    charging_power = st.number_input("Charging Power (kW)", 10.0, 350.0, 120.0)

with col2:
    charging_time = st.number_input("Charging Time (hours)", 0.5, 15.0, 6.0)
    maintenance_cost = st.number_input("Annual Maintenance Cost (USD)", 100, 5000, 1000)
    insurance_cost = st.number_input("Insurance Cost (USD)", 100, 5000, 1500)
    electricity_cost = st.number_input("Electricity Cost per kWh (USD)", 0.05, 0.5, 0.2)
    monthly_cost = st.number_input("Average Monthly Charging Cost (USD)", 20, 1000, 300)

# Predict button
if st.button("🔮 Predict Resale Value"):
    input_data = np.array([[year, battery, battery_health, range_km, charging_power,
                            charging_time, 15, 25000, 60, 180, 7.5, 25, 2,
                            maintenance_cost, insurance_cost, electricity_cost, monthly_cost]])
    predicted_value = model.predict(input_data)[0]
    st.success(f"💰 **Estimated Resale Value:** ${predicted_value:,.2f}")

# Footer
st.markdown("<br><center>Developed by <b>Pratim Sahoo</b> | Week 2 AI Internship Project 🌐</center>", unsafe_allow_html=True)
