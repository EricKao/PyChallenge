# Created by Eric

import random

# Random generate 2 lists
a = random.sample(range(100), 10)
b = random.sample(range(100), 15)

# Generate a set by using list comprehensions
print [result for result in set(a) if result in b]

