# -*- coding: utf-8 -*-

from sys import argv

script, file = argv

txt = open(file)

print(txt.read())

file2 = input("Input file name again : ")

txt2 = open(file2)

print(txt2.read())
