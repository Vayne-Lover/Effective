#!/usr/local/bin/python
v={'red':['5'],'green':[''],'blue':['0']}
print v

red=v.get('red',[''])[0] or 0
print red

blue=v.get('blue',[''])
blue=int(blue[0]) if blue[0] else 0 
print blue

def get_first_value(v,k,default=0):
  found=v.get(k,[''])
  if found[0]:
    fount=int(found[0])
  else:
    found=default
  return found
print get_first_value(v,'green')
