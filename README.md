# Ethereum & MegaETH Learning Notes 🧠

Hi! 👋  
This repository is my personal collection of learning notes and small experiments as I explore the Ethereum ecosystem and the upcoming MegaETH network.

I'm not a developer, but I'm fascinated by how decentralized systems work — especially how scaling, block production, and validator economics are evolving.

---

## 📚 Topics I'm Learning
- How Ethereum transactions are broadcast and confirmed
- What MEV and sequencers are (and how MegaETH rotates them globally)
- Basics of gas fees, block times, and Layer 2 rollups
- The difference between full nodes, light clients, and sequencers

---

## ⚙️ Small Script Example

Below is a simple Python script that fetches the latest Ethereum block number from a public API.

```python
# scripts/get_latest_block.py
import requests

def get_latest_block():
    response = requests.get("https://rpc.ankr.com/eth")
    if response.status_code == 200:
        print("Ethereum RPC connected successfully!")
    else:
        print("Failed to connect to Ethereum RPC.")

if __name__ == "__main__":
    get_latest_block()
```

*(Note: This is a basic example to test RPC connectivity — not an on-chain transaction.)*

---

## 🌐 Why MegaETH Interests Me
MegaETH is pioneering a near-instant EVM with global sequencer rotation and proximity markets.
That means:
- Block production rotates geographically (Tokyo → Amsterdam → Virginia → LA)
- It optimizes latency for where economic activity happens
- Market makers can colocate near sequencers to reduce delay

I’m following MegaETH’s architecture closely because it’s one of the first systems to combine real-time block production with a community auction model.

---

## 🧾 References
- [Ethereum.org](https://ethereum.org)
- [MegaETH Whitepaper](https://docs.megaeth.io)
- [Understanding Sequencer Rotation](https://megaeth.io/blog)

---

## 💬 Contact
If you’re also exploring MegaETH or Ethereum scaling, feel free to open an issue or discussion!
