import random

# Random number
random_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
score = int(100)

while guess != random_number:
    if guess > random_number:
        print("You guessed to high, Try again!")
        guess = int(input("Guess a number between 1 and 100: "))
    elif guess < random_number:
        print("You guessed to low, Try again!")
        guess = int(input("Guess a number between 1 and 100: "))

if guess == random_number:
    print("You guessed it!")

#TODO add scoring sytem
#TODO add leaderbord
#TODO add different hints