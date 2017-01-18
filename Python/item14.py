#!/usr/local/bin/python
def divide1(x,y):
  try:
    return True,x/y
  except Exception , e:
    print e
    return False,None

x1=5
y1=0
x2=2
y2=1
success1,result1= divide1(x1,y1)
if not success1:
  print "Error"
else:
  print result1

success2,result2= divide1(x2,y2)
if not success2:
  print "Error"
else:
  print result2
