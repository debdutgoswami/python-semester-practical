def kaprekar(n: int):
    copy = n*n

    l = [int(str(copy)[:len(str(copy))//2]),int(str(copy)[len(str(copy))//2:])]
    copy = sum(l)

    if(copy==n):
        print("Kaprekar Number")
    else:
        print("Not Kaprekar Number")

n = int(input())
kaprekar(n)