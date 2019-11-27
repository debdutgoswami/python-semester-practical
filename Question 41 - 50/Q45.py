c = 0

with open(r'Question 41 - 50/file.txt', 'r') as lines:
    for line in lines:
        words = line.split()
        c += len(words)

print("number of words in the file: ", c)