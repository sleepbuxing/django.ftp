#coding=utf-8
from socket import *
def main():
	udpSocket = socket(AF_INET,SOCK_DGRAM)
	udpSocket.bind(("192.168.19.146",9565))

	while True:
		recvDate = udpSocket.recvfrom(1024)
		print("[%s]:%s"%(str(recvDate[1])),recvDate[0].decode("utf-8"))

if __name__ == "__main__":
	main()