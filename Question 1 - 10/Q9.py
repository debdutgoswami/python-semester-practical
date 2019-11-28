d1 = {
    1: 89,
    2: 45,
    3: 235
}

d2 ={
    3: 12,
    4: 78,
    5: 65
}

d3 = dict()

for key in d1.keys():
    d3[key] = d3.get(key, 0) + d1[key]

for key in d2.keys():
    d3[key] = d3.get(key,0) + d2[key]

print(d3)