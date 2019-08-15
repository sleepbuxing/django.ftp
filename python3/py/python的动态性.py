#coding=utf-8
import types
class Person(object):
	def __init__(self, newName, newAge):
		self.name = newName
		self.age = newAge

	def run(self):
		print("%s正在跑----"%(self.name))

laowang = Person("老王", 88)
print(laowang.name)
print(laowang.age)
laowang.run()

##添加新的方法

def eat(self):
	print("%s正在吃----"%(self.eat))

laowang.eat = types.MethodType(eat, laowang)
laowang.eat()
