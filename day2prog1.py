##creating a checksum of all the boxes in santa's warehouse
##data contains 250 inputs and we are checking if each letter contains two identical letters or three identical letters or both and adding those sums together.


def checksum(id):
    length = len(id)
    i = 0
    #for every char
    cur = id[i]
    foundtwo = 0
    foundthree = 0
    sum = 0
    while sum < 2:
        for char in id:
            cur = char
            








    #sum = 0
    ##if we find that the tally contains matches of two or thee we quit with an output of 2,
    ##otherwise we continue to the end and report 1 or 0
    ##has it hit two?
    #print(id)
    #while sum < 2:

    #    tally = []
    #    for char in id:
    #        for char2 in id:
    #            if char == char2:
    #                print("found a match" + char + char2)
    #        #if len(tally) == 0:
    #        #    tally = [char]
    #        #elif char == tally[i]:
    #        #    print("we matched a: " + char)
    #        #    if
    #        #else:
    #        #    print("not matches")
    #        #    temp = [char]
    #        #    tally = tally + temp
    #        #    i = i + 1
    #print("end of loop tally" + str(tally))


    #        #print(char)
    return(sum)


##initial idea is to have a function that takes in the line, identifies if it matches none, one, or both criteria, and then outputs a checksum of 0-2 based on matches. for efficiency it should check if a match has been found before evaling the if statements to avoid checking for 2x match after finding one
##TODO: read in file
boxes = open("day2input.sample",'r')
##TODO: loop through lines
boxids = boxes.readlines()
#keep track of the total checksum
checksumTotal = 0


for ids in boxids:
    #list of previous chars catagorized into a list of lists
    tally = []
    checksum(ids)
    double = 0
    #has it hit three?
    triple = 0
#    for chars in ids:

##TODO: evaluate lines char for char against the rest of the line.
