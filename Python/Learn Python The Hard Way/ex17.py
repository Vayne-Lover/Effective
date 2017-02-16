# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script,from_file,to_file=argv

print("You are in {0}".format(script))
print("The destiny file exists? {0}".format(exists(to_file)))

infile=open(from_file)
data=infile.read()

outfile=open(to_file,"w")
outfile.write(data)

infile.close()
outfile.close()
