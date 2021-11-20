#Import modules
import random

#initiate paramaters
random_number_low = int(1)
random_number_high = int(5)
score = int(100)
scoreboard = {}

###Functions###

def update_scoreboard(scoreboard, score, username):
    scoreboard.update({username: score,})
    scoreboard_sorted = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)
    return scoreboard, scoreboard_sorted

#yes or no function
def yes_or_no(question):
    reply = input(question)
    while reply != 'y'  or reply != 'n':
        if reply == 'y':
            return True
        if reply == 'n':
            return False 
        reply = input(question)

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
        guess = int(input("Guess a number between " + str(random_number_low) + " and " + str(random_number_high) + ": "))
    elif guess < random_number:
        print("You guessed to low, Try again!")
        score, scoresubstraction = scoring_function(score)
        print("Your score is now ", score, " you lost " , scoresubstraction, " points" )
        guess = int(input("Guess a number between " + str(random_number_low) + " and " + str(random_number_high) + ": "))  
    return guess , score


#main function
def main(random_number_low, random_number_high, score, scoreboard):
    #intro to the game
    print("In this game you will be asked to gues a number between ", random_number_low, " and ", random_number_high, ".\nYou will start with a score and everytime you gues wrong you will lose between 0 and 10 points. \nGood luck!")
    #get Initial information
    username = str(input("please input your name for the leaderboard: "))
    guess = int(input("Guess a number between " + str(random_number_low) + " and " + str(random_number_high) + ": "))
    random_number = random.randint(random_number_low, random_number_high)

    #loop through guesses
    while guess != random_number:
        guess, score = high_Or_Low(guess, score, random_number)
    if guess == random_number:
        scoreboard, scoreboard_sorted = update_scoreboard(scoreboard, score, username)
        print("You guessed it! Your score was: ", score, "\nThe scoreboard is now:")
        for i in scoreboard_sorted:
            print(i[0], i[1])
        
        if yes_or_no("Do you want to play again (y/n)") == True:
            score = int(100)
            main(random_number_low, random_number_high, score, scoreboard)
        

#call main
main(random_number_low, random_number_high, score, scoreboard)

#TODO make leaderboard persistent
#TODO add different hints
#TODO empty input breaks it