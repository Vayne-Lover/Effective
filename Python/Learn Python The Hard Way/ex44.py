# -*- coding:utf-8 -*-

class Parent:
  def implicit(self):
    print("Parent's function")

class Child(Parent):
  pass

class A:
  def override(self):
    print("A!")

class B(A):
  def override(self):
    print("B!")

if __name__=="__main__":
  dad=Parent()
  child=Child()

  dad.implicit()
  child.implicit()

  a=A()
  b=B()

  a.override()
  b.override()
