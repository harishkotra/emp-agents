# Model Types

When initializing an agent, you need to specify which model to use. The model type can be provided as a parameter when creating either OpenAIBase or AnthropicBase agents, using the respective enums `OpenAIModelType` and `AnthropicModelType`.

## OpenAI Models

For OpenAIBase agents, you can use any of these OpenAIModelType values:

* `gpt3_5` - "gpt-3.5-turbo-0125"
* `gpt3_5_turbo` - "gpt-3.5-turbo"
* `gpt4` - "gpt-4"
* `gpt4_turbo` - "gpt-4-turbo"
* `gpt4o_mini` - "gpt-4o-mini" (128,000 tokens)
* `gpt4o` - "gpt-4o"
* `gpt_o1_mini` - "o1-mini"
* `gpt_o1_preview` - "o1-preview"

## Anthropic Models

For AnthropicBase agents, you can use any of these AnthropicModelType values:

* `claude_3_5_sonnet` - "claude-3-5-sonnet-20240620"
* `claude_3_opus` - "claude-3-opus-20240229"
* `claude_3_sonnet` - "claude-3-sonnet-20240229"
* `claude_3_haiku` - "claude-3-haiku-20240307"
* `claude_2_1` - "claude-2.1"
* `claude_2_0` - "claude-2.0"
* `claude_instant_1_2` - "claude-instant-1.2"


Then, when you create an agent, you can specify the model type as a parameter:

```python
from emp_agents import AgentBase, OpenAIProvider, AnthropicProvider
from emp_agents.providers import OpenAIModelType, AnthropicModelType

# for openai models
agent = AgentBase(
    provider=OpenAIProvider(),
    default_model=OpenAIModelType.gpt4o_mini
)

# or for anthropic
agent = AgentBase(
    provider=AnthropicProvider(),
    default_model=AnthropicModelType.claude_3_5_sonnet
)
```
