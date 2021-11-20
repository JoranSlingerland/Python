#Import modules
import random

#initiate paramaters
random_number = random.randint(1, 100)
score = int(100)

#Scoring function
def scoringfunction(score):
    scoresubstraction = random.randint(0, 10)
    score = score -scoresubstraction
    return score, scoresubstraction

#main function
def main(random_number, score):
#get first guess
    guess = int(input("Guess a number between 1 and 100: "))

    #loop through guesses
    while guess != random_number:
        if guess > random_number:
            print("You guessed to high, Try again!")
            score, scoresubstraction = scoringfunction(score)
            print("Your score is now ", score, " you lost " , scoresubstraction, " points" )
            guess = int(input("Guess a number between 1 and 100: "))
        elif guess < random_number:
            print("You guessed to low, Try again!")
            score, scoresubstraction = scoringfunction(score)
            print("Your score is now ", score, " you lost " , scoresubstraction, " points" )
            guess = int(input("Guess a number between 1 and 100: "))
    if guess == random_number:
        print("You guessed it! Your score was: ", score)

#call main
main(random_number, score)

#TODO Everything is a module now
#TODO add leaderbord
#TODO add different hints