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

class Song:
  def __init__(self,lyrics):
    self.lyrics=lyrics

  def show(self):
    for line in self.lyrics:
      print(line)

if __name__=="__main__":
  ap=Apple(20)
  ap.apple()
  ap.show()

  happy=Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
  bull=Song(["They rally around tha family",
                        "With pockets full of shells"])

  happy.show()
  bull.show()

