# -*- coding: utf-8 -*-

class Animal:
    pass

class Dog(Animal):
    def __init__(self,name):
        self.name=name

class Cat(Animal):
    def __init__(self,name):
        self.name=name

class Person:
    def __init__(self,name):
        self.name=name
        self.pet=None

class Employee(Person):
    def __init__(self,name,salary):
        super(Employee, self).__init__(name)
        self.salary=salary

if __name__=="__main__":
    dog_rover=Dog("Rover")
    cat_satan=Cat("Satan")
    mary=Person("Mary")
    mary.pet=cat_satan
    frank=Employee("Frank",200000)