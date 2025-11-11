import streamlit as st
import joblib
import numpy as np


st.set_page_config(
    page_title="EV Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #FFFFFF;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1400px !important;
            margin: auto;
            background-color: #161a25;
            border-radius: 20px;
            box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.1);
        }
        h1, h2 {
            color: #4DB8FF;
        }
        div.stButton > button {
            background: linear-gradient(to right, #0099ff, #66ccff);
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 10px;
            font-size: 1.1rem;
            width: 100%;
        }
        div.stButton > button:hover {
            background: linear-gradient(to right, #007acc, #33bbff);
        }
        .chat-box {
            height: 400px;
            overflow-y: auto;
            padding: 10px;
            background-color: #11141b;
            border-radius: 10px;
            margin-bottom: 10px;
            border: 1px solid #333;
        }
    </style>
""", unsafe_allow_html=True)


model = joblib.load("ev_price_prediction_model.pkl")


st.markdown("<h1 style='text-align:center;'>🔌 EV Dashboard — Price Prediction & Chatbot</h1>", unsafe_allow_html=True)


left, right = st.columns([1.2, 1])


with left:
    st.markdown("## 💰 EV Resale Value Prediction")

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input("Manufacturing Year", 2010, 2025, 2022, key="year_input")
        battery = st.number_input("Battery Capacity (kWh)", 20.0, 200.0, 75.0, key="battery_input")
        battery_health = st.slider("Battery Health (%)", 60, 100, 90, key="battery_health")
        range_km = st.number_input("Range (km)", 100, 1000, 350, key="range_input")

    with col2:
        charging_power = st.number_input("Charging Power (kW)", 10.0, 350.0, 120.0, key="power_input")
        charging_time = st.number_input("Charging Time (hours)", 0.5, 15.0, 6.0, key="time_input")
        maintenance_cost = st.number_input("Maintenance Cost (USD)", 100, 5000, 1000, key="maint_cost")
        insurance_cost = st.number_input("Insurance Cost (USD)", 100, 5000, 1500, key="ins_cost")

    electricity_cost = st.number_input("Electricity Cost per kWh (USD)", 0.05, 0.5, 0.2, key="elec_cost")
    monthly_cost = st.number_input("Monthly Charging Cost (USD)", 20, 1000, 300, key="month_cost")

    
    if st.button("🔮 Predict Resale Value", key="predict_btn"):
        input_data = np.array([[year, battery, battery_health, range_km, charging_power,
                                charging_time, 15, 25000, 60, 180, 7.5, 25, 2,
                                maintenance_cost, insurance_cost, electricity_cost, monthly_cost]])

        
        raw_value = model.predict(input_data)[0]

        
        predicted_value = raw_value * 0.55  

        st.success(f"### 💵 Estimated Value: **${predicted_value:,.2f}**")


with right:
    st.markdown("## 🤖 EV Chatbot Assistant")

    
    st.markdown("""
        <style>
        .chat-container {
            height: 450px;
            overflow-y: auto;
            padding: 15px;
            background-color: #1a1d27;
            border-radius: 12px;
            border: 1px solid #333;
        }
        .bot-msg {
            background-color: #2c2f3a;
            padding: 10px 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            color: white;
            max-width: 80%;
        }
        .user-msg {
            background-color: #1e3a8a;
            padding: 10px 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            color: white;
            max-width: 80%;
            margin-left: auto;   /* Align right */
        }
        </style>
    """, unsafe_allow_html=True)

    from google import generativeai
    generativeai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model_g = generativeai.GenerativeModel("models/gemini-2.0-flash-lite-001")

    
    if "wa_chat" not in st.session_state:
        st.session_state.wa_chat = [
            {"role": "assistant", "content": "Hello! 👋 Ask me anything about EVs ⚡🚗"}
        ]

    
    
    
    chat_html = "<div class='chat-container'>"

    for msg in st.session_state.wa_chat:
        if msg["role"] == "assistant":
            chat_html += f"<div class='bot-msg'>🤖 {msg['content']}</div>"
        else:
            chat_html += f"<div class='user-msg'>🧑 {msg['content']}</div>"

    chat_html += "</div>"

    st.markdown(chat_html, unsafe_allow_html=True)

    
    
    
    with st.form("wa_chat_form", clear_on_submit=True):
        user_input = st.text_input("Type your message…", key="wa_input")
        send = st.form_submit_button("Send")

    if send and user_input.strip():
        
        st.session_state.wa_chat.append({"role": "user", "content": user_input})

        
        prompt = "\n".join(
            f"{m['role']}: {m['content']}" for m in st.session_state.wa_chat
        )

        
        try:
            response = model_g.generate_content(prompt)
            reply = response.text.strip()
        except Exception as e:
            reply = f"⚠️ Error: {e}"

       
        st.session_state.wa_chat.append({"role": "assistant", "content": reply})

        st.rerun()
