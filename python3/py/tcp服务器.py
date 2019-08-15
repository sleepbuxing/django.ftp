#coding=utf-8

from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
bindAddr = ("192.168.1.100",9565) 
serverSocket.bind(bindAddr)
serverSocket.listen(10)
clientSocket,clientInfo = serverSocket.accept()
recvData = clientSocket.recv(1024)
print("%s:%s"%(str(clientInfo),recvData.decode("utf-8")))

clientSocket.close()
serverSocket.close()

