import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5
active_clients = []
# Function to listen for upcoming messages from a client
def listen_for_messages(client):
        while 1:
           message = client.recv(2048).decode('utf-8')
           if message != '':
                final_msg = username + ~ + message
                send_message_to_all(final_msg)
           else:
                print("The message send from client {username} is empty")
                
# Function to send message to a single client
def send_message_to_client(client, message):
        client.sendall(message.encode())
        
# Function to send any new message to all the clients that are currently connected to this server
def send_messages_to_all(from_username, message):
        for user in active_clients:
           send_message_to_client(user[1],message)
        
# Function to handle client
def client_handler(client):
        while 1:
           username = client.recv(2048).decode('utf-8')
           if username != '':
                active_clients.append((username, client))
                break
           else :
                print("Client username is empty")
        threading.Thread(target=listen_for_messages,args=(client,username, )).start()
        
# Main function
def main():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
           server.bind((HOST,PORT))
           print(f"Running the server on {HOST} {PORT}")
        except:
           print(f"Unable to bind to host {HOST} and port {PORT}")

        server.listen(LISTENER_LIMIT)

        while 1:
           client, address = server.accept()
           print(f"Successfully connected to client {address[0]} {address[1]}")
          
if __name__ == '__main__':
        main()
