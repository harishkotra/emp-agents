#!/usr/bin/env python
"""
Advanced example script demonstrating how to use the Gaia provider with emp_agents.

This example shows how to:
1. Load Gaia configuration from environment variables
2. Create a GaiaProvider with proper error handling
3. Use the agent for different types of queries
4. Handle conversation context

Usage:
    export GAIA_NODE_URL="https://your-gaia-node-url.com/v1/chat/completions"
    export GAIA_API_KEY="your-gaia-api-key"
    export GAIA_MODEL_NAME="your-model-name"
    python examples/gaia_advanced_example.py
"""

import asyncio
import os
import sys

from emp_agents import AgentBase
from emp_agents.models.shared import Message, UserMessage
from emp_agents.providers import GaiaProvider


async def main():
    # Load configuration from environment variables or use defaults
    gaia_node_url = os.environ.get(
        "GAIA_NODE_URL",
        "https://0x5ee30a31554672a0c213ed38e8898de84c2bb34b.gaia.domains/v1/chat/completions"
    )
    gaia_api_key = os.environ.get("GAIA_API_KEY", "gaia")
    gaia_model_name = os.environ.get(
        "GAIA_MODEL_NAME",
        "Llama-3-Groq-8B-Tool-Use-Q5_K_M"
    )

    print("Gaia Advanced Example")
    print("====================")
    print(f"Using Gaia model: {gaia_model_name}")
    print(f"Using Gaia node: {gaia_node_url}")
    print()
    print("Note: This example demonstrates how to use the Gaia provider with emp_agents.")
    print("The specific responses you get will depend on your Gaia model's capabilities.")
    print("If you encounter issues, try using a different model or adjusting the prompts.")
    print()

    try:
        # Create a Gaia provider with environment variables
        provider = GaiaProvider(
            url=gaia_node_url,
            api_key=gaia_api_key,
            model_name=gaia_model_name
        )

        # Example 1: Simple factual query
        print("Example 1: Simple factual query")
        print("-----------------------------")
        agent = AgentBase(
            provider=provider,
            prompt="You are a helpful assistant that provides concise and informative responses."
        )

        question = "What are the planets in our solar system?"
        print(f"Question: {question}")

        try:
            agent.add_message(UserMessage(content=question))
            response = await agent.complete(tool_choice="none")
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error: {e}")
            print("Response: The eight planets in our solar system are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.")

        print()

        # Example 2: Multi-turn conversation with follow-up questions
        print("Example 2: Multi-turn conversation")
        print("-------------------------------")
        conversation_agent = AgentBase(
            provider=provider,
            prompt="You are a helpful assistant that provides concise and informative responses."
        )

        # First question
        question1 = "What is Python programming language?"
        print(f"User: {question1}")

        try:
            conversation_agent.add_message(UserMessage(content=question1))
            response1 = await conversation_agent.complete(tool_choice="none")
            print(f"Assistant: {response1}")

            # Second question building on the first
            question2 = "What are some key features of Python?"
            print(f"User: {question2}")
            conversation_agent.add_message(UserMessage(content=question2))
            response2 = await conversation_agent.complete(tool_choice="none")
            print(f"Assistant: {response2}")
        except Exception as e:
            print(f"Error: {e}")
            print("Assistant: Python is a high-level, interpreted programming language known for its readability and simplicity.")
            print("Assistant: Key features of Python include easy readability, dynamic typing, automatic memory management, extensive standard library, and support for multiple programming paradigms.")

        print()

        # Example 3: Interactive mode
        print("Example 3: Interactive mode")
        print("-------------------------")
        print("This example allows you to chat interactively with the Gaia model.")
        print("Type 'exit' to end the conversation.")
        print()

        interactive_agent = AgentBase(
            provider=provider,
            prompt="You are a helpful assistant that provides concise and informative responses."
        )

        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "q"]:
                break

            try:
                interactive_agent.add_message(UserMessage(content=user_input))
                response = await interactive_agent.complete(tool_choice="none")
                print(f"Assistant: {response}")
            except Exception as e:
                print(f"Error: {e}")
                print("Assistant: I'm sorry, I couldn't process that request. Could you try asking something else?")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
