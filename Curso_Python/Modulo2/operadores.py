'''
Ejercicio 1
Operaciones con listas. Dado las siguientes listas, cuyos datos se corresponden entre ellos por la posición
en la que se encuentran (Ana <-> 30 años <-> color rojo), obtener:

1) El nombre de la persona con mayor edad
2) La lista de las personas a las que les gusta el color rojo
3) La suma de la edad a las que les gusta el color verde
'''
from functools import reduce

def mayor(n,n1):
    return n if n[1] > n1[1] else n1 

def color(n):
    if n[2] == 'red':
        return n 

def verde(n1):
    if n1[2] == 'green':
        return n1
def suma_green(p,n):
    return p[1]+n[1]

names = ['Ana', 'Juan', 'Maria', 'Jose', 'Rafa']
age = [30, 32, 43, 12, 45]
fav_color = ['red', 'green', 'red', 'green', 'red']


listas = list(zip(names,age,fav_color))

print("#### El nombre de la persona con mayor edad ####")
edad = reduce(mayor,listas)
print(edad)


print("#### La lista de las personas a las que les gusta el color rojo ####")
rojo = list(filter(color,listas))
print(rojo)


print("#### La suma de la edad a las que les gusta el color verde ####")
sum_green = list(filter(verde,listas))
sum_green = reduce(suma_green,sum_green)
print(sum_green)