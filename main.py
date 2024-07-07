import ast
import json
import os
import time
import random
from datetime import datetime

from Block import Block
from create_json import save_json, count_files_in_directory
from env import system_account
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
        save_json(self.create_genesis_block() , genesis=True)

    def create_genesis_block(self):
        data = {
            "transaction_data": {
                "transferer_public_key": "000000000000000000000000000000000",
                "reciever_public_key": system_account,
                "transfer_amount": 1000000000
            }
        }
        data = data['transaction_data']
        data['transferer_balnce'] = {
            "minted": 0,
            "donated": data['transfer_amount']
        }

        data['reciever_balnce'] = {
            "minted": data['transfer_amount'],
            "donated": 0
        }
        genesis_block = Block(time.time(), json.dumps(data), "0")
        new_block_json = json.dumps(genesis_block.__dict__)
        return new_block_json

    def get_latest_block(self):
        return get_latest()

    def get_block_data(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        print(new_block)
        return new_block

    def add_block(self, new_block):
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

def do_initial_transaction(my_blockchain , data):
    try:
        data = validate_inputs(Transaction_Data(), data)
        data['transferer_balnce'] = get_balance(public_key=data['transferer_public_key'])
        data['transferer_balnce']['minted_tokens']-=data['transfer_amount']
        data['transferer_balnce']['donated_token']+= data['transfer_amount']
        data['reciever_balnce'] = get_balance(public_key=data['reciever_public_key'])
        data['reciever_balnce']['minted_tokens']+= data['transfer_amount']
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

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data =  json.load(file)
        return json.loads(data)

def get_balance(public_key):
    print(public_key)
    dir_list = os.listdir("nodes")
    validator = random.choice(dir_list)
    blocks = os.listdir(f"nodes/{validator}")
    directory_path = f"nodes/{validator}"
    print(blocks)
    while True:
        try:
            latest_block = None
            latest_block_name = None
            latest_timestamp = None
            for json_file in blocks:
                file_path = os.path.join(directory_path, json_file)
                block_data = read_json_file(file_path)
                block_timestamp = block_data['timestamp']
                if latest_timestamp is None or block_timestamp > latest_timestamp:
                    latest_block = block_data
                    latest_timestamp = block_timestamp
                    latest_block_name = json_file
            blocks.remove(latest_block_name)
            print(blocks)
            print("Latest block:")
            print(print(latest_block))
            data = json.loads(latest_block['data'])
            print(data['transferer_public_key'])
            print(data['reciever_public_key'])
            if data['transferer_public_key'] == public_key:
                balance = {
                    "minted_tokens": data['transferer_minted_token_balance'],
                    "donated_token": data['transferer_donated_token_balance']
                }
                return balance
            elif data['reciever_public_key'] == public_key:
                balance = {
                    "minted_tokens": data['reciever_minted_token_balance'],
                    "donated_token": data['reciever_donated_token_balance']
                }
                return balance
        except Exception as e:
            print(e)
            balance = {
                "minted_tokens": 0,
                "donated_token": 0
            }
            return balance


def do_transaction(my_blockchain , data):
    try:
        json_string = data['parameters']['transaction_data'].decode('utf-8')
        data = json.loads(json_string)
        data = validate_inputs(Transaction_Data(), data)
        data['transferer_balnce'] = get_balance(public_key=data['transferer_public_key'])
        data['transferer_balnce']['minted_tokens'] -= data['transfer_amount']
        data['transferer_balnce']['donated_token'] += data['transfer_amount']
        data['reciever_balnce'] = get_balance(public_key=data['reciever_public_key'])
        data['reciever_balnce']['minted_tokens'] += data['transfer_amount']
        response = {
            'state': True,
            "block":my_blockchain.get_latest_block(Block(time.time(), json.dumps(data), my_blockchain.get_latest_block().hash))
        }
        return response
    except Exception as e:
        response = {
            'state': False,
            'error': str(e)
        }
        return response

def get_chain_by_node(public_key):
    blocks = os.listdir(f"nodes/{public_key}")
    print(blocks)
    chain = []
    directory_path = f"nodes/{public_key}"
    for json_file in blocks:
        file_path = os.path.join(directory_path, json_file)
        block_data = read_json_file(file_path)
        data = json.loads(block_data['data'])
        block_data['data'] = data
        print(block_data)
        chain.append(block_data)
    return chain


# Check if the blockchain is valid
# is_valid = my_blockchain.is_chain_valid()
# print(f"Is the blockchain valid? {is_valid}")
transferer_public_key = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEf9Sl4SgieBlB9tQEWwEe3WBp4kvu093xXl6QKnOLo5cWb0wIxiCstxz4zvpx6VB8+2ChN2RFIQSqPEjc4dnOqA=="
reciever_public_key = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEf9Sl4SgieBlB9tQEWwEe3WBp4kvu093xXl6QKnOLo5cWb0wIxiCstxz4zvpx6VB8+2ChN2RFIQSqPEjc4dnOqA=="

# balance = get_balance(transferer_public_key)
# print(balance)
# public_key = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEwhYr+Ggz0xDTS1Q4SYdoSwgHxdz22OPBETsJUcS6eCi4eG9NDva0xDzDLlNThS0JicPf05CyKVdXfjDZ153wKw=="
# get_chain_by_node(public_key)