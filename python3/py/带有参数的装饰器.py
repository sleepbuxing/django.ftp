#coding=utf-8

def func(functionName):
	def func_in(*args, **kwargs):
		functionName(*args, **kwargs)
	return func_in

@func
def test(a, b):
	print("a=%d, b=%d"%(a, b))

test(11, 22)