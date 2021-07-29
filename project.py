import random

chances = 0
number = random.randint(1, 9)

print('Number Guessing Game')
print('Guess a number (beteween 1 and 9)')

while chances < 5:
    guess=int(input('Enter Your Guess:- '))

    if guess == number:

        print("Congrats You Won!!!")
        break

    if guess < number:
        print('Your Guess was Too low, Guess a Number Higher than',guess)

    if guess > number:
        print('Your Guess was Too High, Guess a Number Lower than',guess)
        
    chances = chances+1

if chances > 5:
    print("Oops Try Again You Failed Dumbo")
