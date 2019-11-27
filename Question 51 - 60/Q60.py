dictionary = dict()

tup = tuple([78,45,12,12,45,7])

for i in tup:
    dictionary[i] = dictionary.get(i, 0) + 1

[print(key) for key, value in dictionary.items() if value>1]
