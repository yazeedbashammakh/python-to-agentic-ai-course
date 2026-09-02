
from google.adk.agents import LlmAgent

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

# 2. Assign sub-agents to the parent agent
# The hierarchy is strictly built by providing the sub_agents list to the parent
root_agent = LlmAgent(
    name="Coordinator",
    model="gemini-2.5-flash",
    description="Learning assistant that directs users to either code or math experts.",
    instruction="""
    Analyze the user request:
    1. If they ask about programming or software development, delegate to code_tutor_agent.
    2. If they ask about calculations, formulas, or math proofs, delegate to math_tutor_agent.
    """,
    sub_agents=[code_tutor, math_tutor]
)
