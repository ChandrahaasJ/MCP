from dotenv import load_dotenv
import os
from google import genai
import asyncio
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
load_dotenv(dotenv_path=r"D:\CODES\Projects\MCPservers\mcp_assignment\.env");

api_key=os.getenv("LLM")
client=genai.Client(api_key=api_key)

async def generate_answer(client,prompt):
    response = await client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text

async def main():
    try:
        print("establishing connection to mcp server")
        server_params=StdioServerParameters(
            command="python",
            args=["server.py"]
        )
        async with stdio_client(server_params) as (read,write):
            print("connected to mcp server")
            async with ClientSession(read,write) as session:
                print("session created,initializing...")
                await session.initialize()
                print("session initialized")

                print("requesting tools")
                tools_res=await session.list_tools()
                tools=tools_res.tools
                print(dir(tools[0]))
            # while True:
            #     prompt=input("Enter a prompt:")
            #     answer=await generate_answer(session,prompt)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("closing session")
        await session.close()

if __name__ == "__main__":
    asyncio.run(main())









