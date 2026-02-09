import streamlit as st
import random

# --- PAGE CONFIGURATION & THEME ---
st.set_page_config(page_title="HEALNET AI Assistant", page_icon="🛡️", layout="centered")

# Custom CSS for Professional Watermark and Background
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f7f6;
    }
    .watermark {
        position: fixed;
        bottom: 50px;
        left: 50%;
        transform: translate(-50%, 0);
        font-size: 100px;
        color: rgba(0, 0, 0, 0.03);
        font-weight: bold;
        z-index: -1;
        pointer-events: none;
    }
    .main-header {
        font-family: 'Helvetica Neue', sans-serif;
        color: #1a5276;
        text-align: center;
        font-weight: 800;
    }
    </style>
    <div class="watermark">HEALNET</div>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>HEALNET AI Health Assistant</h1>", unsafe_allow_html=True)

# --- AI LOGIC FUNCTIONS ---
def get_aqi(location):
    # Simulated Global AQI Logic
    return random.randint(30, 350)

def generate_health_summary(aqi, gender, condition):
    peak_hours = "7:00 AM – 10:30 AM (Traffic Inversion) and 5:30 PM – 9:00 PM (Congestion Peaks)"
    
    if aqi > 150:
        status_color = "red"
        status_text = "UNHEALTHY"
        action = f"<b style='color:red;'>STAY INDOORS</b>"
    else:
        status_color = "green"
        status_text = "MODERATE"
        action = f"<b style='color:green;'>SAFE FOR OUTDOORS</b>"

    # Core 50-word advice
    advice = f"""
    The AQI in your area is <span style='color:{status_color}; font-weight:bold;'>{aqi} ({status_text})</span>. 
    As a {gender} with {condition}, you must {action}. Avoid <i>strenuous exercise</i> during peak pollution hours: 
    <b>{peak_hours}</b>. Maintain <b>high hydration</b> and use N95 masks if transit is necessary. 
    <i>Prioritize indoor air filtration</i> to protect your respiratory system from long-term inflammation.
    """
    return advice

# --- USER INPUT SECTION ---
with st.container():
    st.subheader("📍 Personal & Location Details")
    location = st.text_input("Enter your Location (City, State, or Area):", placeholder="e.g. Dwarka, Delhi or Brooklyn, New York")
    
    gender = st.radio("Select Gender:", ["Male", "Female", "Other"], horizontal=True)
    
    health_options = [
        "None", "Asthma", "COPD", "Bronchitis", "Diabetes", "Hypertension", 
        "Obesity", "Cardiovascular Disease", "Other (Type below)"
    ]
    primary_condition = st.selectbox("Select Primary Health Condition:", health_options)
    
    manual_condition = ""
    if primary_condition == "Other (Type below)":
        manual_condition = st.text_input("Please specify your health condition:")
    
    final_condition = manual_condition if manual_condition else primary_condition

# --- ROUTINE MODIFICATION SECTION ---
st.divider()
st.subheader("🕒 Routine Optimizer")
user_routine = st.text_area("Describe your typical daily routine (e.g., 'I jog at 8am, walk to work at 9am'):")

if st.button("🚀 Analyze and Modify My Routine"):
    aqi_val = get_aqi(location)
    st.markdown(f"### Current AQI for {location}: **{aqi_val}**")
    
    # Logic for routine modification
    st.write("### 📅 Your AI-Modified Routine")
    st.write(f"Based on a {aqi_val} AQI, we have optimized your day:")
    st.info(f"1. **Morning Activity:** Move your outdoor jog to **indoor stretching** or a treadmill.\n"
            f"2. **Commute:** If you travel during **peak hours**, ensure windows are closed.\n"
            f"3. **Exercise:** Best time for any outdoor activity today is between **1:00 PM and 4:00 PM**.")
    
    st.markdown(generate_health_summary(aqi_val, gender, final_condition), unsafe_allow_html=True)

# --- ADVANCED AI ADVICE BUTTONS ---
st.divider()
col1, col2 = st.columns(2)

if col1.button("🩺 More Health Advice"):
    st.write("### AI Specialized Health Guidance")
    user_query = st.text_area("What specific health advice do you need?", max_chars=100)
    if user_query:
        # Structured 30-60 word response
        st.success(f"**AI Advice for {final_condition}:** To manage your condition effectively, focus on an **anti-inflammatory diet** rich in antioxidants. Ensure **7-9 hours of disciplined sleep** to allow your body to recover from oxidative stress caused by urban pollutants. If symptoms of {final_condition} persist, monitor your peak flow and consult a specialist immediately. Stay proactive with hydration.")

if col2.button("☁️ Weather & Pollution Forecast"):
    st.write("### 5-Day Environmental Forecast")
    st.warning(f"**AI Prediction for {location}:** Short-term data indicates a **15% rise** in PM2.5 levels over the next 48 hours due to low wind speeds. HEALNET recommends avoiding long commutes on Tuesday and Wednesday. We expect a 'Clear Sky' window on Friday afternoon for outdoor recreation.")

# Footer info
st.caption("HEALNET AI provides generalized advice based on environmental data. Always consult a medical professional for emergencies.")