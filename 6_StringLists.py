__author__ = "Eric"

# Get input
Str = raw_input("Please enter input string: ")

# Filter ",", "!", " ", ";", "." symbols
Str = Str.replace(",", "")
Str = Str.replace("!", "")
Str = Str.replace(" ", "")
Str = Str.replace(";", "")
Str = Str.replace(".", "")

# Male str to all lowercase letters
Str = Str.lower()

# Check palindrome
for i in range(0, len(Str)/2):
    if Str[i] != Str[-1 - i]:
        print "Not a palindrome!"
        exit()

# Print result
print "It's a palindrome!"

