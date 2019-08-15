栈：先进后出
队列：先进先出
queue完成普通进程间的通信
from multiprocessing import Queue
q = Queue(3)
q.qsize()
q.put("")
q.get()
q.empty()
q.full()

进程池中进程间的通信：
from multiprocessing import Manager, Pool
q = Manager().Queue()
po = Pool()
po.apply()
po.close()
po.join()

help(po.apply_async)



