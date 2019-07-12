
""" 
--- Advent of code day 2 ---
--- Part Two ---
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)
"""
print("hello part222")
print("this is another one")

#define set
#TODO add real set file
boxids = open("day2input",'r')
##TODO: loop through lines
boxes = boxids.readlines()
#boxes = [
#    "abcde",
#    "fghij",
#    "klmno",
#    "pqrst",
#    "fguij",
#    "axcye",
#    "wvxyz"
#    ]
print(boxes)

for i in boxes:
    for other in boxes:
        if other == i:
           four = 4 
        else:
            temp = ""
            diff = 0
            for pos in range(0,len(other)):
                if diff <= 1:
                    if i[pos] == other[pos]:
                       temp = temp + other[pos] 
                    else:
                        diff = diff + 1
            if len(temp) == len(i)-1:
                print("i is " + i)
                print("other is " + other)
                print("temp is " + temp)
                #    ##The failure here is that I need to be iterating through array spaces rather than letters, this is checking letter[1] against letter [12345] of the next word and failing after two letters. we need to be checking word1[1] against word2[1]
                #    for pos2 in other:
                #        if pos == pos2:
                #            #print(i + " " + other + " " + pos + " " + pos2)
                #            temp = temp + pos
                #            if len(temp) == len(i):
                #                print("temp is " + temp)
                #        else:
                #            diff = diff + 1
                #        print(len(temp))
    #
                #        print("temp is " + temp)