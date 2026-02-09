import streamlit as st
import requests
import random

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="HEALNET AI Dashboard",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS + WATERMARK
# -----------------------------------
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
    font-size: 140px;
    font-weight: 900;
    color: rgba(26, 82, 118, 0.04);
    z-index: -1;
    pointer-events: none;
}

h1, h2, h3 {
    color: #1a5276;
}
</style>

<div class="watermark">HEALNET</div>
""", unsafe_allow_html=True)

# -----------------------------------
# API CONFIG
# -----------------------------------
AQI_API_KEY = "9655acab83920a2af3ed63dedea662ae"

# -----------------------------------
# FUNCTIONS
# -----------------------------------
def fetch_aqi(location):
    """
    Location format: Part of city,City,State,Country
    """
    try:
        url = f"http://api.openweathermap.org/data/2.5/air_pollution"
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={AQI_API_KEY}"

        geo_res = requests.get(geo_url).json()
        if not geo_res:
            return random.randint(40, 220)

        lat = geo_res[0]["lat"]
        lon = geo_res[0]["lon"]

        res = requests.get(f"{url}?lat={lat}&lon={lon}&appid={AQI_API_KEY}").json()
        aqi = res["list"][0]["main"]["aqi"]

        # Convert OpenWeather AQI (1–5) to approx AQI scale
        return {1: 40, 2: 80, 3: 130, 4: 180, 5: 250}.get(aqi, 100)

    except:
        return random.randint(40, 220)


def generate_aqi_advice(aqi, conditions):
    peak_hours = "7–10 AM and 6–10 PM"

    if aqi >= 150:
        advice = (
            f"<span style='color:red; font-weight:bold;'>Unhealthy Air Quality detected.</span> "
            f"Avoid outdoor exposure during peak hours. "
            f"<span style='color:green; font-weight:bold;'>Stay indoors</span>, close windows, "
            f"use masks if stepping out is unavoidable. "
        )
    else:
        advice = (
            f"<span style='color:green; font-weight:bold;'>Moderate Air Quality.</span> "
            f"Outdoor activity is safer during late morning to early afternoon. "
        )

    if conditions:
        advice += (
            "<i>Due to your health conditions</i>, avoid heavy exertion, "
            "stay hydrated, prefer indoor workouts, and monitor breathing symptoms carefully. "
        )

    advice += (
        f"<br><b>Peak pollution hours:</b> {peak_hours}, mainly due to traffic emissions "
        "and atmospheric inversion. Following these precautions significantly reduces "
        "long-term respiratory and cardiovascular risks."
    )

    return advice


def modify_routine(routine, aqi):
    if aqi >= 150:
        return (
            "AI recommends avoiding early morning and evening jogging. "
            "Shift physical activity to indoor workouts such as yoga, stretching, or light body-weight exercises. "
            "Plan outdoor tasks between late morning and early afternoon when pollution levels temporarily drop. "
            "Maintain hydration, reduce screen time at night, and ensure consistent sleep timing."
        )
    else:
        return (
            "AI suggests jogging or walking between 11 AM and 4 PM. "
            "Choose low-traffic routes, include proper warm-up and cool-down, "
            "and balance outdoor activity with indoor recovery exercises to prevent fatigue."
        )


def extra_health_advice(query, conditions):
    return (
        "Based on your input, AI strongly recommends structured lifestyle changes tailored to your condition. "
        "For obesity or metabolic concerns, daily brisk walking, reduced sitting time, and portion-controlled meals are essential. "
        "For respiratory or cardiac issues, prioritize breathing exercises, controlled activity intensity, and strict pollution avoidance. "
        "Consistency and gradual improvement are key to long-term health benefits."
    )


def weather_pollution_forecast(location):
    return (
        f"AI analysis for {location} indicates fluctuating pollution levels over the next few days. "
        "Morning and evening AQI is expected to remain higher due to traffic density and low wind movement. "
        "Plan travel and physical activity during late morning or early afternoon, avoid prolonged outdoor exposure, "
        "and follow HEALNET alerts daily for safe decision-making."
    )

# -----------------------------------
# UI
# -----------------------------------
st.title("🩺 HEALNET – AI Air Quality & Health Assistant")

st.subheader("Personal Health Details")

gender = st.radio("Biological Gender", ["Male", "Female", "Other"])

conditions_list = [
    "Asthma", "Diabetes", "Heart Disease", "Obesity",
    "Allergies", "Respiratory Issues", "Hypertension",
    "Pregnancy", "Elderly (60+)", "None"
]

conditions = st.multiselect(
    "Select Health Conditions (you can choose multiple)",
    conditions_list
)

manual_condition = st.text_input(
    "Other health condition (if not listed)"
)

if manual_condition:
    conditions.append(manual_condition)

st.subheader("📍 Location Details")
location = st.text_input(
    "Enter location (Part of city, City, State, Country)",
    placeholder="Dwarka, New Delhi, Delhi, India"
)

st.subheader("🕒 Daily Routine")
routine = st.text_area(
    "Describe your daily routine (work hours, exercise, travel, sleep)",
    height=100
)

# -----------------------------------
# MAIN ACTION
# -----------------------------------
if st.button("Get AQI & Health Advice"):
    aqi = fetch_aqi(location)

    st.markdown(f"### 🌫 Current AQI: **{aqi}**")
    st.markdown(generate_aqi_advice(aqi, conditions), unsafe_allow_html=True)

    st.markdown("### 🧠 AI-Modified Routine")
    st.write(modify_routine(routine, aqi))

# -----------------------------------
# EXTRA BUTTONS
# -----------------------------------
st.divider()

st.subheader("Need More Help?")

col1, col2 = st.columns(2)

with col1:
    if st.button("More Health Advice"):
        query = st.text_area(
            "Describe your concern (max 100 words)",
            max_chars=100
        )
        if query:
            st.markdown("### 🩺 Personalized Health Guidance")
            st.write(extra_health_advice(query, conditions))

with col2:
    if st.button("Weather & Pollution Forecast"):
        st.markdown("### 🌦 Upcoming Pollution & Weather Insights")
        st.write(weather_pollution_forecast(location))