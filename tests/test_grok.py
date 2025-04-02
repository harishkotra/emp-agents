import json
from datetime import datetime
from unittest.mock import AsyncMock, patch

import pytest

from emp_agents.agents import AgentBase
from emp_agents.models import GenericTool, Property, Request, UserMessage
from emp_agents.providers import GrokModelType, GrokProvider


class AgentForTesting(AgentBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


@pytest.mark.asyncio
async def test_grok_provider():
    agent = AgentForTesting(
        provider=GrokProvider(
            api_key="test_api_key",
            default_model=GrokModelType.grok_1_5,
        ),
    )
    assert agent.provider.default_model == GrokModelType.grok_1_5
    assert agent.provider.api_key == "test_api_key"


@pytest.mark.asyncio
@patch("httpx.AsyncClient.post")
async def test_grok_completion(mock_post):
    response_data = {
        "id": "test-id",
        "object": "chat.completion",
        "created": int(datetime.now().timestamp()),
        "model": "grok-1.5",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "This is a test response from Grok",
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 10,
            "total_tokens": 20,
        },
    }

    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.json = AsyncMock(return_value=response_data)
    mock_post.return_value = mock_response

    provider = GrokProvider(api_key="test_api_key")
    request = Request(
        model=GrokModelType.grok_1_5,
        messages=[UserMessage(content="Hello, Grok!")],
    )
    response = await provider.completion(request)

    assert response.text == "This is a test response from Grok"
    assert response.model == "grok-1.5"
    assert len(response.choices) == 1
    assert response.choices[0].message.content == "This is a test response from Grok"

    mock_post.assert_called_once()

    call_args = mock_post.call_args
    assert call_args is not None
    assert call_args[0][0] == "https://api.grok.x/v1/chat/completions"

    assert "json" in call_args[1]
    request_body = call_args[1]["json"]
    assert request_body["model"] == "grok-1.5"
    assert len(request_body["messages"]) == 1
    assert request_body["messages"][0]["role"] == "user"
    assert request_body["messages"][0]["content"] == "Hello, Grok!"


@pytest.mark.asyncio
@patch("httpx.AsyncClient.post")
async def test_grok_with_tools(mock_post):
    response_data = {
        "id": "test-id",
        "object": "chat.completion",
        "created": int(datetime.now().timestamp()),
        "model": "grok-1.5",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "I would check the weather for you, but I'm just a test.",
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": 15,
            "completion_tokens": 12,
            "total_tokens": 27,
        },
    }

    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.json = AsyncMock(return_value=response_data)
    mock_post.return_value = mock_response

    weather_tool = GenericTool(
        name="get_weather",
        description="Get the current weather in a location",
        parameters={
            "location": Property(
                type="string",
                description="The city and state, e.g. San Francisco, CA",
            ),
            "unit": Property(
                type="string",
                description="The unit of temperature, either 'celsius' or 'fahrenheit'",
                enum=["celsius", "fahrenheit"],
            ),
        },
        required=["location"],
        func=lambda **kwargs: None,  # Dummy function for testing
    )
    provider = GrokProvider(api_key="test_api_key")
    request = Request(
        model=GrokModelType.grok_1_5,
        messages=[UserMessage(content="What's the weather in San Francisco?")],
        tools=[weather_tool],
        tool_choice="auto",
    )

    await provider.completion(request)

    mock_post.assert_called_once()
    call_args = mock_post.call_args
    request_body = call_args[1]["json"]
    assert "tools" in request_body
    assert len(request_body["tools"]) == 1
    assert request_body["tools"][0]["function"]["name"] == "get_weather"
    assert request_body["tool_choice"] == "auto"
