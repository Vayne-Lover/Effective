# -*- coding: utf-8 -*-

a=20
b=30
c=15

if a>b:
  print("{0}>{1}".format(a,b))

if a<b:
  print("{0}<{1}".format(a,b))

if a<c:
  print("{0}<{1}".format(a,c))

if a>c:
  print("{0}>{1}".format(a,c))

c+=5

if a>=c:
  print("{0}>={1}".format(a,c))

if a<=c:
  print("{0}<={1}".format(a,c))

if a==c:
  print("{0}=={1}".format(a,c))

