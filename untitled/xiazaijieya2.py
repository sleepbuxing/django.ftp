import os
import ftplib
import zipfile
import sys
from unrar import rarfile
import riqi
import configparser
import getabsopath

def jieyarar(localfile, destpath):
    basefile = os.path.basename(localfile)
    dirname = os.path.splitext(basefile)
    destpath = destpath + dirname[0]
    unrfile = rarfile.RarFile(localfile)
    unrfile.extractall(destpath)
    print("%s   已完成解压"%localfile)

def ftpDownload(ftp, remotefile, localfile):
    ftp.retrbinary('RETR %s' % remotefile, open(localfile, 'wb').write)
    print("%s   已完成下载"%localfile)

def ftpConnect(host, user, passwd):
    try:
        myftp = ftplib.FTP(host)
        myftp.login(user, passwd)
        print("%s登录成功"%host)
        return myftp
    except ftplib.error_perm:
        print("%s connect fail"%host)
        return

def unzipFile(localfile, destpath):
    ##函数负责解压到指定的目录下
    basefile = os.path.basename(localfile)
    dirname = os.path.splitext(basefile)
    destpath = destpath + dirname[0]
    try:
        with zipfile.ZipFile(localfile) as zfile:
            zfile.extractall(path=destpath)
            print("%s   已完成解压"%localfile)
    except zipfile.BadZipFile as e:
        print(zfile + 'is a bad zip file,please check')
    # 此处的destpath C:/untitled/un/致远天风稳健20190620

if __name__ == '__main__':
    yyyymmdd = riqi.isweekend().strftime("%Y%m%d")
    print(yyyymmdd)
    ##localpath下载到本地的目录,destpath将下载的文件解压后的目录
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
    infofo = getabsopath.absolufile('config.ini', 'path', 'downinfo')
    info = open(infofo)
    infocon = info.readlines()
    #输出到指定文件
    logfile = getabsopath.absolufile('config.ini', 'path', 'logfile')
    savestdout = sys.stdout
    with open(logfile, 'a+', encoding='utf-8') as f:
        sys.stdout = f
        print("----------开始下载并解压--------------")
        for eachinfo in infocon:
            (downip, downuser, downpwd) = eachinfo.split('|')
            downpwd = downpwd.strip()
            for eachline in datacon:
                (dataip, xyz, biaozhun, ip1, path1, ip2, path2) = eachline.split('|')
                path2 = path2.strip()
                biaozhun = biaozhun.replace('yyyymmdd', yyyymmdd)
                if downip == dataip:
                    ftp = ftpConnect(downip, downuser, downpwd)
                    #biaozhun = biaozhun.replace('yyyymmdd', yyyymmdd)
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
                        fullfilename = (biaozhun.strip('/')).replace('/', '')
                        try:
                            os.mkdir(destpath + fullfilename)
                        except FileExistsError:
                            pass
                        try:
                            #ftp.cwd(biaozhun)
                            files = ftp.nlst(biaozhun)
                            for file in files:
                                middlefile = os.path.basename(file)
                                # 下载文件夹下的文件，而非压缩文件
                                ftpDownload(ftp, file, destpath + fullfilename + '/' + middlefile)
                        except ftplib.error_perm:
                            print("%s 文件不存在" % biaozhun)
                    ftp.quit()
    sys.stdout = savestdout
    data.close()
    info.close()