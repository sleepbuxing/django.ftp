#coding=utf-8
from socket import *
udpSocket = socket(AF_INET,SOCK_DGRAM)
destIp = input("请输入目的IP：")
destPort = int(input("请输入目的端口："))
sendDate = input("请输入要发送的数据：")
udpSocket.bind((destIp,destPort))
udpSocket.sendto(sendDate.encode("utf-8"),(destPort,destPort))