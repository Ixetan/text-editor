from datetime import datetime


def saveFile(text, filename):
    f = open(filename, 'w+')
    f.write(text)
    f.close()

def openFile(fileename):
    f = open(fileename, 'r')
    lines = f.readlines()
    return ''.join(lines)

def parseText(text):
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')
        for j in range(len(lines[i])):
            if lines[i][j] in ['if', 'from', 'import', 'input', 'for', 'print', 'int', 'str', 'def', 'return', 'else', 'elif', 'while', 'try', 'case', 'class', 'break', 'match', 'assert']:
                lines[i][j] = {"text": lines[i][j], "color": "keyword"}
            else:
                lines[i][j] = {"text": lines[i][j], "color": "black"}
                
                
    return lines