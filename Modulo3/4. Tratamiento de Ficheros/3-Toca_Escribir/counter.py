from io import open
import sys

#Aceptamos parámetros obtenidos por consola
#Esto no hace falta tocarlo, el parámetro de consola se almacena en la variable user_input
user_input = ""
if len(sys.argv) == 2:
    user_input = sys.argv[1]


#Nuestro fichero se encontrara en esta misma carpeta
file_route = "counter.txt"

#Tenemos que abrir el fichero (ojo, que si no existe debe crearlo y escribir un 0)
#¿Que cómo sabemos si no existe? 
#¿Hay algún tipo de open() que lance una excepción si el fichero ya existe?



#Si el fichero existe pero está entero en blanco también escribimos un 0



# Vamos a leer el contenido, ver la última linea e intentar transformarla a número
# Recordad capturar las excepciones, si salta alguna excepción, mostrad el mensaje "Fichero corrupto"

#Si el parámetro del usuario es "inc", incrementamos en uno la siguiente linea
#Si el parámetro del usuario es "dec", decrementamos en uno la siguiente linea



#Para las pruebas tendremos que llamar a este fichero pasándole el parámetro:
#python counter.py dec
#python counter.py inc