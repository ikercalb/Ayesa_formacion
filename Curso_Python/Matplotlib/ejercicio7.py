import matplotlib.pyplot as plt
import numpy as np

frutas = ["Manzana", "Pera", "Platano", "Mandarina", "Cereza"]
cantidad = np.random.randint(0, 101, size=5)

plt.bar(frutas, height=cantidad, yerr=cantidad * 0.1, capsize=10)

plt.title("Cantidad de frutas")
plt.xlabel("Frutas")
plt.ylabel("Cantidad")

plt.show()
