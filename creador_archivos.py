import os

i = 20
cantidad = 15

for _ in range(cantidad):
    nombre_archivo = fr"Ejercicios_basicos\Iteradores\{i}.py"

    with open(nombre_archivo, 'w') as archivo:
        archivo.write(fr"#Ejercicio{i}")
    i = i + 1