from io import open
import sys
sys.path.insert(0,'../1-Leyendo Personas')
from reader import readFileCompletely, readFileLineByLine
#No os preocupeis por estas lineas. Las veremos cuando toquemos los modulos y paquetes



class Person:
    pass
    #TODO: Definir la clase

filename = "../1-Leyendo_Personas/people.txt"
listOfPeople = readFileLineByLine(filename)
print(listOfPeople)
#TODO: Recorrer la lista "listOfPeople" creando objetos del tipo "Person" y mostrandolas por consola
#Recuerda que el formato en el que se debe mostrar cada persona es:
# (id=1) Rafael Caro => 05/01/1992