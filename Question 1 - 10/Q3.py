dictionary = {
    'name': "Debdut Goswami",
    'dept': "CSE",
    'subject': ["Python", "Data Structure", "Computer Organisation"]
}

key = input('enter the key to be checked - ')

check = dictionary.get(key, None)

if(check): print("exist")
else: print("doesn't exist")