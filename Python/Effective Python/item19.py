# -*- coding: utf-8 -*-

def remainder(number,divisor):
  return number % divisor

def flow_rate(weight,time,period=1):
  return weight/time*period

if __name__=="__main__":
  print(remainder(20,7))
  print(remainder(20,divisor=7))
  print(remainder(number=20,divisor=7))
  print(remainder(divisor=7,number=20))

  print(flow_rate(0.5,3))
  print(flow_rate(6,3,100))
