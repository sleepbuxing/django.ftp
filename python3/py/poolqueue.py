from multiprocessing import Manager,Pool
import os
import time
import random

def reader():
	pass

def writer():
	pass

def main():
	print("%s start"%os.getpid())
	q = Manager().Queue()
	po = pool(5)
	po.apply

if __name__ == "__main__":
	main()
