import os
import shutil
import sys
import riqi
import configparser
import getabsopath

if __name__ == '__main__':
    yyyymmdd = riqi.isweekend().strftime("%Y%m%d")
    curr = os.path.dirname(os.path.realpath(__file__))
    localpath = getabsopath.absolufile('config.ini', 'path', 'localpath')
    try:
        os.chdir(localpath)
    except FileNotFoundError:
        os.mkdir(localpath)
    destpath = getabsopath.absolufile('config.ini', 'path', 'destpath')
    try:
        os.chdir(destpath)
    except  FileNotFoundError:
        os.mkdir(destpath)
    dataa = getabsopath.absolufile('config.ini', 'path', 'data')
    data = open(dataa)
    datacon = data.readlines()
    #输出到指定文件：
    logfile = getabsopath.absolufile('config.ini', 'path', 'logfile')
    savestdout = sys.stdout
    with open(logfile, 'a+', encoding='utf-8') as f:
        sys.stdout = f
        print("----------开始重命名文件--------------")
        for eachline in datacon:
            (dataip, xyz, biaozhun, ip1, path1, ip2, path2) = eachline.split('|')
            biaozhun = biaozhun.replace('yyyymmdd', yyyymmdd)
            tt = os.path.basename(biaozhun)

            if '.' in tt:
                (filename, diuqi) = tt.split('.')
                try:
                    os.chdir(destpath + filename)
                    files = os.listdir()
                    for file in files:
                        (filepre,fileback) = file.split('.')
                        lastname = filepre + xyz + '.' + fileback
                        os.rename(file, lastname)
                        print("%s   重命名完成" % (destpath + filename + '/' + lastname))
                except FileNotFoundError:
                    print('%s 不存在'%(destpath + filename))
            else:
                fullfilename = (biaozhun.strip('/')).replace('/', '')
                if os.path.isdir(destpath + fullfilename):
                    os.chdir(destpath + fullfilename)
                    files = os.listdir()
                    for file in files:
                        (filepre,fileback) = file.split('.')
                        lastname = filepre + xyz + '.' + fileback
                        os.rename(file, lastname)
                        print("%s   重命名完成"%(destpath + fullfilename +  '/' + lastname))
                else:
                    print('%s 不存在'%(destpath + fullfilename))
    sys.stdout = savestdout
    data.close()

