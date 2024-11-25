# Tools

Tools allow Large Language Models (LLMs) to interact with external systems and perform actions in the real world. While LLMs are powerful at understanding and generating text, they are limited to working with information provided in their training data and context window. Tools extend their capabilities by enabling them to:

- Access real-time information (e.g., current weather, stock prices, web searches)
- Perform calculations and data analysis
- Interact with APIs and external services
- Execute code and system commands
- Read and write files
- And much more

---

## How Tools Work

When using tools with an LLM:

1. The tools are registered with the agent/model as available functions it can call
2. The LLM analyzes the user's request and determines if it needs to use any tools
3. If needed, the LLM generates a structured call to the appropriate tool with parameters
4. The tool executes and returns results back to the LLM
5. The LLM incorporates the tool's output into its response


!!! tip "Tool Communication Format"
    Different models have different communication formats for tools calls, which we have standardized and abstracted to simplify using different models.
