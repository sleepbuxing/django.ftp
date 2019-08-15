#coding=utf-8
from socket import *
udpSocket = socket(AF_INET,SOCK_DGRAM)
destIp = "192.168.."
destPort = 9565
sendDate = input("请输入要发送的数据：")
udpSocket.bind((destIp,destPort))
recvDate = udpSocket.recvfrom(1024)
content,destInfo = recvDate
print("content is %s"%content.decode("utf-8"))
