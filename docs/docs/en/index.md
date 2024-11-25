---
hide:
  - navigation
search:
  exclude: true
---

# emp-agents

<b>Integrating AI Agents with Blockchain</b>

---

# Features

emp-agents is a set of tools for integrating AI agents with blockchain interactions. It provides a simple interface for AI agents to:

- Execute onchain actions through smart contract calls
- Fetch and analyze blockchain data to inform decision making
- Monitor real-time blockchain activity and market conditions
- Interact with popular AI models like OpenAI and Anthropic
- Create autonomous agents that combine data analysis with onchain execution

All tooling in emp-agents is used daily by the Empyreal development team, and we hope that sharing this tooling with you will facilitate your development. Particular attention has been paid to creating standardized interfaces for AI model interactions, especially in the pursuit of simplified integration with blockchain systems.

By creating consistent abstractions across different AI providers like OpenAI and Anthropic, we have made a unified async library for building AI agents that can interact with blockchain data and execute onchain actions. This means users can have greater flexibility in choosing AI models while maintaining a consistent development experience. Without these abstractions, it would be very difficult to build reliable AI agents that can safely interact with blockchain systems.

---

# Install

All the libraries in emp-agents works on Linux, macOS, Windows and most Unix-style operating systems. You can install it with pip as usual:

```sh
pip install emp-agents
```

!!! tip
    eth-packages are libraries for RPC/Onchain interactions. They facilitate execution of onchain actions by providing typed interfaces, RPC connections, and contract abstractions that agents can use to interact with various blockchain networks.
