# -*- coding: utf-8 -*-

def print_two(* args):
  arg1,arg2=args
  print("{0},{1}".format(arg1,arg2))

def print_two_again(arg1,arg2):
  print("{0},{1}".format(arg1,arg2))

def print_one(arg):
  print(arg)

def print_none():
  print("None")

print_two("A","B")

print_two_again("A","B")

print_one("C")

print_none()
