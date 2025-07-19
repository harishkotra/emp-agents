#!/usr/bin/env python
"""
Simple example script demonstrating how to use the Gaia provider with emp_agents.

This example shows how to:
1. Create a GaiaProvider with your own Gaia Node URL, API Key, and Model Name
2. Create an Agent using this provider
3. Send simple queries to the agent

Usage:
    # Set your Gaia credentials (optional, defaults are provided for testing)
    export GAIA_NODE_URL="your-gaia-node-url"
    export GAIA_API_KEY="your-gaia-api-key"
    export GAIA_MODEL_NAME="your-model-name"

    # Run the example
    python examples/gaia_example.py
"""

import asyncio
import os

from emp_agents import AgentBase
from emp_agents.providers import GaiaProvider


async def main():
    # Get Gaia credentials from environment variables or use defaults for testing
    gaia_node_url = os.environ.get(
        "GAIA_NODE_URL",
        "https://0x5ee30a31554672a0c213ed38e8898de84c2bb34b.gaia.domains/v1/chat/completions"
    )
    gaia_api_key = os.environ.get("GAIA_API_KEY", "gaia")
    gaia_model_name = os.environ.get(
        "GAIA_MODEL_NAME",
        "Llama-3-Groq-8B-Tool-Use-Q5_K_M"
    )

    print("Gaia Provider Example")
    print("====================")
    print(f"Using Gaia model: {gaia_model_name}")
    print(f"Using Gaia node: {gaia_node_url}")
    print()

    # Create a Gaia provider with your custom settings
    provider = GaiaProvider(
        url=gaia_node_url,
        api_key=gaia_api_key,
        model_name=gaia_model_name
    )

    # Create an agent using the Gaia provider
    agent = AgentBase(
        provider=provider,
        prompt="You are a helpful assistant that provides concise and informative responses."
    )

    # Example 1: Simple question
    print("Example 1: Simple question")
    print("-------------------------")
    question = "What are the benefits of using LLMs for code generation?"
    print(f"Question: {question}")
    response = await agent.answer(question)
    print(f"Response: {response}")
    print()

    # Example 2: Technical explanation
    print("Example 2: Technical explanation")
    print("------------------------------")
    question = "Explain how WebAssembly works in simple terms."
    print(f"Question: {question}")

    # Use the complete method with tool_choice="none" to disable tool calls
    agent.add_message(agent._make_message(question))
    response = await agent.complete(tool_choice="none")
    print(f"Response: {response}")
    print()

    # Example 3: Creative content
    print("Example 3: Creative content")
    print("-------------------------")
    question = "Write a short poem about programming."
    print(f"Question: {question}")

    # Use the complete method with tool_choice="none" to disable tool calls
    agent.add_message(agent._make_message(question))
    response = await agent.complete(tool_choice="none")
    print(f"Response: {response}")

    print("\nThis example demonstrates how to use the Gaia provider with emp_agents.")
    print("You can connect to your own Gaia Node by setting the environment variables:")
    print("  GAIA_NODE_URL, GAIA_API_KEY, and GAIA_MODEL_NAME")


if __name__ == "__main__":
    asyncio.run(main())
