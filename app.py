from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# --- AI Logic Functions ---

def fetch_aqi(city):
    """Simulates fetching real-time AQI data."""
    return random.randint(40, 220)

def generate_aqi_advice(aqi, conditions):
    """AI logic for AQI health reasoning."""
    peak_hours = "7–10 AM and 6–10 PM"
    status = "Unhealthy" if aqi > 150 else "Moderate to Good"
    
    advice = f"The current AQI is {aqi} ({status}). "
    advice += f"Pollution levels usually spike during {peak_hours} due to traffic emissions and atmospheric inversion. "
    
    if aqi > 150:
        advice += "Stay indoors and use air purifiers. "
    else:
        advice += "Air quality is acceptable for short outdoor durations. "
        
    if conditions:
        advice += f"Given your health conditions ({conditions}), please avoid any outdoor exertion and keep rescue inhalers or medications ready."
    
    return advice

def modify_routine(routine, aqi):
    """AI logic for routine adjustment."""
    if aqi > 150:
        return f"MODIFIED: Your routine '{routine}' should be moved indoors. Avoid outdoor activity. Suggesting mid-day (12-3 PM) for errands when inversion lifts."
    return f"SUGGESTED: Your routine '{routine}' is safe, but monitor breathing. Best to schedule heavy tasks between 11 AM and 4 PM."

def extra_health_advice(conditions):
    """Generalized health AI function."""
    return (f"Regardless of AQI, prioritize hydration and 7-9 hours of sleep to support lung recovery. "
            f"If managing {conditions or 'general health'}, include antioxidant-rich foods like berries and leafy greens "
            f"to combat oxidative stress from particulate matter. Maintain metabolic health with light indoor stretching.")

def weather_pollution_forecast(city):
    """AI forecasting logic."""
    return (f"Forecast for {city}: Short-term pollution trends show a 15% increase in PM2.5. "
            "Expect higher morning and evening density. HEALNET Alert: Plan travel between 1 PM and 5 PM for lower exposure.")

# --- API Endpoints (POST Only) ---

@app.route('/get_advice', methods=['POST'])
def get_advice():
    data = request.json
    city = data.get('city', 'Unknown')
    conditions = data.get('conditions', '')
    routine = data.get('routine', 'Daily work')
    
    aqi = fetch_aqi(city)
    advice = generate_aqi_advice(aqi, conditions)
    adjusted_routine = modify_routine(routine, aqi)
    
    return jsonify({
        "city": city,
        "aqi": aqi,
        "health_advisory": advice,
        "routine_adjustment": adjusted_routine,
        "peak_hours": "7–10 AM and 6–10 PM"
    })

@app.route('/extra_health', methods=['POST'])
def extra_health():
    data = request.json
    conditions = data.get('conditions', 'none')
    advice = extra_health_advice(conditions)
    return jsonify({"extra_health_recommendation": advice})

@app.route('/weather_info', methods=['POST'])
def weather_info():
    data = request.json
    city = data.get('city', 'Unknown')
    forecast = weather_pollution_forecast(city)
    return jsonify({"city": city, "pollution_forecast": forecast})

if __name__ == "__main__":
    # Running strictly as a backend AI service
    app.run(debug=True)