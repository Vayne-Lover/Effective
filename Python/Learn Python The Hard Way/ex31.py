# -*- coding: utf-8 -*-

print("Choose 1 or 2 !")

answer = input("> ")

if answer == "1" :
  
  print("Choose a or b !")
  
  answer1 = input("> ")

  if answer1 == "a" :
    
    print("You choose {0} !".format(answer1))

  elif answer1 == "b" :
    
    print("You choose {0} !".format(answer1))

  else :
    print("You choose {0} !".format(answer1))

else :

  print("Choose c or d !")
  
  answer2 = input("> ")

  if answer2 == "c" or answer2 == "d" :
    
    print("You choose {0} !".format(answer2))

  else :
    print("You choose {0} !".format(answer2))
