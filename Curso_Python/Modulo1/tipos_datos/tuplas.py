tupla1 = (1,2,3)
tupla2 = (4,5,6)
tuplas = tupla1+tupla2
tuplas*3

#para operar con tuplas hay que pasarlas a lista y despues volver a pasarlas a tupla
tupla3 = (1,23,9,76,43,52,63,11)
a = list(tupla3)
a.sort()
tupla3 = tuple(a)


#contar cuantas veces esta x en una tupla
tupla4 = ('Hola',1, 'mundo', 2)
tupla4.count('hola')

#preguntar si esta x
1 in tupla4


#Ejercicio 5 
tupla5 = (0,1)
tupla6 = (1,0)
tupla_completa = tupla5+tupla6
tupla_completa = tupla_completa*4
print(tupla_completa)


