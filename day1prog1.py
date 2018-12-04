with open('day1input') as f:
    line = f.readline()
    cnt = 1
    while line:
        print(line)
        if line[0]=="-":
          print("NEGATIVE")
        else:
          print("POSITIVE")
        line = f.readline()
        cnt += 1
