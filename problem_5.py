import hashlib
import time


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)

        hash_str = hash_str.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return 'Timestamp: {}\nData: {}\nSHA256 Hash: {}\nPrev Hash: {}\n'\
            .format(self.timestamp, self.data, self.hash, self.previous_hash)


class Blockchain:
    def __init__(self):
        self.tail = None

    def add_block(self, data):
        prev_hash = 0
        if self.tail:
            prev_hash = self.tail.hash
        new_block = Block(time.time(), data, prev_hash)
        new_block.prev = self.tail
        self.tail = new_block


blockchain = Blockchain()
blockchain.add_block('some data 0')
blockchain.add_block('some data 1')
blockchain.add_block('some data 2')
blockchain.add_block('some data 3')

print(blockchain.tail)
print(blockchain.tail.prev)
print(blockchain.tail.prev.prev)
print(blockchain.tail.prev.prev.prev)

blockchain_empty = Blockchain()
print(blockchain_empty.tail)  # None

blockchain_large = Blockchain()
for i in range(1000):
    blockchain_large.add_block('data' + str(i))
print(blockchain_large.tail)
print(blockchain_large.tail.prev)
print(blockchain_large.tail.prev.prev)
print(blockchain_large.tail.prev.prev.prev)
