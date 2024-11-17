from datetime import datetime

def saveFile(text, filename):
    f = open(filename, 'w+')
    f.write(text)
    f.close()

def openFile(fileename):
    f = open(fileename, 'r')
    lines = f.readlines()
    return ''.join(lines)