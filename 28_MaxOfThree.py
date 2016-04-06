# This program implement a function that takes as input three variables,
# and returns the largest of the three.
#
# Created by Eric


def GetMaxNum(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            return num1
    else:
        if num2 >= num3:
            return num2
    return num3

def main():
    # Get the search number from user
    Num1 = int(raw_input("Please enter 1st number: "))
    Num2 = int(raw_input("Please enter 2nd number: "))
    Num3 = int(raw_input("Please enter 3rd number: "))
    print GetMaxNum(Num1, Num2, Num3)

if __name__ == "__main__":
    main()
