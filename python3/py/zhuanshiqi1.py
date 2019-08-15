#coding=utf-8

def makeBold(fn):
	def wrapped():
		return "<b>" + fn() + "</b>"
	return wrapped

def makeItalic(fn):
	def wrapped():
		return "<i>" + fn() + "</i>" 
	return wrapped
@makeBold
@makeItalic
def test3():
	return "hello world"

ret = test3()
print(ret)