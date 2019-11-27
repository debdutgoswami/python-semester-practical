longest = ""

with open(r'Question 51 - 60/file.txt','r') as lines:

    for line in lines:
        l = line.split()
        m = max(l,key=len)
        if(len(longest)<len(m)): longest = m

print("the longest word in file is ",longest)