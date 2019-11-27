import matplotlib.pyplot as plt

dictionary = {
    "student 1": 45,
    "student 2": 78,
    "student 3": 50,
    "student 4": 90
}


plt.bar(list(dictionary.keys()), list(dictionary.values()))
plt.title("student marks")
plt.show()