# Browser-use Researching from Main Repository
Research based on Browser-use library.

This repository serves as the foundation for building intelligent agents that interact with websites, enabling tasks such as extracting relevant information from web pages and automating processes. The research focuses on applying these technologies to optimize tasks related to monitoring legislative changes, as demonstrated in the example of monitoring the Boletín Oficial del Estado (BOE).


## Enable AI to control your browser 🤖

## Quick start

With pip:

```bash
pip install browser-use
```

(optional) install playwright:

```bash
playwright install
```

Spin up your agent (test.py):

```python 
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

asyncio.run(main()))
```

And don't forget to add your API keys to your `.env` file.

```bash
OPENAI_API_KEY=
```

For other settings, models, and more, check out the [documentation 📕](https://docs.browser-use.com).

## Test with UI

You can test [browser-use with a UI repository](https://github.com/browser-use/web-ui)

Or simply run the gradio example:

```
uv pip install gradio
```

```bash
python examples/gradio.py
```
