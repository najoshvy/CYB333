import socket

def start_server(host='localhost', port=5000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(1)
    print(f"Server listening on {host}:{port}")
    try:
        while True:
            client, addr = server.accept()
            print(f"Connection from {addr}")
            
            try:
                data = client.recv(1024).decode()
                print(f"Received: {data}")
                
                client.send("Message received".encode())
            except Exception as e:
                print(f"Error handling client: {e}")
            finally:
                client.close()
    except KeyboardInterrupt:
        print("Server shutting down")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
    print("Connection closed")