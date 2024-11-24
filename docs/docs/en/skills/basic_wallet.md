The SimpleWalletSkill provides basic wallet functionality for managing private keys and addresses. It stores the private key in memory using context variables.

The wallet skill consists of the following tools:

- `create_wallet`: Creates a new private key wallet
- `set_private_key`: Sets an existing private key
- `get_private_key`: Retrieves the current private key
- `clear_private_key`: Clears the stored private key
- `get_address`: Gets the wallet address for the current private key

---

The `create_wallet` tool generates a new private key wallet and stores it in memory. It returns a message containing both the wallet address and private key.

---

The `set_private_key` tool allows you to import an existing private key. It takes one parameter:

- `private_key`: The private key string to import

The tool returns a success message when the key is set.

---

The `get_private_key` tool retrieves the currently stored private key. If no key is set, it returns "No private key set".

---

The `clear_private_key` tool removes the stored private key from memory. It returns a confirmation message when complete.

---

The `get_address` tool derives and returns the wallet address for the currently stored private key. If no key is set, it returns "No private key set".
