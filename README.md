# 🛠️ Simple Python Blockchain 🧑‍💻

A simple Python-based blockchain implementation where each block contains the **index**, **timestamp**, **previous hash**, **data**, and **unique hash**. This project is designed to demonstrate how blockchain works, and how blocks are securely connected to form an immutable chain.

---

## 🚀 Features

- **Block Class**: Each block in the chain contains essential properties like **index**, **timestamp**, **previous hash**, **data**, and **hash**.
- **Blockchain Class**: Manages the blockchain, adds new blocks, and displays the entire chain.
- **SHA-256 Hashing**: Each block's hash is calculated using the **SHA-256** algorithm.
- **Genesis Block**: The first block of the blockchain, created with no previous block.
- **Immutable Chain**: Once added, blocks cannot be modified, ensuring data integrity.

---

## 📜 How It Works

- The blockchain starts with a **Genesis Block** (the first block) which does not have a previous block. Each subsequent block in the chain references the **previous hash** of the last block, making it tamper-resistant.
- **Blocks** are created with specific data and the hash of the previous block, which ensures the integrity of the blockchain.
  
---

## 🔧 Installation & Setup

1. **Clone the repository to your local machine**:

   ```bash
   git clone https://github.com/apurwaanandd/blockchain-implementation-python.git
