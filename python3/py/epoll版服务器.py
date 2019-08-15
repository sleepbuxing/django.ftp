#select	最多套接字1024		轮询的方式检测
#poll	没有套接字上限	轮询的方式检测
#epoll	没有套接字上限	事件通知机制
#select.EPOLLIN	判断是否是接收数据的事件
#select.EPOLLOUT
#文件描述符FD：
#import sys
#sys.stdin	标准输入  键盘
#sys.stdout	标准输出	 屏幕
#sys.stderr	标准错误	 屏幕
#根据文件描述符找到它对应的套接字
#只有套接字可以接收数据
#epoll对文件描述符的两种处理模式：ET和LT
#ET：当epoll检测到描述符事件发生并将事件通知应用程序，应用程序必须立即处理该事件；否则，再不通知。
#epool.register(s.fileno(),select.EPOLLIN|select.EPOLLET)
#
#
import select

s = socket.socket(socket.AF_INET,socket.SOCL_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind("",9565)
s.listen(100)

epoll = select.epoll()
epoll_list = epoll.poll()
for fd,events in epoll_list:
	if fd == s.fileno():
		conn,addr=s.accept() 

	elif events == select.EPOLLIN:
		recvData = connections[fd].recv(1024)
		if len(recvData)>0:
			print("recv:%s"%recvData)
		else:
			epoll.unregister(fd)
			connections[fd].close()
			print("%s---offline--"%str(address[fd]))






