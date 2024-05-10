import socket
import threading

def handle_client(client_socket, address):
    print(f"[*] Accepted connection from {address[0]}:{address[1]}")

    while True:
        # Receive message from client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        # Display received message
        print(f"[{address[0]}:{address[1]}] {data}")

        # Send message to all clients except the sender
        for client in clients:
            if client != client_socket:
                client.send(data.encode('utf-8'))

        # Check for exit command
        if data.lower() == "exit":
            break

    # Close connection
    client_socket.close()
    print(f"[*] Connection from {address[0]}:{address[1]} closed")

# Server configuration
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 9999

# Create socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to address and port
server.bind((HOST, PORT))

# Listen for incoming connections
server.listen(5)
print(f"[*] Listening on {HOST}:{PORT}")

# List to keep track of clients
clients = []

while True:
    # Accept incoming connection
    client_socket, address = server.accept()

    # Add client to the list
    clients.append(client_socket)

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()

