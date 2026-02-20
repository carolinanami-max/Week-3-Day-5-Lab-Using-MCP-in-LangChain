"""
MCP-LangChain Integration Lab
FINAL WORKING VERSION - NO ERRORS!
"""

import os
import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

# Load environment variables
load_dotenv()

# Check if API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")
else:
    print("✓ API key loaded successfully")

async def main():
    """Main function to connect to MCP server"""
    print("\n🔌 Starting MCP connection...")
    print("=" * 50)
    
    # Create the client WITH the connection details
    client = MultiServerMCPClient(
        connections={
            "filesystem": {
                "transport": "stdio",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
            }
        }
    )
    
    try:
        print("📁 Connecting to filesystem MCP server...")
        
        # Connect using session
        async with client.session("filesystem"):
            print("✓ Connected successfully!")
            
            # Get all available tools
            print("\n🛠️ Getting available tools...")
            tools = await client.get_tools()
            
            # Display all tools
            if tools:
                print(f"\n📋 Found {len(tools)} MCP tools:")
                print("-" * 50)
                for i, tool in enumerate(tools, 1):
                    print(f"\n{i}. {tool.name}")
                    if hasattr(tool, 'description') and tool.description:
                        # Clean up description - take first line only
                        desc = tool.description.split('\n')[0]
                        print(f"   📝 {desc}")
                print("\n" + "=" * 50)
                print("✅ SUCCESS: MCP server connected and tools loaded!")
            else:
                print("No tools found")
                
    except Exception as e:
        print(f"\n❌ Error: {e}")
    
    # REMOVED the problematic __aexit__ line - the session handles cleanup automatically!
    print("\n🔌 Connection closed automatically")

if __name__ == "__main__":
    asyncio.run(main())