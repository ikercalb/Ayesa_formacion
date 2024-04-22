numeros = [1,2,3,4,5,6]
diasdelasemana = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']

listadelistas = [[1,2,3],[4,5,6],[7,8,9]]

dias = ['Lunes','Martes','Miercoles']
jueves = ['Jueves']
dias+jueves 

#lista[xprincipio : xfinal] el principio sale el final se excluye.

numeros[1] = 1.5
numeros.index(1.5)
numeros.remove(1.5)

1.5 in numeros




#EJERCICIO 4
i = 0
primitiva = []
for _ in range(5):
    primitiva.append(int(input()))
    i =+ 1
    
primitiva.sort()
print(primitiva)