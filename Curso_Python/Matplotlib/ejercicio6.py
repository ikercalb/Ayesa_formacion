import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(0,101, size=100)
y = np.random.randint(100,201, size=100)


plt.scatter(x,y, c=x,cmap='rainbow')

plt.title("relacion altura edad")
plt.xlabel("edad")
plt.ylabel("altura")
plt.ylim(0,250)
plt.xlim(0,150)
 
plt.show()