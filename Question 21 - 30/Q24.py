d1 = {
    1: 56,
    2: 78
}

d2 = {
    2:89,
    5: 56
}

for key in d1.keys():
    d1[key] = d2.get(key,0) + d1[key]

print(d1)