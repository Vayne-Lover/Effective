# -*- coding: utf-8 -*-

def remainder(number,divisor):
  return number % divisor

if __name__=="__main__":
  print(remainder(20,7))
  print(remainder(20,divisor=7))
  print(remainder(number=20,divisor=7))
  print(remainder(divisor=7,number=20))
