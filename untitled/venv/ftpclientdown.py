import os
import ftplib

host = '192.168.19.1'
user = 'csizxzq'
passwd = '13676308'
#下载到本地的路径和文件名,路径必须带/
localpath = 'C:/untitled/test/'
#ftp服务器路径和文件名，路径必须带/
remotepath = 'idxdata/data/bonddata/specified_bond_valuation/'

#remotefile = remotepath + remotefilename

def ftpConnect(host,user,passwd):
    myftp = ftplib.FTP(host)
    myftp.login(user,passwd)
    return myftp

def ftpDownload(ftp,remotefile,localfile):
    ftp.retrbinary('RETR %s' %remotefile,open(localfile,'wb').write)

if __name__ == '__main__':
    ftp = ftpConnect(host,user,passwd)
    filelist = ftp.nlst(remotepath)
    riqi = input("请输入年月日：")
#带文件名的全路径
    for list in filelist:
        #basename = os.path.basename(list)
        if ( riqi in list):
            #basenamefile.append(basename)
            basenamefile = os.path.basename(list)
            localfile = localpath + basenamefile
            ftpdownfile = ftpDownload(ftp, list, localfile)
    ftp.quit()

