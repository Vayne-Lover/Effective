#!/usr/local/bin/python

def func(a,b):
  try :
    print a*b
  except Exception , e:
    print e
  else:
    print 'Finished'
  finally:
    print 'End'

if __name__=='__main__':
  func(1,2)
