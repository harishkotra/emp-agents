from typing import Optional

from pydantic import Field

from emp_agents.models.shared.tools import GenericTool
from emp_agents.providers.standard_request import StandardRequest

from .types import GaiaModelType


class Request(StandardRequest[GaiaModelType]):
    """
    Request model for Gaia API.
    """

    tools: Optional[list[GenericTool]] = Field(default=None)
