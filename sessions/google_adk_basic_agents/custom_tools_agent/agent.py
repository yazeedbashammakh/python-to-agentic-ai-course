
from google.adk.agents import Agent
from google.adk.tools import google_search


# 1. Define the custom function tool
def get_student_fee_status(student_id: str) -> dict:
    """Retrieves the tuition fee payment status and balance for a student by their unique student ID.
    
    Args:
        student_id: The unique identifier of the student (e.g., 'STU123', 'STU456').
        
    Returns:
        A dictionary with the student's name, payment status, and outstanding balance.
    """
    # Dummy database records
    records = {
        "STU123": {"name": "Aarav Sharma", "status": "Paid", "balance": 0.0},
        "STU456": {"name": "Priya Patel", "status": "Pending", "balance": 1200.00},
        "STU789": {"name": "Rahul Verma", "status": "Overdue", "balance": 3500.50}
    }
    return records.get(student_id, {"status": "Error", "message": f"Student ID {student_id} not found."})


# 2. Initialize the agent and pass the custom function into tools
root_agent = Agent(
    name="fee_coordinator",
    model="gemini-2.5-flash",
    instruction=(
        "You are a helpful university administrative assistant. "
        "Use the get_student_fee_status tool to check details when a user asks about fee status. "
        "Always repeat the student's name, status, and outstanding balance in a friendly, conversational tone."
    ),
    tools=[get_student_fee_status, google_search]
)
