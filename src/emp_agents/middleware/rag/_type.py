from abc import abstractmethod

from emp_agents.agents.base import Message

from .. import Middleware


class Rag(Middleware):
    @abstractmethod
    async def get_context(self, query: str) -> str: ...

    async def process(self, messages: list[Message]) -> list[Message]:
        if len(messages) == 0:
            return messages

        message = messages[-1]
        if message.content is None:
            return messages

        context = await self.get_context(message.content)
        message.content += f"\n\nThe Following Context is retrieved from relevant datasources:\n\n{context}"
        return messages
