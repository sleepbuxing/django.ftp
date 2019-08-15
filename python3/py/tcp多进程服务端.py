#coding=utf-8
from socket import *

def clientDeal(clientSocket):
	while True:
		clientSocket.recv()
		clientSocket.send()

s = socket(AF_INET,SOCK_STREAM)
s.bind()
s.listen()
while True:
	clientSocket,clientInfo = s.accept()
	p = Process(target=clientDeal,args=(clientSocket,))