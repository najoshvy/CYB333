import socket

def start_server(host='localhost', port=5000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"Server listening on {host}:{port}")
    
    try:
        while True:
            client, addr = server.accept()
            print(f"Connection from {addr}")
            
            data = client.recv(1024).decode()
            print(f"Received: {data}")
            
            client.send("Message received".encode())
            client.close()
    except KeyboardInterrupt:
        print("Server shutting down")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()