# -*- coding: utf-8 -*-

from sys import exit

def gold_room():
  print("You enter a room full of gold.")
  print("How much gold will you take?")

  answer=input("> : ")

  if answer.isdigit() :
    amount=int(answer)
  else:
    print("Die !")
    exit(0)

  if amount <= 50 :
    print("Nice!")
    exit(0)
  else:
    print("You die!")
    exit(0)

if __name__ == "__main__" :
  gold_room()
