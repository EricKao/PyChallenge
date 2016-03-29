# Created by Eric Kao

import random

def GenerateRandomNumber():
    # Random generate number between 1 ~ 9
    return random.randint(1, 9)

# Define variables
TotalGuessNumber = 0

# Generate a random number
RandomNumber = GenerateRandomNumber()

while True:
    # Get input information from user
    Input = raw_input("Please enter guess a number: ")
    Input = Input.lower()
    if Input == "exit":
        break

    TotalGuessNumber += 1
    Input = int(Input)
    if Input == RandomNumber:
        print "You guess the correct number, you guess %s time(s)!" % TotalGuessNumber
        break
    else:
        print "Oh, you entered the wrong number. Please enter again!"
