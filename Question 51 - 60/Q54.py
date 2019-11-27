dictionary = {
    'name': "Debdut Goswami",
    'dept': "CSE",
    'subject': "Python"
}


dictionary = sorted(dictionary.items(), key = lambda kv:kv[1])
print(dict(dictionary))