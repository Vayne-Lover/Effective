# -*- coding: utf-8 -*-

import os

def openFile():
    os.system('rm test.txt')
    os.system('ls -l test.txt')
    fp=open('test.txt','w')
    fp.write('Hello!')
    fp.close()
    os.system('ls -l test.txt')
    
    with open('test.txt','r') as fp:
        print(fp.read())

if __name__=="__main__":
    openFile()
