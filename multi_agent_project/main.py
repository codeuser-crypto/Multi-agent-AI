import os
from dotenv import load_dotenv
from agents.spacex_agent import spacex_agent
from agents.weather_agent import weather_agent
from agents.summary_agent import summary_agent

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
print("🔑 Loaded WEATHER_API_KEY:", os.getenv("WEATHER_API_KEY"))  # For debug

# User goal
goal = "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."

def run_multi_agent_system(goal):
    print(f"\n🚀 User Goal: {goal}\n")

    data = {}
    
    # Agent 1: Get SpaceX launch details
    data["launch"] = spacex_agent()

    # Agent 2: Get weather at launch location
    data["weather"] = weather_agent(data["launch"])

    # Agent 3: Summarize possibility of delay
    result = summary_agent(data)

    return result

# Run system
if __name__ == "__main__":
    result = run_multi_agent_system(goal)
    print("\nFinal Result:\n", result)
