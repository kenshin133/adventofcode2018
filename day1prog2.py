## this one is to find the first time a match is made between an old sum and a new some.

#load file full of adjustments
with open('day1input') as f:
    line = f.readline()
    ##setup
    cnt = 1
    frequency = 0
    match = 0
    # this should keep track of previous totals
    frequencies=[]
    ##TODO change this to a while not matched where it will loop through the list
    ## multiple times until it finds a match
    while match == 0:
        while line:
            ##add the adjustment to the frequency, this could be one statement but i made it two
            frequency = frequency + int(line)
            frequencies=frequencies + [frequency]
            print(frequencies)
            if cnt == 10:
                match = 1
            cnt += 1
        #print the sum of all
        print(frequency)
        line = f.readline()
