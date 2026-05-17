# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment Setup

This project uses a Python 3.12 virtual environment located at `.venv/`.

```bash
source .venv/bin/activate
```

Run the agent:
```bash
python agent1.py
```

Install new dependencies (activate venv first):
```bash
pip install <package>
```

## Architecture

This is a single-file conversational agent (`agent1.py`) built on the **deepagents** framework (LangChain's "Deep Agents" library, v0.6.1), which enables sub-agent spawning, planning, and mock filesystem access on top of LangGraph.

**Key components:**

- `create_agent` from `langchain.agents` — constructs a ReAct-style tool-calling agent backed by a LangGraph state machine
- **Model**: OpenRouter (`langchain-openrouter`) routing to `deepseek/deepseek-v4-flash`; can also swap in Anthropic or Google Gemini models since those packages are installed
- **Tools**: plain Python functions with type hints and docstrings — `create_agent` introspects the signature and docstring to generate the tool schema automatically
- **Conversation history**: a rolling window of the last `N=10` messages is passed to `agent.invoke({"messages": ...})` each turn

**Supported model provider prefixes** (via installed integrations):
- `openrouter:<model>` — OpenRouter (requires `OPENROUTER_API_KEY`)
- Anthropic models — via `langchain-anthropic` (requires `ANTHROPIC_API_KEY`)
- Google models — via `langchain-google-genai` (requires `GOOGLE_API_KEY`)

## Environment Variables

Stored in `.env`, loaded automatically via `python-dotenv`:

| Variable | Purpose |
|---|---|
| `OPENROUTER_API_KEY` | Required for the current OpenRouter-backed model |
