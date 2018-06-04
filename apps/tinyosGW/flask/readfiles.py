#!/usr/bin/python

import os

FILE_PATH = "./server"

def chkEth(line):
    if line[0] == " ": return False
    return True

def isInt(str):
    try:
        int(str)
        return True
    except:
        return False

def splitEth(line):
    return line.split(" ")[0]

def isIP(line):
    if line.find('inet addr:') < 0: return False
    return True

def splitIP(line):
    #print 'splitIP : %s' % line
    dev_ip = line.split('inet addr:')[1].split(' ')[0]
    #dev_ip = line.split('inet addr:')
    #print 'dev : %s' % dev_ip
    return dev_ip

def readFile(file_name):
    res = {}
    d_res = []

    filepath = "%s/%s" % (FILE_PATH, file_name)
    f = open(filepath, "r")
    lines = f.readlines()
    for line in lines:
        if not line[0] == " " and not isInt(line[0]) and len(line) > 1:
          ifdes = splitEth(line)
          d_res.append(ifdes)
          #print ">> %s\t\t%s" % (ifdes, line)
        elif line[0] == " " and not isInt(line[0]) and len(line) > 1 and isIP(line):
          d_res.append(splitIP(line))
          #print splitIP(line)
        elif isInt(line[0]):
          d_res.append("IP")
          d_res.append(line.replace('\n',''))
          #print ">> %s" % (line)
        else:
          pass
    f.close()
    res[file_name.replace('.txt','')] = d_res
    return res

def getFile():
    file_res = []
    file_lists = os.listdir(FILE_PATH)
    print file_lists
    for file_list in file_lists:
        res = readFile(file_list)
        file_res.append(res)
    return file_res

print getFile()
