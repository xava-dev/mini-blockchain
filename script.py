from blockchain import Blockchain


# The blockchain I have built only exists on a local machine

# It is important to know that actual blockchain applications
# operate on multiple computers in a decentralized manner

block_one_transactions = {
    "sender": "Xava",
    "receiver": "Neill",
    "amount": "100"
}
block_two_transactions = {
    "sender": "Neill",
    "receiver": "Michael",
    "amount": "20"
}
block_three_transactions = {
    "sender": "Neill",
    "receiver": "Jason",
    "amount": "50"
}
fake_transactions = {
    "sender": "Neill",
    "receiver": "Michael",
    "amount": "0"
}

# create a local blockchain instance from Blockchain class
local_blockchain = Blockchain()

# adds three blocks with transactions
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)

# prints all blocks
local_blockchain.print_blocks()
# checks that blockchain is valid - returns valid
local_blockchain.validate_chain()

# changes a block
local_blockchain.chain[2].transactions = fake_transactions
# prints all blocks
local_blockchain.print_blocks()
# checks that blockchain is valid - returns invalid
local_blockchain.validate_chain()
