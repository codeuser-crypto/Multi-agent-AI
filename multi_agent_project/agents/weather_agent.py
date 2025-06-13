import requests, os
from dotenv import load_dotenv
load_dotenv

WEATHER_API_KEY = "ab8840fb174a6afa6121311a162206ec"

def weather_agent(launch_data):
    location = launch_data["location"]
    city = location or "Cape Canaveral"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    res = requests.get(url).json()

    if "weather" not in res or "main" not in res:
        print("⚠️ Weather API error:", res)
        return {
            "description": "unavailable",
            "temp": "unknown"
        }

    return {
        "description": res["weather"][0]["description"],
        "temp": res["main"]["temp"]
    }