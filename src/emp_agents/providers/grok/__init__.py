import os
from typing import ClassVar

import httpx
from pydantic import Field

from emp_agents.exceptions import InvalidModelException
from emp_agents.models import GenericTool, Provider, SystemMessage
from emp_agents.models.shared.request import Request as BaseRequest

from .request import Request
from .response import Response
from .tool import Function, Parameters, Property, Tool
from .types import GrokModelType


class GrokProvider(Provider[Response]):
    URL: ClassVar[str] = "https://api.grok.x/v1/chat/completions"

    api_key: str = Field(default_factory=lambda: os.environ["GROK_API_KEY"])
    default_model: GrokModelType = Field(default=GrokModelType.grok_1_5)

    @property
    def headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

    def _from_request(self, request: BaseRequest):
        exclude = ["system"]
        result = request.model_dump(exclude_none=True)
        if request.system:
            messages = [SystemMessage(content=request.system)] + request.messages
        else:
            messages = request.messages

        def set_additional_properties_false(schema):
            if isinstance(schema, dict):
                if schema.get("type") == "object":
                    schema["additionalProperties"] = False
                for key, value in schema.items():
                    set_additional_properties_false(value)
            elif isinstance(schema, list):
                for item in schema:
                    set_additional_properties_false(item)

        if "response_format" in result:
            assert request.response_format is not None

            model_schema = request.response_format.model_json_schema()
            set_additional_properties_false(model_schema)
            del result["response_format"]
            result["response_format"] = {
                "type": "json_schema",
                "json_schema": {
                    "name": request.response_format.__name__,
                    "description": "response format",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "additionalProperties": False,
                        **model_schema,
                    },
                },
            }
        result["messages"] = [m.model_dump() for m in messages]
        result["tools"] = (
            [self.to_tool_call(t).model_dump(exclude_none=True) for t in request.tools]
            if request.tools
            else None
        )

        for field in exclude:
            if field in result:
                del result[field]

        return result

    async def completion(self, request: BaseRequest) -> Response:
        grok_request = self._from_request(request)
        async with httpx.AsyncClient(headers=self.headers) as client:
            response = await client.post(self.URL, json=grok_request, timeout=None)
        if response.status_code >= 400:
            error_data = await response.json()
            if response.status_code == 404:
                raise InvalidModelException(error_data)
            raise ValueError(error_data)
        return Response(**(await response.json()))

    def to_tool_call(self, tool: GenericTool):
        return Tool(
            type="function",
            function=Function(
                description=tool.description,
                name=tool.name,
                parameters=Parameters(
                    properties={
                        key: Property(**param.model_dump(exclude_none=True))
                        for key, param in tool.parameters.items()
                    },
                    required=tool.required,
                ),
            ),
            strict=True,
        )


__all__ = [
    "GrokModelType",
    "Request",
    "Response",
    "Tool",
    "Function",
    "Property",
    "Parameters",
]
