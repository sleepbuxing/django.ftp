import os
import shutil
import sys
import riqi
import configparser
import getabsopath

if __name__ == '__main__':
    yyyymmdd = riqi.isweekend()
    curr = os.path.dirname(os.path.realpath(__file__))

    localpath = getabsopath.absolufile('config.ini', 'path', 'localpath')
    try:
        os.chdir(localpath)
    except FileNotFoundError:
        os.mkdir(localpath)
    destpath = conf.get('path', 'destpath')
    destpath = os.path.join(curr, destpath)
    try:
        os.chdir(destpath)
    except  FileNotFoundError:
        os.mkdir(destpath)
    dataa = getabsopath.absolufile('config.ini', 'path', 'data')
    data = open(dataa)
    datacon = data.readlines()


    for eachline in datacon:
        (dataip, xyz, biaozhun, ip1, path1, ip2, path2) = eachline.split('|')
        #xyz = xyz + '.dbf'
        biaozhun = biaozhun.replace('yyyymmdd',yyyymmdd)
        #print(biaozhun)
        tt = os.path.basename(biaozhun)
        #print(tt)
        if '.' in tt:
            (filename,diuqi) = tt.split('.')
            try:
                os.chdir(destpath + filename)
                files = os.listdir()
                for file in files:
                    (filepre,fileback) = file.split('.')
                    lastname = filepre + xyz + '.' + fileback
                    os.rename(file, lastname)
                    #shutil.move(lastname,lastpath)
            except FileNotFoundError:
                print('%s 不存在'%(destpath + filename))
        else:
            if os.path.isdir(destpath + tt):
                filename = tt
                os.chdir(destpath + filename)
                files = os.listdir()
                for file in files:
                    (filepre,fileback) = file.split('.')
                    lastname = filepre + xyz + '.' + fileback
                    os.rename(file,lastname)
                    #shutil.move(lastname,lastpath)
            else:
                print('%s 不存在'%(destpath + tt))


