# This program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
#
# Created by Eric

List = [5, 10, 15, 20, 25]

def GetNewList(list):
    return [list[0], list[-1]]

print GetNewList(List)
