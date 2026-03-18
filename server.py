from mcp.server.fastmcp import FastMCP
from github_client import create_repo, add_file

mcp = FastMCP("github-mcp-server")


@mcp.tool()
def create_repo_tool(repo_name: str) -> str:
    result = create_repo(repo_name)

    if result["status"] == "success":
        return "Repository created successfully"
    return f"Error: {result['message']}"


@mcp.tool()
def add_file_tool(repo_name: str, filename: str, content: str) -> str:
    result = add_file(repo_name, filename, content)

    if result["status"] == "success":
        return result["message"]
    return f"Error: {result['message']}"


if __name__ == "__main__":
    mcp.run(transport="stdio")