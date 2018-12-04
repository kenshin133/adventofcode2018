##day1 puzzle1 of the coding advent, to help santa we have to calibrate this thing and find the frequency after all the adjustments listed in day1input

#load file full of adjustments
with open('day1input') as f:
    line = f.readline()
    ##setup
    cnt = 1
    frequency = 0

    
    while line:
        #print(int(line))
        ##add the adjustment to the frequency, this could be one statement but i made it two
        if line[0]=="-":
          frequency = frequency + int(line)
        else:
          frequency = frequency + int(line)
        #print the sum of all
        print(frequency)
        line = f.readline()
        cnt += 1
