# -*- coding: utf-8 -*-

__author__ = "Vayne Lover"

class PrintTable(object):
  def __init__(self):
    print("Start to print!")
    self.print99()

  def print99(self):
    for i in range(1,10):
      for j in range(1,i+1):
        print("{0} X {1} = {2:2d}".format(j,i,i*j),end=" ")
      print(u'\n')

if __name__=="__main__":
  pt=PrintTable()
