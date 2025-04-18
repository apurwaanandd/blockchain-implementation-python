import hashlib
import time

# Block class to represent each block in the blockchain
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

# Function to calculate the hash of a block
def calculate_hash(block):
    block_string = str(block.index) + str(block.timestamp) + str(block.previous_hash) + str(block.data)
    return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

# Function to create the genesis block (first block in the blockchain)
def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(Block(0, "0", time.time(), "Genesis Block", "")))

# Blockchain class to represent the blockchain
class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]  # Start with the genesis block

    # Method to add a new block to the blockchain
    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = self.create_new_block(last_block, data)
        self.chain.append(new_block)

    # Method to create a new block
    def create_new_block(self, last_block, data):
        index = last_block.index + 1
        timestamp = time.time()
        previous_hash = last_block.hash
        hash = calculate_hash(Block(index, previous_hash, timestamp, data, ""))
        return Block(index, previous_hash, timestamp, data, hash)

    # Method to display the blockchain
    def display_chain(self):
        for block in self.chain:
            print(f"Block #{block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}\n")

# Testing the Blockchain
my_blockchain = Blockchain()

# Add some blocks to the blockchain
my_blockchain.add_block("Block 1 Data")
my_blockchain.add_block("Block 2 Data")
my_blockchain.add_block("Block 3 Data")

# Display the entire blockchain
my_blockchain.display_chain()
