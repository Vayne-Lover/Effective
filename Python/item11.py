#!/usr/local/bin/python
names=['Cecilia','Lise','Marie']
letters=[len(n) for n in names]
#print letters

longest=None
max_len=0
index=0

#for i in range(len(names)):
#  length=len(names[i])
#  if length>max_len:
#      index=i
#      max_len=length
#print names[index],max_len

#for i,name in enumerate(names):
#  if len(name)>max_len:
#    index=i
#    max_len=len(name)
#print names[index],max_len

for name,letter in zip(names,letters):
  if letter>max_len:
    longest=name
    max_len=letter
print longest,max_len
