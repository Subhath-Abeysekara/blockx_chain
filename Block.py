import hashlib

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.timestamp}{self.data}{self.previous_hash}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def __repr__(self):
        return f"Block(timestamp: {self.timestamp}, data: {self.data}, hash: {self.hash}, previous_hash: {self.previous_hash})"

