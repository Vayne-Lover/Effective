# -*- coding: utf-8 -*-

def sort_priority(num,pro):
  res=num[:]
  def helper(x):
    if x in pro:
      return (0,x)
    return (1,x)
  res.sort(key=helper)
  return res

def sort_priority2(num,pro):
  found=[False]
  def helper(x):
    nonlocal found
    if x in pro:
      found[0]=True
      return (0,x)
    return (1,x)
  num.sort(key=helper)
  return found

def sort_priority3(num,pro):
  found=False
  def helper(x):
    nonlocal found
    if x in pro:
      found=True
      return (0,x)
    return (1,x)
  num.sort(key=helper)
  return found

if __name__=='__main__':
  numbers=[2,5,7,4,1,3,8,6]
  group=[2,4,8]

  print(sort_priority(numbers,group))
  print(numbers)
  print(sort_priority2(numbers,group))
  print(numbers)
  print(sort_priority3(numbers,group))
  print(numbers)
