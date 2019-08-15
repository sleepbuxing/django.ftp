import os
import configparser

def absolufile(confname,conflabel, confkey):
    current = os.path.dirname(os.path.realpath(__file__))
    conf = configparser.ConfigParser()
    conffile = os.path.join(current, confname)
    conf.read(conffile)
    filename = conf.get(conflabel, confkey)
    absolupath = os.path.join(current, filename)
    return absolupath