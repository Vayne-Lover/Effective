#!/usr/local/bin/python
def normalize(numbers):
  total=sum(numbers)
  result=[]
  for v in numbers:
    percent=100*v/total
    result.append(percent)
  return result

visits=[15,35,80]
percentages=normalize(visits)
print(percentages)
