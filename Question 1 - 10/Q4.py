import math

def strong(num: int) -> bool:
    num = str(num)
    s = [math.factorial(int(num[i])) for i in range(len(num))]

    if(sum(s)==int(num)): return True
    return False

n = int(input("enter the number - "))
print(strong(n))
