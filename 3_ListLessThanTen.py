# Get input number from user
Number = int(raw_input("Please input the threshold number: "))

# Initial list variables
InitList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ResultList = []


# Print elements in list that less than number
print([element for element in InitList if element < Number])
