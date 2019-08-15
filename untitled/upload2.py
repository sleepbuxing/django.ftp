import os
import ftplib
import sys
import riqi
import configparser

def ftpUpload(ftp, remotefile, localfile):
    ftp.storbinary('STOR %s' %remotefile,open(localfile,'rb'))

def ftpConnect(host, user, passwd):
    myftp = ftplib.FTP(host)
    myftp.login(user, passwd)
    return myftp

if __name__ == '__main__':
    yyyymmdd = riqi.isweekend()

    curr = os.path.dirname(os.path.realpath(__file__))
    configpath = os.path.join(curr, 'config.ini')
    conf = configparser.ConfigParser()
    conf.read(configpath)
    dataa = conf.get('path', 'data')
    dataa = os.path.join(curr, dataa)
    localpath = conf.get('path', 'localpath')
    localpath = os.path.join(curr, localpath)
    destpath = conf.get('path', 'destpath')
    destpath = os.path.join(curr, destpath)
    infofo = conf.get('path', 'upinfo')
    infofo = os.path.join(curr, infofo)

    data = open(dataa)
    datacon = data.readlines()

    info = open(infofo)
    infocon = info.readlines()
    localpath = destpath


    for eachinfo in infocon:
        (upip, upuser, uppwd) = eachinfo.split('|')
        uppwd = uppwd.strip('\n')
        for eachline in datacon:
            (dataip, xyz, biaozhun, ip1, path1, ip2, path2) = eachline.split('|')
            biaozhun = biaozhun.replace('yyyymmdd', yyyymmdd)
            path2 = path2.strip('\n')
            if upip == ip2:
                uppwd = uppwd.strip('\n')
                ftp = ftpConnect(upip, upuser, uppwd)
                try:
                    # ftp服务器判断日期的文件夹是否存在，不存在则创建
                    destpath2 = path2.strip('\n')
                    destpath2 = destpath2.strip('\n')
                    destpath2 = destpath2.replace('yyyymmdd', yyyymmdd)
                    ftp.cwd(destpath2)
                except ftplib.error_perm:
                    ftp.mkd(destpath2)
                os.chdir(localpath)
                filename = os.path.basename(biaozhun)
                if ('.zip' in biaozhun or '.rar' in biaozhun or '.RAR' in biaozhun):

                    (filefre, diuqi) = filename.split('.')
                    try:
                        os.chdir(localpath + filefre)
                        files = os.listdir()
                        for file in files:
                            ftpUpload(ftp, destpath2 + file, localpath  + filefre + '/' + file)
                    except FileNotFoundError:
                        print('%s 不存在'%(localpath + filename))

                else:
                    try:
                        os.chdir(localpath + filename)
                        files = os.listdir()
                        for file in files:
                            ftpUpload(ftp, destpath2 + filename, localpath  + filename + '/' + file)
                    except FileNotFoundError:
                        print('%s 不存在' % (localpath + filename))

                ftp.quit()

