from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv
import asyncio, os

load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

def get_time(city: str) -> str:
    """Get the current time for a given city."""
    return f"The current time in {city} is 12:00 PM."

def get_population(city: str) -> str:
    """Get the population of a given city."""
    return f"The population of {city} is approximately 1 million people."

SERVER = os.path.join(os.path.dirname(__file__), "server.py")

async def main():
    client = MultiServerMCPClient({
        "fs": {"command": "python", "args": [SERVER], "transport": "stdio"}
    })
    mcp_tools = await client.get_tools()
    agent = create_agent(
        model="openrouter:deepseek/deepseek-v4-flash",
        tools=[get_weather, get_time, get_population] + mcp_tools,
        system_prompt="You are a helpful assistant.",
    )
    history = []
    N = 10
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ("exit", "quit"):
                break
            history.append({"role": "user", "content": user_input})
            result = await agent.ainvoke({"messages": history[-N:]})
            last_msg = result["messages"][-1]
            content = last_msg.content
            if isinstance(content, str):
                assistant_reply = content
            elif isinstance(content, list):
                assistant_reply = next(
                    (b["text"] for b in content if isinstance(b, dict) and b.get("type") == "text"),
                    ""
                )
            else:
                assistant_reply = ""
            history.append({"role": "assistant", "content": assistant_reply})
            print("Agent:", assistant_reply)
    finally:
        for session in client.sessions.values():
            await session.__aexit__(None, None, None)

asyncio.run(main())
