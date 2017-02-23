# -*- coding: utf-8 -*-

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

a=add(10,20)

b=sub(90,20)

c=mul(5,2)

d=div(50,25)

print(a,b,c,d)

print(add(a,sub(200,mul(5,div(10,2)))))
