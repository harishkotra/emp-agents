from typing import Annotated, Optional

from pydantic import Field, PlainSerializer

from emp_agents.models.shared.tools import GenericTool
from emp_agents.providers.openai.tool import Tool
from emp_agents.providers.standard_request import StandardRequest

from .types import GrokModelType


class Request(StandardRequest[GrokModelType]):
    """
    Request model for Grok API, which follows the OpenAI API format.
    """

    tools: Annotated[
        Optional[list[GenericTool]],
        PlainSerializer(
            lambda tools_list: (
                [tool.to_grok() for tool in tools_list]
                if tools_list is not None
                else None
            ),
            return_type=Optional[list[Tool]],
        ),
    ] = Field(default=None)
