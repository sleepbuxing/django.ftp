#coding=utf-8
from socket import *
clientSocket = socket(AF_INET, SOCK_STREAM)
destAddr = ("192.168..",9565)
clientSocket.connect(destAddr)
sendDate = "你好啊！"
clientSocket.send(sendDate.encode("utf-8"))
recvDate = clientSocket.recv(1024)
print("recvDate:%s"%(recvDate.decode("utf-8")))
clientSocket.close()
