import os

i = 2
cantidad = 7

for _ in range(cantidad):
    nombre_archivo = fr"Matplotlib\ejercicio{i}.py"

    with open(nombre_archivo, 'w') as archivo:
        archivo.write(fr"import matplotlib.pyplot as plt")
    i = i + 1