#coding=utf-8
def test(number):
	print("------1-----")
	def test_in(number2):
		print("--------2-----")
		print(number + number2)
	return test_in

ret = test(100)
ret(100)
ret(200)
ret(300)
print(ret(1))


def line_conf(a, b):
	def line(x):
			return a*x + b
	return line

line1 = line_conf(1, 1)
print(line1(5))
