# Para generar las tablas que vamos a utilizar debemos ejecutar las siguientes sentencias SQL:

# CREATE TABLE category(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(100) UNIQUE NOT NULL)

# CREATE TABLE dish(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(100) UNIQUE NOT NULL, 
#     category_id INTEGER NOT NULL,
#     FOREIGN KEY(categoria_id) REFERENCES categoria(id))


#¿Qué ocurre si la tabla ya existe? Estaría bien capturar esa excepción