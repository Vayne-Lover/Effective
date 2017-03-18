# -*- codig: utf-8 -*-

def log(mes,v):
  if not v:
    print(mes)
  else:
    v_str=",".join(str(i) for i in v)
    print(mes,v_str)

log("Hi!",[2,4])

log("Ha!",[])
