dictionary1 = {
    'name': "Debdut Goswami",
    'dept': "CSE",
    'subject': ["Python", "Data Structure", "Computer Organisation"]
}

dictionary2 = {
    'semester': '3rd'
}

mergedDictionary = {}

for key in dictionary1.keys():
    mergedDictionary[key] = dictionary1[key]

for key in dictionary2.keys():
    mergedDictionary[key] = dictionary2[key]

for key, value in mergedDictionary.items():
    print(key,": ",value)