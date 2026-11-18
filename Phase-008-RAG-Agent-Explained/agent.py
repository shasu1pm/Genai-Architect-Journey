"""The CrewAI shopping agent: one Agent, one Task and one Crew, wired to the MCP tools.

The MCP server (mcp_server.py) is started over stdio and its tools are handed to the
agent. Run this file directly for a one-question smoke test; app.py (Streamlit) and
api.py (FastAPI) import `crew` from here.
"""
import os
import sys
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters

load_dotenv()

server_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mcp_server.py")
server_params = StdioServerParameters(
    command=sys.executable,
    args=[server_file],
    env=dict(os.environ),
)

mcp_adapter = MCPServerAdapter(server_params)
shop_tools = mcp_adapter.tools
print("MCP tools loaded:", [tool.name for tool in shop_tools])

shop_agent = Agent(
    role="Shopping Assistant",
    goal="Help customers find products and manage their shopping cart",
    backstory=(
        "You are a friendly shopping assistant for the ShopEasy online store. "
        "For any question about products, prices or features, always use the search_products tool "
        "and answer only from what it returns. Never make up products or prices. "
        "Before adding to the cart, use search_products to get the exact product name and price. "
        "Use the cart tools to add, remove, view or clear the cart."
    ),
    tools=shop_tools,
    llm="gpt-4o-mini",
    verbose=True,
)

shop_task = Task(
    description=(
        "Previous chat (for context, can be empty):\n{history}\n\n"
        "Customer's new message: {question}"
    ),
    expected_output="A short, clear and friendly reply to the customer.",
    agent=shop_agent,
)

crew = Crew(
    agents=[shop_agent],
    tasks=[shop_task],
    verbose=True,
)

if __name__ == "__main__":
    answer = crew.kickoff(inputs={"history": "", "question": "Which headphones do you have and what is the price?"})
    print(answer)
    mcp_adapter.stop()
