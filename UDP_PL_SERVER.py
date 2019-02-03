#!/usr/bin/env python3

# Sean Reid
# UDP Server 


vowels = ('a','e','i','o','u','A','E','I','O','U')
def translateWord(word):
	firstLetter = word[0]
	if firstLetter in vowels:
		return word + "ay"
	else:
		return word[1:] + word[0] + "ay"

def translateSentence(sentence):
	words = sentence.split(" ")
	PigLatinSentence = ""
	for word in words:
		PigLatinSentence = PigLatinSentence + translateWord(word)
		PigLatinSentence = PigLatinSentence + " "
	return PigLatinSentence



import socket

bufferSize = 2048
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind((socket.gethostbyname(""), serverPort))
print ("The server is ready to receive.")


while True:
	message, clientAddress = serverSocket.recvfrom(bufferSize)
	pigMessage = message.decode()
	pig = translateSentence(pigMessage)
	serverSocket.sendto(pig.encode(),clientAddress)

