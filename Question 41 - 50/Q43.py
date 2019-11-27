import math

def isPrime(n: int) -> bool:
    for i in range(2,n//2):
        if n%i==0: return False
    return True

def primefactors(n: int) -> list:
    l = []
    c = 1
    while(c<n):
        if n%c == 0 and isPrime(c): l.append(c)
        c += 1

    return l

n = int(input())
print(primefactors(n))