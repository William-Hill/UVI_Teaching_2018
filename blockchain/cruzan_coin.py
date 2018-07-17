'''A simple blockchain implementation.
Inspired by https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b'''

from __future__ import print_function
import hashlib
import datetime

class Block:
    '''Blocks of data that will create the Blockchain'''
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        '''returns a sha256 hash of the Block's index, timestamp, data,
        and previous block's hash'''

        sha_hash = hashlib.sha256()
        sha_hash.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha_hash.hexdigest()


def create_genesis_block():
    '''Create the first block in the chain'''
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")

def next_block(previous_block):
    '''Create the next block in the chain'''
    index = previous_block.index + 1
    timestamp = datetime.datetime.now()
    data = "I'm block {}".format(index)
    return Block(index, timestamp, data, previous_block.hash)


def create_block_chain(num_of_blocks):
    block_chain = [create_genesis_block()]
    previous_block = block_chain[0]

    for _ in range(0, num_of_blocks):
        new_block = next_block(previous_block)
        block_chain.append(new_block)
        previous_block = new_block

        print("Block #{} was added to the blockchain".format(new_block.index))
        print("Hash: {}\n".format(new_block.hash))


create_block_chain(10)
