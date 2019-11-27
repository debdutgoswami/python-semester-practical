n = int(input())

with open(r'Question 51 - 60/file.txt') as f:
    c = 0
    for line in f.readlines():
        if(c>=n): break
        print(line,end="")
        c += 1