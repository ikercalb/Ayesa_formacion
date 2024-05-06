#EJERCICIO 1
import sqlite3


#Vamos a crear una nueva base de datos. Ponle de nombre "restaurants" y comprueba cómo se genera
conexion = sqlite3.connect('restaurants.db')
#Recuerda importar SQLite 3 y que se crean con el método connect()
conexion.close()

# Cerramos la conexión! Si no la cerramos quedará abierta
# y no podremos gestionar el fichero
