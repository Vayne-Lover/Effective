# -*- coding: utf-8 -*-

things = "Apples Oranges Crows Telephone Light Sugar"

a=things.split(" ")

more=["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(a) != 10 :
  next=more.pop()
  a.append(next)

print(a)

print(more[0])

print(more[-1])

print(" ".join(more))

print("#".join(more[1:2]))


