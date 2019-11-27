import matplotlib.pyplot as plt

x = [2, 6, 9, 1]
y = [8, 3, 7, 1]

plt.plot(x,y)
plt.title('line')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(axis='both')
plt.show()