# ToolAgent

A simple conversational AI agent with tool-calling capabilities, built on [deepagents](https://github.com/langchain-ai/deepagents) and LangGraph.

## Features

- Interactive CLI chat loop
- Tool calling (weather, time, population lookups)
- Sliding conversation history window
- Powered by DeepSeek via OpenRouter

## Setup

```bash
# Activate the virtual environment
source .venv/bin/activate

# Add your API key to .env
echo 'OPENROUTER_API_KEY="your-key-here"' > .env
```

## Usage

```bash
python agent1.py
```

Type `exit` or `quit` to stop.

## Switching Models

Change the `model` argument in `agent1.py` to use a different provider:

```python
# OpenRouter
model="openrouter:deepseek/deepseek-v4-flash"

# Anthropic (requires ANTHROPIC_API_KEY)
model="anthropic:claude-sonnet-4-6"

# Google (requires GOOGLE_API_KEY)
model="google:gemini-2.0-flash"
```

## Adding Tools

Define any Python function with type hints and a docstring — `create_agent` will register it automatically:

```python
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"Sunny in {city}!"
```

Then pass it in the `tools` list when creating the agent.
