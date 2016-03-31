# This program randomly generate password for user
#
# Created by Eric

import random

WeakPasswordList = ["p@ssw0rd", "hell0", "H!2O16"]

# Generate password for weak/strong password
def GenPassword(Mode = "strong"):
    Password = ""
    if Mode == "strong":
        for i in range(1, 9):
            Password += chr(random.randint(33, 127))
        return Password
    else:
        Password += WeakPasswordList[random.randint(0, 2)]
        return Password

# Get input mode from user
String = raw_input("Please input your password mode (Strong, Weak): ")

# Check password mode and begin to generate
if String.lower() == "strong":
    print GenPassword()
elif String.lower() == "weak":
    print GenPassword("weak")
