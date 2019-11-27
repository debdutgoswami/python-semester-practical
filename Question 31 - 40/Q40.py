import matplotlib.pyplot as plt

x = [70, 20, 10]

plt.pie(x)
plt.legend({1999: 70, 1998: 20, 2000: 10})
plt.title("Students birth year")
plt.show()