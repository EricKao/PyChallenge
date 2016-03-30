# Created by Eric

def CheckIfPrime(Num):
    for i in range(2, Num):
        if Num % i == 0:
            return False
    return True

# Get input information from user
Number = int(raw_input("Please input your number: "))

if CheckIfPrime(Number):
    print "It's a prime number!"
else:
    print "It's not a prime number!"
