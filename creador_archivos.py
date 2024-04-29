import os

i = 2
cantidad = 15

for _ in range(cantidad):
    nombre_archivo = fr"Matplotlib\grafica{i}.py"

    with open(nombre_archivo, 'w') as archivo:
        archivo.write(fr"#Grafica{i}")
    i = i + 1