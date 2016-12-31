#!/usr/local/bin/python
x=['a','b','c','d','e','f']
print x[:20]
print x[:4]
print x[-3:]
print x[1:-1]
y=x[:]
y[1:]='A'
print y
