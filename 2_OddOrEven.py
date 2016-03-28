# Get input number from user
Number = int(raw_input("Please input the number: "))

# Check number is odd or even
if Number % 4 == 0:
    print "This number is a multiple of 4!"
elif Number % 2 == 0:
    print "This is a even number!"
else:
    print "This ia a odd number!"
