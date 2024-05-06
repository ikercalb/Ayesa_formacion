'''
Ejercicio 1
Probar la función FILTER para obtener una lista solo con los números pares de la lista original.
'''
def par(n):
    return n % 2 == 0

numbers = [1, 12, 3, 34, 45, 68, 25, 14, 26, 78, 96]




odd_list = list(filter(par,numbers))

print(odd_list)