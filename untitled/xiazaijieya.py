import os
import ftplib
import zipfile
import sys
from unrar import rarfile

def jieyarar(localfile,destpath):
    basefile = os.path.basename(localfile)
    dirname = os.path.splitext(basefile)
    destpath = destpath  + dirname[0]
    print(destpath)
    #os.mkdir(destpath)

    unrfile = rarfile.RarFile(localfile)
    unrfile.extractall(destpath)

def ftpDownload(ftp,remotefile,localfile):
    ftp.retrbinary('RETR %s' %remotefile,open(localfile,'wb').write)

def ftpConnect(host,user,passwd):
    try:
        myftp = ftplib.FTP(host)
        myftp.login(user,passwd)
        return myftp
    except ftplib.error_perm:
        print("connect fail")
        return

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
    #此处的destpath C:/untitled/un/致远天风稳健20190620
    
if __name__ == '__main__':
    yyyymmdd = sys.argv[1]
    #yyyymmdd = '20190619'
    data = open('C:/untitled/config.txt')
    ##下载到本地的目录
    localpath = 'C:/untitled/download/'
    ##将下载的文件解压后的目录
    destpath = 'C:/untitled/un/'
    ##ftp服务器的主机
    host = '192.168.19.1'
    ##ftp有下载权限的用户名和密码
    user = 'ftpuser'
    passwd = '357vuerm@'
    ftp = ftpConnect(host,user,passwd)

    for eachline in data:
        (biaozhun,xyz) = eachline.split(' ')
        biaozhun = biaozhun.replace('yyyymmdd',yyyymmdd)
        # biaozhun  /天风证券/致远天风稳健20190620.zip
        # remotepath /天风证券
        #filename  致远天风稳健20190620.zip
        remotepath = os.path.dirname(biaozhun)
        filename = os.path.basename(biaozhun)
        # localfile C:/untitled/download/致远天风稳健20190620.zip
        localfile = localpath + filename
        if ('.zip' in biaozhun or '.rar' in biaozhun or '.RAR' in biaozhun):
            #下载规定日期的
            if (yyyymmdd in biaozhun):
                try:
                    ftpDownload(ftp, biaozhun, localfile)
                    zipflag = zipfile.is_zipfile(localfile)
                    if zipflag:
                        unzipFile(localfile, destpath)
                    else:
                        jieyarar(localfile, destpath)
                except ftplib.error_perm:
                    print("%s 文件不存在"%biaozhun)

                #根据zipflag判断是否是zip的包

        else:
            try:
                os.mkdir(destpath + filename)
                try:
                    files = ftp.nlst(biaozhun)
                    for file in files:
                        middlefile = os.path.basename(file)
                        #下载文件夹下的文件，而非压缩文件
                        ftpDownload(ftp, file, destpath + filename + '/' + middlefile)
                except ftplib.error_perm:
                    print("%s 文件不存在"%biaozhun)
            except FileExistsError:
                #os.mkdir(destpath + filename)
                try:
                    files = ftp.nlst(biaozhun)
                    for file in files:
                        middlefile = os.path.basename(file)
                        ftpDownload(ftp, file, destpath + filename + '/' + middlefile)
                except ftplib.error_perm:
                    print('%s 文件不存在'%biaozhun)
    ftp.quit()
