#!/usr/local/bin/python
from math import sqrt

def prime(n):
  try:
    if isinstance(n,int):
      if n <= 2:
        return True 
      for i in range(2,int(sqrt(n))+1):
        if n%i==0:
          return False
      return True
    else:
      return False
  except Exception , e:
    print e

if __name__=='__main__':
  for i in xrange(1,10):
    print prime(i)
