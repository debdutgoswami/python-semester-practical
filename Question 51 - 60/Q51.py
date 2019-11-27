def count(s: str)->int:
    c = 0
    for i in s:
        c += 1
    return c

s = input("enter the string - ")

print("the length of the string is ", count(s))
