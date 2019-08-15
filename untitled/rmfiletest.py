import os
import sys
import configparser

path = 'C:/untitled/un/宇纳复兴6号私募证券投资基金/aaaa.txt'
#传入文件名及路径，删除文件
def rmfile(filepath):
    try:
        os.remove(filepath)
        print("%s 删除完成"%filepath)
    except FileNotFoundError:
        print("%s 文件不存在"%filepath)
if __name__ == '__main__':
    curr = os.path.dirname(os.path.realpath(__file__))
    configfile = os.path.join(curr, 'config.ini')
    conf = configparser.ConfigParser()
    conf.read(configfile)
    logfilename = conf.get('path', 'logfile')
    logfile = os.path.join(curr, logfilename)
    savestdout = sys.stdout
    with open(logfile, 'a+', encoding='utf-8') as f:
        sys.stdout = f
        rmfile(path)
    sys.stdout = savestdout








