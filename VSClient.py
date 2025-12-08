import socket

def main():
    host = '127.0.0.1'  # Server's IP address
    port = 5000        # Server's port number

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect((host, port))
        print("Connected to the server.")

        # Send a message to the server
        message = "Hello, Server!"
        client_socket.sendall(message.encode())
        print("Message sent to the server.")

        # Receive a response from the server
        response = client_socket.recv(1024)
        print("Received from server:", response.decode())

if __name__ == "__main__":
    main()
    print("Connection closed.")