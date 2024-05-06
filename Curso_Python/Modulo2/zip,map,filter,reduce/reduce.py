'''
Ejercicio 1
Probar la función REDUCE para obtener el número mas grande de la lista
'''
from functools import reduce

def mayor(prev, element):
  print(prev)
  return prev if prev > element else element 
    
numbers = [1, 12, 3, 34, 45, 68, 25, 14, 26, 78, 96]
max_number = reduce(mayor,numbers)

print(max_number)