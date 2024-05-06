#Grafica3
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,10,100, endpoint=True)

y1 = 4 + 2 * np.sin(2 * x)
y2 = 3 + 2 * np.sin(2 * x)

plt.plot(x,y1)


plt.show()

plt.plot(x,y2)

plt.show()