t = ""

with open(r'Question 31 - 40/file.txt', 'r') as file1:

    for line in file1.readlines():
        t += " "+line.rstrip()

with open(r'Question 31 - 40/file.txt','w') as f:

    f.write(t)


