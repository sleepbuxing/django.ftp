#coding=utf-8
def w1(func):
	def inner():
		print("------正在验证-------")
		if False:
			func()
		else:
			print("没有权限")
	return inner
@w1
def f1():
	print("----f1-----")

@w1
def f2():
	print("-------f2------")

#f1 = w1(f1)
#f2 = w1(f2)

f1()
f2()