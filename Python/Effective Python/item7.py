#!/usr/local/bin/python
a=[1,2,3,4,5,6,7,8,9]
squares=[x**2 for x in a]
print squares
s=map(lambda x:x**2,a)
print s
even_squares=[x**2 for x in a if x%2==0]
print even_squares
alt=map(lambda x:x**2,filter(lambda x:x%2==0,a))
print alt
chile={'a':1,'bb':2,'ccc':3}
rank={rank:name for name,rank in chile.items()}
print rank
len_set={len(name) for name in rank.values()}
print len_set
