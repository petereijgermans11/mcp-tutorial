from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide two numbers and return the result."""
    return a / b

if __name__ == "__main__":
    mcp.run()

