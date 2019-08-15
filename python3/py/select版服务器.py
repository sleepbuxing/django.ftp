#select对所有套接字先依次进行检查标记（可收还是可发），
#再按分类（可收还是可发）返回元组（套接字）
#import select 
#select.select([1],[2],[3])
# 
#[1]列表1 要检测的套接字是否可以收数据
#【2】列表2 要检测的套接字是否可以发数据
#【3】列表3 要检测的套接字是否产生异常
#
#
#
import socket
import select
import sys

server = socket.socket(socket.AF_INET,socket.STREAM)
server.bind("",9565)
server.listen(10)

inputs = [server,sys.stdin]

while True:
	readable,writeable,exceptional = select.select([inputs],[],[])
	for sock in readable:
		if sock == server:
			conn,addr = server.accept()
			inputs.append(conn)
		else:
			data = sock.recv(1024)
			if date:
				sock.send(data)




