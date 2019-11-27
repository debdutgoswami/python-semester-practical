l = []

with open(r'Question 11 - 20/file.txt', 'r') as lines:
    for line in lines:
        l.append(line.rstrip())

print(l)