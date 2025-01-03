import asyncio
import os

from emp_agents.agents.history import AbstractConversationProvider
from emp_agents.agents.skills import SkillsAgent
from emp_agents.tools.protocol.erc20 import ERC20Skill
from emp_agents.tools.protocol.gmx import GmxSkill
from emp_agents.tools.protocol.network import NetworkSkill
from emp_agents.tools.protocol.wallets import SimpleWalletSkill
from emp_agents.types import OpenAIModelType
from emp_agents.models import Message
from emp_agents.types import OpenAIModelType
from pydantic import Field
import random

external_conversation = [
    Message(role="user", content="Hello, how are you?"),
    Message(role="assistant", content="I'm fine, thank you!"),
]


class RandomConversationProvider(AbstractConversationProvider):

    def set_history(self, messages: list[Message]) -> None:
        pass

    def add_message(self, message: Message) -> None:
        external_conversation.append(message)

    def add_messages(self, messages: list[Message]) -> None:
        external_conversation.extend(messages)

    def get_history(self) -> list[Message]:
        return random.sample(
            external_conversation, k=min(len(external_conversation), 2)
        )

    def reset(self) -> None:
        pass


class ERC20Agent(SkillsAgent):
    def _load_implicits(self):
        if private_key := os.environ.get("EMP_AGENT_PRIVATE_KEY"):
            SimpleWalletSkill.set_private_key(private_key)
        if network := os.environ.get("EMP_AGENT_NETWORK", "ArbitrumSepolia"):
            NetworkSkill.set_network(network)


conversation_provider = RandomConversationProvider()

agent = ERC20Agent(
    skills=[
        ERC20Skill,
        NetworkSkill,
        SimpleWalletSkill,
        GmxSkill,
    ],
    default_model=OpenAIModelType.gpt4o_mini,
    _conversation=conversation_provider,
)

if __name__ == "__main__":
    asyncio.run(agent.run())
