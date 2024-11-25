import asyncio
import os

from emp_agents.agents.persistentagent import PersistentAgent, PersistentAgentConfig
from emp_agents.models.protocol.registry import ToolRegistry
from emp_agents.types import AnthropicModelType

describe_protocol_tool = ToolRegistry.get_tool("ERC20Skill", "describe_protocol")

agent = PersistentAgent.from_config(
    PersistentAgentConfig(
        agent_id="dynamic_agent",
        name="Tools",
        description="Tools for interacting with the blockchain",
        tools=[describe_protocol_tool],
        default_model=AnthropicModelType.claude_3_5_sonnet,
        extra={
            "openai_api_key": os.environ.get("OPENAI_API_KEY"),
        },
    )
)

if __name__ == "__main__":
    asyncio.run(agent.run())
