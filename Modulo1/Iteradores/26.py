#Ejercicio26

palabra1 = input("Introduce la palabra1: ")
palabra2 = input("Introduce la palabra2: ")

if palabra1[-3:] == palabra2[-3:]:
    print("Rima")
elif palabra1[-2:] == palabra2[-2:]:
    print("rima poco")
else:
    print("no rima")
