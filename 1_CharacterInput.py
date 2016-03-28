# Get input information from user
Name = raw_input("Please input your name: ")
Age = int(raw_input("Please input your age: "))
RepeatNumber = int(raw_input("Please input your repeat number: "))

# Calculate the number of turn 100 years old
RemainAge = 100 - Age

# Print user name
print("Your name is " + Name)

# Repeat remain age info for 'RepeatNumber' times
print(RepeatNumber * ("Your will turn 100 years old in " + str(RemainAge) + "\n"))

