from multiprocessing import Pool,Manager
import os

def copyFileTask(name,oldFolderName,newFolderName,queue):
	fr = open(oldFolderName+"/"+name)
	content = fr.read()
	fw = open(newFolderName+"/"+name,"w")
	fw.write(content)
	fr.close()
	fw.close()

	queue.put(name)



def main():
	oldFolderName = input("请输入目录名：")
	newFolderName = oldFolderName + ".bak"
	os.mkdir(newFolderName)
	fileNames = os.listdir(oldFolderName)

	pool = Pool(5)
	queue = Manager.Queue()
	for name in fileNames:
		pool.apply_async(copyFileTask,args=(name,oldFolderName,newFolderName,queue))
	
	num = 0
	allNum = len(fileNames)
	while num < allNum:
		queue.get()
		num += 1
		copyRate = num/allNum
		print("\r%.2f%%"%(copyRate*100),end="")

if __name__ == "__main__":
	main()