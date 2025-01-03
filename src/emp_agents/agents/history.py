from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

from emp_agents.models import Message


class AbstractConversationProvider(ABC):
    @abstractmethod
    def set_history(self, messages: list[Message]) -> None:
        pass

    @abstractmethod
    def add_message(self, message: Message) -> None:
        pass

    @abstractmethod
    def add_messages(self, messages: list[Message]) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def get_history(self) -> list[Message]:
        pass


class ConversationProvider(AbstractConversationProvider, BaseModel):
    history: list[Message] = Field(default_factory=list)

    def set_history(self, messages: list[Message]) -> None:
        self.reset()
        self.add_messages(messages)

    def add_message(self, message: Message) -> None:
        self.history.append(message)

    def add_messages(self, messages: list[Message]) -> None:
        self.history.extend(messages)

    def reset(self) -> None:
        self.history.clear()

    def get_history(self) -> list[Message]:
        return self.history.copy()
