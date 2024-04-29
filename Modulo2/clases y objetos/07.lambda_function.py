"""
Ejercicio 1.
Crear una función lambda que dada una lista de numeros te devuelva la misma lista con los numeros negados.
Guardar dicha función lambda en un parametro y ejecutarla con una lsita para probarlo.
"""


a = list(map(lambda x: x * -1, [1,32,4,454,2,1]))
print(a)







'''
Ejercicio 2
Operaciones con listas. Dado las siguientes listas, cuyos datos se corresponden entre ellos por la posición
en la que se encuentran (Ana <-> 30 años <-> color rojo), obtener:

1) El nombre de la persona con mayor edad
2) La lista de las personas a las que les gusta el color rojo
3) La suma de la edad a las que les gusta el color verde
'''

from functools import reduce

names = ['Ana', 'Juan', 'Maria', 'Jose', 'Rafa']
age = [30, 32, 43, 12, 45]
fav_color = ['red', 'green', 'red', 'green', 'red']

zipped_list = list(zip(names,age,fav_color))

print("1)")

ej1 = reduce(lambda x,y: x if x[1] > y[1] else y,zipped_list)
print(ej1)

print("2)")

ej2 = list(filter(lambda x: x if x[2] == "red" else 0, zipped_list))
print(ej2)

print("3)")

ej2 = list(filter(lambda x: x if x[2] == "green" else 0, zipped_list))
ej2 = reduce(lambda x,y: x[1]+y[1], ej2)
print(ej2)

