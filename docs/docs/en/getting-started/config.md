An agent can be loaded from a config object, using the `PersistentAgentConfig` and an agent that inherits from the `emp_agents.agents.PersistentAgent` class.  This allows for an agent to be loaded via `PersistentAgent.from_config(config)`, where the config is an object of type `PersistentAgentConfig`.


```python
from emp_agents.config.agent_config import PersistentAgentConfig
from emp_agents.agents.persistentagent import PersistentAgent

config = PersistentAgentConfig(
    agent_id="test-agent-1",
    name="Test Agent",
    description="A test agent",
    default_model="gpt-3.5-turbo",
    prompt="You are a test assistant",
    tools=[],
    requires=[],
)
agent = PersistentAgent.from_config(config)
```
