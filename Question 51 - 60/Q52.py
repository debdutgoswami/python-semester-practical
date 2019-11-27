def power(n: int, p: int)->float:
    if(p == 0):
        return 1
    elif(p<0):
        return (1/n)*power(n, p+1)
    else:
        return n*power(n,p-1)

n = int(input("enter the number: "))
p = int(input("enter the power: "))

print(power(n,p))