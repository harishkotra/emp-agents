The DexScreenerSkill provides functionality for interacting with the DexScreener API to get information about trading pairs and tokens across different chains.

The skill consists of the following tools:

- `search_pairs`: Search for trading pairs matching a query
- `get_pair_by_chain`: Get pair info for a specific chain and pair address
- `find_pairs_by_tokens`: Find trading pairs by token addresses
- `get_token_profiles`: Get latest token profiles
- `get_latest_boosted_tokens`: Get recently boosted tokens
- `get_top_boosted_tokens`: Get tokens with most active boosts

---

The `search_pairs` tool searches for trading pairs matching a query string. It takes one parameter:

- `query`: The search query to find trading pairs

The tool is rate-limited to 300 requests per minute.

---

The `get_pair_by_chain` tool retrieves pair information for a specific chain and pair address. It takes two parameters:

- `chain_id`: The chain to search on (ethereum, solana, arbitrum, base, or bsc)
- `pair_id`: The pair contract address

The tool is rate-limited to 300 requests per minute.

---

The `find_pairs_by_tokens` tool finds trading pairs by token addresses. It takes one parameter:

- `token_addresses`: List of token addresses (maximum 30)

The tool is rate-limited to 300 requests per minute.

---

The `get_token_profiles` tool retrieves the latest token profiles.

The tool is rate-limited to 60 requests per minute.

---

The `get_latest_boosted_tokens` tool gets information about recently boosted tokens.

The tool is rate-limited to 60 requests per minute.

---

The `get_top_boosted_tokens` tool retrieves tokens with the most active boosts.

The tool is rate-limited to 60 requests per minute.
