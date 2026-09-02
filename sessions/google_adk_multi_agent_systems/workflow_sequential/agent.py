
from google.adk.agents import Agent, SequentialAgent

# Step 1: Research
researcher = Agent(
    model="gemini-2.5-flash",
    name="researcher",
    instruction="Research the given topic and provide key findings.",
)

# Step 2: Write
writer = Agent(
    model="gemini-2.5-flash",
    name="writer",
    instruction="Take the research findings and write a clear summary.",
)

# Step 3: Edit
editor = Agent(
    model="gemini-2.5-flash",
    name="editor",
    instruction="Review and polish the summary for clarity and grammar.",
)

# Sequential Pipeline: Research → Write → Edit
root_agent = SequentialAgent(
    name="content_pipeline",
    sub_agents=[researcher, writer, editor],
)
