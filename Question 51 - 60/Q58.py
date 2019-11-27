import matplotlib.pyplot as plt

x = [2,6,9,1,8,10,7,5]
y = [8,3,7,1,9,5,2,6]

plt.scatter(x,y)
plt.grid(axis='both')
plt.xlabel('x')
plt.ylabel('y')
plt.show()