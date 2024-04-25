#Ejercicio23

pares = []
impares = []

pricipio = int(input("Introduce el principio: "))
fin = int(input("Introduce el fin: "))

for i in range(pricipio+1, fin):

    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print("pares: ", pares)
print("inpares: ", impares)