
import random

print("please enter  the minimum value: ")
mini = int(input())
print("please enter the maximum value: ")
maxi = int(input())

number = random.randrange(mini,maxi)


print(f"i am thinking of numbers between {mini} and {maxi}. can i guess what it is?")

guess = 0

while(guess != number):
  guess = int(input())
  if guess < number:
    print("your guess is too low ")
  elif guess > number:
    print("your guess is too high")
  else:
    break
  print("try again")

print("Congrats you guessed the number")

