import matplotlib.pyplot as plt
import numpy as np
newYork = [300, 298, 314, 415, 388, 351, 367]
tokyo = [100, 142, 138, 149, 178, 200, 153]
london =  [256, 278, 214, 248, 236, 266, 299]
spain = [150, 189, 241, 291, 345, 300, 257]

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]


fig, ax = plt.subplots(2, 2)
g = ax.plot(np.random.randn(50).cumsum())
fig.set_facecolor('grey')
fig.set_size_inches(15, 7)
fig.suptitle('bolsa de valores')

ax[0, 0].set_title('New York')
ax[0, 1].set_title('tokyo')
ax[1, 0].set_title('london')
ax[1, 1].set_title('spain')

g1 = ax[0, 0].plot(dias, newYork)
g2 = ax[0, 1].plot(dias, tokyo)
g3 = ax[1, 0].plot(dias, london)
g4 = ax[1, 1].plot(dias, spain)

g1[0].set_color('Green')
g1[0].set_marker('v')
g1[0].set_linestyle('--')
g1[0]._linewidth(2)
g1[0].set_markersize(2)


g2[0].set_color('blue')
g2[0].set_marker('*')
g2[0].set_linestyle(':')


g3[0].set_color('yellow')
g3[0].set_marker('s')
g3[0].set_linestyle('-.')


g4[0].set_color('red')
g4[0].set_marker('d')
g4[0].set_linestyle('-')


plt.show()




