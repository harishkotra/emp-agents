from emp_agents.agents.planner import Planner
from emp_agents.providers import OpenAIModelType, OpenAIProvider

agent = Planner(
    provider=OpenAIProvider(),
    default_model=OpenAIModelType.gpt4o_mini,
)


async def main():
    subject = "find good investing opportunities"
    task_list = await agent.generate(subject)
    print(task_list)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
