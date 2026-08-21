from google.adk.agents import Agent
from weather_agent.weather_tool import get_current_weather


root_agent = Agent(
    name="weather_agent",
    model="gemini-2.5-flash",
    instruction=(
        "You are a helpful weather assistant."
        "Use the get_current_weather tool to provide accurate and up-to-date weather information when asked."
        "Always provide the weather details in a clear and concise manner."
    ),
    tools=[get_current_weather]
)
