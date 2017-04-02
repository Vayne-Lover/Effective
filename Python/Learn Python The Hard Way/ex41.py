# -*- coding: utf-8 -*-

import random
from urllib import urlopen
from sys import argv

WORD_URL = "http://learncodethehardway.org/words.txt"
words=[]

if argv[1]=="english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for line in urlopen(WORD_URL).readlines():
  words.append(line)

print(words)
