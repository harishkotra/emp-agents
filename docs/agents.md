# Building agents

## Overview

The **emp-agents** SDK provides a unified interface for creating and managing AI agents that can interact with various external systems, including blockchain networks. This abstraction allows developers to seamlessly switch between different AI models, such as OpenAI and Anthropic, without changing the underlying code structure. The agents are designed to be modular and extensible, allowing you to easily add new capabilities through tools and skills.

## Creating an Agent

To create an agent, you can instantiate the `SkillsAgent` class, which allows you to define the skills (tools) that the agent will use. Below is a minimal example of how to create an agent and run it:

```python
import asyncio
import os

from eth_rpc import set_alchemy_key

from emp_agents.types import AnthropicModelType
from emp_agents.agents.skills import SkillsAgent
from emp_agents.tools.protocol.erc20 import ERC20Skill

if alchemy_key := os.environ.get("ALCHEMY_KEY"):
    set_alchemy_key(alchemy_key)

agent = SkillsAgent(
    skills=[
        ERC20Skill,
    ],
    default_model=AnthropicModelType.claude_3_5_sonnet,
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
)

if __name__ == "__main__":
    asyncio.run(agent.run())
```

## Running an example

```bash
OPENAI_API_KEY=<your-openai-api-key> ALCHEMY_KEY=<your-alchemy-key> python examples/erc20.py
```
## Available Agent Skills

The following agent skills are currently available in the **emp-agents** SDK:

- [ERC20Skill](../src/emp_agents/tools/protocol/erc20.py): A skill for interacting with ERC20 tokens on the blockchain.
- [SimpleWalletSkill](../src/emp_agents/tools/protocol/wallets.py): A skill for managing simple wallet operations.
- [GMXTool](../src/emp_agents/tools/protocol/gmx.py): A skill for interacting with GMX decentralized exchange.
- [TwitterSkill](../src/emp_agents/tools/twitter/__init__.py): A skill for managing Twitter interactions and posting tweets.


Feel free to explore these skills and integrate them into your agents as needed. 


## Extending the Skills Ecosystem

To extend the skills ecosystem, you can create new skill classes that implement the necessary functionality. The following classes are essential for defining new skills:

- `SkillSet`: This class serves as a base for creating AI-related skills, allowing them to interact with various AI models.
- `view_action`: A decorator that marks a method as a view action, which can be called to retrieve information without modifying the state.
- `onchain_action`: A decorator that marks a method as an on-chain action, which interacts with blockchain networks.

### Creating a New Skill

Here’s a simple example of how to create a new skill that fetches weather data from an API:

```python
import aiohttp
from typing import Annotated
from typing_extensions import Doc
from emp_agents.models.protocol import SkillSet, view_action, onchain_action


class WeatherSkill(SkillSet):
    @view_action
    @staticmethod
    async def get_weather_info(city: Annotated[str, Doc("The name of city in the format of wttr.in")]) -> str:
        """Fetch weather data for a given city from a public."""
        url = f"https://wttr.in/{city}?format=3"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()  # Returns a simple weather report
                else:
                    return f"Error fetching weather data: {response.status}"
```
