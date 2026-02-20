"""
Step 5: Access MCP Resources
"""

import os
import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

print("=" * 60)
print("STEP 5: Accessing MCP Resources")
print("=" * 60)

async def main():
    # Connect to MCP server
    print("\n📁 Connecting to MCP filesystem server...")
    
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
        async with client.session("filesystem"):
            print("✓ Connected to MCP server")
            
            # Get resources (read-only data)
            print("\n📚 Getting available resources...")
            resources = await client.get_resources()
            
            if resources:
                print(f"✓ Found {len(resources)} resources")
                for i, resource in enumerate(resources, 1):
                    print(f"\n  {i}. {resource}")
            else:
                print("ℹ️ No resources found - this is normal for filesystem server")
                print("   Resources are different from tools. They provide read-only data.")
                print("   The filesystem server focuses on TOOLS (read/write) not RESOURCES.")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
    
    print("\n🔌 Connection closed")

if __name__ == "__main__":
    asyncio.run(main())