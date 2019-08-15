import os
import ftplib

host = '192.168.19.1'
user = '123'
passwd = '123'
#下载到本地的路径和文件名,路径必须带/
localpath = 'C:/untitled/un'
#ftp服务器路径和文件名，路径必须带/
remotepath = 'C:/ftptest/testftp'

#remotefile = remotepath + remotefilename

def ftpConnect(host,user,passwd):
    myftp = ftplib.FTP(host)
    myftp.login(user,passwd)
    return myftp

def ftpUpload(ftp,remotefile,localfile):
    ftp.storbinary('STOR %s' %remotefile,open(localfile,'rb'))
    ftp.quit()
if __name__ == '__main__':
    ftp = ftpConnect(host,user,passwd)
    aa = os.listdir(localpath)
    print(aa)
#带文件名的全路径

    ftpdownfile = ftpUpload(ftp, remotepath, localpath)


