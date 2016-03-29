__author__ = "Eric"

while True:
    # Get input
    User1 = str(raw_input("Please User1 enter input(Rock, Scissors, Paper): "))
    User2 = str(raw_input("Please User2 enter input(Rock, Scissors, Paper): "))

    # Make input string into lowercase
    User1 = User1.lower()
    User2 = User2.lower()

    # Check final result
    if User1 == User2:
        print "No one win, you both took the same!"
    elif User1 == "rock" and User2 == "scissors":
        print "User1 win!"
    elif User1 == "scissors" and User2 == "paper":
        print "User1 win!"
    elif User1 == "paper" and User2 == "rock":
        print "User1 win!"
    else:
        print "User2 win!"

    # Check if user want to play again
    while True:
        PlayAgain = str(raw_input("Do you want to play a again? "))
        PlayAgain = PlayAgain.lower()
        if PlayAgain == "y" or PlayAgain == "n":
            break

    # Exit game
    if PlayAgain == "n":
        break
