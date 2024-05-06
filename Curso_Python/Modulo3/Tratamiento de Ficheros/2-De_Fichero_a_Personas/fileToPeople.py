from io import open
import sys
sys.path.insert(0,'../1-Leyendo Personas')
from reader import readFileLineByLine
#No os preocupeis por estas lineas. Las veremos cuando toquemos los modulos y paquetes



class Person:
    def __init__(self,id,name,surname,date_of_birth):
        self.id = id
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __str__(self):
        return print("id(",self.id,")", self.name, " ", self.surname, " => ", self.date_of_birth)
    #TODO: Definir la clase

filename = "../Leyendo_Personas/people.txt"
listOfPeople = readFileLineByLine(filename)

#TODO: Recorrer la lista "listOfPeople" creando objetos del tipo "Person" y mostrandolas por consola
for lista in listOfPeople:
    ob_split = lista.split(";")
    p = Person(ob_split[0],ob_split[1],ob_split[2],ob_split[3].replace("\n",""))
    p.__str__()


#Recuerda que el formato en el que se debe mostrar cada persona es:
# (id=1) Rafael Caro => 05/01/1992