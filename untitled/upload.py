import os
import ftplib
import sys

def ftpUpload(ftp, remotefile, localfile):
    ftp.storbinary('STOR %s' %remotefile,open(localfile,'rb'))

def ftpConnect(host, user, passwd):
    myftp = ftplib.FTP(host)
    myftp.login(user, passwd)
    return myftp

if __name__ == '__main__':
    yyyymmdd = sys.argv[1]
    #yyyymmdd = '20190619'
    data = open('C:/untitled/config.txt')
    datacon = data.readlines()
    localpath = 'C:/untitled/last/'
    destpath = '/托管数据/估值核算/'
    host = '192.168.19.1'
    user = 'ftpuser'
    passwd = '357vuerm@'
    ftp = ftpConnect(host, user, passwd)
    try:
        #ftp服务器判断日期的文件夹是否存在，不存在则创建
        ftp.cwd(destpath + yyyymmdd)
    except ftplib.error_perm:
        ftp.mkd(destpath + yyyymmdd)
    os.chdir(localpath)
    files = os.listdir()
    destpath = destpath + yyyymmdd + '/'
    for file in files:
        ftpUpload(ftp,destpath + file, localpath + file)

    ftp.quit()



