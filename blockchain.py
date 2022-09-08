# imports the Block class from block.py
from block import Block


class Blockchain:
    # initializing a blockchain with only the genesis block
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    # the first block in the blockchain
    def genesis_block(self):
        transactions = {}
        genesis_block = Block(transactions, "0")
        self.chain.append(genesis_block)
        return self.chain

    # prints contents of each block in the blockchain
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()

    # adds block to the blockchain
    def add_block(self, transactions):
        previous_hash = (self.chain[len(self.chain)-1]).hash
        new_block = Block(transactions, previous_hash)
        new_block.generate_hash()
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return proof, new_block

    # checks every block to validate that the previous hash value of current block
    # matches with the hash value inside of the previous block
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if (current.hash != current.generate_hash()):
                print(
                    "The current hash of the block does not equal the generated hash of the block. The blockchain is invalid.")
                return False
            if (current.previous_hash != previous.generate_hash()):
                print(
                    "The previous block's hash does not equal the previous hash value stored in the current block. The blockchain is invalid.")
                return False
        print(
            "The blockchain is valid.")
        return True

    # math problem with a certain difficulty to find the generated hash
    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:difficulty] != '0'*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
