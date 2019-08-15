import os
import configparser
import riqi
from datetime import *
import re
import sys

#根据配置文件获取绝对路径:confname配置文件名；label配置文件中的标签;
#key标签下的关键词
def absolufile(confname,conflabel, confkey):
    current = os.path.dirname(os.path.realpath(__file__))
    conf = configparser.ConfigParser()
    conffile = os.path.join(current, confname)
    conf.read(conffile)
    filename = conf.get(conflabel, confkey)
    absolupath = os.path.join(current, filename)
    return absolupath

def rmfile(rmfilepath):
    try:
        os.remove(rmfilepath)
        print("%s 删除完成"%rmfilepath)
    except FileNotFoundError:
        print("%s 文件不存在"%rmfilepath)

def modconffile(conffile):
    nianyueri = riqi.isweekend()
    yyyymmdd = datetime.strftime(nianyueri, "%Y%m%d")
    mmdd = datetime.strftime(nianyueri, "%m%d")
    mdd = (datetime.strftime(nianyueri, "%m%d")).strip('0')
    #整理需要删除的文件名格式
    filemodes = []
    with open(conffile, 'r', encoding='utf-8') as f:
        content = f.readlines()
        for line in content:
            line  = line.strip('\n')
            line = line.replace("yyyymmdd", yyyymmdd)
            line = line.replace("mmdd", mmdd)
            line = line.replace("mdd", mdd)
            filemodes.append(line)
    return filemodes

if __name__ == '__main__':
    curr = os.path.dirname(os.path.realpath(__file__))
    # 获取需要删除文件的配置文件
    rmfilepath = absolufile('config.ini', 'path', 'rmfilename')
    filemodes = modconffile(rmfilepath)
    dirdestpath = absolufile('config.ini', 'path', 'destpath')
    dirlists = os.listdir(dirdestpath)
    #开启日志输出
    logfile = absolufile('config.ini', 'path', 'logfile')
    savestdout = sys.stdout
    with open(logfile, 'a+', encoding='utf-8') as f:
        sys.stdout = f
        print("----------开始删除文件--------------")

        for dirlist in dirlists:
            destpath = os.path.join(dirdestpath, dirlist)
            os.chdir(destpath)
            filelists = os.listdir(destpath)
            #filemode配置文件的文件名；filelist需要删除的文件
            for filelist in filelists:
                for filemode in filemodes:
                    if re.match(filemode, filelist):
                        realpath = os.path.realpath(filelist)
                        rmfile(realpath)
    sys.stdout = savestdout









