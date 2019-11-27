def sumofdigit(n: int) -> int:
    s=0
    for i in str(n):
        s += int(i)

    return s

dictionary = {
    1: 789,
    2: 526,
    3: 4578
}

for key, value in dictionary.items():
    dictionary[key] = sumofdigit(value)

[print(key, value) for key, value in dictionary.items()]