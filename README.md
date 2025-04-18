# Simple Python Blockchain

This is a simple Python implementation of a blockchain, where each block contains the following properties:
- **Index**: The position of the block in the blockchain.
- **Timestamp**: The time when the block was created.
- **Previous Hash**: The hash of the previous block in the chain.
- **Data**: The data contained in the block.
- **Hash**: The unique hash of the block generated using SHA-256.

The goal of this project is to demonstrate how a basic blockchain works and how blocks are connected in a chain.

## Features

- **Block Class**: Contains the properties of a block such as index, timestamp, previous hash, data, and hash.
- **Blockchain Class**: Manages the chain of blocks and allows adding new blocks.
- **Hash Calculation**: SHA-256 is used to generate the unique hash for each block.
- **Genesis Block**: The first block in the chain, created without a previous block.
- **Chain Display**: Iterates through each block to display its details (index, timestamp, previous hash, data, and hash).

## Prerequisites

- Python 3.x
- Basic understanding of Blockchain technology

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/apurwaanandd/simple-python-blockchain.git
