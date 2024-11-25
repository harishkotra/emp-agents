# Context Window

The context window is a fundamental concept in Large Language Models (LLMs) that refers to the maximum amount of text that the model can process at once. This includes both the input (prompt) and the expected output.

## Key Points

- The context window is measured in tokens (roughly 4 characters per token in English)
- Different models have different context window sizes:
  - GPT-4 Turbo: 128K tokens
  - Claude 3 Opus: 200K tokens
  - GPT-3.5 Turbo: 16K tokens
- Longer conversations need to be summarized to fit within the context window
- The context window affects:
  - Memory of previous conversation
  - Ability to process long documents
  - Cost (as most models charge per token)

## Managing Context

emp-agents provides tools to help manage the context window:

- Token counting via `count_tokens()` function
- Conversation summarization via `summarize_conversation()` or `agent.summarize()`
- Automatic tracking of conversation history

See the [Summarizing Conversations](../getting-started/summarize.md) section for practical examples of context management.


```python
from emp_agents import AgentBase
from emp_agents.models import Message, Role

messages = [
    Message(role=Role.user, content="Hello, how are you?"),
    Message(role=Role.assistant, content="I'm doing great, thank you!"),
]

agent = AgentBase()
agent.add_messages(messages)
token_count = agent.get_token_count()
print(token_count)

# Output: 35
```
