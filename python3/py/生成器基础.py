列表很大，占用太多的内存空间，故用生成器；生成器保存创建列表的方法；
创建方法一 [] 换成（）
	next(var)
有yield的函数已经是生成器了，不能按照普通的函数一样去调用。
会返回yield后边的值。 
def tests():
	i = 0 
	while i<5:
		temp = yield i
		print(i)
		i+=1

ret = tests()
#给生成器赋值
#第一次传None
#ret.send(None)
ret.send("haha")


