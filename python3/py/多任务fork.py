import os
import time

ret = os.fork()
print(ret)
if ret == 0:
	while True:
		print(“-------ppprogress------”)
		print("%d"%os.getid())
		time.sleep(1)
else:
	while True:
		print("-------pprogress------")
		print("%d"%os.getppid())
		time.sleep(1)


