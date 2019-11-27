import math
import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0,4*math.pi+0.01,0.01)

amplitude = np.sin(time)

plt.plot(time, amplitude)
plt.title('sin')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.grid(axis='both')
plt.show()