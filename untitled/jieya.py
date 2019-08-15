import os
import zipfile
from unrar import rarfile

sourcepath = 'C:/untitled/test/'
destpath='C:/untitled/un/'

def unrarFile(localfile,destpath):
    basefile = os.path.basename(localfile)
    dirname = os.path.splitext(basefile)
    destpath = destpath  + dirname[0]
    try:
        unrfile = rarfile.RarFile(localfile)
        unrfile.extractall(path=destpath)
    except  rarfile.BadRarFile as e:
        pass
        #print(rfile+'is a bad file,please check')
def unzipFile(localfile,destpath):
    ##函数负责解压到指定的目录下
    basefile = os.path.basename(localfile)
    dirname = os.path.splitext(basefile)
    destpath = destpath  +  dirname[0]
    try:
        with zipfile.ZipFile(localfile) as zfile:
            zfile.extractall(path=destpath)
    except zipfile.BadZipFile as e:
        print(zfile+'is a bad zip file,please check')
if __name__ == '__main__':
    riqi = input("请输入年月日：")
    filebase = os.listdir(sourcepath)
    for file in filebase:
        if (file.endswith('.zip') and riqi in file):
            localfile = sourcepath + file
            unzipFile(localfile,destpath)
        elif ((file.endswith('.rar') or file.endswith('.RAR')) and riqi in file):
            localfile = sourcepath + file
            unrarFile(localfile,destpath)

        else:
            pass


