# This program draw game boards that look like this:
#
#            --- --- ---
#           |   |   |   |
#            --- --- ---
#           |   |   |   |
#            --- --- ---
#           |   |   |   |
#            --- --- ---
#
# Created by Eric

def DrawHorizonLine(num):
    print " " + ("--- " * num)

def DrawVerticalLine(num):
    print "|" + ("   |" * num)

def main():
    # Get game board size
    Number = int(raw_input("Please enter the size of game board: "))

    # Draw game board
    for index in range(0, Number):
        DrawHorizonLine(Number)
        DrawVerticalLine(Number)
    DrawHorizonLine(Number)

if __name__ == "__main__":
    main()
