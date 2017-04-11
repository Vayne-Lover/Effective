# -*- coding:utf-8 -*-

class Parent:
  def implicit(self):
    print("Parent's function")

class Child(Parent):
  pass

if __name__=="__main__":
  dad=Parent()
  child=Child()

  dad.implicit()
  child.implicit()
