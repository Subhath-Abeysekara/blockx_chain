import ast
import json
import os
import time
from Block import Block
from create_json import save_json, count_files_in_directory
from schemas.data_schema import Transaction_Data
from validate_data.validate_data import validate_inputs


def get_latest():
    dir_list = os.listdir("nodes")
    print(dir_list)
    for dir in dir_list:
        directory_path = f"nodes/{dir}"
        num_files = count_files_in_directory(directory_path=directory_path)
        block_name = f'Block{num_files}.json' if num_files > 1 else 'GenesisBlock.json'
        file_path = os.path.join(directory_path, block_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(type(data))
            data = ast.literal_eval(data)
            return Block(
                    timestamp=data['timestamp'],
                    data=data['data'],
                    previous_hash=data['previous_hash']
                )

class Blockchain:
    def __init__(self):
        save_json(self.create_genesis_block())

    def create_genesis_block(self):
        genesis_block = Block(time.time(), "Genesis Block", "0")
        new_block_json = json.dumps(genesis_block.__dict__)
        return new_block_json

    def get_latest_block(self):
        return get_latest()

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        new_block_json = json.dumps(new_block.__dict__)
        print(new_block_json)
        save_json(new_block_json)

    # def is_chain_valid(self):
    #     for i in range(1, len(self.chain)):
    #         current_block = self.chain[i]
    #         previous_block = self.chain[i - 1]
    #
    #         if current_block.hash != current_block.calculate_hash():
    #             return False
    #
    #         if current_block.previous_hash != previous_block.hash:
    #             return False
    #
    #     return True

def do_transaction(my_blockchain , data):
    try:
        json_string = data['parameters']['transaction_data'].decode('utf-8')
        data = json.loads(json_string)
        data = validate_inputs(Transaction_Data(), data)
        my_blockchain.add_block(Block(time.time(), json.dumps(data), my_blockchain.get_latest_block().hash))
        response = {
            'state': True,
        }
        return response
    except Exception as e:
        response = {
            'state': False,
            'error': str(e)
        }
        return response


# Check if the blockchain is valid
# is_valid = my_blockchain.is_chain_valid()
# print(f"Is the blockchain valid? {is_valid}")

