from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService, DatabaseSessionService

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


# session_service = InMemorySessionService()

DB_URL = "sqlite+aiosqlite:///./session_demo.db"
session_service = DatabaseSessionService(db_url=DB_URL)

runner = Runner(
    agent=root_agent,
    app_name="my-app",
    session_service=session_service,
)


