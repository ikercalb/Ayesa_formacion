#Ejercicio25
palabra = input("introduce una palabra: ")
vocales = ["a","e","i","o","u"]
busqueda = input("introduce una vocal: ")
c = 0
if busqueda in vocales:
    for x in range(len(palabra)):
        if palabra[x].lower() == busqueda:
            c += 1
else:
    print("no es una vocal")

print("se ha encontrado: ", c)