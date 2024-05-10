import socket
import threading

def receive_messages(client_socket):
    while True:
        # Receive message from server
        data = client_socket.recv(1024).decode('utf-8')
        print(data)
        if data == "exit":
            break

# Client configuration
HOST = '127.0.0.1'
PORT = 9999

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect((HOST, PORT))

# Start a thread to receive messages from server
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Send messages to server
while True:
    message = input()
    client.send(message.encode('utf-8'))
    if message.lower() == "exit":
        break

# Close the connection
client.close()



