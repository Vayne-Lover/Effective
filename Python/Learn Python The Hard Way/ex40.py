# -*- coding: utf-8 -*-

stf={"apple":"I'm an apple."}
print(stf['apple'])

def apple():
  print("Apple in function!")

class Apple:
  def __init__(self,number):
    self.number=number
  
  def apple(self):
    print("Apple in class function")

  def show(self):
    print(self.number)  

if __name__=="__main__":
  ap=Apple(20)
  ap.apple()
  ap.show()
