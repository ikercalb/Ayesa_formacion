import sqlite3

def add_category(category_name):
    #TODO: Completad este fichero
    #Tiene que insertar una nueva categoría en la base de datos
    conexion = sqlite3.connect('restaurants.db')
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO category (name) VALUES (?)', (category_name,))
#   cursor.execute('INSERT INTO category (name) VALUES (\''+category_name+'\')', (category_name,))
    conexion.commit()
    conexion.close()

#La sentencia para agregar datos a una tabla es:
#INSERT INTO [nombre_de_la_tabla] VALUES (valor1, valor2, valor3,...)
#Los valores deben estar en el orden en el que se declararon en la tabla

add_category("starter")
add_category("principal")
add_category("dessert")