import json

with open("libreria.json") as file:
    libreria = json.load(file)

#Ejercicio1
print(len(libreria["bookstore"]["book"]))


#ejercicio 2
max = int(input("Introduce el maximo: "))
min = int(input("Introduce el minimo: "))
for libro in libreria["bookstore"]["book"]:
    if min < float(libro["price"]) < max:
        print(libro['title']['__text'])

#ejercicio 3
cadena = input("Introduce el libro: ")
for libro in libreria["bookstore"]["book"]:
    if libro['title']['__text'].startswith(cadena):
        print(libro['title']['__text'])
        print(libro['year'])

libros = {}
for libro in libreria["bookstore"]["book"]:

    autores = []
    autores.append(libro["author"])
    print(autores)
    a = libro['title']['__text']
    libros[a] = autores

print(libros)