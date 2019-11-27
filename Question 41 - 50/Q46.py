def factorial(n: int) -> int:
    if n<0: return None
    if n==0 or n==1: return 1
    else:
        return n*factorial(n-1)

n = int(input())

if(factorial(n)):
    print(factorial(n))
else:
    print("VALUE ERROR")