# Para generar las tablas que vamos a utilizar debemos ejecutar las siguientes sentencias SQL:
import sqlite3
conexion = sqlite3.connect('restaurants.db')

cursor = conexion.cursor()
try:
    cursor.execute("CREATE TABLE category(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(100) UNIQUE NOT NULL)")
    cursor.execute("CREATE TABLE dish (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100) UNIQUE NOT NULL,category_id INTEGER NOT NULL,FOREIGN KEY(category_id) REFERENCES categoria(id))")

except sqlite3.OperationalError:
    print("YA EXISTEN")

conexion.commit()
conexion.close()
#¿Qué ocurre si la tabla ya existe? Estaría bien capturar esa excepción