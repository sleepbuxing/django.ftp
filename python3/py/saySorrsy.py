#coding=utf-8
import time
def saySorry():
	print("亲爱的，我错了，我能吃饭了吗")
	time.sleep(1)


if __name__ == "__main__":
	for i in range(5):
		saySorry()

#coding=utf-8
import time
from threading import Thread 
def daySorry():
	print("亲爱的，我错了，我能吃饭了吗")
	time.sleep(1)


for i in range(10):
	t = Thread(target=daySorry)
	t.start()


