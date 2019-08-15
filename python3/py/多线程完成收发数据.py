#coding=utf-8
from socket import *
from threading import Thread
#收数据
def recvDate():
	while True:
		recvInfo = udpSocket.recvfrom(1024)
		print(">>%s:%s"%(str(recvInfo[1]),recvInfo[0].decode("utf-8")))

#发数据
def sendDate():
	while True:
		sendInfo = input("<<")
		udpSocket.sendto(sendInfo.encode("utf-8"),(destIp,destPort))
udpSocket = None
destIp = ""
destPort = 0

#主函数
def main():
	global udpSocket
	global destIp
	global destPort

	udpSocket = socket(AF_INET,SOCK_DGRAM)
	udpSocket.bind(("192.168.19.146", 9565))

	destIp = input("请输入IP：")
	destPort = int(input("请输入port："))

	tr = Thread(target=recvDate)
	ts = Thread(target=sendDate)
	
	tr.start()
	ts.start()
	tr.join()
	ts.join()

if __name__ == "__main__":
	main()




