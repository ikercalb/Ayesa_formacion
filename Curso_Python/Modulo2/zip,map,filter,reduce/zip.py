'''
Ejercicio 1
Probar la función ZIP para unir 3 listas y comprobar que ocurre cuando las listas
tienen diferente tamaño.
'''

names = ['Ana', 'Juan', 'Maria', 'Jose', 'Rafa']
age = [30, 32, 43, 12, 45, 43, 42]
fav_color = ['red', 'blue', 'red', 'green']


zipped_list = zip(names,age,fav_color)
print(list(zipped_list))