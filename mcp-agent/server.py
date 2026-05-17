from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("fs")

@mcp.tool()
def list_directory(path: str) -> str:
    """List files and folders in a local directory."""
    try:
        entries = os.listdir(path)
        return "\n".join(entries) if entries else "(empty)"
    except OSError as e:
        return f"Error: {e.strerror}: {path}"

if __name__ == "__main__":
    mcp.run()
