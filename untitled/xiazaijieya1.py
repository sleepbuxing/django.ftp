import os
import ftplib
import zipfile
import sys
from unrar import rarfile
import riqi
import configparser

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
    try:
        myftp = ftplib.FTP(host)
        myftp.login(user, passwd)
        return myftp
    except ftplib.error_perm:
        print("connect fail")
        return

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

if __name__ == '__main__':
    yyyymmdd = riqi.isweekend().strftime("%Y%m%d")
    ##localpath下载到本地的目录,destpath将下载的文件解压后的目录

    curr = os.path.dirname(os.path.realpath(__file__))
    configpath = os.path.join(curr, 'config.ini')
    conf = configparser.ConfigParser()
    conf.read(configpath)
    dataa = conf.get('path', 'data')
    dataa = os.path.join(curr, dataa)
    localpath = conf.get('path', 'localpath')
    localpath = os.path.join(curr, localpath)
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
    infofo = conf.get('path', 'downinfo')
    infofo = os.path.join(curr, infofo)
    data = open(dataa)
    datacon = data.readlines()

    info = open(infofo)
    infocon = info.readlines()
    for eachinfo in infocon:
        (downip, downuser, downpwd) = eachinfo.split('|')
        downpwd = downpwd.strip()
        for eachline in datacon:
            (dataip, xyz, biaozhun, ip1, path1, ip2, path2) = eachline.split('|')
            path2 = path2.strip()
            if downip == dataip:
                ftp = ftpConnect(downip, downuser, downpwd)
                biaozhun = biaozhun.replace('yyyymmdd', yyyymmdd)
                remotepath = os.path.dirname(biaozhun)
                filename = os.path.basename(biaozhun)
                localfile = localpath + filename
                if ('.zip' in biaozhun or '.rar' in biaozhun or '.RAR' in biaozhun):
                    # 下载规定日期的
                    # biaozhun  /天风证券/致远天风稳健20190620.zip
                    # remotepath /天风证券
                    # filename  致远天风稳健20190620.zip
                    # localfile C:/untitled/download/致远天风稳健20190620.zip
                    if (yyyymmdd in biaozhun):
                        try:
                            ftpDownload(ftp, biaozhun, localfile)
                            zipflag = zipfile.is_zipfile(localfile)
                            if zipflag:
                                unzipFile(localfile, destpath)
                            else:
                                jieyarar(localfile, destpath)
                        except ftplib.error_perm:
                            print("%s 文件不存在" % biaozhun)
                else:
                    try:
                        os.mkdir(destpath + filename)
                        try:
                            files = ftp.nlst(biaozhun)
                            for file in files:
                                middlefile = os.path.basename(file)
                                # 下载文件夹下的文件，而非压缩文件
                                ftpDownload(ftp, file, destpath + filename + '/' + middlefile)
                        except ftplib.error_perm:
                            print("%s 文件不存在" % biaozhun)
                    except FileExistsError:
                        # os.mkdir(destpath + filename)
                        try:
                            files = ftp.nlst(biaozhun)
                            for file in files:
                                middlefile = os.path.basename(file)
                                ftpDownload(ftp, file, destpath + filename + '/' + middlefile)
                        except ftplib.error_perm:
                            print('%s 文件不存在' % biaozhun)
                ftp.quit()
