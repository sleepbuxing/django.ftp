from multiprocessing import Process
import time
##主进程会等着所有的子进程先结束
def test():
	while True:
		print("----test----")
		time.sleep(1)

p = Process(target=test)
p.start()  #让这个进程开始执行test函数的代码
p.join()	#等待子进程结束
while True:
	print("----main----")
	time.sleep(1)

