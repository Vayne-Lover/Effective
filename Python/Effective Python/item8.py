#!/usr/local/bin/python
matrix=[[1,2,3],[4,5,6],[7,8,9]]
x1=[x for row in matrix for x in row]
print x1
#x2=[x for i in sublist for sublist in matrix]
#print x2
y1=[y for y in row for row in matrix]
print y1
y2=[[y for y in row] for row in matrix]
print y2
squared=[[x**2 for x in row] for row in matrix]
print squared
a=[1,2,3,4,5,6,7,8,9,10]
b=[x for x in a if x>4 if x%2==0]
c=[x for x in a if x>4 and x%2==0]
print b
print c
f=[[x for x in row if x%3==0] for row in matrix if sum(row)>=9]
print f
