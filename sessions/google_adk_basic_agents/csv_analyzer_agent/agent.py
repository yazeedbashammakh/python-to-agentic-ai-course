import os
import pandas as pd
from google.adk.agents import Agent

# 1. Define the custom CSV analysis function tool
def analyze_sales_data(metric: str) -> dict:
    """Analyzes a local CSV sales dataset and computes the specified metric.
    
    Args:
        metric: The sales metric to calculate. Supported metrics are:
                'total_revenue' (sum of Sales),
                'average_sales' (mean of Sales),
                'total_quantity' (sum of Quantity).
                
    Returns:
        A dictionary containing the metric name, the calculated value, and success status.
    """
    csv_path = os.path.join(os.path.dirname(__file__), "sales_data.csv")
    try:
        df = pd.read_csv(csv_path)
        if metric == "total_revenue":
            val = float(df["Sales"].sum())
        elif metric == "average_sales":
            val = float(df["Sales"].mean())
        elif metric == "total_quantity":
            val = int(df["Quantity"].sum())
        else:
            return {"status": "Error", "message": f"Unsupported metric: {metric}"}
        return {"status": "Success", "metric": metric, "value": val}
    except Exception as e:
        return {"status": "Error", "message": str(e)}

# 2. Initialize the agent and register the custom tool
root_agent = Agent(
    name="sales_analyst",
    model="gemini-2.5-flash",
    instruction=(
        "You are an automated sales database analyst. "
        "Use the analyze_sales_data tool to extract sales metrics when asked. "
        "Be precise and report results back clearly to the user."
    ),
    tools=[analyze_sales_data]
)
