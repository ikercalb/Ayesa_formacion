'''
Ejercicio 1
Probar la función MAP para obtener una lista con el número de caracteres de cada uno de los nombres.
'''
def count(s):
    return len(s)
names = ['Ana', 'Juan', 'Maria', 'Jose', 'Rafa']

name = map(count, names)
count_list = list(name)
print(count_list)