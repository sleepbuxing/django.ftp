import os
import ftplib
import zipfile
from unrar import rarfile


def jieyarar(localfile, destpath):
    basefile = os.path.basename(localfile)
    dirname = os.path.splitext(basefile)
    destpath = destpath + dirname[0]
    print(destpath)
    # os.mkdir(destpath)

    unrfile = rarfile.RarFile(localfile)
    unrfile.extractall(destpath)


def ftpDownload(ftp, remotefile, localfile):
    ftp.retrbinary('RETR %s' % remotefile, open(localfile, 'wb').write)


def ftpConnect(host, user, passwd):
    myftp = ftplib.FTP(host)
    myftp.login(user, passwd)
    # myftp.encoding = 'utf8'
    return myftp


def unzipFile(localfile, destpath):
    ##函数负责解压到指定的目录下
    basefile = os.path.basename(localfile)
    dirname = os.path.splitext(basefile)
    destpath = destpath + dirname[0]
    try:
        with zipfile.ZipFile(localfile) as zfile:
            zfile.extractall(path=destpath)
    except zipfile.BadZipFile as e:
        print(zfile + 'is a bad zip file,please check')
    # 此处的destpath C:/untitled/un/致远天风稳健20190620
    os.remove(destpath + '/' + 'mktdt04.txt')


if __name__ == '__main__':
    yyyymmdd = '20190620'
    data = open('C:/untitled/config.txt')
    localpath = 'C:/untitled/download/'
    destpath = 'C:/untitled/un/'
    # unzipdir = 'C:/untitled/un/'
    host = '192.168.19.1'
    user = 'ftpuser'
    passwd = '357vuerm@'
    ftp = ftpConnect(host, user, passwd)

    for eachline in data:
        (biaozhun, xyz) = eachline.split(' ')
        biaozhun = biaozhun.replace('yyyymmdd', yyyymmdd)

        if ('.zip' in biaozhun and '20190620' in biaozhun):
            # biaozhun  /天风证券/致远天风稳健20190620.zip
            # remotepath /天风证券

            remotepath = os.path.dirname(biaozhun)
            filename = os.path.basename(biaozhun)
            # localfile C:/untitled/download/致远天风稳健20190620.zip
            localfile = localpath + filename

            ftpDownload(ftp, biaozhun, localfile)
            unzipFile(localfile, destpath)
        elif ((biaozhun.endswith('.rar') or biaozhun.endswith('.RAR')) and yyyymmdd in biaozhun):
            # print(biaozhun)
            remotepath = os.path.dirname(biaozhun)
            filename = os.path.basename(biaozhun)
            localfile = localpath + filename

            ftpDownload(ftp, biaozhun, localfile)
            print(localfile)
            print(destpath)
            jieyarar(localfile, destpath)

    ftp.quit()



