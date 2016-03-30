# This program that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates
#
# Created by Eric

def RemoveDuplicate1(input):
    return list(set(input))

def RemoveDuplicate2(input):
    newlist = []
    for i in input:
        if i not in newlist:
            newlist.append(i)
    return newlist

List = [1, 1, 2, 3, 4, 4, 4, 5, 5, 6]

print "Method by using set: %s" % RemoveDuplicate1(List)
print "Method by using set: {}".format(RemoveDuplicate2(List))
