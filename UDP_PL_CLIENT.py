#!/usr/bin/env python3

# Sean Reid
# UDP CLIENT


import socket


serverName = socket.gethostbyname("")
serverPort = 12000
bufferSize = 2048

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = input("Input a sentence to be translated into Pig Latin: ")
clientSocket.sendto(message.encode(),(serverName, serverPort))
pigMessage, serverAddress = clientSocket.recvfrom(bufferSize)
print(pigMessage.decode())
clientSocket.close()
