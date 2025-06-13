def summary_agent(data):
    weather = data.get("weather", {})
    launch = data.get("launch", {})
    
    if not weather or not launch:
        return "Missing data to summarize."

    summary = f"The next SpaceX launch is '{launch['name']}' on {launch['date']} at {launch['location']}.\n"
    summary += f"Weather forecast: {weather['description']} with temperature {weather['temp']}°C.\n"

    if "rain" in weather['description'].lower():
        summary += "🚨 Possible delay due to rain."
    else:
        summary += "✅ Launch likely on schedule."

    return summary
