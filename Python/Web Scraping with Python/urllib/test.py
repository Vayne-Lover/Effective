# -*- coding: utf-8 -*-

import urllib.request

def clear():
    time.sleep(3)
    OS=platform.system()
    if (OS==u"Windows"):
        os.system("cls")
    else:
        os.system("clear")

def link():
    url="http://www.baidu.com"
    try:
        res=urllib.request.urlopen(url)
    except Exception:
        print("Request Error!")
        exit()
    with open("./baidu.txt","wb") as fp:
        fp.write(res.read())
    print(res.geturl())
    print(res.getcode())
    print(res.info())

if __name__=="__main__":
    link()
