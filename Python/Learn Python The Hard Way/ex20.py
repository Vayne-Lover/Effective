# -*- coding: utf-8 -*-

from sys import argv

script,file=argv

def print_all(f):
  print f.read()

def rewind(f):
  f.seek(0)

def print_line(count,f):
  print count,f.readline()

currentFile=open(file)

print("Print the whole file!")

print_all(currentFile)

print("Back to start!")

rewind(currentFile)

print("Print each line!")

count=1

print_line(count,currentFile)

count+=1

print_line(count,currentFile)

count+=1

print_line(count,currentFile)
