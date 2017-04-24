# -*- coding: utf-8 -*-

__author__="Vayne Lover"

class Fib(object):
  def __init__(self):
    self.fib=[1,1]

  def main(self,size=2):
    while len(self.fib)<size:
      self.fib.append(self.fib[-1]+self.fib[-2])

  def show(self):
    print(self.fib)

if __name__=="__main__":
  f=Fib()
  f.main(size=10)
  f.show()
