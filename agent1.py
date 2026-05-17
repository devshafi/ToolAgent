from langchain.agents import create_agent
from dotenv import load_dotenv
import os

# Load the api key from env
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

agent = create_agent(
    model="openrouter:deepseek/deepseek-v4-flash",
    tools=[get_weather, get_time, get_population],
    system_prompt="You are a helpful assistant.",
)

history = []
N = 10  # number of messages to keep

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break
    history.append({"role": "user", "content": user_input})
    result = agent.invoke({"messages": history[-N:]})
    last_msg = result["messages"][-1]
    assistant_reply = next(
        (b["text"] for b in (getattr(last_msg, "content_blocks", None) or []) if b["type"] == "text"),
        last_msg.content if isinstance(last_msg.content, str) else ""
    )
    history.append({"role": "assistant", "content": assistant_reply})
    print("Agent:", assistant_reply)