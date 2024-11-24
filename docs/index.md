---
hide:
  - navigation
search:
  exclude: true
---

# emp-agents

A library for building low-code, capable and extensible autonomous agent systems

<b>Integrating AI Agents with Blockchain</b>

---

# Features

The **emp-agents** SDK is a set of tooling for integrating AI agents with various external systems and enables blockchain interactions. It provides a simple interface for AI agents to:

- Execute onchain actions through smart contract calls
- Fetch and analyze blockchain data to inform decision making
- Monitor real-time blockchain activity and market conditions
- Interact with popular AI models like OpenAI and Anthropic
- Create autonomous agents that combine data analysis with onchain execution

All tooling in emp-agents is used daily by the Empyreal development team, and we hope that sharing this tooling with you will facilitate your development. Particular attention has been paid to creating standardized interfaces for AI model interactions, especially in the pursuit of simplified integration with blockchain systems.

By creating consistent abstractions across different AI providers like OpenAI and Anthropic, we have made a unified async library for building AI agents that can interact with blockchain data and execute onchain actions. This means users can have greater flexibility in choosing AI models while maintaining a consistent development experience. Without these abstractions, it would be very difficult to build reliable AI agents that can safely interact with blockchain systems.

---

# Install

All the libraries in eth-packages works on Linux, macOS, Windows and most Unix-style operating systems. You can install it with pip as usual:

```sh
pip install emp-agents
```

!!! tip
    eth-packages are libraries for RPC/Onchain interactions. They facilitate execution of onchain actions by providing typed interfaces, RPC connections, and contract abstractions that agents can use to interact with various blockchain networks.
---

# eth-packages Quickstart

The library is designed to abstract significant aspects of the contract ABIs into typed python, making your static analsysi more effective.  This is also valuable as it enables LLMs to generate code in a much less verbose way, leaning into their strengths of structured abstraction without forcing them to impart as much domain knowledge.

In this example, we show a variety of language features.  We are able to access data from multiple blockchains, getting information about Blocks, calling smart contracts directly to access onchain data, and subscribing to log data to see historical events.

Additionally, we have integrated with Alchemy and Infura (Coming Soon!) for simple RPC access.  This makes it easy to utilize your credentials to easily access a variety of chains without having to populate the RPCs manually.

You'll also notice the `<Type>[Network]` syntax, which allows to easily specify the network for the request.

```python
from eth_rpc import *
from eth_rpc.utils import to_checksum
from eth_rpc.ens import lookup_addr
from eth_rpc.networks import Arbitrum, Base, Ethereum
from eth_typeshed import *
from eth_typeshed.erc20 import *

# set your alchemy key globaly to configure it for all networks
set_alchemy_key("<ALCHEMY_KEY>")

# or set the RPC url for a network directly
set_rpc_url(Ethereum, "<MY PRIVATE RPC URL>")

# get the latest block on ethereum
block: Block[Ethereum] = await Block[Ethereum].latest(with_tx_data=True)

# calculate the total value of all transactions in a block
total_value = 0
for tx in block.transactions:
    total_value += tx.value

# get the latest block on arbitrum
block2: Block[Arbitrum] = await Block[Arbitrum].latest()

# create an ERC20 contract object on Arbitrum and access its name, symbol and decimals
usdt = ERC20[Arbitrum](address=to_checksum('0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9'))
name = await usdt.name().get()
symbol = await usdt.symbol().get()
decimals = await usdt.decimals().get()

# or do it as a multicall (defaults to the standard multicall contract)
(name, symbol, decimals) = await multicall[Arbitrum].execute(
    usdt.name(),
    usdt.symbol(),
    usdt.decimals(),
)

# get vitalik's usdt balance at a specific block
vitalik_addr = await lookup_addr('vitalik.eth')
balance = await usdt.balance_of(vitalik_addr).get(
    block_number=246_802_382,
)

# subscribe to transfer events on Arbitrum for USDT
async for event in TransferEvent[Base].set_filter(
    addresses=[usdt.address]
).subscribe():
    data = event.event
    print(f'{data.sender} sent {data.recipient} {data.amount / 10 ** decimals} {name}')
```
