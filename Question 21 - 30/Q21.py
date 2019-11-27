c = 0

with open(r'Question 21 - 30/file.txt', 'r') as lines:

    for line in lines:
        for character in line:
            if character in "AEIOUaeiou":
                c += 1

print(c)