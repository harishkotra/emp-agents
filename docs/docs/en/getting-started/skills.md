Skills are a collection of tools that an agent can use to interact with the world.  They are defined by a class that implements the `SkillSet` class.


you can define a skill as a class with multiple functions, each should be a staticmethod and should be decorated with one of three decorators:

- `@onchain_action` for functions that interact with a blockchain, such as sending transactions
- `@tool_method` for functions that are not mutative, but are not related to modifying onchain state
- `@view_action` for functions that are read-only and do not affect external state

---

For example, a skill that enables an agent to perform addition and subtraction could be defined as follows:

```python
from typing import Annotated
from typing_extensions import Doc

from emp_agents.models.protocol import SkillSet, view_action


class MathSkill(SkillSet):
    """A skill for performing basic math operations"""

    @view_action
    @staticmethod
    async def add(
        a: Annotated[int, Doc("The first number to add")],
        b: Annotated[int, Doc("The second number to add")],
    ) -> int:
        """Add two integers"""
        return a + b

    @view_action
    @staticmethod
    async def subtract(
        a: Annotated[int, Doc("The first number to subtract")],
        b: Annotated[int, Doc("The second number to subtract")],
    ) -> int:
        """Subtract two integers"""
        return a - b
```

This can then be utilized by an agent by providing it to the agent's `skills` parameter.

```python
from emp_agents import AgentBase

agent = AgentBase(
    prompt="You are a helpful assistant that can perform basic math operations",
    skills=[
        MathSkill,
    ],
)
```
