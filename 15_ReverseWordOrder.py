# This program that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
#
# Created by Eric

# Get input string from user
String = raw_input("Please input your string: ")

# Print result in reverse way
print " ".join(String.split()[::-1])

