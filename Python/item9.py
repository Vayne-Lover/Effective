#!/usr/local/bin/python
v=[len(x) for x in open('file.txt')]
print v
it=(len(x) for x in open('file.txt'))
print it
print next(it)
roots=((x,x**2) for x in it)
print next(roots)
