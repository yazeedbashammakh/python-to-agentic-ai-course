
from google.adk.tools import ToolContext
from google.adk.agents import LlmAgent


def process_cart_action(tool_context: ToolContext, item_id: str, action: str) -> str:
    """Manages the user's current shopping cart, applies loyalty benefits, and checks global inventory.
    Args:
        tool_context (ToolContext): The context object that provides access to the agent's state and tools.
        item_id (str): The unique identifier of the item to be added or removed from the cart.
        action (str): The action to perform, either "add" or "remove".
    """
    
    # -------------------------------------------------------------
    # 1. APP LEVEL (app: Prefix) - Shared Global Inventory & Rules
    # -------------------------------------------------------------
    # Retrieve system-wide inventory dictionary from the global app state
    inventory = tool_context.state.get("app:flash_sale_inventory", {"ITEM_99": 5, "ITEM_100": 10, "ITEM_101": 0})
    store_promo_active = tool_context.state.get("app:global_promo_active", True)
    
    if action == "add":
        available_stock = inventory.get(item_id, 0)
        if available_stock <= 0:
            return f"Error: Item {item_id} is globally out of stock for this flash sale!"
            
        # Deduct item from global inventory so other users can't buy it
        inventory[item_id] = available_stock - 1
        tool_context.state["app:flash_sale_inventory"] = inventory

    # -------------------------------------------------------------
    # 2. USER LEVEL (user: Prefix) - Persistent Customer Data
    # -------------------------------------------------------------
    # Fetching profile data that persists across separate visits
    if "user:loyalty_tier" not in tool_context.state:
        tool_context.state["user:loyalty_tier"] = 'STANDARD'

    user_tier = tool_context.state.get("user:loyalty_tier", "STANDARD") # e.g., VIP, GOLD
    shipping_zip = tool_context.state.get("user:saved_shipping_zip", "90210")
    
    # Give VIP users automatic perks
    discount_multiplier = 0.85 if user_tier == "VIP" else 1.0

    # -------------------------------------------------------------
    # 3. SESSION LEVEL (No Prefix) - Current Active Cart
    # -------------------------------------------------------------
    # Fetch or initialize the cart isolated to this specific chat session
    if "active_shopping_cart" not in tool_context.state:
        tool_context.state["active_shopping_cart"] = []
    current_cart = tool_context.state.get("active_shopping_cart", [])
    
    if action == "add":
        current_cart.append(item_id)
    elif action == "remove" and item_id in current_cart:
        current_cart.remove(item_id)
        # Return item back to global inventory pool
        inventory[item_id] = inventory.get(item_id, 0) - 1
        tool_context.state["app:flash_sale_inventory"] = inventory
        
    tool_context.state["active_shopping_cart"] = current_cart

    # -------------------------------------------------------------
    # Summary Output for the LLM to process
    # -------------------------------------------------------------
    return (
        f"Action successful. Current Session Cart contains: {current_cart}.\n"
        f"User Tier Profile: {user_tier} (Applied Discount Factor: {discount_multiplier}). Shipping to: {shipping_zip}.\n"
        f"App Inventory Update: Only {inventory.get(item_id, 0)} units left globally for Item {item_id}. "
        f"Global Promo Status: {store_promo_active}."
    )

def list_current_inventory(tool_context: ToolContext) -> str:
    """Retrieves and lists the entire live product catalog and available stock levels."""
    # 1. Fetch the global app-level state dictionary
    if "app:flash_sale_inventory" not in tool_context.state:
        tool_context.state["app:flash_sale_inventory"] = {
            "ITEM_99": 5, 
            "ITEM_100": 10, 
            "ITEM_101": 0
        }
        inventory = tool_context.state.get("app:flash_sale_inventory", {"ITEM_99": 5, "ITEM_100": 10, "ITEM_101": 0})
    
    if not inventory:
        return "The flash sale store catalog is currently empty."
        
    # 2. Format a human-readable list for the agent to use
    lines = ["Here is the current live product inventory:"]
    for item_id, stock in inventory.items():
        status = f"{stock} units available" if stock > 0 else "OUT OF STOCK"
        lines.append(f"- Product Code: {item_id} | Stock Status: {status}")
        
    return "\n".join(lines)


root_agent = LlmAgent(
    name="checkout_assistant",
    model="gemini-2.5-flash",
    instruction=(
        "You are an AI sales assistant helping a user in the {{user:loyalty_tier | default('STANDARD')}} tier. "
        "Their current active session cart is: {{active_shopping_cart | default('[]')}}. "
        "Help them manage their items."
    ),
    tools=[process_cart_action, list_current_inventory]
)


# user input -> Agent invoke (InvocationContext) -> ToolContext ()