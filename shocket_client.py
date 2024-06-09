import socket
import time


def start_client():
    # Create a socket object
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Get the local machine name
        host = '127.0.0.1'
        port = 12345

        # Connection to the server
        client_socket.connect((host, port))

        # Send a message to the server
        message = str({
            'contract_id':"contract",
            "method":"greet",
            "parameters":"World world"
        })
        client_socket.send(message.encode('utf-8'))

        # Receive a response from the server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

        time.sleep(5)

    # Close the connection
    # client_socket.close()

if __name__ == "__main__":
    start_client()
