from abc import ABC, abstractmethod
from typing import Awaitable

from pydantic import BaseModel

from emp_agents.models import Message


class Middleware(BaseModel, ABC):
    name: str
    description: str

    @abstractmethod
    async def process(
        self, messages: list[Message]
    ) -> Awaitable[list[Message]] | list[Message]: ...
