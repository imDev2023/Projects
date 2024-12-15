import random

n = random.randint(1, 20)
userInput = -1
guesses = 1

while(userInput!=n):
  userInput = int(input("Guess a number between 1 to 20: "))
  if(userInput > n):
    print("Lower number please")
    guesses+=1
  elif(userInput < n ):
    print("Higher number please")
    guesses+=1

print(f"You have guessed the number {n} in {guesses} attempts")
