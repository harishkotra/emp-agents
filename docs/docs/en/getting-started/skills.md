Skills are a collection of tools that an agent can use to interact with the world.  They are defined by a class that implements the `SkillSet` class.


you can define a skill as a class with multiple functions, each should be a staticmethod and should be decorated with `@view_action` or `@onchain_action` depending on whether it is a view or a function that interacts with a blockchain.


```python
class MathSkill(SkillSet):
    """A skill for performing basic math operations"""

    @view_action
    @staticmethod
    async def add(a: int, b: int) -> int:
        """Add two integers"""
        return a + b

    @view_action
    @staticmethod
    async def subtract(a: int, b: int) -> int:
        """Subtract two integers"""
        return a - b
```


This can then be utilized by an agent by providing it to the agent's `skills` parameter.


```python
from emp_agents import AgentBase

agent = AgentBase(
    prompt="You are a helpful assistant that can perform basic math operations",
    skills=[MathSkill],
)
```
