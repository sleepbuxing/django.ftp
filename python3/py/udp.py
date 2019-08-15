#coding=utf-8

from socket import *
udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.bind(("192.168..", 10000))
udpSocket.sendto(b"hahaha",("192.168.."),8888)

recvDate = udpSocket.recvfrom(1024)
print(recvDate)
 