#Ejercicio20
lista = []
while True:
    numero = int(input("Introduce el numero: "))
    
    if numero == -1:
            print("El conjunto es: ")
            suma = sum(lista)
            len = len(lista)
            promedio = suma/len
            print(promedio)
            break
    else:
        lista.append(numero)