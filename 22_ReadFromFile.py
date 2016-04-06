# Given a .txt file that has a list of a bunch of names,
# count how many of each name there are in the file,
# and print out the results to the screen.
#
# Created by Eric

# Dictionary for name table
NameTable = {}

# Count how many name are there in the text
def CountName(Text):
    Text = Text.strip().split("\n")
    for Name in Text:
        if Name not in NameTable.keys():
            NameTable[Name] = 1
        else:
            NameTable[Name] += 1

    print NameTable

# Main function
def main():
    with open(r'Reference/nameslist.txt', 'r') as OpenFile:
        AllText = OpenFile.read()
        CountName(AllText)

if __name__ == "__main__":
    main()
