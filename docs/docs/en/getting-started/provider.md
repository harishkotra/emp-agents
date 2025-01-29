# Provider

Providers are used to connect the `AgentBase` to different LLM providers.

Currently we support OpenAI and Anthropic using `OpenAIProvider` and `AnthropicProvider`.

In order to use the provider, you need to pass the api_key directly to the provider, or set the `api_key` environment variable.

```bash
export OPENAI_API_KEY=...
export ANTHROPIC_API_KEY=...
```

## Example

```python
import asyncio
from emp_agents import AgentBase, OpenAIProvider

agent = AgentBase(
    provider=OpenAIProvider(),
)

print(asyncio.run(agent.answer("What is the capital of France?")))
```
