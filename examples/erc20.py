import asyncio
import os

from eth_rpc import set_alchemy_key

from emp_agents.agents.skills import SkillsAgent
from emp_agents.tools.dexscreener import DexScreenerSkill
from emp_agents.tools.protocol.erc20 import ERC20Skill
from emp_agents.tools.protocol.wallets import SimpleWalletSkill
from emp_agents.types import AnthropicModelType

if alchemy_key := os.environ.get("ALCHEMY_KEY"):
    set_alchemy_key(alchemy_key)


agent = SkillsAgent(
    skills=[
        ERC20Skill,
        SimpleWalletSkill,
        DexScreenerSkill,
    ],
    default_model=AnthropicModelType.claude_3_5_sonnet,
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
)


if __name__ == "__main__":
    asyncio.run(agent.run())
