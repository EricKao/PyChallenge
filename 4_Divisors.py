# Get input number and print a list of divisors
Number = int(raw_input("Please enter input number: "))
print([element for element in range(1, Number+1) if Number % element == 0])
