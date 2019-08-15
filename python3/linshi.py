try:
	fh = open("testfile","w")
	fh.write("test")
except IOError:
	print("Error:没有找到文件")
else:
	print("sucess")
	fh.close()

