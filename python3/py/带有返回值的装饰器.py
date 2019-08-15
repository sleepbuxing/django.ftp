#coding=utf-8

def func(fuc):
	def fun_in():
		aaa = fuc()
		return aaa
	return fun_in

def test():
	print("-----test------")
	return "haha"

ret = test()

print(ret)