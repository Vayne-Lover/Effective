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

class C:
  def func(self):
    print("Function in C")

class D(C):
  def func(self):
    print("Before D")
    super(D,self).func()
    print("After C")

if __name__=="__main__":
  dad=Parent()
  child=Child()

  dad.implicit()
  child.implicit()

  a=A()
  b=B()

  a.override()
  b.override()

  c=C()
  d=D()

  c.func()
  d.func()
