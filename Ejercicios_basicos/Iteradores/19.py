#Ejercicio19

a = input("Introduce el primer valor: ")
b = input("Introduce el segundo valor: ")
lista = []

while a > b:
    lista.append(b)
    b = input("Introduce el segundo valor: ")

print(lista)