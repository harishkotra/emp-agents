# Provider

Providers are used to connect the `AgentBase` to different LLM providers.

Currently we support OpenAI, Anthropic and OpenRouter using `OpenAIProvider`, `AnthropicProvider` and `OpenRouterProvider`.

In order to integrate an additional provider, you need to create a new provider class that implements the `Provider` protocol.

```python
from pydantic import BaseModel
from emp_agents.models import Provider, Request, ResponseT


class Response(ResponseT):
    """A response object that is specific to the provider, that implements the ResponseT interface."""


class LLMProvider(Provider[Response]):
    api_key: str | None = None
    default_model: str | None = None

    def _load_model(self, model: str | None) -> str:
        if model is None:
            model = self.default_model
        if not model:
            raise ValueError("No model provided")
        return model

    async def completion(self, request: Request) -> Response:
        """A function that takes the Generic Request object, and returns a provider's Response object."""
```

In order to use an existing provider, you need to pass the api_key directly to the provider, or set the `api_key` environment variable.  Then you can inject the provider as a dependency into the `AgentBase` class.

## Example

Update your environment variables with your provider's api key.

```bash
export OPENAI_API_KEY=...
export ANTHROPIC_API_KEY=...
export OPENROUTER_API_KEY=...
```

Then you can inject the provider as a dependency into the `AgentBase` class.

```python
import asyncio
from emp_agents import AgentBase, OpenAIProvider

agent = AgentBase(
    provider=OpenAIProvider(),
)

print(asyncio.run(agent.answer("What is the capital of France?")))
```
