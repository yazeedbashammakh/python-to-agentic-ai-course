
from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

# 1. Define the specialized sub-agents first
code_tutor = LlmAgent(
    name="code_tutor_agent",
    model="gemini-2.5-flash",
    instruction="You are an expert programmer. Provide coding explanations and debug logic."
)

math_tutor = LlmAgent(
    name="math_tutor_agent",
    model="gemini-2.5-flash",
    instruction="You are a mathematics professor. Solve equations and explain core math principles."
)

code_tutor_tool = AgentTool(
    agent=code_tutor
)

math_tutor_tool = AgentTool(
    agent=math_tutor
)

# 2. Assign sub-agents to the parent agent
# The hierarchy is strictly built by providing the sub_agents list to the parent
root_agent = LlmAgent(
    name="Coordinator",
    model="gemini-2.5-flash",
    description="Learning assistant that directs users to either code or math experts.",
    instruction="""
    Analyze the user request:
    1. If they ask about programming or software development then use tool code_tutor_tool.
    2. If they ask about calculations, formulas, or math proofs then use tool math_tutor_tool.

    1. Service Now Ticket:
        - Categorize the ticket based on the description.
    2. Sumarise,
    3. Documentation Update
    4. Correct user assignment
    5. Provide a possible solution to the assignee.
    6. Send mail to someone with the solution.
    """,
    tools=[code_tutor_tool, math_tutor_tool],
    # sub_agents=[code_tutor, math_tutor]
)



# Python program: --> 
# Flow of the program:
# Workflow: 
  # Sequential Workflow:
  # Paralle Workflow:
  # Loop Workflow:
