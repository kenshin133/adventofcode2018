"""--- Day 3: No Matter How You Slice It ---
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?"""

def render(array):
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row])
    #  for row in array]))
    #print each row with a newline
    for i in fabric:
        print()
        #print each collumn with no newline
        for j in i:
            print(j, end='')
def fill(array):
    args=array.split()
#    print(args)
    wh = args[3].split("x")
#    print(wh)
    w = int(wh[0])
#    print(w)
    h = int(wh[1])
 #   print(h)
#    extract x and y and format
    xy = args[2].split(",")

#    convert x and y
    x = int(xy[0].replace(":",""))
    y = int(xy[1].replace(":",""))
#def fill(x,y,w,h):
    #fill in the fabric with a 'plan'
    #TODO use the format they give
    for g in range(0,w):
        for r in range(0,h):
            if fabric[r+y][g+x] == "X" or fabric[r+y][g+x] == "#":
                fabric[r+y][g+x] = "X"
            else:
                fabric[r+y][g+x] = '#'
def countdup(array):
    conflict=0
    for g in range(0,len(array[0])):
        for r in range(0,len(array)):
            if fabric[g][r] == "X":
                conflict=conflict+1
    print(str(conflict) + " conflicts")
def overlapping(array):
    args=array.split()
#    print(args)
    wh = args[3].split("x")
#    print(wh)
    w = int(wh[0])
#    print(w)                                                             
    h = int(wh[1])
 #   print(h)
#    extract x and y and format
    xy = args[2].split(",")

#    convert x and y
    x = int(xy[0].replace(":",""))
    y = int(xy[1].replace(":",""))
#def fill(x,y,w,h):
    #fill in the fabric with a 'plan'
    #TODO use the format they give
    overlap=0
    for g in range(0,w):
        for r in range(0,h):
            if fabric[r+y][g+x] == "X":

                overlap=1
    if overlap==0:
        print(args[0] + "had no overlap")

print("hello day3 puzzle3")

pats = open("day3input",'r')
##TODO: loop through lines
patshapes = pats.readlines()

##temp size
width = 1000
height = 1000
##input : 
input1 = "#1 @ 1,3: 4x4"
input2 = "#2 @ 3,1: 4x4"
input3 = "#3 @ 5,5: 2x2"

#array will likely be 1000inches on all sides
fabric = [["."]*width for i in range(height)]

#too much spacing but it works to show the state of the array
for pat in patshapes:
    fill(pat)
for pat in patshapes:
    overlapping(pat)
print()
#render(fabric)
print()
#print(len(fabric[0]))
#print(len(fabric))
countdup(fabric)
