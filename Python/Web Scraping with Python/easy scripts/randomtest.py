# -*- coding: utf-8 -*-

__author__="Vayne Lover"

import random
import time

class Ball(object):
  def __init__(self):
    self.main()

  def main(self):
    while True:
      try:
        num=input("Please input the number of tests : ")
        num=int(num)
      except ValueError:
        print("Error!Please input a number!")
        continue
      else:
        break
    array=[0]*10
    for i in range(0,num):
      number=random.randint(1,10)
      array[number-1]+=1
    for i in range(0,10):
      print("There are {0} numbers in the array {1}.Result is {2:2f}".format(array[i],i,array[i]*1.0/num))
 
if __name__=="__main__":
  start_time=time.time()
  ball=Ball()    
  end_time=time.time()
  print("The program costs {0}".format(end_time-start_time))
