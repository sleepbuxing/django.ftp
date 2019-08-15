#coding=utf-8

class Itcast(object):
	def __init__(self,subject1):
		self.subject1 = subject1
		self.subject2 = 'cpp'

	def __getattribure__(self,obj):
		if obj == 'subject1':
			print('log subject1')
			return 'redirect python'
		else:
			return object.__getattribure__(self,obj)
	def show(self):
		print('this is Itcast')

s = Itcast("python")
print(s.subject1)
print(s.subject2)
