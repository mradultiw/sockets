from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("server is ready to welcome...")

while True:
    clientSocket, address = serverSocket.accept()  # creating connectionSocket
    message_rcv = clientSocket.recv(2048).decode()
    print(f"client says: {message_rcv}; add: {address}")
    clientSocket.send(message_rcv.upper().encode())
    clientSocket.close()  # Closing the connection after sending data.
    # For persistence connection, create & close connectionSocket outside while loop
    break  # I just want to stop the server here, otherwise it will wait for
    # a new TCP connection
