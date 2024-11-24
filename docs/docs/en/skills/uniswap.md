An example skill is the UniswapSkill, which allows for interacting with the Uniswap protocol.

The Uniswap skill currently consists of two tools:

- `get_price`: Get the price of a token in USD
- `swap`: Swap an exact amount of ETH for tokens

---

The `get_price` tool can be used to get the price of a token in terms of another token on Uniswap V2. It takes the following parameters:

- `network`: The network to query the price on. Can be one of: "ethereum", "arbitrum", or "base"
- `token_in`: The address of the token you want to swap from
- `token_out`: The address of the token you want to swap to

The tool returns the price as a JSON string containing a "price" field with the numeric price value.

---
The `swap` tool can be used to swap tokens on Uniswap V2. It supports three types of swaps:

- ETH to tokens
- Tokens to ETH
- Tokens to tokens

The tool takes the following parameters:

- `network`: The network to execute the swap on ("ethereum", "arbitrum", or "base")
- `input_token`: The address of the token to swap from. Use `None` if swapping from ETH
- `output_token`: The address of the token to swap to. Use `None` if swapping to ETH
- `amount_in`: The amount of input tokens to swap
- `recipient`: The address that will receive the output tokens
- `slippage`: The maximum acceptable slippage percentage (e.g. 0.05 for 5%)
- `deadline`: Optional Unix timestamp deadline for the swap. If not provided, defaults to 1 minute from now

The tool returns the transaction hash of the executed swap.

---
