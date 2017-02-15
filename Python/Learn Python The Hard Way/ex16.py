# -*- coding: utf-8 -*-

from sys import argv

script,file=argv

file1=open(file,"w")

file1.truncate()

promot="Please input the words."

line1=input(promot)

line2=input(promot)

line3=input(promot)

file1.write(line1)

file1.write("\n")

file1.write(line2)

file1.write("\n")

file1.write(line3)

file1.write("\n")

print("Finished!")

file1.close()

file2=open(file)

print(file2.read())

file2.close()
