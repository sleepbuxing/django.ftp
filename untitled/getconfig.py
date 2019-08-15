import configparser
import os
curr = os.path.dirname(os.path.realpath(__file__))
configpath = os.path.join(curr, 'config.ini')


conf = configparser.ConfigParser()
conf.read(configpath)
aa = conf.get('downftp', 'server')
bb = conf.get('upftpone', 'server')
sections = conf.sections()
for section in sections:
    if 'upftp' in section:
        aa = conf.get(section,'server')
        print(aa)

