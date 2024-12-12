import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])

youStr = input("Enter you choice: ")
yourDict = { "s" : 1, "w" : -1, "g" : 0}
reverseDict = {1: "Snake", -1: "Water", 0 : "Gun"}

you = yourDict[youStr]

print(f"You Chose {reverseDict[you]} Computer Chose {reverseDict[computer]}")

if(computer == you):
  print("It's a tie!")

else:
  if(computer == -1 and you == 1):
    print("You WIN!")

  elif(computer == 1 and you == -1):
    print("You LOSE!")

  elif(computer == 0 and you == -1):
    print("You Win!")

  elif(computer == 0 and you == 1):
    print("You LOSE!")

  elif(computer == -1 and you == 0):
    print("You LOSE!")

  elif(computer == 1 and you == 0):
    print("You WIN!")
