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

class Parents():

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Children(Parents):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Children, self).altered()
        print("CHILD, AFTER PARENT altered()")

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

  dad = Parents()
  son = Children()

  dad.implicit()
  son.implicit()

  dad.override()
  son.override()

  dad.altered()
  son.altered()
