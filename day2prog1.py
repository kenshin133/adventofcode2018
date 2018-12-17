##creating a checksum of all the boxes in santa's warehouse
##data contains 250 inputs and we are checking if each letter contains two identical letters or three identical letters or both and adding those sums together.


def checksum(id):
    length = len(id)
    #for every char
    sum = 0
    foundthree = 0
    foundtwo = 0
    for char in id:
        found = 0
        i = 0
        while i < length - 1:
            if char == id[i]:
                found = found + 1
#                print(str(found) + " " + str(char) + "'s")
                i = i + 1
            else:
                i = i + 1
        if found == 3 and foundthree == 0:
            print("found three "+char)
            foundthree = 1
        elif found == 2 and foundtwo == 0:
            print("found two " + char)
            print("adding to triples : " +str(triples))
            foundtwo = 1
    sum=foundthree + foundtwo
    print("the checksum for " + str(id) + "is " + str(sum))
    return(foundtwo, foundthree)







##initial idea is to have a function that takes in the line, identifies if it matches none, one, or both criteria, and then outputs a checksum of 0-2 based on matches. for efficiency it should check if a match has been found before evaling the if statements to avoid checking for 2x match after finding one
##TODO: read in file
boxes = open("day2input",'r')
##TODO: loop through lines
boxids = boxes.readlines()
#keep track of the total checksum
checksumTotal = 0
triples = 0
doubles = 0
for ids in boxids:
    #list of previous chars catagorized into a list of lists
    tally = []
    double = 0
    #has it hit three?
    triple = 0
    print("triples : " + str(triples))
#    for chars in ids:
    tempdoubles,temptriples = checksum(ids)
    triples = triples+temptriples
    doubles = doubles + tempdoubles
checksumTotal = triples * doubles
print("the total should be 12")
print("the total is " + str(checksumTotal))
##TODO: evaluate lines char for char against the rest of the line.
