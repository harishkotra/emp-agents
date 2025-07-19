# Using the Gaia Provider

The Gaia provider allows you to connect to your own Gaia Node for LLM inference with emp_agents.

## Setup

To use the Gaia provider, you'll need:

1. A Gaia Node URL
2. A Gaia API Key
3. The name of the model you want to use

## Basic Usage

```python
from emp_agents import AgentBase
from emp_agents.providers import GaiaProvider

# Create a Gaia provider
provider = GaiaProvider(
    url="https://your-gaia-node-url.com/v1/chat/completions",
    api_key="your-gaia-api-key",
    model_name="your-model-name"
)

# Create an agent using the Gaia provider
agent = AgentBase(provider=provider)

# Use the agent
response = await agent.answer("Hello, how can you help me today?")
print(response)
```

## Environment Variables

For better security, you can use environment variables to store your Gaia credentials:

```bash
export GAIA_NODE_URL="https://your-gaia-node-url.com/v1/chat/completions"
export GAIA_API_KEY="your-gaia-api-key"
export GAIA_MODEL_NAME="your-model-name"
```

Then in your code:

```python
import os
from emp_agents import AgentBase
from emp_agents.providers import GaiaProvider

provider = GaiaProvider(
    url=os.environ["GAIA_NODE_URL"],
    api_key=os.environ["GAIA_API_KEY"],
    model_name=os.environ["GAIA_MODEL_NAME"]
)

agent = AgentBase(provider=provider)
```

## Advanced Features

The Gaia provider supports all the features of emp_agents, including:

- System messages
- Conversation history
- Function calling (tools)
- Structured output

See the examples in `examples/gaia_example.py` and `examples/gaia_advanced_example.py` for more details.
