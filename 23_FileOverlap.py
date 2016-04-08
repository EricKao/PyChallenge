# Given two .txt files that have lists of numbers in them
# This program finds the numbers that are overlapping.
#
# Created by Eric

# Find overlap in two lists
def GetOverlap(listOne, listTwo):
    return [item for item in listOne if item in listTwo]

# Main function
def main():
    # Open file and split text line by line
    with open(r'Reference/primenumbers.txt', 'r') as PrimeNum:
        PrimeText = PrimeNum.read()
        PrimeText = PrimeText.splitlines()

    # Open file and split text line by line
    with open(r'Reference/happynumbers.txt', 'r') as HappyNum:
        HappyText = HappyNum.read()
        HappyText = HappyText.splitlines()

    # Get overlap
    print GetOverlap(PrimeText, HappyText)

if __name__ == "__main__":
    main()
