from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

# Define the root agent using OpenAI's GPT-4o via LiteLLM
root_agent = LlmAgent(
    model=LiteLlm(model="openai/gpt-4o"),
    name="gpt_agent",
    description="An ADK agent powered by OpenAI GPT-4o",
    instruction="You are a helpful assistant.",
)
