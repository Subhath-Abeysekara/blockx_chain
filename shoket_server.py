import ast
import json
import socket
from excute_text_code import execute_contract_code
from main import Blockchain, do_transaction
from schemas.data_schema import Data
from select_random_nodes import select_nodes
from validate_data.validate_data import validate_inputs
my_blockchain = Blockchain()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    while True:
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received message: {data}")
        message_dict = ast.literal_eval(data)
        print(f"Decoded dictionary: {message_dict}")
        try:
            validate_inputs(Data(), message_dict)
            headers = message_dict['headers']
            data = message_dict['data']
            contract_id = data['contract_id']
            method = headers['method']
            try:
                if method == "transfer_tokens":
                    parameters = [data['parameters']['signature'], data['parameters']['public_key'],
                                  data['parameters']['transaction_data']]
                    print(parameters)
                    response = execute_contract_code(contract_id, method, parameters)
                    if response['state']:
                        response = do_transaction(my_blockchain, data)
                elif method == "log_user":
                    parameters = data['parameters']
                    print(parameters)
                    response = execute_contract_code(contract_id, method, parameters)
                elif method == "select_nodes":
                    print(data['parameters']['public_key'])
                    response = select_nodes(data['parameters']['public_key'])
                    print(response)
                else:
                    response = execute_contract_code(contract_id, method)
            except Exception as e:
                response = {
                    'state': False,
                    'error': str(e)
                }
            response_data = json.dumps(response).encode('utf-8')
            client_socket.send(response_data)
        except Exception as e:
            print(e)
            response = {
                'state':False,
                'error':str(e)
            }
            response_data = json.dumps(response).encode('utf-8')
            client_socket.send(response_data)
        client_socket.close()

if __name__ == "__main__":
    start_server()
