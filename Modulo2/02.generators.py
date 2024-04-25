'''
Ejercicio 1
Dado el siguiente generador, ejecutarlo en un bluce for imprimiendo
los elementos generados y comprobar en que orden se imprimen las sentencias.
'''

def five_numbers_generator():
  n = 0
  print('Elemento 0')
  yield n

  n +=1
  print('Elemento 1')
  yield n

  n +=1
  print('Elemento 2')
  yield n

for n in five_numbers_generator():
  print(n)


'''
Ejercicio 2
Crear un generador, pow_generator, que dado un numero n devuelva
en cada acceso la x^x, yendo x de 1 hasta n.
'''

def pow_generator(n):
   for x in range(1, n+1):
        yield x ** x
        
for i in pow_generator(5):
    print(i)
  