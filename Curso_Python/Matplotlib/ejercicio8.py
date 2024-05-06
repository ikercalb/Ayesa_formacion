import matplotlib.pyplot as plt
import numpy as np

vehiculo = ["Coche", "Motocicleta", "Bicicleta", "Autobus"]
cantidad = np.random.randint(100, 201, size=4)

plt.pie(cantidad, labels=vehiculo, autopct='%1.1f%%', shadow=True)
plt.title("Venta de vehiculos")
plt.show()
