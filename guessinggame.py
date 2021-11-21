#!/user/bin/env python
"""This is a small game that will ask you to gues a number"""

#Import modules
import random
import json

###Functions###
def write_dict_to_json(scoreboard, filename):
    """Write data to file"""
    with open(filename, "w+", encoding="utf-8") as filename:
        json.dump(scoreboard, filename)

def read_file(filename):
    """Read data from file"""
    with open(filename, encoding="utf-8") as file:
        file.read(filename)
    return file

def update_scoreboard(scoreboard, score, username):
    """Updates scoreboard"""
    scoreboard.update({username: score,})
    scoreboard_sorted = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)
    return scoreboard, scoreboard_sorted

def yes_or_no(question):
    """Asks yes or no question"""
    reply = input(question)
    while reply != 'y'  or reply != 'n':
        if reply == 'y':
            return True
        if reply == 'n':
            return False
        reply = input(question)

def scoring_function(score):
    """Update the score"""
    scoresubstraction = random.randint(0, 10)
    score = score -scoresubstraction
    return score, scoresubstraction

def high_or_low(guess, score, random_number, random_number_low, random_number_high):
    """Checks if the guess is higher or lower"""
    if guess > random_number:
        print("You guessed to high, Try again!")
        score, scoresubstraction = scoring_function(score)
        print(f"Your score is now {score} you lost {scoresubstraction} points")
        guess = int(input(f"Guess a number between {random_number_low} and {random_number_high}: "))
    elif guess < random_number:
        print("You guessed to low, Try again!")
        score, scoresubstraction = scoring_function(score)
        print(f"Your score is now {score} you lost {scoresubstraction} points")
        guess = int(input(f"Guess a number between {random_number_low} and {random_number_high}: "))
    return guess , score

def main(scoreboard, random_number_low = 1, random_number_high = 5, score = 100):
    """Main function"""
    #temp variables
    scoreboard_filename = 'scoreboard.json'

    #intro to the game
    print("In this game you will be asked to gues a number between"
    f" {random_number_low} and {random_number_high}.\nYou will start with a score and every time"
    " you gues wrong you will lose between 0 and 10 points. \nGood luck!")

    #get Initial information
    username = str(input("please input your name for the leaderboard: "))
    guess = int(input(f"Guess a number between {random_number_low} and {random_number_high}: "))
    random_number = random.randint(random_number_low, random_number_high)

    #loop through guesses
    while guess != random_number:
        guess, score = high_or_low(guess, score, random_number,
        random_number_low, random_number_high)
    if guess == random_number:
        scoreboard, scoreboard_sorted = update_scoreboard(scoreboard, score, username)
        print(f"You guessed it! Your score was: {score}\nThe scoreboard is now:")
        for i in scoreboard_sorted:
            print(i[0], i[1])

        if yes_or_no("Do you want to play again? (y/n)") is True:
            main(scoreboard)
        if yes_or_no("Do you want to save the scoreboard? (y/n)") is True:
            write_dict_to_json(scoreboard, scoreboard_filename)


#call main
if __name__ == '__main__':
    main(scoreboard = {},)
