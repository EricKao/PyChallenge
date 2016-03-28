__author__ = "Eric"

# Import random module
import random

# Define variables
a = []
b = []
c = set()

# Random generate 2 lists
random.seed()

for element in range(1, 11):
    a.append(random.randint(1, 101))

for element in range(1, 13):
    b.append(random.randint(1, 101))

# Find intersection into a set
c = {element for element in a if element in b}

# Print final result
print c
