
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("No Readme Test Server")

@mcp.tool()
def hello(name: str = "World") -> str:
    """向指定用户打招呼"""
    return f"Hello, {name}! MCP Server is working."

@mcp.tool()
def add(a: int, b: int) -> int:
    """计算两个整数的和"""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="stdio")
