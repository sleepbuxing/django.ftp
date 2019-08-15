from multiprocessing import Pool
import os
import random
import time

def worker():
	for i in range(random.randint(1,9)):
		print("%d"%os.getpid())

pool = Pool(10)
for j in range(10):
	pool.apply_async(worker)
	#pool.apply(worker) #不会并行，程序堵塞
pool.close()#不能再次添加新任务
pool.join()#主进程等待子进程结束






