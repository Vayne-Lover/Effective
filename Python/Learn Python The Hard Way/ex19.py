# -*- coding: utf-8 -*-

def test(a,b):
  print("{0} ".format(a),end="")
  print("{0} ".format(b))
  print("End!")
    
c=5

d=6

test(1,3)

test(c,d)

test(1+2,3+4)
