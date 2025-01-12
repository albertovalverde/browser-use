from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

async def main():
    agent = Agent(
        task="""Go to the Boletín Oficial del Estado website, 
        search for 'despidos colectivos' in the search bar, 
        return the last 5 titles listed""",
        llm=ChatOpenAI(model="gpt-4o",temperature=0.50)
    )
    result = await agent.run()
    print(result)

asyncio.run(main())