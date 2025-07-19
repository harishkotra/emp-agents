from typing import Optional

from pydantic import Field

from emp_agents.providers.openai import OpenAIProviderBase
from emp_agents.providers.openai.response import Response


class GaiaProvider(OpenAIProviderBase[str]):
    """
    Provider for Gaia API.

    This provider allows users to connect to their own Gaia Node by specifying:
    - url: The URL of the Gaia Node
    - api_key: The API key for the Gaia Node
    - model_name: The name of the model to use
    """

    url: str = Field(description="URL of the Gaia Node")
    api_key: str = Field(description="API key for the Gaia Node")
    default_model: str = Field(default="default")

    def __init__(
        self,
        url: str,
        api_key: str,
        model_name: str,
        **kwargs
    ):
        """
        Initialize the Gaia provider with the specified URL, API key, and model name.

        Args:
            url: The URL of the Gaia Node
            api_key: The API key for the Gaia Node
            model_name: The name of the model to use
        """
        # Set default_model to the model_name
        kwargs["default_model"] = model_name
        super().__init__(url=url, api_key=api_key, **kwargs)


__all__ = [
    "GaiaProvider",
    "Response",
]
