import requests

def spacex_agent():
    url = "https://api.spacexdata.com/v4/launches/next"
    res = requests.get(url).json()
    launch_data = {
        "name": res.get("name"),
        "date": res.get("date_utc"),
        "location": "Cape Canaveral"
    }
    return launch_data
