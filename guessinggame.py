#Import modules
import random

#initiate paramaters
random_number_low = int(1)
random_number_high = int(10)
score = int(100)


###Functions###

#yes or no function
def yes_or_no(question):
    reply = str(input(question, " Do you want to play again (y/n)" ))
    while reply == 'y'  or reply == 'n':
        if reply == 'y':
            return True
        if reply == 'n':
            return False 
        reply = str(input(question, " Do you want to play again (y/n)" ))

#Scoring function
def scoring_function(score):
    scoresubstraction = random.randint(0, 10)
    score = score -scoresubstraction
    return score, scoresubstraction

#higher or lower function
def high_Or_Low(guess, score, random_number):
    if guess > random_number:
        print("You guessed to high, Try again!")
        score, scoresubstraction = scoring_function(score)
        print("Your score is now ", score, " you lost " , scoresubstraction, " points" )
        guess = int(input("Guess a number between 1 and 100: "))
    elif guess < random_number:
        print("You guessed to low, Try again!")
        score, scoresubstraction = scoring_function(score)
        print("Your score is now ", score, " you lost " , scoresubstraction, " points" )
        guess = int(input("Guess a number between 1 and 100: "))     
    return guess , score


#main function
def main(random_number_low, random_number_high, score):
    #intro to the game
    print("In this game you will be asked to gues a number between ", random_number_low, " and ", random_number_high, ".\nYou will start with a score and everytime you gues wrong you will lose between 0 and 10 points. \nGood luck!")
    #get Initial information
    username = str(input("please input your name for the leaderboard: "))
    guess = int(input("Guess a number between 1 and 100: "))
    random_number = random.randint(random_number_low, random_number_high)

    #loop through guesses
    while guess != random_number:
        guess, score = high_Or_Low(guess, score, random_number)
    if guess == random_number:
        print("You guessed it! Your score was: ", score)

    # if yes_or_no("Do you want to play again") == True:
    #     score = int(100)
    #     main(random_number_low, random_number_high, score)

#call main
main(random_number_low, random_number_high, score)

#TODO Play game again
#TODO add leaderbord
#TODO add different hints