#!/usr/local/bin/python

def sort_priority(num,pro):
  res=num[:]
  def helper(x):
    if x in pro:
      return (0,x)
    return (1,x)
  res.sort(key=helper)
  return res

numbers=[2,5,7,4,1,3,8,6]
group=[2,4,8]

print sort_priority(numbers,group)
