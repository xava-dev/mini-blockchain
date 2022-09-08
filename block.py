import datetime
from hashlib import sha256


class Block:
    # initializes block
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    # generates a unique hash from time, transactions, previous hash and nonce
    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) + \
            str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

    # prints out the contents of the block
    def print_contents(self):
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)
