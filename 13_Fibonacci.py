# This program that asks the user how many Fibonnaci numbers to generate and then generates them.
#
# Created by Eric

# Generate Fibonacci number by the given number
def Fibonacci(Num):
    if Num == 0:
        return 0
    elif Num == 1:
        return 1
    else:
        return Fibonacci(Num - 1) + Fibonacci(Num - 2)

# Get input information from user
FibNumber = int(raw_input("Please input your Fibonacci number: "))

# Generate Fibonacci number
if FibNumber == 0:
    print [0]
else:
    print [Fibonacci(i) for i in range(1, FibNumber + 1)]
