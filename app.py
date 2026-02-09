import streamlit as st
import random
import pandas as pd
import requests

# -----------------------------
# API KEY (FOR REAL AQI / WEATHER API)
# -----------------------------
AQI_API_KEY = "9655acab83920a2af3ed63dedea662ae"
# This key can later be used with OpenWeather / AQICN APIs

# -----------------------------
# AI ARCHITECTURE: UI & THEME
# -----------------------------
st.set_page_config(
    page_title="HEALNET AI Dashboard",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #ffffff;
    background-image: radial-gradient(#e1f0ff 0.5px, #ffffff 0.5px);
    background-size: 20px 20px;
}
.watermark {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-30deg);
    font-size: 150px;
    font-weight: 900;
    color: rgba(26, 82, 118, 0.03);
    z-index: -1;
    pointer-events: none;
    white-space: nowrap;
}
</style>
<div class="watermark">HEALNET AI</div>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.title("🫁 HEALNET – AI Air Quality & Health Assistant")
st.caption("Personalized AQI-based health and routine recommendations")

# -----------------------------
# MOCK AQI FETCH (REPLACE WITH REAL API LATER)
# -----------------------------
def fetch_aqi(city):
    """
    Placeholder AQI generator.
    Can be replaced with real API using AQI_API_KEY.
    """
    return random.randint(40, 220)

# -----------------------------
# AQI HEALTH ADVICE (50–70 WORDS)
# -----------------------------
def generate_aqi_advice(aqi, conditions):
    peak_hours = "7–10 AM and 6–10 PM"

    advice = (
        f"The current air quality index is {aqi}, indicating variable pollution exposure levels. "
        f"Peak pollution hours occur between {peak_hours}, primarily due to traffic emissions and atmospheric inversion. "
        "Outdoor activities should be planned during late morning or early afternoon, avoiding congested roads, "
        "while maintaining hydration and limiting prolonged exposure to polluted air."
    )

    if conditions:
        advice += (
            " Individuals with existing health conditions should take extra precautions, "
            "reduce outdoor exertion, prefer indoor exercises, and follow preventive routines consistently."
        )

    return advice

# -----------------------------
# ROUTINE MODIFICATION LOGIC
# -----------------------------
def modify_routine(routine, aqi):
    if aqi > 150:
        return (
            "Due to unhealthy air quality, AI advises avoiding jogging or running during early mornings and evenings. "
            "Shift physical activity to indoor workouts, yoga, stretching, or breathing exercises. "
            "Outdoor tasks should be scheduled during mid-day hours while ensuring hydration and regular sleep patterns."
        )
    else:
        return (
            "Air quality is suitable for outdoor activity. AI recommends jogging or walking between 11 AM and 4 PM, "
            "selecting low-traffic routes, performing proper warm-ups and cool-downs, "
            "and balancing outdoor exercise with indoor recovery activities."
        )

# -----------------------------
# EXTRA HEALTH ADVICE (30–60 WORDS)
# -----------------------------
def extra_health_advice(query, conditions):
    return (
        "Based on your concern, AI suggests gradual lifestyle improvements including balanced nutrition, "
        "adequate hydration, regular movement, and consistent sleep cycles. "
        "People with metabolic or respiratory conditions should prioritize daily walking, "
        "breathing exercises, and pollution-aware activity planning."
    )

# -----------------------------
# WEATHER & POLLUTION FORECAST
# -----------------------------
def weather_pollution_forecast(city):
    return (
        f"AI-based pollution forecasting for {city} suggests fluctuating air quality in the coming days. "
        "Morning and evening pollution levels are expected to remain higher due to traffic density. "
        "Outdoor activities should be planned during late morning or afternoon, "
        "while monitoring daily HEALNET alerts for safe exposure guidance."
    )

# -----------------------------
# USER HEALTH PROFILE
# -----------------------------
st.subheader("🧬 User Health Profile")

age = st.number_input("Age", min_value=1, max_value=120, step=1)

gender = st.selectbox(
    "Biological Gender",
    ["Male", "Female", "Prefer not to say"]
)

health_conditions = st.multiselect(
    "Select Health Conditions (Multiple allowed)",
    [
        "None",
        "Asthma",
        "Bronchitis",
        "COPD",
        "Allergies",
        "Heart Disease",
        "High Blood Pressure",
        "Diabetes",
        "Obesity",
        "Lung Infection",
        "Pneumonia",
        "Sinus Issues",
        "Thyroid Disorder",
        "Anxiety",
        "Weak Immunity",
        "Elderly (60+)",
        "Pregnancy",
        "Post-COVID Issues"
    ]
)

manual_condition = st.text_input(
    "Other Health Condition (if not listed)"
)

final_conditions = health_conditions.copy()
if manual_condition.strip():
    final_conditions.append(manual_condition.strip())

# -----------------------------
# LOCATION & ROUTINE INPUT
# -----------------------------
st.subheader("📍 Location & Daily Routine")

city = st.text_input("Enter City (India)")

routine = st.text_area(
    "Describe Your Daily Routine (sleep, work, exercise, travel)"
)

# -----------------------------
# AI PROCESSING
# -----------------------------
if st.button("🔍 Get AI Health Advice"):
    aqi = fetch_aqi(city)

    st.success(f"Current AQI for {city}: {aqi}")

    st.markdown("### 🫁 AQI Health Advisory")
    st.write(generate_aqi_advice(aqi, final_conditions))

    st.markdown("### 🏃 AI-Modified Routine")
    st.write(modify_routine(routine, aqi))

    st.markdown("### ❤️ Extra Health Guidance")
    st.write(extra_health_advice("", final_conditions))

    st.markdown("### 🌤 Weather & Pollution Forecast")
    st.write(weather_pollution_forecast(city))

    st.info("⏰ Peak Pollution Hours: 7–10 AM and 6–10 PM")

# -----------------------------
# FOOTER
# -----------------------------
st.caption("⚕️ HEALNET AI – Educational and awareness use only. Not a medical diagnosis.")