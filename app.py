import streamlit as st
import random

# Page Styling
st.set_page_config(page_title="AI AQI Assistant", page_icon="🌬️")
st.title("🌬️ AI Environmental Health Assistant")

# --- AI Logic Functions ---
def fetch_aqi(city):
    return random.randint(40, 220)

def generate_aqi_advice(aqi, conditions):
    peak_hours = "7–10 AM and 6–10 PM"
    status = "Unhealthy" if aqi > 150 else "Moderate to Good"
    advice = f"### Status: {status} (AQI: {aqi})\n"
    advice += f"Pollution levels usually spike during **{peak_hours}** due to traffic emissions. "
    if aqi > 150:
        advice += "🔴 **Action:** Stay indoors and use air purifiers."
    else:
        advice += "🟢 **Action:** Air quality is acceptable for short outdoor durations."
    return advice

# --- User Interface ---
city = st.text_input("Enter your City:", "New York")
health_history = st.selectbox("Do you have any respiratory conditions?", ["None", "Asthma", "COPD", "Bronchitis"])

if st.button("Get AI Health Advice"):
    aqi_value = fetch_aqi(city)
    advice = generate_aqi_advice(aqi_value, health_history)
    
    st.divider()
    st.subheader(f"AI Analysis for {city}")
    st.info(advice)
    
    if health_history != "None":
        st.warning(f"**Special Note:** Since you have {health_history}, please keep your medication ready regardless of the AQI.")

    st.success("✨ HEALNET Alert: Plan travel between 1 PM and 5 PM for lower exposure.")