#coding=utf-8

def Nums(num):
	a,b = 0,1
	for x in range(num):
		yield b
		a,b= b, a+b

ret = Nums(10)		

a = next(ret)
a = next(ret)
a=ret.__next__()

for i in ret:
	print(i)

