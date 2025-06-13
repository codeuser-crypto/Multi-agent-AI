def planner_agent(goal):
    if "launch" in goal and "weather" in goal:
        return ["get_launch", "get_weather", "summarize"]
    else:
        return ["summarize"]
