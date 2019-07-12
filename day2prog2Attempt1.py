
""" --- Part Two ---
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

Although it hasn't changed, you can still get your puzzle input. """

##Basic
##two loops, grab the first ID, and check it against all the others letter by letter. if you find a letter that differs set a variable, if two are found, fail the block and move on to the next one. eventually ending with a match or fail case.

##Test items
ids = ["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"]
##fghij and fguij are the right finderss
for i in ids:
    ##TODO check item against next items
        ##TODO check current letter of item against current letter of other item
    print(i)