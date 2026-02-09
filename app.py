from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# -----------------------------
# MOCK AQI FETCH (Replace with real API later)
# -----------------------------
def fetch_aqi(city):
    # Placeholder for real AQI API like OpenWeather / AQICN
    return random.randint(40, 220)

# -----------------------------
# CORE AI AQI HEALTH LOGIC
# -----------------------------
def generate_aqi_advice(aqi, conditions):
    peak_hours = "7–10 AM and 6–10 PM"

    if aqi > 150:
        base = (
            "Air quality is unhealthy. Avoid outdoor activities during peak hours. "
            "Stay indoors, keep windows closed, and use masks if outdoor exposure is unavoidable. "
        )
    else:
        base = (
            "Air quality is moderate. Outdoor activities are safer during late morning to early afternoon. "
        )

    if conditions:
        base += (
            "Since you have health conditions, limit exposure, stay hydrated, "
            "avoid heavy exertion, and prefer indoor exercises like stretching or yoga. "
        )

    base += (
        f"Peak pollution hours are {peak_hours} due to traffic emissions and atmospheric inversion. "
        "Following preventive guidance reduces long-term respiratory and cardiovascular risks."
    )

    return base

# -----------------------------
# ROUTINE MODIFICATION LOGIC
# -----------------------------
def modify_routine(routine, aqi):
    if aqi > 150:
        return (
            "AI suggests avoiding early morning and evening jogging. "
            "Shift physical activity to indoor workouts, breathing exercises, or light stretching. "
            "Plan outdoor tasks during mid-day when air quality improves. "
            "Maintain hydration and consistent sleep timing."
        )
    else:
        return (
            "AI recommends scheduling jogging or walking between 11 AM and 4 PM. "
            "Avoid traffic-heavy routes, include warm-up and cool-down sessions, "
            "and balance outdoor activity with indoor recovery exercises."
        )

# -----------------------------
# EXTRA HEALTH ADVICE (30–60 WORDS)
# -----------------------------
def extra_health_advice(query, conditions):
    advice = (
        "Based on your concern, AI recommends gradual lifestyle adjustments such as controlled physical activity, "
        "balanced nutrition, adequate hydration, and consistent sleep patterns. "
        "For conditions like obesity or diabetes, daily walking and reduced sedentary time are advised, "
        "while respiratory users should focus on breathing exercises and pollution-safe routines."
    )
    return advice

# -----------------------------
# WEATHER & POLLUTION FORECAST
# -----------------------------
def weather_pollution_forecast(city):
    return (
        f"AI-based pollution forecasting for {city} indicates fluctuating AQI levels over the coming days. "
        "Morning and evening pollution is expected to remain higher due to traffic density. "
        "Users should plan travel during late morning or afternoon, avoid prolonged outdoor exposure, "
        "and follow daily HEALNET alerts for safe activity planning."
    )

# -----------------------------
# API ROUTES
# -----------------------------
@app.route("/get_advice", methods=["POST"])
def get_advice():
    data = request.json
    city = data.get("city")
    conditions = data.get("conditions", [])
    routine = data.get("routine", "")

    aqi = fetch_aqi(city)

    return jsonify({
        "aqi": aqi,
        "aqi_advice": generate_aqi_advice(aqi, conditions),
        "routine_advice": modify_routine(routine, aqi),
        "peak_hours": "7–10 AM and 6–10 PM"
    })

@app.route("/extra_health", methods=["POST"])
def extra_health():
    data = request.json
    query = data.get("query")
    conditions = data.get("conditions", [])

    return jsonify({
        "health_advice": extra_health_advice(query, conditions)
    })

@app.route("/weather_info", methods=["POST"])
def weather_info():
    data = request.json
    city = data.get("city")

    return jsonify({
        "forecast": weather_pollution_forecast(city)
    })

# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)