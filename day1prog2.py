## this one is to find the first time a match is made between an old sum and a new some.

#load file full of adjustments
##setup
cnt = 1
frequency = 0
match = 0
# this should keep track of previous totals
frequencies=[]
##TODO change this to a while not matched where it will loop through the list
## multiple times until it finds a match
while match == 0:
    with open('day1inputtimes11') as f:
        line = f.readline()
        while line:
            ##add the adjustment to the frequency, this could be one statement but i made it two
            frequency = frequency + int(line)
            for fre in frequencies:
                if str(fre) == str(frequency):
                    match = fre
                    print(match)
                    exit()
            frequencies=frequencies + [frequency]
#            print("checking " + str(len(frequencies)) + "vectors")
            if len(frequencies) % 10000 == 0:
                if len(frequencies) % 50000 == 0:
                    print(frequencies)
                print("checking " + str(len(frequencies)) + "vectors")
            cnt += 1
            line = f.readline()
        #print the sum of all
        cnt = 1
print(frequency)
print("match is " + str(match))
