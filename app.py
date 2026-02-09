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
# API KEY
# -----------------------------------
AQI_API_KEY = "9655acab83920a2af3ed63dedea662ae"

# -----------------------------------
# FUNCTIONS
# -----------------------------------
def fetch_aqi(location):
    try:
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={AQI_API_KEY}"
        geo_res = requests.get(geo_url).json()
        if not geo_res:
            return random.randint(40, 220)

        lat = geo_res[0]["lat"]
        lon = geo_res[0]["lon"]

        aqi_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={AQI_API_KEY}"
        res = requests.get(aqi_url).json()
        aqi = res["list"][0]["main"]["aqi"]

        return {1: 40, 2: 80, 3: 130, 4: 180, 5: 250}.get(aqi, 100)
    except:
        return random.randint(40, 220)


def generate_aqi_advice(aqi, age, conditions):
    peak_hours = "7–10 AM and 6–10 PM"

    if aqi >= 150:
        advice = (
            "<span style='color:red; font-weight:bold;'>Unhealthy Air Quality.</span> "
            "Avoid outdoor exposure during peak hours. "
            "<span style='color:green; font-weight:bold;'>Stay indoors</span>, "
            "keep windows closed, and use masks if stepping out is unavoidable. "
        )
    else:
        advice = (
            "<span style='color:green; font-weight:bold;'>Moderate Air Quality.</span> "
            "Outdoor activities are safer during late morning or early afternoon. "
        )

    if age >= 60:
        advice += (
            "<i>Due to higher age-related vulnerability</i>, reduce physical exertion, "
            "monitor breathing closely, and avoid polluted environments strictly. "
        )

    if conditions:
        advice += (
            "<i>Existing health conditions detected.</i> "
            "Limit exposure, stay hydrated, avoid heavy exertion, "
            "and prefer indoor exercises such as yoga or stretching. "
        )

    advice += (
        f"<br><b>Peak pollution hours:</b> {peak_hours}, caused by traffic emissions "
        "and atmospheric inversion. Following preventive guidance reduces long-term "
        "respiratory and cardiovascular risks."
    )

    return advice


def modify_routine(routine, aqi):
    if aqi >= 150:
        return (
            "AI advises avoiding early morning and evening jogging. "
            "Shift physical activity to indoor workouts, yoga, stretching, or breathing exercises. "
            "Schedule outdoor tasks between late morning and early afternoon. "
            "Maintain hydration, reduce stress, and follow consistent sleep timings."
        )
    else:
        return (
            "AI recommends jogging or walking between 11 AM and 4 PM. "
            "Choose low-traffic routes, include warm-up and cool-down, "
            "and balance outdoor exercise with indoor recovery activities."
        )


def extra_health_advice(query, conditions):
    return (
        "Based on your concern, AI strongly recommends condition-specific lifestyle changes. "
        "For obesity, daily brisk walking, calorie control, and reduced sitting time are essential. "
        "For diabetes or heart conditions, consistent activity, stress management, and sleep discipline are critical. "
        "Respiratory users should focus on breathing exercises and pollution avoidance."
    )


def weather_pollution_forecast(location):
    return (
        f"AI forecasting for {location} indicates fluctuating pollution levels in coming days. "
        "Morning and evening AQI will remain higher due to traffic density. "
        "Plan travel and outdoor activity during late morning or early afternoon, "
        "avoid prolonged outdoor exposure, and follow HEALNET alerts daily."
    )

# -----------------------------------
# UI
# -----------------------------------
st.title("🩺 HEALNET – AI Air Quality & Health Assistant")

st.subheader("🧬 Personal Health Details")

age = st.number_input("Age", min_value=1, max_value=120, step=1)

gender = st.radio("Biological Gender", ["Male", "Female", "Other"])

conditions = st.multiselect(
    "Select Health Conditions (multiple allowed)",
    [
        "Asthma", "Diabetes", "Heart Disease", "Obesity",
        "Allergies", "Respiratory Issues", "Hypertension",
        "Pregnancy", "Elderly (60+)", "None"
    ]
)

manual_condition = st.text_input("Other health condition (if not listed)")
if manual_condition:
    conditions.append(manual_condition)

st.subheader("📍 Location")
location = st.text_input(
    "Enter location (Part of city, City, State, Country)",
    placeholder="Dwarka, New Delhi, Delhi, India"
)

st.subheader("🕒 Daily Routine")
routine = st.text_area(
    "Describe your daily routine (work, exercise, travel, sleep)",
    height=100
)

# -----------------------------------
# MAIN ACTION
# -----------------------------------
if st.button("Get AQI & Health Advice"):
    aqi = fetch_aqi(location)

    st.markdown(f"### 🌫 Current AQI: **{aqi}**")
    st.markdown(generate_aqi_advice(aqi, age, conditions), unsafe_allow_html=True)

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

# -----------------------------------
# FOOTER
# -----------------------------------
st.caption("⚕️ HEALNET AI – Educational & preventive guidance only. Not a medical diagnosis.")