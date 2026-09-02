from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field
from google.adk.agents import Agent

# 1. Define categorical options using Enums
class TicketCategory(str, Enum):
    BILLING = "billing"
    TECHNICAL = "technical"
    ACCOUNT_ACCESS = "account_access"
    FEATURE_REQUEST = "feature_request"

class UrgencyLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

# 2. Define the structured output schema
class TicketAnalysis(BaseModel):
    category: TicketCategory = Field(description="The primary department for this issue.")
    urgency: UrgencyLevel = Field(description="Priority level based on user frustration or business impact.")
    summary: str = Field(description="A concise, 1-sentence summary of the user's issue.")
    account_id: Optional[str] = Field(None, description="The extracted account or customer ID if mentioned.")
    key_phrases: List[str] = Field(description="3-5 extracted keywords or error codes.")
    summary: str = Field(description="A concise, 1-sentence summary of the user's issue.")



# 3. Configure the ADK Router Agent
root_agent = Agent(
    name="ticket_triage_agent",
    model="gemini-2.5-flash",
    instruction=(
        "Analyze incoming customer support emails. Extract the structural metadata "
        "required by the output schema to route the ticket efficiently."
    ),
    output_schema=TicketAnalysis,
)



