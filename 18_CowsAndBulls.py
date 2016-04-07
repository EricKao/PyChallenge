# This program that will play the "cows and bulls" game with the user.
#
# Created by Eric

import random


def main():
    NumberLength = 4
    TotalCount = 0

    print "Welcome to the Cows and Bulls Game!"

    # Generate 4-digit number
    Number = "".join(str(random.randint(1, 9)) for i in range(1, NumberLength + 1))

    while True:
        Cows = 0
        Bulls = 0
        TotalCount += 1

        # Get number
        Answer = raw_input("Please enter your answer: ")

        # Check Cows
        for index in range(0, NumberLength):
            if Number[index] == Answer[index]:
                Cows += 1

        # Check Bulls
        for indexNum in range(0, NumberLength):
            for indexAns in range(0, NumberLength):
                if (Number[indexNum] == Answer[indexAns]
                    and indexNum != indexAns
                    and Number[indexNum] == Answer[indexNum]):
                    Bulls += 1

        # Print total counts or currently status
        if Cows == NumberLength:
            print "Congratulation! Total Times: %s" % TotalCount
            break
        else:
            print "Cows: %s, Bulls: %s" % (Cows, Bulls)

if __name__ == "__main__":
    main()
