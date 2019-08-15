import os
import ftplib
import sys
import riqi
import configparser
import getabsopath

def ftpUpload(ftp, remotefile, localfile):
    ftp.storbinary('STOR %s' %remotefile,open(localfile,'rb'))
    print("已上传到 %s"%remotefile)

def ftpConnect(host, user, passwd):
    myftp = ftplib.FTP(host)
    myftp.login(user, passwd)
    return myftp

if __name__ == '__main__':
    yyyymmdd = riqi.isweekend().strftime("%Y%m%d")
    curr = os.path.dirname(os.path.realpath(__file__))
    localpath = getabsopath.absolufile('config.ini', 'path', 'localpath')
    destpath = getabsopath.absolufile('config.ini', 'path', 'destpath')
    dataa = getabsopath.absolufile('config.ini', 'path', 'data')
    fdataa = open(dataa)
    datacon = fdataa.readlines()
    infofo = getabsopath.absolufile('config.ini', 'path', 'upinfo')
    finfofo = open(infofo)
    infocon = finfofo.readlines()
    localpath = destpath
    #输出到指定文件
    logfile = getabsopath.absolufile('config.ini', 'path', 'logfile')
    savestdout = sys.stdout
    with open(logfile, 'a+', encoding='utf-8') as f:
        sys.stdout = f
        print("----------开始上传文件--------------")
        for eachline in datacon:
            (dataip, xyz, biaozhun, ip1, path1, ip2, path2) = eachline.split('|')
            biaozhun = biaozhun.replace('yyyymmdd', yyyymmdd)
            path2 = path2.strip()
            if ip1 == ip2:
                for eachinfo in infocon:
                    (upip, upuser, uppwd) = eachinfo.split('|')
                    uppwd = uppwd.strip()
                    if ip1 == upip:
                        ftp = ftpConnect(upip, upuser, uppwd)
                        try:
                            # ftp服务器判断日期的文件夹是否存在，不存在则创建
                            destpath1 = path1.replace('yyyymmdd', yyyymmdd)
                            ftp.cwd(destpath1)
                        except ftplib.error_perm:
                            ftp.mkd(destpath1)
                        os.chdir(localpath)
                        filename = os.path.basename(biaozhun)
                        if ('.zip' in biaozhun or '.rar' in biaozhun or '.RAR' in biaozhun):
                            (filefre, diuqi) = filename.split('.')
                            try:
                                os.chdir(localpath + filefre)
                                files = os.listdir()
                                print("%s   开始上传到%s"%((localpath + filefre), upip))
                                for file in files:
                                    ftpUpload(ftp, destpath1 + file, localpath + filefre + '/' + file)
                                print("%s   上传到%s完成"%((localpath + filefre), upip))
                            except FileNotFoundError:
                                print('%s 不存在' % (localpath + filefre))

                        else:
                            fullfilename = (biaozhun.strip('/')).replace('/', '')
                            try:
                                os.chdir(localpath + fullfilename)
                                files = os.listdir()
                                print("%s   开始上传到%s"%((localpath + fullfilename), upip))
                                for file in files:
                                    ftpUpload(ftp, destpath1 + file, localpath + fullfilename + '/' + file)
                                print("%s   上传到%s完成" % ((localpath + fullfilename), upip))
                            except FileNotFoundError:
                                print('%s 不存在' % (localpath + fullfilename))
                        ftp.quit()
            else:
                for eachinfo in infocon:
                    (upip, upuser, uppwd) = eachinfo.split('|')
                    uppwd = uppwd.strip('\n')
                    if ip1 == upip:
                        ftp = ftpConnect(upip, upuser, uppwd)
                        try:
                            # ftp服务器判断日期的文件夹是否存在，不存在则创建
                            destpath1 = path1.replace('yyyymmdd', yyyymmdd)
                            ftp.cwd(destpath1)
                        except ftplib.error_perm:
                            ftp.mkd(destpath1)
                        os.chdir(localpath)
                        filename = os.path.basename(biaozhun)
                        if ('.zip' in biaozhun or '.rar' in biaozhun or '.RAR' in biaozhun):
                            (filefre, diuqi) = filename.split('.')
                            try:
                                os.chdir(localpath + filefre)
                                files = os.listdir()
                                print("%s   开始上传到%s" % ((localpath + filefre), upip))
                                for file in files:
                                    ftpUpload(ftp, destpath1 + file, localpath + filefre + '/' + file)
                                print("%s   上传到%s完成" % ((localpath + filefre), upip))
                            except FileNotFoundError:
                                print('%s 不存在' % (localpath + filefre))

                        else:
                            fullfilename = (biaozhun.strip('/')).replace('/', '')
                            try:
                                os.chdir(localpath + fullfilename)
                                files = os.listdir()
                                print("%s   开始上传到%s" % ((localpath + fullfilename), upip))
                                for file in files:
                                    ftpUpload(ftp, destpath1 + file, localpath + fullfilename + '/' + file)
                                print("%s   上传到%s完成" % ((localpath + fullfilename), upip))
                            except FileNotFoundError:
                                print('%s 不存在' % (localpath + fullfilename))
                        ftp.quit()
                    if ip2 == upip:
                        ftp = ftpConnect(upip, upuser, uppwd)
                        try:
                            # ftp服务器判断日期的文件夹是否存在，不存在则创建
                            destpath2 = path2.replace('yyyymmdd', yyyymmdd)
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
                                print("%s   开始上传到%s" % ((localpath + filefre), upip))
                                for file in files:
                                    ftpUpload(ftp, destpath2 + file, localpath + filefre + '/' + file)
                                print("%s   上传到%s完成" % ((localpath + filefre), upip))
                            except FileNotFoundError:
                                print('%s 不存在' % (localpath + filefre))

                        else:
                            fullfilename = (biaozhun.strip('/')).replace('/', '')
                            try:
                                os.chdir(localpath + fullfilename)
                                files = os.listdir()
                                print("%s   开始上传到%s" % ((localpath + fullfilename), upip))
                                for file in files:
                                    ftpUpload(ftp, destpath2 + file, localpath + fullfilename + '/' + file)
                                print("%s   上传到%s完成" % ((localpath + fullfilename), upip))
                            except FileNotFoundError:
                                print('%s 不存在' % (localpath + fullfilename))
                        ftp.quit()
    sys.stdout = savestdout
    fdataa.close()
    finfofo.close()