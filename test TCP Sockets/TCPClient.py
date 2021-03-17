from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("Connected to server successfully...\n")

# just one request. Put while loop for persistenct connection.
message_snd = input("Enter lowercase sentence: ")
clientSocket.send(message_snd.encode())
message_rcv = clientSocket.recv(2048)
print(f"server says: {message_rcv.decode()}")
clientSocket.close()
