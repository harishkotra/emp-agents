import os

from emp_agents.agents.planner import Planner
from emp_agents.types import OpenAIModelType

agent = Planner(
    default_model=OpenAIModelType.gpt4o_mini,
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
)


async def main():
    subject = "find good investing opportunities"
    task_list = await agent.generate(subject)
    print(task_list)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
