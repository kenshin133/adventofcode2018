##creating a checksum of all the boxes in santa's warehouse
##data contains 250 inputs and we are checking if each letter contains two identical letters or three identical letters or both and adding those sums together.
def checksum(tally, id):
    sum = 0
    #if we find that the tally contains matches of two or thee we quit with an output of 2,
    #otherwise we continue to the end and report 1 or 0
    #has it hit two?
    for char in id:
        print(id)
    return(sum)
##initial idea is to have a function that takes in the line, identifies if it matches none, one, or both criteria, and then outputs a checksum of 0-2 based on matches. for efficiency it should check if a match has been found before evaling the if statements to avoid checking for 2x match after finding one
##TODO: read in file
boxes = open("day2input.sample",'r')
##TODO: loop through lines
boxids = boxids.readlines()
#keep track of the total checksum
checksumTotal = 0
for ids in boxids:
    #list of previous chars catagorized into a list of lists
    tally = []
    print(checksum(tally, id))
    double = 0
    #has it hit three?
    triple = 0
#    for chars in ids:

##TODO: evaluate lines char for char against the rest of the line.
