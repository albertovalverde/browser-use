# browser-use
Enable AI to control your browser 🤖

# Quick start

With pip:

```bash
pip install browser-use
```

(optional) install playwright:

```bash
playwright install
```

Spin up your agent:

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

### Test with UI

You can test [browser-use with a UI repository](https://github.com/browser-use/web-ui)

Or simply run the gradio example:

```
uv pip install gradio
```

```bash
python examples/gradio.py
```
