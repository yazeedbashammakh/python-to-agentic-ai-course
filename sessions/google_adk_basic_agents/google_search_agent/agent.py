



from google.adk.agents import LlmAgent
from google.adk.tools import google_search

# Define the agent with the google_search tool
root_agent = LlmAgent(
    name="search_assistant",
    model="gemini-2.5-flash",
    instruction=(
        "You are a helpful research assistant. "
        "Use the google_search tool when asked about current events, "
        "recent developments, or facts requiring real-time web searches. "
        "Always ground your answers in the search results."
    ),
    tools=[google_search]
)