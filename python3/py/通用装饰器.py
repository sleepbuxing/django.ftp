#coding=utf-8

def func(fucName):
	def func_in(*args, **kwargs):
		ret = fucName(*args, **kwargs)
		return ret
	return func_in

@func
def test():
	print("---无参数无返回值test------")

@func
def test2():
	print("---无参数有返回值test2----")
	return "haha"

@func
def test3(a, b):
	print("---有参数无返回值test3----")
	print("---a=%d, b=%d"%(a, b))

@func
def test4(a, b, c):
	print("---有参数有返回值----")
	return a + b + c 

test()
aa = test2()
print(aa)

test3(11, 22)

bb = test4(11, 22, 33)
print(bb)
