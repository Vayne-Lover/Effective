# -*- coding: utf-8 -*-

def normalize(numbers):
  total=sum(numbers)
  result=[]
  for v in numbers:
    percent=100*v/total
    result.append(percent)
  return result

def normalize_copy(numbers):
  num=list(numbers)
  total=sum(num)
  result=[]
  for v in num:
    percent=100*v/total
    result.append(percent)
  return result


visits=[15,35,80]
print("*********")
percentages1=normalize(visits)
print(percentages1)
print("*********")
percentages2=normalize_copy(visits)
print(percentages2)
