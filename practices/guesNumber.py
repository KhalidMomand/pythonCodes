#!/usrs/bin/env python3

'''
Task:
Task a program to prompt user for guesing a number

'''


#let's  see the solution

import random


secretNumber = random.randint(1, 20)

print(" I am guessing of a number between (1, 20) let's guess the number")

for guessTaken in range(1, 7):
   print("Take a guess.")
   guess = int(input())

   if guess < secretNumber:
      print("Your guess is too low")
   elif guess > secretNumber:
      print("Your guess is too high.")
   else:
      break

if guess == secretNumber:
   print("Good Job! you guessed my number in {} guesses.".format(guessTaken))
else:
   print('Nope, The number I was thinking of was {}.'.format(secretNumber))


