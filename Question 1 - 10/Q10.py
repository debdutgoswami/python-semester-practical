def strong(num: int) -> bool:
    s = 0
    s = sum([i for i in range(1,num) if(num%i == 0)])

    if(s==num): return True
    return False

n = int(input("enter the number: "))

if(strong(n)): print("Perfect")
else: print("not Perfect")