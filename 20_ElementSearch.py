# This program decides whether or not the given number is inside the list
# and returns (then prints) an appropriate boolean.
#
# Created by Eric

Element = [1, 3, 5, 30, 42, 43, 500]


def ElementBinarySearch(List, Num):
    Left = 0
    Right = len(List) - 1
    while Left <= Right:
        Middle = (Left + Right) / 2
        if Num == List[Middle]:
            return True
        elif Num > List[Middle]:
            Left = Middle + 1
        else:
            Right = Middle - 1

    return False

def ElementSearch(List, Num):
    return Num in List

def main():
    # Get the search number from user
    SearchNum = int(raw_input("Please enter search number: "))

    # Search number by using element search
    print ElementSearch(Element, SearchNum)

    # Search number by using binary search
    print ElementBinarySearch(Element, SearchNum)

if __name__ == "__main__":
    main()
